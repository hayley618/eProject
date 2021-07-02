from appium import webdriver
from test_appium.page.base_page import BasePage
from test_appium.page.main_page import MainPage


class App(BasePage):
    def start(self):
        if self.driver == None:
            print("self.driver==None,初始化driver")
            self.log.info("self.driver==None,初始化driver")
            caps = {}
            caps['platformName'] = 'Android'
            caps['platformVersion'] = '6.0.1'
            caps['deviceName'] = 'MuMu'
            caps['appPackage'] = 'com.tencent.wework'
            caps['appActivity'] = '.launch.WwMainActivity'
            caps['unicodeKeyboard'] = 'true'
            caps['resetKeyboard'] = 'true'  # 中文输入
            caps['noReset'] = 'true'    # 不重置环境
            caps['dontStopAppOnReset'] = 'true'  # 启动之前不停止app
            # caps['skipServerInstallation'] = 'true'  # 跳过 uiautomator2 server的安装
            caps['skipDeviceInitialization'] = 'true'  # 跳过设备初始化
            caps['settings[waitForIdleTimeout]'] = 0  # 等待页面空闲的时间
            self.driver = webdriver.Remote('http://localhost:4723/wd/hub', caps)
            self.driver.implicitly_wait(15)
        else:
            print("已有driver，复用")
            self.log.info("已有driver，复用")
            self.driver.launch_app()
        return self

    def restart(self):
        self.log.info("关闭app")
        self.driver.close_app()
        self.log.info("启动app")
        self.driver.launch_app()

    def back(self):
        self.log.info("返回上一级")
        self.driver.back()

    def stop(self):
        self.driver.quit()

    def goto_main(self):
        # 进入首页
        return MainPage(self.driver)