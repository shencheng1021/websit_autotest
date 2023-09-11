# -*- coding: utf-8 -*-

"""
@author: shencheng
@software: PyCharm
@description: test
@time: 2022/4/13 9:34
"""
import time
import unittest
from selenium import webdriver


class BaseUtil(unittest.TestCase):
    def setUp(self) -> None:
        global driver
        self.driver = webdriver.Chrome()
        driver = self.driver
        self.driver.implicitly_wait(10)
        self.driver.get('http://172.24.100.75:10006/#/login')
        self.driver.maximize_window()

    def tearDown(self) -> None:
        time.sleep(5)
        self.driver.quit()