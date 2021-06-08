import pytest
import yaml
import Calculator

data = yaml.safe_load(open("../datas/data_cal.yaml"))


class TestCal:

    def setup(self):
        self.cal = Calculator.Cal()

    def setup_class(self):
        print("开始计算")

    def teardown_class(self):
        print("计算结束")


    # 相加
    @pytest.mark.parametrize('a,b,expect', data["add"])
    def test_add(self, a, b, expect):
        result = self.cal.add(a, b)
        assert expect == round(result, 2)
        print("a+b=", result)

    # 相除
    @pytest.mark.parametrize('a,b,expect', data["div"])
    def test_div(self, a, b, expect):
        try:
            result = self.cal.div(a, b)
            assert expect == round(result, 2)
            print("a/b=", result)
        except ZeroDivisionError:
            print("fail，除数不能为0")

    # 相减
    @pytest.mark.parametrize('a,b,expect', data["sub"])
    def test_sub(self, a, b, expect):
        result = self.cal.sub(a, b)
        assert expect == round(result, 2)
        print("a-b=", result)

    # 相乘
    @pytest.mark.parametrize('a,b,expect', data["multi"])
    def test_multi(self, a, b, expect):
        result = self.cal.multi(a, b)
        assert expect == round(result, 2)
        print("a*b=", result)

