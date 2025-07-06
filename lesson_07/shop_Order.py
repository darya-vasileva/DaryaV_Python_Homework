from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class OrderPage:
    def __init__(self, driver):
        self.driver = driver

    def first_name(self, first_name):
        self.add_first_name = self.driver.find_element(By.ID, "first-name")
        self.add_first_name.send_keys(first_name)

    def last_name(self, last_name):
        self.last_name = self.driver.find_element(By.ID, "last-name")
        self.last_name.send_keys(last_name)

    def postal_code(self, zip):
        self.code = self.driver.find_element(By.ID, "postal-code")
        self.code.send_keys(zip)

    def continue_button(self):
        self_continue = self.driver.find_element(By.ID, "continue")
        self_continue.click()

    def total_check(self):
        WebDriverWait(self.driver, 15).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "cart_item")))
        total = self.driver.find_element(By.CLASS_NAME, "summary_total_label")
        return total.text
