# -*- coding: utf-8 -*-

"""
@author: shencheng
@software: PyCharm
@description: test
@time: 2022/4/13 9:34
"""
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from web_test_tytest.base1.base_page import BasePage

class LoginPage(BasePage):
    #定位页面元素
    slmode_loc=(By.ID,'tab-second')
    username_loc=(By.XPATH, "//input[@placeholder='请输入手机号码']")
    password_loc=(By.XPATH, "//div[@class='c-phonecode-input']/div/input")
    checkbox_loc=(By.XPATH, "//span[@class='el-checkbox__inner']")
    loginbutton_loc=(By.XPATH, "//div[@class='el-tabs__content']/button")
    organization_loc=(By.XPATH,"//input[@type='text']")
    organization_01_loc=(By.XPATH,"//span[contains(text(),'砼联数字科技有限公司')]")
    username_failwarn_loc=(By.XPATH,"//form[@class ='el-form login-form-body']/div[1]/div/div[2]")
    checkcode_fail_loc=(By.XPATH,"//p[@class='el-message__content']")
    checkcode_null_loc = (By.XPATH, "//form[@class ='el-form login-form-body']/div[3]/div/div[2]")



    #页面的动作
    #登录动作
    def slmode_eshop(self,id,username,password):
        self.goto_iframe(id)
        time.sleep(1)
        self.click(LoginPage.slmode_loc)
        self.send_keys(LoginPage.username_loc,username)
        self.send_keys(LoginPage.password_loc,password)
        self.click(LoginPage.checkbox_loc)
        self.click(LoginPage.loginbutton_loc)

    #登录成功的检查点动作
    def check_point_shop(self):
        self.quit_iframe()
        self.click(LoginPage.organization_loc)
        return self.get_text(LoginPage.organization_01_loc)

    #登录失败的检查点动作
    def loginfail_check_shop(self,loc):
        return self.get_text(loc)



