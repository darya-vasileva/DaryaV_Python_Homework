from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install())
    )

driver.get(
    "http://the-internet.herokuapp.com"
)

element = WebDriverWait(driver, 20).until(
    EC.visibility_of_element_located((By.LINK_TEXT, "A/B Testing"))
)

print(f"Элемент {element.text} найден и виден")

driver.quit()
