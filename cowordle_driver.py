from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time
from wordle_bot import Bot
from word_reservoir import cowordle_answer_list

# Customizable variables
IS_HARD_MODE = True
USERNAME = "Simon101"
bot = Bot(words=cowordle_answer_list,
          starting_words=["salet"])

NUM_LETTERS = 5
COWORDLE_GREY_CLASS = "Row-letter Row-letter-double letter-absent"
COWORDLE_YELLOW_CLASS = "Row-letter Row-letter-double letter-elsewhere"
COWORDLE_GREEN_CLASS = "Row-letter Row-letter-double letter-correct"


def enter_word(word):
    for letter in word:
        time.sleep(0.015)
        keys[key_to_index[letter]].click()
    time.sleep()
    keys[key_to_index["enter"]].click()


def game_over():
    try:
        game.find_element(By.CLASS_NAME, "timer")
    except NoSuchElementException:
        return True
    return False


def click(driver, by, element):
    WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((by, element))).click()


def send_keys(driver, by, element, keys):
    WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((by, element))).send_keys(keys)


key_to_index = {
    'q': 0, 'w': 1, 'e': 2, 'r': 3, 't': 4, 'y': 5, 'u': 6, 'i': 7, 'o': 8, 'p': 9, 'a': 10, 's': 11, 'd': 12, 'f': 13,
    'g': 14, 'h': 15, 'j': 16, 'k': 17, 'l': 18, 'del': 19, 'z': 20, 'x': 21, 'c': 22, 'v': 23, 'b': 24, 'n': 25, 'm': 26, 'enter': 27
}

hint_to_num = {
    COWORDLE_GREY_CLASS: 0,
    COWORDLE_YELLOW_CLASS: 1,
    COWORDLE_GREEN_CLASS: 2
}

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

game = webdriver.Chrome(options=options)
game.get("https://cowordle.org/mode-2")

click(game, By.CLASS_NAME,
      "difficulty_hard_btn" if IS_HARD_MODE else "difficulty_normal_btn")
send_keys(game, By.XPATH,
          "/html/body/div[1]/div/section/div/div[1]/div/div/div/div/div[5]/div[2]/div/div[1]/div[3]/div/input", USERNAME)
click(game, By.CLASS_NAME, "start_btn")

WebDriverWait(game, 20).until(
    EC.presence_of_element_located((By.CLASS_NAME, "timer")))

keys = game.find_elements(By.CLASS_NAME, "Game-keyboard-button")

i = 1

while True:
    if game_over():
        time.sleep(0.5)
        click(game, By.XPATH,
              "/html/body/div[1]/div/section/div/div[1]/div/div/div/div/div[7]/div[2]/div/div[3]/button")
        bot.reset()
        WebDriverWait(game, 100).until(
            EC.presence_of_element_located((By.CLASS_NAME, "timer")))

        i = 1

    if i > 6:
        continue

    word = bot.calculate_guess()
    enter_word(word)

    while not game.find_element(
        By.XPATH, f"/html/body/div[1]/div/section/div/div[1]/div/div/div/div/div[2]/div[1]/div/div[1]/div/div[1]/div[{i}]/div[5]"
    ).get_attribute("class") in (COWORDLE_GREY_CLASS, COWORDLE_YELLOW_CLASS, COWORDLE_GREEN_CLASS):
        continue

    hints = [game.find_element(
        By.XPATH, f"/html/body/div[1]/div/section/div/div[1]/div/div/div/div/div[2]/div[1]/div/div[1]/div/div[1]/div[{i}]/div[{j}]") for j in range(1, NUM_LETTERS + 1)]

    hints_for_bot = [hint_to_num[hints[j].get_attribute(
        "class")] for j in range(0, NUM_LETTERS)]
    bot.absorb_hints(hints_for_bot)

    i += 1
