"""
后台管理文章审核页面
"""
import time

from selenium.webdriver.common.by import By

from base.mis.base_page import BasePage, BaseHandle
from utils import DriverUtils, select_option


class AuditPage(BasePage):
    def __init__(self):
        super().__init__()
        # 输入要审核的文章标题
        self.input_audit = (By.CSS_SELECTOR, "[placeholder='请输入: 文章名称']")
        # 结束按钮
        self.end_time = (By.CSS_SELECTOR, "[placeholder*='结束']")
        # 点击查询
        self.search_btn = (By.CSS_SELECTOR, ".find")
        # 点击审核通过
        self.aduit_ok = (By.XPATH, "//*[text()='通过']")
        # 确定通过按钮
        self.submit_btn = (By.CSS_SELECTOR, ".el-button--primary")

    def find_input_audit(self):
        return self.find_elt(self.input_audit)

    def find_search_option(self):
        return self.find_elt(self.search_btn)

    def find_end_time(self):
        return self.find_elt(self.end_time)

    def find_aduit_ok(self):
        return self.find_elt(self.aduit_ok)

    def find_submit_btn(self):
        return self.find_elt(self.submit_btn)


# 操作层
class HomeHandle(BaseHandle):
    def __init__(self):
        # 实例化对象库层的类
        self.login_page = AuditPage()
        # 获取浏览器驱动对象，用于下拉选择对象使用
        self.driver = DriverUtils.get_mis_driver()

    # 输入你要查询的内容
    def input_input_audit(self, text):
        self.input_text(self.login_page.find_input_audit(), text)

    # 去掉结束时间的筛选条件
    def click_end_time(self):
        self.login_page.find_end_time().clear()

    # 调用时输入要筛选的对象
    def select_option(self, option):
        select_option(self.driver, "请选择状态", option)

    # 点击查询
    def click_search_btn(self):
        self.login_page.find_search_option().click()

    # 点击审核通过按钮
    def click_aduit_ok(self):
        self.login_page.find_aduit_ok().click()

    # 点击确定按钮
    def click_submit_btn(self):
        self.login_page.find_submit_btn().click()


# 业务层
class AuditProxy:
    def __init__(self):
        self.home_handle = HomeHandle()

    # 实现后台首页的业务实现,审核文章
    def test_audit_proxy(self, text):
        # 输入文章名称
        self.home_handle.input_input_audit(text)
        # 选择待审核
        self.home_handle.select_option("待审核")
        # 清空结束时间
        self.home_handle.click_end_time()
        # 点击查询按钮
        self.home_handle.click_search_btn()
        # 点击审核通过按钮
        self.home_handle.click_aduit_ok()
        # 点击确定按钮
        self.home_handle.click_submit_btn()
        time.sleep(2)
        # 选择审核通过
        self.home_handle.select_option("审核通过")
        # 点击查询
        self.home_handle.click_search_btn()
