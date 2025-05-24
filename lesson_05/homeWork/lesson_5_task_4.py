from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Firefox()
driver.get("http://the-internet.herokuapp.com/login")

text_input1 = driver.find_element(By.NAME, "username")
text_input1.send_keys("tomsmith")

text_input2 = driver.find_element(By.NAME, "password")
text_input2.send_keys("SuperSecretPassword!")

driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

sleep(3)

success_message = driver.find_element(By.CSS_SELECTOR,
                                      'div[class="flash success"]').text
print(success_message)


driver.quit()
