# -*- coding: utf-8 -*-

"""
@author: shencheng
@software: PyCharm
@description: test
@time: 2022/4/13 9:34
"""
import unittest

from selenium import webdriver


class BaseUtil(unittest.TestCase):

    def setUp(self) -> None:
        global driver
        self.driver = webdriver.Chrome()
        driver = self.driver
        self.driver.implicitly_wait(10)
        self.driver.get('http://172.24.100.2:22222/tjf-website/#/')
        self.driver.maximize_window()
    def tearDown(self) -> None:
        #self.driver.quit()
        pass