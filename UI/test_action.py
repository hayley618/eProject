import time

import pytest
from selenium import webdriver
# def test_selenium():
#     driver = webdriver.Chrome()
#     driver.get("https://www.baidu.com/")
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestActionChains():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.action = ActionChains(self.driver)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()

    def test_click(self):
        self.driver.get("https://sahitest.com/demo/clicks.htm")
        element_click = self.driver.find_element(By.XPATH, '//input[3]')
        element_rightclick = self.driver.find_element(By.XPATH, '//input[4]')
        element_doubleclick = self.driver.find_element(By.XPATH, '//input[2]')
        self.action.click(element_click).perform()
        # WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(By.XPATH.''))
        time.sleep(3)
        self.action.double_click(element_doubleclick).perform()
        time.sleep(3)
        self.action.context_click(element_rightclick)
        time.sleep(3)

    def test_move_to(self):
        self.driver.get("https://www.baidu.com/")
        ele = self.driver.find_element(By.ID, "s-usersetting-top")
        self.action.move_to_element(ele).perform()
        time.sleep(3)

    def test_drag(self):
        self.driver.get("https://sahitest.com/demo/dragDropMooTools.htm")
        ele_drag = self.driver.find_element(By.ID, "dragger")
        ele_drop1 = self.driver.find_element(By.XPATH, "//div[2]")
        ele_drop2 = self.driver.find_element(By.XPATH, "//div[3]")
        ele_drop3 = self.driver.find_element(By.XPATH, "//div[4]")
        self.action.drag_and_drop(ele_drag, ele_drop1).perform()
        time.sleep(3)
        self.action.click_and_hold(ele_drag).release(ele_drop2).perform()
        time.sleep(3)
        self.action.click_and_hold(ele_drag).move_to_element(ele_drop3).release().perform()
        time.sleep(3)

    def test_label(self):
        self.driver.get("https://sahitest.com/demo/label.htm")
        ele1 = self.driver.find_element(By.XPATH, "//label/input")
        self.action.click(ele1).perform()
        # ele1.click()
        self.action.send_keys('username' + Keys.SPACE + 'tom').pause(1)
        self.action.send_keys(Keys.BACK_SPACE).perform()
        time.sleep(3)

# if __name__ == '__main__':
#     pytest.main(['-v', '-s', 'test_action.py'])
