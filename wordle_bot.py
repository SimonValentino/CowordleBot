from word_reservoir import answer_list, guess_list
import numpy as np

class Bot:
    def __init__(self, *, guessable_words=answer_list, starting_word="stare"):
        self.__words_to_consider = guessable_words
        self.__narrowed_list = answer_list
        self.__guess = "stare"
    
    def calculate_guess(self):
        for word in self.words_to_consider:
            eval_to_word = {}
            
            for possible_answer in self.__narrowed_list:
                word_strength = self.__evaluate_word(word, possible_answer)
    
    def absorb_hints(self, hints):
        pass
    
    def __evaluate_word(self, guess, possible_answer):
        result = [2 if guess[i] == possible_answer[i] else 0 for i in range(len(guess))]
        
        answer_counts = {}
        for letter in possible_answer:
            answer_counts[letter] = answer_counts.get(letter, 0) + 1
        
        for i, letter in enumerate(guess):
            if result[i] == 0 and letter in answer_counts and answer_counts[letter] > 0:
                result[i] = 1
                answer_counts[letter] -= 1

        return tuple(result)
