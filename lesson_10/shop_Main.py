from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class ShopMainPage:
    """
    Главная страница магазина
    """
    def __init__(self, driver):
        self.driver = driver

    def add_item(self, product_name: str) -> None:
        """
        Добавление товара в корзину
        """
        WebDriverWait(self.driver, 10)
        add_button = self.driver.find_element(
            By.CSS_SELECTOR, f"[data-test='{f"add-to-cart-{product_name}"}']")
        add_button.click()

    def shopping_cart(self):
        """
        Переход в корзину
        """
        self.cart = self.driver.find_element(
            By.CLASS_NAME, "shopping_cart_link")
        self.cart.click()
