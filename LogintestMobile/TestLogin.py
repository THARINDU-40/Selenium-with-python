import unittest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from HtmlTestRunner import HTMLTestRunner
from LoginPage import LoginPage
from LoginPageLocators import LoginPageLocators

class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.options = FirefoxOptions()
        cls.options.add_argument("--start-maximized")
        cls.driver = webdriver.Firefox()
        cls.login_page = LoginPage(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_login_success(self):
        self.login_page.load()
        self.login_page.enter_username("Rcanada")
        self.login_page.enter_password("admin")
        self.login_page.click_login()
        self.assertTrue('dashboard.jsp' in self.driver.current_url)

    def test_login_failure(self):
        self.login_page.load()
        self.login_page.enter_username("Vcanada")
        self.login_page.enter_password("admin")
        self.login_page.click_login()
        self.assertFalse('dashboard.jsp' in self.driver.current_url)

    def test_login_admin(self):
        self.login_page.load()
        self.login_page.enter_username("admin")
        self.login_page.enter_password("admin")
        self.login_page.click_login()
        self.assertFalse('dashboard.jsp' in self.driver.current_url)

if __name__ == "__main__":
    unittest.main(testRunner=HTMLTestRunner(output='reports'))
