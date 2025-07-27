import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from calculator import Calculator


@pytest.fixture
def driver():
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install())
        )
    yield driver
    driver.quit()


@allure.title("Сложение двух чисел в калькуляторе с задержкой вычисления")
@allure.description("""
                    Тест проверяет основные функции калькулятора с
                    заданной задержкой перед вычислением
                    """)
@allure.feature("Основные операции калькулятора с задержкой вычисления")
@allure.severity("blocker")
def test_calculator(driver):
    with allure.step("Перейти на сайт калькулятора"):
        driver.get("""
            https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html
                """)
        calculator = Calculator(driver)

    with allure.step("Ввести значение в поле задержки перед вычислением"):
        calculator.input_delay("45")

    with allure.step("""
                    Нажать кнопки калькулятора для вычисления выражения '7+8='
                    """):
        calculator.click_button("7")
        calculator.click_button("+")
        calculator.click_button("8")
        calculator.click_button("=")
        WebDriverWait(driver, 50).until(
            EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15")
            )
    with allure.step("Получить результат вычисления"):
        result = calculator.get_result()

    with allure.step("Проверить результат вычисления"):
        assert result == "15"
