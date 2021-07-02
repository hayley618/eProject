import time
from selenium.webdriver.common.by import By
from test_work_qq.page.base_page import BasePage
from test_work_qq.page.contact_page import ContactPage


class AddmemberPage(BasePage):
    # 设定为元组
    # 页面元素定位不需要全部展示，所以设置为私有
    __ele_username = (By.ID, 'username')
    __ele_acctid = (By.ID, 'memberAdd_acctid')
    __ele_phone = (By.ID, 'memberAdd_phone')
    def add_member(self, username, acctid, phone):
        # *的作用：解元组
        self.find(*self.__ele_username).send_keys(username)
        self.find(*self.__ele_acctid).send_keys(acctid)
        self.find(*self.__ele_phone).send_keys(phone)
        self.find(By.LINK_TEXT, '保存').click()
        time.sleep(3)
        return ContactPage(self.driver)

    def add_member_fail(self, username, acctid, phone):
        # *的作用：解元组
        self.driver.find_element(*self.__ele_username).send_keys(username)
        self.driver.find_element(*self.__ele_acctid).send_keys(acctid)
        self.driver.find_element(*self.__ele_phone).send_keys(phone)
        self.driver.find_element(By.LINK_TEXT, '保存').click()
        time.sleep(3)
        ele_fail_list = []
        ele_fails = self.driver.find_elements(By.CSS_SELECTOR, '.ww_inputWithTips_tips')
        for ele_fail in ele_fails:
            ele_fail_list.append(ele_fail.text)
        print(ele_fail_list)
        return ele_fail_list