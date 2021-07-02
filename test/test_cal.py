import pytest
import yaml
from test import Calculator
import allure
data = yaml.safe_load(open("../datas/data_cal.yaml"))

@allure.feature('计算器测试')
class TestCal:

    def setup(self):
        self.cal = Calculator.Cal()

    # 相加
    @allure.story('相加')
    @pytest.mark.run(order=-1)
    @pytest.mark.parametrize('a,b,expect', data["add"])
    def test_add(self, open, a, b, expect):
        result = self.cal.add(a, b)     # 实际结果
        assert expect == round(result, 2)   # 保留2位小数
        print("a+b=", result)

    # 相除
    @allure.story('相除')
    @pytest.mark.run(order=2)
    @pytest.mark.parametrize('a,b,expect', data["div"])
    def test_div(self, open, a, b, expect):
        try:
            result = self.cal.div(a, b)
            assert expect == round(result, 2)
            print("a/b=", result)
        except ZeroDivisionError:
            print("fail，除数不能为0")

    # 相减
    @allure.story('相减')
    @pytest.mark.run(order=1)
    @pytest.mark.parametrize('a,b,expect', data["sub"])
    def test_sub(self, open, a, b, expect):
        result = self.cal.sub(a, b)
        assert expect == round(result, 2)
        print("a-b=", result)

    # 相乘
    @allure.story('相乘')
    @pytest.mark.run(order=-2)
    @pytest.mark.parametrize('a,b,expect', data["multi"])
    def test_multi(self, open, a, b, expect):
        result = self.cal.multi(a, b)
        assert expect == round(result, 2)
        print("a*b=", result)

