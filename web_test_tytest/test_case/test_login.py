# -*- coding: utf-8 -*-

"""
@author: shencheng
@software: PyCharm
@description: test
@time: 2022/4/13 9:34
"""
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest

driver=webdriver.Chrome()
driver.get("https://www.baidu.com/")
driver.maximize_window()
driver.find_element(By.ID,"kw").send_keys('砼联数字科技有限公司')
driver.find_element(By.ID,"su").click()
time.sleep(5)
driver.find_element(By.XPATH,"/html/body/div[3]/div[3]/div[1]/div[3]/div[1]/div[1]/div[1]/h3/a").click()
driver.switch_to.window(driver.window_handles[-1])
driver.find_element(By.XPATH,"//span[contains(text(),'砼联产品')]").click()
time.sleep(2)
driver.find_element(By.XPATH,"//p[@class='menu-name' and contains(text(),'砼联数科')]").click()

driver.find_element(By.XPATH,"//div[@class='exp-btn']").click()