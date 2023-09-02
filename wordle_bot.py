from word_reservoir import answer_list
from statistics import mean


class Bot:
    def __init__(self, answer_list=answer_list, *, starting_word=""):
        self.__narrowed_list = answer_list
        self.__starting_word = starting_word
        self.__guess = starting_word
        self.__eval_to_words = {}

    def calculate_guess(self):
        if self.__guess == self.__starting_word:
            self.__guess = ""
            return self.__starting_word
        
        avg_remaining_wordcount = 1e3

        for word in self.__narrowed_list:
            temp_eval_to_words = {}

            for possible_answer in self.__narrowed_list:
                word_eval = self.evaluate_word(word, possible_answer)

                if word_eval not in temp_eval_to_words:
                    temp_eval_to_words[word_eval] = [possible_answer]
                else:
                    temp_eval_to_words[word_eval].append(possible_answer)

            temp_avg_remaining_wordcount = mean(
                [len(words) for words in temp_eval_to_words.values()])

            if temp_avg_remaining_wordcount < avg_remaining_wordcount:
                avg_remaining_wordcount = temp_avg_remaining_wordcount
                self.__guess = word
                self.__eval_to_words = temp_eval_to_words

        return self.__guess

    def absorb_hints(self, hints):
        self.__narrowed_list = self.__eval_to_words[tuple(hints)]

    def evaluate_word(self, guess, possible_answer):
        result = [2 if guess[i] == possible_answer[i]
                  else 0 for i in range(len(guess))]

        answer_counts = {}
        for letter in possible_answer:
            answer_counts[letter] = answer_counts.get(letter, 0) + 1

        for i, letter in enumerate(guess):
            if result[i] == 0 and letter in answer_counts and answer_counts[letter] > 0:
                result[i] = 1
                answer_counts[letter] -= 1

        return tuple(result)
    
    def reset(self):
        self.__narrowed_list = answer_list
        self.__guess = self.__starting_word
        self.__eval_to_words = {}
