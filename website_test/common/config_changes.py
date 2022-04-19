# -*- coding: utf-8 -*-

"""
@author: shencheng
@software: PyCharm
@file: 操作ini文件中对应键的value值
@time: 2022/04/13 9:36
"""


import configparser

class Config:


    cf = configparser.ConfigParser()
    cf.read('../config_file/website_config.ini', encoding='utf-8')
    #获取键值
    @classmethod
    def get_option(self,section,option):
        value=Config.cf.get(section,option)
        print(value)
        return value

    #设置键值
    @classmethod
    def set_option(self,section,option,value):
        Config.cf.set(section,option,value)
        Config.cf.write(open('../config_file/website_config.ini','w',encoding='utf-8'))

    #删除键值
    @classmethod
    def delet_option(self,section,option):
        Config.cf.remove_option(section,option)
        Config.cf.write(open('../config_file/website_config.ini', 'w', encoding='utf-8'))


