from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Firefox()
driver.get("http://the-internet.herokuapp.com/inputs")

text_input = driver.find_element(By.TAG_NAME, "input")
text_input.send_keys("Sky")
text_input.clear()
text_input = driver.find_element(By.TAG_NAME, "input")
text_input.send_keys("Pro")

sleep(3)
driver.quit()
