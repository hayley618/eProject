import Calculator
import pytest

@pytest.fixture(params = [[1,1,2],[0,0,0],[0.1,-0.1,0]],ids=['int1','zero','float'])
def get_add_datas(request):
    return request.param

def test_get_add_datas(get_add_datas):
    print(get_add_datas)


class TestAdd:
    def setup(self):
        self.cal = Calculator.Cal()

    def setup_class(self):
        print("开始计算")

    def teardown_class(self):
        print("计算结束")

    def test_add(self, get_add_datas):
        result = self.cal.add(get_add_datas[0], get_add_datas[1])
        print(result)
        assert get_add_datas[2] == round(result, 2)
        print("a+b=", result)


