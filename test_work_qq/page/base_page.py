import yaml
from selenium import webdriver

class BasePage:
    def __init__(self, base_driver=None):
        if base_driver == None:
            self.driver = webdriver.Chrome()
            self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx")
            self.driver.maximize_window()
            with open("../testcase/data.yaml", encoding="UTF-8") as f:
                yaml_data = yaml.safe_load(f)
                for cookie in yaml_data:
                    self.driver.add_cookie(cookie)
            self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
            self.driver.implicitly_wait(3)
        else:
            self.driver = base_driver

    def find(self, by, ele=None):
        # 如果传入元组，就需要解包
        # 比如传入（By.ID, 'username'），*by就是把这个数据解包
        if ele == None:
            return self.driver.find_element(*by)
        else:
            return self.driver.find_element(by, ele)

    def finds(self, by, ele=None):
        if ele == None:
            return self.driver.find_elements(*by)
        else:
            return self.driver.find_elements(by, ele)