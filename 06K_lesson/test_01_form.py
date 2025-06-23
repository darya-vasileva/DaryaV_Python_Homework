import pytest
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By


@pytest.fixture
def driver():
    driver = webdriver.Edge(
        service=EdgeService(EdgeChromiumDriverManager().install())
        )
    driver.maximize_window()
    yield driver
    driver.quit()


def test_fill_form(driver):
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
        )

    driver.find_element(By.NAME, "first-name").send_keys("Иван")
    driver.find_element(By.NAME, "last-name").send_keys("Петров")
    driver.find_element(By.NAME, "address").send_keys("Ленина, 55-3")
    driver.find_element(By.NAME, "e-mail").send_keys("test@skypro.com")
    driver.find_element(By.NAME, "phone").send_keys("+7985899998787")
    driver.find_element(By.NAME, "city").send_keys("Москва")
    driver.find_element(By.NAME, "country").send_keys("Россия")
    driver.find_element(By.NAME, "job-position").send_keys("QA")
    driver.find_element(By.NAME, "company").send_keys("SkyPro")

    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

# Проверка подсветки поля Zip code
    zip_field = driver.find_element(By.CSS_SELECTOR, "[id='zip-code']")
    assert 'alert py-2 alert-danger' in zip_field.get_attribute("class")

# Проверка остальных полей
    field_names = [
        "#first-name", "#last-name", "#address", "#e-mail", "#phone", "#city",
        "#country", "#job-position", "#company"
        ]

    for field_name in field_names:
        name = driver.find_element(By.CSS_SELECTOR, field_name)
        assert "alert py-2 alert-success" in name.get_attribute("class")
