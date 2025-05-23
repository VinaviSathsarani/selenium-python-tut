import unittest
import csv
import time
import HtmlTestRunner
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from login_page import LoginPage

class TestLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("Launching Chrome browser...")

        chrome_options = Options()
        chrome_options.add_experimental_option("prefs", {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False
        })
        chrome_options.add_argument("--disable-infobars")
        chrome_options.add_argument("--disable-notifications")

        cls.driver = webdriver.Chrome(options=chrome_options)
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        print("Tests finished. Keeping browser open for 10 seconds...")
        time.sleep(10)
        cls.driver.quit()

    def setUp(self):
        self.login_page = LoginPage(self.driver)
        self.url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
        self.driver.get(self.url)

    def test_login_from_csv(self):
        with open('D:/SeleniumPython/DDTLogin/login_data.csv', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                username = row['username']
                password = row['password']
                expected = row['expected_result']

                with self.subTest(username=username):
                    print(f"\n--- Testing with: {username} / {password} ---")
                    self.login_page.enter_username(username)
                    self.login_page.enter_password(password)
                    self.login_page.click_login()

                    time.sleep(3)

                    is_logged_in = self.login_page.is_dashboard_loaded()

                    if expected == "success":
                        self.assertTrue(is_logged_in, f"Expected success but failed for user {username}")
                    else:
                        self.assertFalse(is_logged_in, f"Expected failure but succeeded for user {username}")

                    self.driver.delete_all_cookies()
                    self.driver.get(self.url)
                    time.sleep(1)

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='reports'))
