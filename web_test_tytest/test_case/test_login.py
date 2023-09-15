# -*- coding: utf-8 -*-

"""
@author: shencheng
@software: PyCharm
@description: test
@time: 2022/4/13 9:34
"""
import time
import unittest

from ddt import ddt, data, unpack

from web_test_tytest.common.excel_util import ExcelUtil
from web_test_tytest.common.logger_util import Logger
from web_test_tytest.page_base.login_page import LoginPage
from web_test_tytest.base1.base_util import BaseUtil




@ddt
class TestLogin(BaseUtil):

    @data(*ExcelUtil().excel_read('login_data'))
    @unpack
    def test_login_01(self,index,username,checkcode,result):
        self.mylogger.info('********登录测试开始,输入用户名：'+str(username)+'输入验证码:'+str(checkcode)+'******')
        self.driver.implicitly_wait(10)
        lp=LoginPage(self.driver)
        lp.slmode_eshop('child',username,checkcode)

        if index == 1:
            lp.goto_merchants_center()
            self.assertEqual(lp.check_point_shop(),result)
        elif index == 2 or index == 3 or index == 4:
            self.assertEqual(lp.loginfail_check_shop(lp.username_failwarn_loc),result)
        elif index == 5:
            self.assertEqual(lp.loginfail_check_shop(lp.checkcode_null_loc),result)
        else:
            self.assertEqual(lp.loginfail_check_shop(lp.checkcode_fail_loc),result)
        self.mylogger.info('********登录测试结束********')


if __name__ == '__main__':
    unittest.main()
