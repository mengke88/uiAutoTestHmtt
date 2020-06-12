"""
自媒体元素定位方法父类
"""

from utils import DriverUtils


# 对象库层—父类
class BasePage:
    # 获取元素驱动对象
    def __init__(self):
        self.driver = DriverUtils.get_mp_driver()

    def find_elt(self, loc):
        """
        # 公用元素定位的方法
        :param loc: loc表示传入定位方式By.id这些和定位元素
        :return:
        """
        return self.driver.find_element(*loc)


# 操作层——父类
class BaseHandle:

    def input_text(self, element, text):
        """
        # 公用模拟输入的方法啊,输入前先清空
        :param element: 表示定位的方式
        :param text: 输入的文本信息
        :return:
        """
        element.clear()
        element.send_keys(text)
