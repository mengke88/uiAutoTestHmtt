"""
用于修改浏览器开关,开始执行时，我们将关闭浏览器传入一个False，这样浏览器
就不执行关闭，因为我们在utils里设置关闭的条件是__key=True
"""
import pytest

from utils import DriverUtils


# 我们使用pytest.mark.run(order=x)来设置执行方法的顺序，这样可以让先登录执行不关闭浏览器，
@pytest.mark.run(order=1)
class TestBegin:
    def test_begin(self):
        DriverUtils.change_mp_key(False)
