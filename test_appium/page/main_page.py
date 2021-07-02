from appium.webdriver.common.mobileby import MobileBy
from test_appium.page.base_page import BasePage
from test_appium.page.contact_page import ContactPage

class MainPage(BasePage):
    __contact_element = (MobileBy.XPATH, '//*[@text="通讯录"]')
    def goto_contactlist(self):
        self.find(*self.__contact_element).click()
        return ContactPage(self.driver)