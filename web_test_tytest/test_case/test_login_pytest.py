# -*- coding: utf-8 -*-

"""
@author: shencheng
@software: PyCharm
@description: test
@time: 2022/4/13 9:34
"""

from web_test_tytest.common.excel_util import ExcelUtil
from web_test_tytest.page_base.login_page import LoginPage
from web_test_tytest.base1.base_util_pytest import BaseUtil
import pytest

class TestLogin(BaseUtil):

    # @data(*ExcelUtil().excel_read('login_data'))
    # @unpack
    @pytest.mark.parametrize('index,username,checkcode,result',ExcelUtil().excel_read('login_data'))
    def test_login_01(self,index,username,checkcode,result):
        self.driver.implicitly_wait(10)
        lp=LoginPage(self.driver)
        lp.slmode_eshop('child',username,checkcode)

        if index == 1:
            assert lp.check_point_shop()==result
            #self.assertEqual(lp.check_point_shop(),result)
        elif index == 2 or index == 3 or index == 4:
            assert lp.loginfail_check_shop(lp.username_failwarn_loc)==result
            #self.assertEqual(lp.loginfail_check_shop(lp.username_failwarn_loc),result)
        elif index == 5:
            assert lp.loginfail_check_shop(lp.checkcode_null_loc)==result
            #self.assertEqual(lp.loginfail_check_shop(lp.checkcode_null_loc),result)
        else:
            assert lp.loginfail_check_shop(lp.checkcode_fail_loc)==result
            #self.assertEqual(lp.loginfail_check_shop(lp.checkcode_fail_loc),result)


