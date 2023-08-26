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
    keys[key_to_index["enter"]].click()
    
def check_game_over():
    try:
        game.find_element(By.CLASS_NAME, "restart_btn")
    except NoSuchElementException:
        return False
    return True

key_to_index = {'q': 0, 'w': 1, 'e': 2, 'r': 3, 't': 4, 'y': 5, 'u': 6, 'i': 7, 'o': 8, 'p': 9, 'a': 10, 's': 11, 'd': 12, 'f': 13,
                'g': 14, 'h': 15, 'j': 16, 'k': 17, 'l': 18, 'del': 19, 'z': 20, 'x': 21, 'c': 22, 'v': 23, 'b': 24, 'n': 25, 'm': 26, 'enter': 27}

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)



game = webdriver.Chrome(options=options)
game.get("https://cowordle.org/mode-2")

WebDriverWait(game, 100).until(
    EC.element_to_be_clickable((By.CLASS_NAME, "difficulty_hard_btn" if IS_HARD_MODE else "difficulty_normal_btn"))).click()
WebDriverWait(game, 100).until(
    EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/section/div/div[1]/div/div/div/div/div[5]/div[2]/div/div[1]/div[3]/div/input"))).send_keys(USERNAME)
WebDriverWait(game, 100).until(
    EC.element_to_be_clickable((By.CLASS_NAME, "start_btn"))).click()



bot = webdriver.Chrome(options=options)
bot.get("https://www.simn.me/eldrow/")

if IS_HARD_MODE:
    WebDriverWait(bot, 100).until(
        EC.element_to_be_clickable((By.ID, "easy"))).click()
    
WebDriverWait(game, 100).until(
    EC.presence_of_element_located((By.CLASS_NAME, "timer")))

keys = game.find_elements(By.CLASS_NAME, "Game-keyboard-button")

while not check_game_over():
    enter_word("stare")
    time.sleep(0.2)
