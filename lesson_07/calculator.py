from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Calculator:
    def __init__(self, driver):
        self.driver = driver
        self.results_selector = (By.CLASS_NAME, "screen")

    def input_delay(self, number):
        delay_value = self.driver.find_element(By.ID, "delay")
        delay_value.clear()
        delay_value.send_keys(number)

    def click_button(self, value):
        button = self.driver.find_element(
            By.XPATH, f"//span[text()='{value}']")
        button.click()

    def get_result(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "screen")))
        result = self.driver.find_element(By.CSS_SELECTOR, ".screen")
        return result.text
