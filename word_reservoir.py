def __get_answer_list():
    words = []
    with open("answer_list.txt", "r") as file:
        for line in file:
            words.append(line.strip())
    return words


def __get_guess_list():
    words = []
    with open("guess_list.txt", "r") as file:
        for line in file:
            words.append(line.strip())
    return words

def __get_cowordle_answer_list():
    words = []
    with open("cowordle_answer_list.txt", "r") as file:
        for line in file:
            words.append(line.strip())
    return words


answer_list = __get_answer_list()
guess_list = __get_guess_list()
cowordle_answer_list = __get_cowordle_answer_list()
