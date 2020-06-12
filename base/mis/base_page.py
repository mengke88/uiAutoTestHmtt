"""
后台管理系统元素定位方法父类
"""

from utils import DriverUtils


# 对象库层—父类
class BasePage:
    # 获取元素驱动对象
    def __init__(self):
        self.driver = DriverUtils.get_mis_driver()

    # 公用元素定位的方法
    def find_elt(self, loc):
        return self.driver.find_element(*loc)


# 操作层——父类
class BaseHandle:
    # 公用模拟输入的方法啊,输入前先清空
    def input_text(self, loc, text):
        loc.clear()
        loc.send_keys(text)
