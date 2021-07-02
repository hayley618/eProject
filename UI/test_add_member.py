import time
import yaml
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestAddmember():
    def setup(self):
        self.driver = webdriver.Chrome()

    def teardown(self):
        self.driver.quit()

    def test_add_member(self):
        self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx")
        with open("../test_work_qq/testcase/data.yaml", encoding="UTF-8") as f:
            yaml_data = yaml.safe_load(f)
            for cookie in yaml_data:
                self.driver.add_cookie(cookie)
            self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
            time.sleep(5)
            self.driver.find_element(By.LINK_TEXT, '添加成员').click()
            time.sleep(5)
            self.driver.find_element(By.ID, 'username').send_keys('smile')
            self.driver.find_element(By.ID, 'memberAdd_acctid').send_keys('18842361111')
            self.driver.find_element(By.LINK_TEXT, '保存并继续添加').click()
