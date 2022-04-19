import unittest

from website_test.base.base_util import BaseUtil
from website_test.pageobject.registered_page import RegisteredPage


class TestCase(BaseUtil):

    def test_01_registered(self):
        '''
        核心企业官网注册功能
        :return:
        '''
        rp=RegisteredPage(self.driver)
        rp.registered_eshop()