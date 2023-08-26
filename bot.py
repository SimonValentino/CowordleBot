from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time

IS_HARD_MODE = True
USERNAME = "gorillagamer"


def enter_word(word):
    for letter in word:
        keys[key_to_index[letter]].click()
    keys[key_to_index["ENTER"]].click()


def check_game_over():
    try:
        game.find_element(By.CLASS_NAME, "restart_btn")
    except NoSuchElementException:
        return False
    return True


def click(driver, by, element):
    WebDriverWait(driver, 100).until(
        EC.element_to_be_clickable((by, element))).click()


def send_keys(driver, by, element, keys):
    WebDriverWait(driver, 100).until(
        EC.element_to_be_clickable((by, element))).send_keys(keys)


key_to_index = {
    'Q': 0, 'W': 1, 'E': 2, 'R': 3, 'T': 4, 'Y': 5, 'U': 6, 'I': 7, 'O': 8, 'P': 9, 'A': 10, 'S': 11, 'D': 12, 'F': 13,
    'G': 14, 'H': 15, 'J': 16, 'K': 17, 'L': 18, 'DEL': 19, 'Z': 20, 'X': 21, 'C': 22, 'V': 23, 'B': 24, 'N': 25, 'M': 26, 'ENTER': 27
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


bot = webdriver.Chrome(options=options)
bot.get("https://www.simn.me/eldrow/")

if IS_HARD_MODE:
    click(bot, By.ID, "easy")

WebDriverWait(game, 100).until(
    EC.presence_of_element_located((By.CLASS_NAME, "timer")))

keys = game.find_elements(By.CLASS_NAME, "Game-keyboard-button")

i = 1
while not check_game_over():
    letters = bot.find_elements(
        By.XPATH, f"/html/body/div/div/section[1]/section[{i}]")[0]
    word = letters.text.replace("\n", "")
    enter_word(word)
    time.sleep(0.2)
    
    
    
    i += 1
