import pytest

from config import Base_Aritcal_Title
from page.mp.ui_home_page import HomePorxy
from page.mp.ui_publish_page import PubProxy
from utils import DriverUtils, element_is_exist


# 1.定义测试类
@pytest.mark.run(order=3)
class TestPubAritical:
    # 2.定义类级别初始化方法
    def setup_class(self):
        # 打开浏览器
        self.driver = DriverUtils.get_mp_driver()
        # 创建需要也变的业务层的对象
        self.home_proxy = HomePorxy()
        self.pun_proxy = PubProxy()

    # 4.定义测试方法
    def test_pub_aritical(self):
        # 5组织测试数据
        title = Base_Aritcal_Title
        content = "1.剑道尘心 2.万剑归宗"
        option = "数码产品"
        # 6.调用业务层的方法
        self.home_proxy.to_publish_artical()
        self.pun_proxy.test_pub_aritcal(title, content, option)
        # 7.断言实际结果
        is_suc = element_is_exist(self.driver, "新增文章成功")
        assert is_suc

    # 3.定义类级别销毁方法
    def teardown_class(self):
        DriverUtils.quit_mp_driver()
