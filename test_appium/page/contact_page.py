from test_appium.page.addmember_page import AddmemberPage
from test_appium.page.base_page import BasePage


class ContactPage(BasePage):

    def goto_add_member(self):
        self.swipe_find('添加成员').click()
        # self.find(MobileBy.ANDROID_UIAUTOMATOR,
        #                           'new UiScrollable(new UiSelector()'
        #                           '.scrollable(true).instance(0))'
        #                           '.scrollIntoView(new UiSelector().text("添加成员").instance(0));').click()
        return AddmemberPage(self.driver)