from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://www.google.com/")

search_input = driver.find_element(By.NAME, "q")
search_input.send_keys("Selenium", Keys.RETURN)

driver.quit()
