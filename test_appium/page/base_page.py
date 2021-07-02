import datetime
import logging
import os
import time

from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException

logging.basicConfig(level=logging.INFO)
class BasePage:
    def __init__(self, driver: WebDriver = None):
        self.driver = driver
        self.log = logging.getLogger(__name__)
        # 将日志记录发送到控制台
        # self.sh = logging.StreamHandler(stream=None)
        # 设置日志的输出格式
        self.format = logging.Formatter("%(asctime)s--%(levelname)s--%(process)d--%(thread)d--%(threadName)s--%(funcName)s--%(lineno)d--%(lineno)d : %(message)s")  # 两个参数是用来设置日志格式和时间格式
        # now = time.time()
        # local_time = time.localtime(now)
        # file_name = time.strftime('%Y-%m-%d %H%M', local_time)
        # 将日志记录发送到磁盘文件
        self.fh = logging.FileHandler('../log/log.txt', mode='w+', encoding="utf-8", delay=False)
        self.fh.setFormatter(self.format)
        # 将日志添加到log.txt
        self.log.addHandler(self.fh)


    def find(self, by, value=None):
        self.log.info(f"定位方式为{by}")
        self.log.info(f"定位元素为{value}")

        # 如果传入元组，就需要解包
        # 比如传入（By.ID, 'username'），*by就是把这个数据解包
        if value == None:
            return self.driver.find_element(*by)
        else:
            return self.driver.find_element(by, value)

    def finds(self, by, value=None):
        if value == None:
            return self.driver.find_elements(*by)
        else:
            return self.driver.find_elements(by, value)

    def swipe_find(self, text, num=5):
        self.driver.implicitly_wait(1)
        # num:默认查找次数
        for i in range(num):
        # while True:
            try:
                ele = self.driver.find_element(MobileBy.XPATH, f'//*[@text="{text}"]')
                self.driver.implicitly_wait(5)
                return ele
            except NoSuchElementException:
                print("未找到，滑动")
                size = self.driver.get_window_size()
                width = size['width']
                height = size['height']
                start_x = width * 0.5
                end_x = start_x
                start_y = height * 0.8
                end_y = height * 0.2
                duration = 2000    # ms
                self.driver.swipe(start_x, start_y, end_x, end_y, duration)
            if i == num-1:
                self.driver.implicitly_wait(5)
                self.log.info(f"找了{i+1}次，没有找到")
                raise NoSuchElementException(f"找了{i+1}次，没有找到")

