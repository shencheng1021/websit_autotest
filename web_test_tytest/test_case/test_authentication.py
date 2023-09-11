# -*- coding: utf-8 -*-

"""
@author: shencheng
@software: PyCharm
@description: 添加实名认证模块自动化测试验证
@time: 2023/9/11 9:34
"""
import unittest

from web_test_tytest.base1.base_util import BaseUtil
from web_test_tytest.page_base.login_page import LoginPage


class TestAuth(BaseUtil):

    def test_auth_01(self):
        lg=LoginPage(self.driver)
        lg.slmode_eshop('child','17754756654','230516')


