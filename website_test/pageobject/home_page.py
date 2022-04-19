# -*- coding: utf-8 -*-

"""
@author: shencheng
@software: PyCharm
@description: 官网首页自动化测试脚本
@time: 2022/4/13 9:34
"""
from selenium.webdriver.common.by import By

from website_test.base.base_page import BasePage


class HomePage(BasePage):

    #页面元素
    #定位点击产品分类的名称
    def product_loc(self,product_name):
        select_the_product_loc = (By.XPATH, '//div[text()="'+product_name+'"]')
        #print(select_the_product_loc)
        return select_the_product_loc

    #定位金融超市金融产品分类
    product_classify_loc=(By.XPATH,'//div[@class="title-box"]/div[1]')

    #定位页面底部帮助栏菜单
    def help_tips_loc(self,help_tips_name):
        help_tips_loc=(By.XPATH,'//li[contains(text(),"'+help_tips_name+'")]')
        return help_tips_loc

    #定位帮助详情标题
    help_title_loc=(By.XPATH,'//div[@class="box-title"]')

    #页面动作
    #首页点击优选产品跳转到金融超市产品详情页
    def home_eshop(self,product_name):
        self.click(HomePage(self.driver).product_loc(product_name))

    #首页点击帮助中心导航栏,跳转到对应的操作指导
    def help_center_eshop(self,help_tips_name):
        self.click(HomePage(self.driver).help_tips_loc(help_tips_name))

    #页面检查点
    #检查是否跳转到金融超市产品分类
    def product_checkpoint(self):
        return self.get_text(HomePage.product_classify_loc)

    #检查是否跳转到对应的操作指导
    def help_details_checkpoint(self):
        return self.get_text(HomePage.help_title_loc)








