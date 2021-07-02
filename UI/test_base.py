from UI.browser_switch import Base

class TestBase(Base):
    def test_base(self):
        self.driver.get("http://www.baidu.com")
