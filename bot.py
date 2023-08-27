from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time

IS_HARD_MODE = True
NUM_LETTERS = 5
USERNAME = "Vintage"
COWORDLE_YELLOW_CLASS = "Row-letter Row-letter-double letter-elsewhere"
COWORDLE_GREEN_CLASS = "Row-letter Row-letter-double letter-correct"
BOT_YELLOW_CLASS = "tile active score-present"
BOT_GREEN_CLASS = "tile active score-correct"


def enter_word(word):
    for letter in word:
        keys[key_to_index[letter]].click()
    keys[key_to_index["ENTER"]].click()


def game_over():
    try:
        game.find_element(By.CLASS_NAME, "timer")
    except NoSuchElementException:
        return True
    return False


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


#options.add_argument("--headless")
bot = webdriver.Chrome(options=options)
bot.get("https://www.simn.me/eldrow/")

if IS_HARD_MODE:
    click(bot, By.ID, "easy")

WebDriverWait(game, 100).until(
    EC.presence_of_element_located((By.CLASS_NAME, "timer")))

keys = game.find_elements(By.CLASS_NAME, "Game-keyboard-button")

i = 1

while True:
    if game_over():
        time.sleep(0.5)
        click(game, By.CLASS_NAME, "restart_btn")
        click(bot, By.XPATH, "/html/body/div/div/div[2]/button[2]")
        WebDriverWait(game, 100).until(
            EC.presence_of_element_located((By.CLASS_NAME, "timer")))

        i = 1
    
    if i > 6:
        continue
    
    while "." in bot.find_element(
        By.XPATH, f"/html/body/div/div/section[1]/section[{i}]").text:
        continue
    
    letters = bot.find_element(
        By.XPATH, f"/html/body/div/div/section[1]/section[{i}]")
    word = letters.text.replace("\n", "")
    enter_word(word)
    
    while not game.find_element(
        By.XPATH, f"/html/body/div[1]/div/section/div/div[1]/div/div/div/div/div[2]/div[1]/div/div[1]/div/div[1]/div[{i}]"
    ).get_attribute("class") == "Row Row-locked-in":
        continue
    
    time.sleep(0.05)

    hints = [game.find_element(
        By.XPATH, f"/html/body/div[1]/div/section/div/div[1]/div/div/div/div/div[2]/div[1]/div/div[1]/div/div[1]/div[{i}]/div[{j}]") for j in range(1, NUM_LETTERS + 1)]
    bot_buttons = [bot.find_element(
        By.XPATH, f"/html/body/div/div/section[1]/section[{i}]/button[{j}]") for j in range(1, NUM_LETTERS + 1)]

    for j in range(0, NUM_LETTERS):
        hint_class = hints[j].get_attribute("class")
        bot_button = bot_buttons[j]
        bot_button_class = bot_button.get_attribute("class")
        
        if hint_class == COWORDLE_YELLOW_CLASS and not bot_button_class == BOT_YELLOW_CLASS:
            bot_button.click()
        elif hint_class == COWORDLE_GREEN_CLASS:
            if bot_button.get_attribute("class") == BOT_YELLOW_CLASS:
                bot_button.click()
            elif not bot_button.get_attribute("class") == BOT_GREEN_CLASS:
                bot_button.click()
                bot_button.click()


    click(bot, By.XPATH, "/html/body/div/div/div[2]/button[1]")

    i += 1
