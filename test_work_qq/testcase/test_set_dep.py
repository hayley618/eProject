import allure
from test_work_qq.page.main_page import MainPage

@allure.feature('设置部门')
class TestSetdep():
    @allure.story('设置部门成功')
    def test_set_dep(self):
        main_page = MainPage()
        dep_list = main_page.goto_contact().set_dep().get_contact_list_dep()
        assert "小海测试企业" in dep_list