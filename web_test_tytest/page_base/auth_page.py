# -*- coding: utf-8 -*-

"""
@author: shencheng
@software: PyCharm
@description: 添加实名认证页面得动作
@time: 2023/9/11 10:57
"""
from selenium.webdriver.common.by import By

from web_test_tytest.base1.base_page import BasePage


class AuthBage(BasePage):
    #定位企业信息管理按钮
    enterprise_management_loc=(By.XPATH,"//div[@class='left-menu']/div[2]")

    #定位修改实名认证按钮
    update_auth_button_loc=(By.XPATH,"//span[contains(text(),'修改实名认证信息')]")

    def auth_shop(self):
        self.quit_iframe()
        self.goto_url('http://172.24.100.75:10006/#/financing')
        self.click(AuthBage.enterprise_management_loc)
        self.click(AuthBage.update_auth_button_loc)

