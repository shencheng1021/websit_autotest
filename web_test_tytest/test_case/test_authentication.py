# -*- coding: utf-8 -*-

"""
@author: shencheng
@software: PyCharm
@description: 添加实名认证模块自动化测试验证
@time: 2023/9/11 9:34
"""
import time
import unittest

from web_test_tytest.base1.base_util import BaseUtil
from web_test_tytest.common.initialization_util import InitializationUtil
from web_test_tytest.common.logger_util import Logger
from web_test_tytest.common.mysql_util import MysqlConnection
from web_test_tytest.page_base.auth_page import AuthBage
from web_test_tytest.page_base.login_page import LoginPage


mylogger = Logger(logger='TestMyLog').getlog()

class TestAuth(BaseUtil):


    def test_auth_01(self):
        '''
        实名认证成功
        :return:
        '''
        mylogger.info("********************初始化实名认证数据**********************")

        InitializationUtil().auth_initialization()

        mylogger.info("********************初始化实名认证数据完成，登录开始**********************")
        lg=LoginPage(self.driver)
        lg.slmode_eshop('child','17754756654','230516')
        mylogger.info("********************登录结束，进入实名认证操作**********************")
        ah=AuthBage(self.driver)
        ah.auth_business_shop('营业执照.png',"北京市","北京市","朝阳区")
        ah.auth_lagal_shop('身份证正面.png','身份证背面.png',"17754254414")
        ah.auth_contactperson_shop('身份证正面.png','身份证背面.png',"17754254414")
        ah.auth_source_shop()
        ah.auth_submit('1')
        ah.goto_auth_shop()
        self.assertEqual(ah.check_point(),"已认证")
        mylogger.info("***************检查点："+ah.check_point()+"，实名认证测试完成**********************")

    def test_auth_02(self):
        '''
        认证失败：重复认证
        :return:
        '''
        mylogger.info("********************登录开始**********************")
        lg = LoginPage(self.driver)
        lg.slmode_eshop('child', '17754756655', '230516')
        mylogger.info("********************登录结束，进入实名认证操作*********************")
        ah = AuthBage(self.driver)
        ah.auth_business_shop('营业执照.png', "北京市", "北京市", "朝阳区")
        ah.auth_lagal_shop('身份证正面.png', '身份证背面.png', "17754254414")
        ah.auth_contactperson_shop('身份证正面.png', '身份证背面.png', "17754254414")
        ah.auth_source_shop()
        ah.auth_submit('1')
        self.assertEqual(ah.check_point_2(),"营业执照号已认证其它企业,请勿重复认证多个企业")
        mylogger.info("***************检查点："+ah.check_point_2()+"，实名认证测试完成**********************")




