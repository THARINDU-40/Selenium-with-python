from LoginPageLocators import LoginPageLocators

class BasePage:
    def __init__(self, driver):
        self.driver = driver

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.locators = LoginPageLocators()

# class LoginPage(BasePage):
#     def __init__(self, driver):
#         super().__init__(driver)
#         self.locators = LoginPageLocators(driver)

    def load(self):
        self.driver.get("https://chinternal.caresystemsinc.com/Capital_Health_QA_Trunk/html_interface/staff/login.jsp")

    def enter_username(self, username):
        self.driver.find_element(*self.locators.USERNAME).clear()
        self.driver.find_element(*self.locators.USERNAME).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.locators.PASSWORD).clear()
        self.driver.find_element(*self.locators.PASSWORD).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.locators.LOGIN_BUTTON).click()
