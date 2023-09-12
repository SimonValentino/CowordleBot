from word_reservoir import answer_list, guess_list
from statistics import mean


class Bot:
    def __init__(self, *, words=answer_list, starting_words="", hard_mode=True):
        self.__words = words
        self.__narrowed_list = words
        self.__starting_words = starting_words
        self.__hard_mode = hard_mode
        self.__eval_to_words = {}
        self.__starting_words_index = 0

    def calculate_guess(self):
        if self.__starting_words_index < len(self.__starting_words):
            words_to_consider = [self.__starting_words[self.__starting_words_index]]
            self.__starting_words_index += 1
        elif len(self.__narrowed_list) == 1 or self.__hard_mode:
            words_to_consider = self.__narrowed_list
        else:
            words_to_consider = self.__words

        avg_remaining_wordcount = 10000

        for word in words_to_consider:
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
                guess = word
                self.__eval_to_words = temp_eval_to_words

        return guess

    def evaluate_word(self, guess, possible_answer):
        hints = [0, 0, 0, 0, 0]

        # Check for greens (2)
        for i in range(5):
            if guess[i] == possible_answer[i]:
                hints[i] = 2
                possible_answer = possible_answer[:i] + \
                    ' ' + possible_answer[i + 1:]

        # Check for yellows (1)
        for i in range(5):
            char = guess[i]
            if char in possible_answer and hints[i] == 0:
                hints[i] = 1
                first_occurrence = possible_answer.find(char)
                possible_answer = possible_answer[:first_occurrence] + \
                    ' ' + possible_answer[first_occurrence + 1:]

        return tuple(hints)
    
    def absorb_hints(self, hints):
        self.__narrowed_list = self.__eval_to_words[tuple(hints)]

    def reset(self):
        self.__narrowed_list = self.__words
        self.__eval_to_words = {}
        self.__starting_words_index = 0
