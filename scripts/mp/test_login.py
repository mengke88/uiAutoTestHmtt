"""
自媒体登录页面测试用例文件，使用request
"""
import pytest

from page.mp.ui_login_page import LoginPorxy
from utils import DriverUtils, element_is_exist


# 1.定义测试类
@pytest.mark.run(order=2)
class TestLogin:
    # 2.定义初始化方法
    def setup_class(self):
        self.driver = DriverUtils.get_mp_driver()
        self.login_proyx = LoginPorxy()

    # 4.定义测试用例方法
    def test_login(self):
        # 5.定义测试数据
        mobile = "15077632873"
        code = "246810"
        # 6.调用业务方法
        self.login_proyx.test_login(mobile, code)
        # 7.执行断言结果
        msg = element_is_exist(self.driver, "江苏传智播客教育科技股")
        assert msg

    # 3. 定义销毁方法
    def teardown_class(self):
        # 关闭浏览器
        DriverUtils.quit_mp_driver()
