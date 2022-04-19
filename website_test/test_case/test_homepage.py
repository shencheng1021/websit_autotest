# -*- coding: utf-8 -*-

"""
@author: shencheng
@software: 砼联数科官网
@description: 砼联数科官网自动化测试脚本
@time: 2022/4/14 15:27
"""
from ddt import ddt, data, unpack

from website_test.base.base_util import BaseUtil
from website_test.common.excel_util import ExcelUtil
from website_test.common.logger_util import Logger
from website_test.pageobject.home_page import HomePage

mylogger = Logger(logger='TestMyLog').getlog()

@ddt
class TestCase(BaseUtil):

    @data(*ExcelUtil().read_excel('productname_data','productname'))
    @unpack
    def test_01_product_details(self,index,product_name):
        '''
        首页点击优先产品分类进行跳转
        :return:
        '''
        mylogger.info('************跳转对应的产品详情测试开始，产品名称：'+product_name+'************')
        hp=HomePage(self.driver)
        hp.home_eshop(product_name)
        if index==8:
            self.assertEqual('资产证券化',hp.product_checkpoint())
        else:
            self.assertEqual(product_name,hp.product_checkpoint())
        mylogger.info('************跳转对应的产品详情测试结束，产品名称：'+product_name+'************')


    def test_02_help_center(self):
        '''
        首页帮助中心跳转功能
        :return:
        '''
        mylogger.info('************帮助信息操作指导页面跳转************')
        hp=HomePage(self.driver)
        hp.help_center_eshop('如何注册账号')
        self.assertEqual('注册流程介绍',hp.help_details_checkpoint())
        mylogger.info('************跳转对应的产品详情测试开始，产品名称************')





