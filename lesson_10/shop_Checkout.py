from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:
    """
    Подтверждение заказа
    """
    def __init__(self, driver):
        self.driver = driver

    def checkout_cart(self):
        """
        Проверяет присутствие всех выбранных товаров в корзине
        и нажимает кнопку подтверждения
        """
        WebDriverWait(self.driver, 15).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "cart_item")))
        checkout_button = self.driver.find_element(By.ID, "checkout")
        checkout_button.click()
