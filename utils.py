"""
获取浏览器驱动的工具类
"""
import time

import appium.webdriver
import selenium.webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


# 选择频道的公用方法
def select_option(driver, channel_element, option):
    """
    这是一个选择框无法向下拉框那样去选择元素的定位选择的方法
    :param driver: 调用时需要传入浏览器驱动对象
    :param channel_elemen: 下拉选择栏元素的队形的placeholder的属性值
    :param option: 目标选择名称
    :return:
    """
    # 点击选项栏
    xpath = "//*[contains(@placeholder,'{}')]".format(channel_element)
    driver.find_element_by_xpath(xpath).click()
    option_list = driver.find_elements_by_css_selector(".el-select-dropdown__item span")
    is_element = False
    # 遍历元素对象的文本
    for i in option_list:
        # 判断遍历的目标是否和我们需要选择的对象目标是否相等,相等就执行点击操作
        if i.text == option:
            i.click()
            is_element = True
            break
        # 如果不相等则鼠标悬停到对应选项，执行下一个向下按键的操作
        else:
            ActionChains(driver).move_to_element(i).send_keys(Keys.DOWN).perform()
            is_element = False
    # 如果翻到最后还未找到该选项则抛出异常提示找不到选项
    if is_element is False:
        NoSuchElementException("can't find {} option".format(option))


# # 根据文本判断元素是否存在的公用元素
# def element_is_exist(driver, text):
#     """
#
#     :param driver: 表示调用该方法需要传入浏览器驱动对象，因为这个页面也需要元素定位
#     :param text: 表示你需要他断言页面的神门文本
#     :return:
#     """
#     # 定义判断找元素xpath的表达式
#     xpath = "//*[contains(text(),'{}')]".format(text)
#     try:
#         # 根据xpath表达式去查找操作后页面是该元素
#         element = driver.find_element(By.XPATH, xpath)
#         # 如果找的到则返回不为空
#         return element is not None
#     # 如果找不到则返回False
#     except Exception as e:
#         print("NoSuchElement text is {} element".format(text))
#         return False

# 根据文本/属性判断元素是否存在的公用函数
def element_is_exist(driver, attr=None, text=None):
    """
    因为以上面的方法来实现定位，web端是以文本形式进行定位text(),但是移动端是以@text()属性值进行定位，所以我们需要加一个判断条件
    用于区分移动端和web端不同定位方式

    :param driver:驱动对象
    :param attr: 需要使用属性找元素的时候才需要传递
    :param text: 如果传了attr属性名，则text表示的是属性值，如果没传attr参数，则text表示
    元素的文本
    :return:
    """
    # attr表示属性值，为空时，用于web端文本定位方式
    if attr is None:
        # 定义找元素xpath的表达式
        xpath = "//*[contains(text(),'{}')]".format(text)
    # 不为空时用于移动端的属性值定位
    else:
        # 定义找元素属性的xpath的表达式
        xpath = "//*[contains(@{},'{}')]".format(attr, text)
    try:
        # 根据xpath表达式去查找操作之后页面是的该元素
        element = driver.find_element(By.XPATH, xpath)
        # 如果找的到则返回不为空
        return element is not None
        # 如果找不到则返回False
    except Exception as e:
        print("NoSuchElement text is {} element".format(text))
        return False


class DriverUtils:
    """定义私有变量，用于判断浏览器"""
    # Mp 自媒体
    __mp_driver = None
    # MIS 后台管理系统
    __mis_driver = None
    # App 移动端
    __app_driver = None

    # MP开关
    __mp_key = True
    __mis_key = True

    # 修改mp开关的方法
    @classmethod
    def change_mp_key(cls, key):
        cls.__mp_key = key

    @classmethod
    def change_mis_key(cls, key):
        cls.__mis_key = key

    # 获取自媒体浏览器驱动
    @classmethod
    def get_mp_driver(cls):
        if cls.__mp_driver is None:
            cls.__mp_driver = selenium.webdriver.Chrome()
            cls.__mp_driver.maximize_window()
            cls.__mp_driver.implicitly_wait(30)
            cls.__mp_driver.get("http://ttmp.research.itcast.cn/")
        return cls.__mp_driver

    # 关闭自媒体浏览器驱动
    @classmethod
    def quit_mp_driver(cls):
        if cls.__mp_driver is not None and cls.__mp_key:
            time.sleep(2)
            cls.__mp_driver.quit()
            cls.__mp_driver = None

    # 获取后台管理系统浏览器驱动
    @classmethod
    def get_mis_driver(cls):
        if cls.__mis_driver is None:
            cls.__mis_driver = selenium.webdriver.Chrome()
            cls.__mis_driver.maximize_window()
            cls.__mis_driver.implicitly_wait(30)
            cls.__mis_driver.get("http://ttmis.research.itcast.cn/")
        return cls.__mis_driver

    # 关闭后台管理系统浏览器驱动
    @classmethod
    def quit_mis_driver(cls):
        if cls.__mis_driver is not None and cls.__mis_key:
            time.sleep(2)
            cls.__mis_driver.quit()
            cls.__mis_driver = None

    # 获取移动端浏览器驱动
    @classmethod
    def get_app_driver(cls):
        if cls.__app_driver is None:
            cap = {
                "platformName": "Android",
                "deviceName": "emulator",
                "appPackage": "com.itcast.toutiaoApp",
                "appActivity": ".MainActivity",
                "noReset": True
            }
            cls.__app_driver = appium.webdriver.Remote("http://127.0.0.1:4723/wd/hub", cap)
            cls.__app_driver.implicitly_wait(30)
        return cls.__app_driver

    # 关闭移动端浏览器驱动
    @classmethod
    def quit_app_driver(cls):
        if cls.__app_driver is not None:
            time.sleep(2)
            cls.__app_driver.quit()
            cls.__app_driver = None
