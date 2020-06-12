"""
后台登录首页测试用例
"""
import pytest

from config import Base_Aritcal_Title
from page.mis.admin_article_audit_page import AuditProxy
from page.mis.admin_home_page import HomeProxy
from utils import DriverUtils, element_is_exist


# 1.定义测试类
@pytest.mark.run(order=103)
class TestMisHome:
    # 2.定义初始化方法
    def setup_class(self):
        # 实例化首页的业务层对象
        self.home_proxy = HomeProxy()
        # 实例化审核文章的业务层对象
        self.audit_proxy = AuditProxy()
        self.driver = DriverUtils.get_mis_driver()

    # 4.定义测试类

    def test_aduit_aritcal(self):
        # 5.定义测试数据
        text = Base_Aritcal_Title
        # 6.调用业务方法
        self.home_proxy.test_home_proxy()
        self.audit_proxy.test_audit_proxy(text)
        # 断言
        msg = element_is_exist(self.driver, text)
        assert msg

    # 3.定义销毁方法
    def teardown_class(self):
        DriverUtils.quit_mis_driver()
