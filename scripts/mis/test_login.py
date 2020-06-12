"""
后台登录系统登录页面测试
"""
# 1.定义测试类
import pytest

from page.mis.admin_login_page import LoginProxy
from utils import DriverUtils, element_is_exist


@pytest.mark.run(order=102)
class TestMisLogin:

    # 2.定义初始化方法
    def setup_class(self):
        self.mis_proxy = LoginProxy()
        self.driver = DriverUtils.get_mis_driver()

    # 4.定义测试用例的方法
    def test_login(self):
        # 5.定义测试数据
        username = "testid"
        password = "testpwd123"
        # 6.调用业务的方法
        self.mis_proxy.test_mis_login(username, password)
        # 7.执行断言结果
        msg = element_is_exist(self.driver, "用户管理")
        assert msg

    # 3.定义销毁的方法
    def teardown_class(self):
        DriverUtils.quit_mis_driver()
