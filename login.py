import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from HtmlTestRunner import HTMLTestRunner

class LoginTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.options = FirefoxOptions()
        cls.options.add_argument("--start-maximized")
        cls.driver = webdriver.Firefox()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_login_success(self):
        is_passed = self.login_testcase("Rcanada", "admin")
        self.assertTrue(is_passed)

    def test_login_failure(self):
        is_passed = self.login_testcase("Vcanada", "admin")
        self.assertFalse(is_passed)

    def test_login_admin(self):
        is_passed = self.login_testcase("admin", "admin")
        self.assertFalse(is_passed)

    def login_testcase(self, username, password):
        self.driver.get("https://chinternal.caresystemsinc.com/Capital_Health_QA_Trunk/html_interface/staff/login.jsp")
        username_text = self.driver.find_element(by=By.ID, value="txtUsername")
        password_text = self.driver.find_element(by=By.ID, value="txtPassword")
        login_btn = self.driver.find_element(by=By.CLASS_NAME, value="btn-primary")
        username_text.send_keys(username)
        password_text.send_keys(password)
        login_btn.click()
        time.sleep(5)

        is_passed = False
        try:
            message_box = self.driver.find_element(by=By.ID, value="messagebox_modal")
            if message_box is not None:
                message_title = self.driver.find_element(by=By.ID, value="messagebox_title")
                message_text = message_title.text
                if message_text == "Confirm":
                    is_passed = True
                
        except:
            is_passed = 'dashboard.jsp' in self.driver.current_url

        return is_passed

if __name__ == "__main__":
    unittest.main(testRunner=HTMLTestRunner(output='reports'))
