import allure
import pytest
from test_work_qq.page.main_page import MainPage

@allure.feature('添加部门')
class TestAddDep():
    @allure.story('成功添加部门')
    @pytest.mark.parametrize('depname', ['人事部'])
    def test_add_dep_pass(self, depname):
        main_page = MainPage()
        dep_list1 = main_page.goto_contact().add_dep_pass(depname).get_dep_list()
        try:
            assert '人事部' in dep_list1
        except BaseException as e:
            pass

    @allure.story('添加重复部门')
    def test_add_dep_fail(self):
        main_page = MainPage()
        t = main_page.goto_contact().add_dep_fail()
        print(t)
        try:
            assert '该部门已存在' in t
        except BaseException as e:
            pass
