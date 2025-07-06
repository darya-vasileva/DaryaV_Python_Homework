import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from shop_LoginPage import Autorization
from shop_Main import ShopMainPage
from shop_Order import OrderPage
from shop_Checkout import CheckoutPage


@pytest.fixture
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--disable-notifications")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()
    yield driver
    driver.quit()


def test_shop(driver):

    autorization = Autorization(driver)
    autorization.input_username("standard_user")
    autorization.input_password("secret_sauce")
    autorization.login_button()

    WebDriverWait(driver, 15).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "inventory_item")))

    shop_main_page = ShopMainPage(driver)
    shop_main_page.add_item("sauce-labs-backpack")
    shop_main_page.add_item("sauce-labs-bolt-t-shirt")
    shop_main_page.add_item("sauce-labs-onesie")
    shop_main_page.shopping_cart()

    checkout_page = CheckoutPage(driver)
    checkout_page.checkout_cart()

    order = OrderPage(driver)
    order.first_name("Дарья")
    order.last_name("Васильева")
    order.postal_code("350000")

    order.continue_button()
    assert order.total_check() == "Total: $58.29"
