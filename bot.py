from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

game = webdriver.Chrome(options=options)
game.get("https://cowordle.org/mode-2")

game.find_element(By.CLASS_NAME, "difficulty_hard_btn").click()
game.find_element(
    By.XPATH,
    "/html/body/div[1]/div/section/div/div[1]/div/div/div/div/div[5]/div[2]/div/div[1]/div[3]/div/input").send_keys("GorillaGamer29")
game.find_element(By.CLASS_NAME, "start_btn").click()



# THIS CODE will be used in the future for making the bot not visible
# options.add_argument("--headless")
# options.add_argument("window-size=1000,300")

bot = webdriver.Chrome(options=options)
bot.get("https://www.simn.me/eldrow/")

bot.find_element(By.ID, "easy").click()
