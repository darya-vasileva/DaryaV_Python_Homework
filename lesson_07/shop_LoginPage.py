from selenium.webdriver.common.by import By


class Autorization:

    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(4)
        self.driver.maximize_window()

    def input_username(self, login):
        self.username = self.driver.find_element(By.ID, "user-name")
        self.username.send_keys(login)

    def input_password(self, key):
        self.password = self.driver.find_element(By.ID, "password")
        self.password.send_keys(key)

    def login_button(self):
        self.login = self.driver.find_element(By.ID, "login-button")
        self.login.click()
