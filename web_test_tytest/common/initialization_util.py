# -*- coding: utf-8 -*-

"""
@author: shencheng
@software: PyCharm
@description: 初始化自动化测试过程中的测试数据
@time: 2023/9/13 10:47
"""
from web_test_tytest.common.mysql_util import MysqlConnection


class InitializationUtil:

    '''
    初始化实名认证产生的认证测试数据
    '''
    def auth_initialization(self):
        MysqlConnection('tjf_manage01').Operate(
            "DELETE  FROM `tjf_manage01`.`t_business_identify`  WHERE `busi_lice_no`='91130609MABN36NQXR'")
        MysqlConnection('tjf_manage01').Operate(
            "DELETE  FROM `tjf_manage01`.`t_trader`  WHERE `name`='河北恩帅贸易有限公司'")