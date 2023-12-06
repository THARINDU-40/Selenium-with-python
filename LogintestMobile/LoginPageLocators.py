from selenium.webdriver.common.by import By

class LoginPageLocators:
    USERNAME = (By.ID, "txtUsername")
    PASSWORD = (By.ID, "txtPassword")
    LOGIN_BUTTON = (By.CLASS_NAME, "btn-primary")

