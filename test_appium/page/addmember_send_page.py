# from test_appium.page.addmember_page import AddmemberPage   循环导入会报错，改成内部导入
import time
from appium.webdriver.common.mobileby import MobileBy
from test_appium.page.base_page import BasePage


class AddmemberSendPage(BasePage):

    __name_locator = (MobileBy.ID, 'com.tencent.wework:id/au0')
    __number_locator = (MobileBy.XPATH, '//*[@text="手机号"]')
    __level_locator = (MobileBy.XPATH, '//*[@text="普通成员"]')
    __level_selector = (MobileBy.XPATH, '//*[@text="上级"]')
    __save_button = (MobileBy.XPATH, '//*[@text="保存"]')

    def add_member_send(self, user, phonenum):
        # 输入各种成员信息，点击保存后返回添加成员页面
        from test_appium.page.addmember_page import AddmemberPage
        self.find(*self.__name_locator).send_keys(user)
        self.find(*self.__number_locator).send_keys(phonenum)
        self.find(*self.__level_locator).click()
        self.find(*self.__level_selector).click()
        self.find(*self.__save_button).click()
        return AddmemberPage(self.driver)
