from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_input = (By.NAME, "username")
        self.password_input = (By.NAME, "password")
        self.login_button = (By.XPATH, "//button[@type='submit']")

    def enter_username(self, username):
        try:
            username_field = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.username_input)
            )
            username_field.clear()
            username_field.send_keys(username)
        except TimeoutException:
            print("Timeout: username field not found.")
            raise

    def enter_password(self, password):
        try:
            password_field = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.password_input)
            )
            password_field.clear()
            password_field.send_keys(password)
        except TimeoutException:
            print("Timeout: password field not found.")
            raise

    def click_login(self):
        try:
            login_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.login_button)
            )
            login_button.click()
        except TimeoutException:
            print("Timeout: login button not clickable.")
            raise

    def is_dashboard_loaded(self):
        try:
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.XPATH, "//h6[text()='Dashboard']"))
            )
            return True
        except TimeoutException:
            return False
