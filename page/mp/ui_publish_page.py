"""
自媒体发布文章页面
"""
# 对象库层
from selenium.webdriver.common.by import By

from base.mp.base_page import BasePage, BaseHandle
from utils import DriverUtils, select_option


class PulPage(BasePage):
    def __init__(self):
        super().__init__()
        # 文章标题
        self.title = (By.CSS_SELECTOR, "[placeholder='文章名称']")
        # frame元素页面
        self.frame = (By.CSS_SELECTOR, "#publishTinymce_ifr")
        # 文章内容
        self.aritcal_content = (By.CSS_SELECTOR, "body")
        # 封面元素
        self.aritcal_cover = (By.XPATH, "//*[text()='自动']")
        # 下拉框
        self.channel = (By.CSS_SELECTOR, "[placeholder='请选择']")
        # 下拉框选项
        self.channel_option = (By.XPATH, "//*[text()='区块链']")
        # 发表
        self.publish_btn = (By.XPATH, "//*[text()='发表']")

    def find_title(self):
        return self.find_elt(self.title)

    def find_frame(self):
        return self.find_elt(self.frame)

    def find_ar_content(self):
        return self.find_elt(self.aritcal_content)

    def find_ar_cover(self):
        return self.find_elt(self.aritcal_cover)

    def find_channel(self):
        return self.find_elt(self.channel)

    def find_channel_option(self):
        return self.find_elt(self.channel_option)

    def find_publish_btn(self):
        return self.find_elt(self.publish_btn)


# 操作层
class PubHandle(BaseHandle):

    def __init__(self):
        self.pub_page = PulPage()
        # 因为切换iframe需要使用到driver，所以要实例化浏览器驱动对象
        self.driver = DriverUtils.get_mp_driver()

    # 输入文章标题
    def input_title(self, title):
        self.input_text(self.pub_page.find_title(), title)

    # 输入文章类内容
    def input_content(self, content):
        # 切换iframe
        self.driver.switch_to.frame(self.pub_page.find_frame())
        # 执行输入
        self.input_text(self.pub_page.find_ar_content(), content)
        # 返回默认主页
        self.driver.switch_to.default_content()

    # 选择封面
    def check_cover(self):
        self.pub_page.find_ar_cover().click()

    # 选择频道
    def check_channel(self, option):
        """
        因为选择频道不是下拉框，而是一种点击选择。所以我们没办法通过下拉拖拽定位来找到对应的选择内容
        所以我们封装一个通用的方法遍历这个选择框的所有元素，在utils里封装
        """
        # self.pub_page.find_channel().click()
        # self.pub_page.find_channel_option().click()
        # 调用封装好的获取选择框的方法
        select_option(self.driver, "请选择", option)

    # 点击发表
    def click_publish_btn(self):
        self.pub_page.find_publish_btn().click()


# 业务层
class PubProxy:
    def __init__(self):
        self.pub_handle = PubHandle()

    # 发布文章
    def test_pub_aritcal(self, title, content, option):
        # 1.输入文章标题
        self.pub_handle.input_title(title)
        # 2.输入内容
        self.pub_handle.input_content(content)
        # 3.选择封面
        self.pub_handle.check_cover()
        # 4.选择频道
        self.pub_handle.check_channel(option)
        # 5.点击发表
        self.pub_handle.click_publish_btn()
