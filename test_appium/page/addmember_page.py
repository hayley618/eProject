from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver

from test_appium.page.addmember_send_page import AddmemberSendPage
from test_appium.page.base_page import BasePage


class AddmemberPage(BasePage):
    __method_add = (MobileBy.XPATH, '//*[contains(@text,"手动")]')
    __toast_locator = (MobileBy.XPATH, '//*[@text="添加成功"]')
    def addmember_send(self):
        # 手动输入添加
        self.find(*self.__method_add).click()
        return AddmemberSendPage(self.driver)
    def find_toast(self):
        self.find(*self.__toast_locator)