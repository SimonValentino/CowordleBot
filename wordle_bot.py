from word_reservoir import answer_list, guess_list
from statistics import mean


class Bot:
    def __init__(self, *, answer_list=answer_list, starting_word="trace"):
        self.__guessable_words = answer_list
        self.__narrowed_list = answer_list
        self.__starting_word = starting_word
        self.__eval_to_words = {}
        self.__has_used_starting_word = False

    def calculate_guess(self):
        if not self.__has_used_starting_word:
            words_to_eval = [self.__starting_word]
            self.__has_used_starting_word = True
        else:
            words_to_eval = self.__guessable_words

        avg_remaining_wordcount = 1e3

        for word in words_to_eval:
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

    def absorb_hints(self, hints):
        self.__narrowed_list = self.__eval_to_words[tuple(hints)]
        self.__guessable_words = self.__narrowed_list

    def evaluate_word(self, guess, possible_answer):
        result = []
        unmatched_answer = list(possible_answer)

        for i in range(len(guess)):
            if guess[i] == possible_answer[i]:
                result.append(2)
                unmatched_answer[i] = None
            elif guess[i] in unmatched_answer:
                result.append(1)
                unmatched_answer[unmatched_answer.index(guess[i])] = None
            else:
                result.append(0)

        return tuple(result)

    def reset(self):
        self.__narrowed_list = answer_list
        self.__eval_to_words = {}
        self.__has_used_starting_word = False
