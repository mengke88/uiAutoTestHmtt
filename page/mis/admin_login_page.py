"""
后台管理登录页面
"""
from selenium.webdriver.common.by import By

from base.mis.base_page import BasePage, BaseHandle
from utils import DriverUtils


class LoginPage(BasePage):
    def __init__(self):
        super().__init__()
        # 账号名
        self.username = (By.NAME, "username")
        # 密码
        self.password = (By.NAME, "password")
        # 登录按钮
        self.login_btn = (By.CSS_SELECTOR, ".input_sub")

    def find_username(self):
        return self.find_elt(self.username)

    def find_password(self):
        return self.find_elt(self.password)

    def find_login_btn(self):
        return self.find_elt(self.login_btn)


# 操作层
class LoginHandle(BaseHandle):
    def __init__(self):
        self.login_page = LoginPage()

    # 输入用户名
    def input_username(self, username):
        self.input_text(self.login_page.find_username(), username)

    # 输入密码
    def input_password(self, password):
        self.input_text(self.login_page.find_password(), password)

    # 点击登录按钮,因为验证码是要点击滑动后才能点击，所以我们采用js删除限制不能点击元素的方法
    def click_login_btn(self):
        # 定义好删除属性值的js脚本
        js = "document.getElementById('inp1').removeAttribute('disabled')"
        # 执行js的方法
        DriverUtils.get_mis_driver().execute_script(js)
        # 点击登录按钮
        self.login_page.find_login_btn().click()


# 业务层
class LoginProxy:
    def __init__(self):
        self.login_handle = LoginHandle()

    # 实现登录功能
    def test_mis_login(self, username, password):
        self.login_handle.input_username(username)
        self.login_handle.input_password(password)
        self.login_handle.click_login_btn()
