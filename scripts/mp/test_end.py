"""
用于关闭浏览器传入一个True让其能执行关闭浏览器的操作
"""
import pytest

from utils import DriverUtils


# 执行完所以用例才传一个True让他关闭浏览器
@pytest.mark.run(order=99)
class TestEnd:
    def test_end(self):
        DriverUtils.change_mp_key(True)
        DriverUtils.quit_mp_driver()
