import allure
import pytest
from test_work_qq.page.main_page import MainPage

@allure.feature('添加成员')
class TestAddmember():
    # 实现测试数据和页面对象分离
    @allure.story('成功添加成员')
    @pytest.mark.parametrize("username, acctid, phone", [("娜娜1", "11112", "13164197419")])
    def test_addmember_pass(self, open, username, acctid, phone):
        with allure.step('step1: 进入首页'):
            main_page = MainPage()
        with allure.step('step2: 点击添加成员——添加成员成功'):
            name_list = main_page.goto_add_member().add_member(username, acctid, phone).get_contact_list_name()
        with allure.step('step3: 断言（列表显示此成员名称）'):
            assert username in name_list

    @allure.story('添加成员手机号重复')
    @pytest.mark.parametrize("username, acctid, phone", [("小可爱", "1101", "18364197412")])
    # @pytest.fixture(ids='成员添加失败')
    def test_addmember_fail(self, open, username, acctid, phone):
        with allure.step('step1: 进入首页'):
            main_page = MainPage()
        with allure.step('step2: 点击添加成员——添加成员失败（手机号重复）'):
            ele_fail_list = main_page.goto_add_member().add_member_fail(username, acctid, phone)
        with allure.step('step3: 断言（手机号已被占用）'):
            for ele_fail in ele_fail_list:
                if ele_fail != "":
                    print(ele_fail)
                    assert '西西1' in ele_fail


