from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest
from Addelements import AddElements
from HtmlTestRunner import HTMLTestRunner

class AddelememtsTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get("https://the-internet.herokuapp.com/")
        cls.driver.maximize_window()
    
    def test_Add_element(self):

        driver =self.driver
        add= AddElements(driver)
        add.clickAddelementsLink
        add.clickAddelements
        time.sleep(2)
        
    @classmethod
    def tear_down(cls):
        cls.driver.quit()
        cls.print("Test completed") 



if __name__ == "__main__":
    unittest.main(testRunner=HTMLTestRunner(output='reports'))