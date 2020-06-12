"""
后台登录首页,并操作进入内容审核页面
"""
"""
后台管理登录页面
"""
from selenium.webdriver.common.by import By

from base.mis.base_page import BasePage, BaseHandle
from utils import DriverUtils

class HomePage(BasePage):
    def __init__(self):
        super().__init__()
        # 点击信息管理
        self.message_ment = (By.XPATH, "//*[text()='信息管理']")
        # 点击内容审核
        self.message_audit = (By.XPATH, "//*[text()='内容审核']")

    # 定位查找方法
    def find_message_ment(self):
        return self.find_elt(self.message_ment)

    def find_message_audit(self):
        return self.find_elt(self.message_audit)


# 操作层
class HomeHandle(BaseHandle):
    def __init__(self):
        # 实例化对象库层的类
        self.login_page = HomePage()
        # 获取浏览器驱动对象，用于下拉选择对象使用
        self.driver = DriverUtils.get_mis_driver()

    # 点击内容管理
    def click_message_ment(self):
        self.login_page.find_message_ment().click()

    # 点击内容审核
    def click_message_audit(self):
        self.login_page.find_message_audit().click()


# 业务层
class HomeProxy:
    def __init__(self):
        self.home_handle = HomeHandle()

    # 实现后台首页的业务实现
    def test_home_proxy(self):
        self.home_handle.click_message_ment()
        self.home_handle.click_message_audit()
