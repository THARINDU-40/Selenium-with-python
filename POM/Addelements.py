from locators import locators

class AddElements():

    def __init__(self,driver):
        self.driver =driver 
        self.Add_elements_LinkText = locators.Add_elements_LinkText
        self.button_Tagname=locators.button_Tagname

    def clickAddelementsLink(self):
         self. driver.find_element_by.LINK_TEXT(self.Add_elements_LinkText).click()

    def clickAddelements(self):
         self. driver.find_element_by.TAG_NAME(self.button_Tagname).click()

