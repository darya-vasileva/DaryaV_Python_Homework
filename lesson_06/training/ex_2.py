from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install())
    )
driver.implicitly_wait(20)
driver.get("https://www.seleniumeasy.com/lander")

driver.find_element(By.ID, "getButtonBoxLink").click()

print("Кнопка 'Приобрести этот домен' найдена и кликнута")
