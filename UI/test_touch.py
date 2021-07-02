import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestTouch():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.action = webdriver.TouchActions(self.driver)

    def teardown(self):
        self.driver.quit()

    def test_touch(self):
        self.driver.get("https://www.baidu.com/")
        ele_search = self.driver.find_element(By.ID, "kw")
        ele_search.click()
        ele_search.send_keys("selenium测试")
        time.sleep(3)
        ele_click = self.driver.find_element(By.ID, "su")
        self.action.tap(ele_click).perform()
        ele_bottom = self.driver.find_element(By.XPATH, "//*[@id='page']//a[last()]")
        self.action.scroll_from_element(ele_click, 0, 1000).perform()
        time.sleep(3)
        self.action.tap(ele_bottom).perform()
        time.sleep(3)

