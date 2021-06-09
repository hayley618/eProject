import pytest
@pytest.fixture(scope="session")
def open():
    print("开始计算")
    yield
    print("执行teardown!")
    print("计算结束")

# hook函数
# def pytest_collection_modifyitems(session, config, items):
#     print("这是收集所有测试用例的方法")
#     print(items)
#     items.reverse()