from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver=webdriver.Chrome(options=options)
driver.get("https://cowordle.org/mode-2")

hard_mode = driver.find_element(By.CLASS_NAME, "difficulty_hard_btn")
hard_mode.click()

name = driver.find_element(By.XPATH, "/html/body/div[1]/div/section/div/div[1]/div/div/div/div/div[5]/div[2]/div/div[1]/div[3]/div/input")
name.send_keys("GorillaGamer29")

start = driver.find_element(By.CLASS_NAME, "start_btn")
start.click()
