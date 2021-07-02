import time
from selenium.webdriver.common.by import By
from test_work_qq.page.add_member_page import AddmemberPage
from test_work_qq.page.base_page import BasePage
from test_work_qq.page.contact_page import ContactPage


class MainPage(BasePage):
    def goto_contact(self):
        self.find(By.ID, 'menu_contacts').click()
        return ContactPage(self.driver)

    def goto_add_member(self):
        self.find(By.LINK_TEXT, '添加成员').click()
        time.sleep(5)
        # 返回要跳转页面的实例对象
        return AddmemberPage(self.driver)