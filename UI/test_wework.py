import time

import yaml
from selenium import webdriver
from selenium.webdriver.common.by import By

# 浏览器复用(获取cookie)
class TestWework():
    def test_wework(self):
        opt = webdriver.ChromeOptions()
        opt.debugger_address = "127.0.0.1:9221"
        self.driver = webdriver.Chrome(options=opt)
        self.driver.implicitly_wait(3)
        self.driver.find_element(By.ID, "menu_contacts").click()
        # 获取cookie信息
        cookie = self.driver.get_cookies()
        # 以写方式把cookie存入yaml文件内
        with open('../test_work_qq/testcase/data.yaml', 'w', encoding='UTF-8') as f:
            yaml.dump(cookie, f)


# 直接传入cookie
def test_cookie_v1():
    driver = webdriver.Chrome()
    driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx")
    cookies = [{'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False, 'value': '5LjB8YKUGg56D-BGhKg3whx9i-K3n9YFLQiSV3qQnuX3LGhmbHKi-amXPpoyg8akcztZWmjAISrAA23C6FJbZGPZjMuow2fjLaJ3hslpktL4G3nK4YgaybvzmAkaelzAu5Ca7pjjOZoVBKueHu9X2J6eUWrSwVoTr7kGE9XgLmlPZMnnhSr0HCFsrbUiBIJ1DUJdYJs2whvpHjhfL1rZA_pa2o23UWRWb4Xukc1og74igoUDJlnwRkJVSjOFexp4eS7PX1ueYIHEtDhxpA1UIQ'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False, 'value': '1688852019807904'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False, 'value': '1970325069369901'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False, 'value': 'fJfI94fJB0G0fvGGqmRwVG03NZv_lep_wefDTqZwA1KP1f8u-tfJ96Zy3UtMpf_s'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False, 'value': 'a1188730'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False, 'value': '11677425763482727'}, {'domain': '.qq.com', 'expiry': 1686905898, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False, 'value': 'GA1.2.2123587250.1623831765'}, {'domain': '.work.weixin.qq.com', 'expiry': 1651218113.037796, 'httpOnly': False, 'name': 'wwrtx.c_gdpr', 'path': '/', 'secure': False, 'value': '0'}, {'domain': '.qq.com', 'expiry': 1886044514.802936, 'httpOnly': False, 'name': 'pac_uid', 'path': '/', 'secure': False, 'value': '0_5d9ebe6236d2e'}, {'domain': '.work.weixin.qq.com', 'expiry': 1626426064.05642, 'httpOnly': False, 'name': 'wwrtx.i18n_lan', 'path': '/', 'secure': False, 'value': 'zh'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False, 'value': 'direct'}, {'domain': '.work.weixin.qq.com', 'expiry': 1655369145, 'httpOnly': False, 'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1623831764,1623833146'}, {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/', 'secure': False, 'value': '1021195500'}, {'domain': '.qq.com', 'expiry': 1623920298, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False, 'value': 'GA1.2.98227703.1623831765'}, {'domain': 'work.weixin.qq.com', 'expiry': 1623863284.145311, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/', 'secure': False, 'value': '3keb9hg'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False, 'value': '1688852019807904'}, {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'fqm_pvqid', 'path': '/', 'secure': False, 'value': 'e56b44dc-a822-49d5-9cc7-fd1e7bdc2539'}, {'domain': '.qq.com', 'expiry': 1868588759, 'httpOnly': False, 'name': 'tvfe_boss_uuid', 'path': '/', 'secure': False, 'value': 'e638e22a717785e9'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.cs_ind', 'path': '/', 'secure': False, 'value': ''}, {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvi', 'path': '/', 'secure': False, 'value': '5784838144'}, {'domain': '.qq.com', 'expiry': 2147483648.377872, 'httpOnly': False, 'name': 'ptcz', 'path': '/', 'secure': False, 'value': '65883b144a5430b64649c89963597b95cfe489c8ae8452e79d2a865fe901e13a'}, {'domain': '.qq.com', 'expiry': 2147483647.302731, 'httpOnly': False, 'name': 'RK', 'path': '/', 'secure': False, 'value': 'MBiluYYRO/'}]
    for cookie in cookies:
        driver.add_cookie(cookie)
    driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts")
    time.sleep(5)

# 以yaml格式打开cookie
def test_cookie_v2():
    driver = webdriver.Chrome()
    driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx")
    # 打开yaml文件(cookies)
    with open("../test_work_qq/testcase/data.yaml", encoding="UTF-8") as f:
        yaml_data = yaml.safe_load(f)
        for cookie in yaml_data:
            driver.add_cookie(cookie)   # cookie添加到driver里
        driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        time.sleep(5)
        driver.find_element(By.LINK_TEXT, '添加成员').click()
        time.sleep(5)
        driver.find_element(By.ID, 'username').send_keys('肖可可')
        driver.find_element(By.ID, 'memberAdd_acctid').send_keys('16643257101')
        driver.find_element(By.LINK_TEXT, '保存并继续添加').click()