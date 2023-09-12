# -*- coding: utf-8 -*-

"""
@author: shencheng
@software: PyCharm
@description: test
@time: 2022/4/13 9:34
"""
import os
import time

from selenium import webdriver
from selenium.webdriver.support.select import Select


class BasePage:
    def __init__(self,driver):
        self.driver = driver

    def locator_element(self,loc):
        return self.driver.find_element(*loc)

    def click(self,loc):
        self.locator_element(loc).click()

    def send_keys(self,loc,key):
        self.locator_element(loc).send_keys(key)

    #定义进框架的关键字
    def goto_iframe(self,id):
        self.driver.switch_to.frame(id)
    #定义出框架的关键字
    def quit_iframe(self):
        self.driver.switch_to.default_content()

    def goto_url(self,url):
        self.driver.get(url)

    def get_text(self,loc):
        return self.locator_element(loc).text

    def select_value(self,loc,value):
        s=Select(self.locator_element(loc))
        s.select_by_value(value)

    def upload_file(self,loc,filepath):
        relativepath=os.path.dirname(__file__).split("base1")[0]+'/data/'
        self.send_keys(loc,relativepath+filepath)



