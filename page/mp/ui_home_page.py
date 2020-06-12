"""
自媒体主页页面
"""
"""
自媒体登录页面文件
"""
from selenium.webdriver.common.by import By

from base.mp.base_page import BasePage, BaseHandle


# 对象库层
class HomePage(BasePage):

    # 1.定义初始化方法
    def __init__(self):
        super().__init__()
        # 2.将所需要操作的元素定义一个对应的实力属性
        # 3.实例属性存储元素by定位方式以及对应值
        # 内容管理
        self.content_manager = (By.XPATH, "//*[text()='内容管理']")
        # 发布文章
        self.publish_artical = (By.XPATH, "//*[contains(text(),'发布文章')]")

    # 定义找到元素的方法
    def find_manager(self):
        return self.find_elt(self.content_manager)

    def find_artical(self):
        return self.find_elt(self.publish_artical)


# 操作层
class HomeHandle:
    def __init__(self):
        self.home_page = HomePage()

    # 点击操作
    def click_manager(self):
        self.home_page.find_manager().click()

    def click_artical(self):
        self.home_page.find_artical().click()


# 业务层
class HomePorxy:

    def __init__(self):
        self.home_handle = HomeHandle()

    # 实现业务进入文章页面
    def to_publish_artical(self):
        self.home_handle.click_manager()
        self.home_handle.click_artical()
