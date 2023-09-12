# -*- coding: utf-8 -*-

"""
@author: shencheng
@software: PyCharm
@description: test
@time: 2022/4/13 9:34
"""
import os
import time

from selenium.webdriver.common.by import By

from selenium import webdriver
from selenium.webdriver.support.select import Select


driver = webdriver.Chrome()

filepath=os.path.abspath(os.path.dirname(__file__)).split("test_case")[0]
print(filepath)

driver.get('http://172.24.100.75:10006/#/login')
driver.implicitly_wait(10)
driver.maximize_window()
driver.switch_to.frame('child')
time.sleep(2)
driver.find_element(By.XPATH,"//*[@id='tab-second']").click()
driver.find_element(By.XPATH, "//input[@placeholder='请输入手机号码']").send_keys('17785425547')
driver.find_element(By.XPATH, "//div[@class='c-phonecode-input']/div/input").send_keys('230516')
driver.find_element(By.XPATH, "//span[@class='el-checkbox__inner']").click()
driver.find_element(By.XPATH, "//div[@class='el-tabs__content']/button").click()
driver.switch_to.default_content()
driver.find_element(By.XPATH,"//div[@class='tag-inside']/ul[6]/li").click()
driver.find_element(By.XPATH,"//div[contains(text(),'企业信息管理')]").click()
driver.find_element(By.XPATH,"//span[contains(text(),'修改实名认证信息')]").click()
driver.find_element(By.XPATH,"//div[@class='busiLice-list']/div/div/div/input").send_keys(filepath+'/data/营业执照.png')
time.sleep(5)

s=Select(driver.find_element(By.XPATH,"//div[@class='distpicker-address-wrapper']/label[1]/select"))
s.select_by_value("北京市")

c=Select(driver.find_element(By.XPATH,"//div[@class='distpicker-address-wrapper']/label[2]/select"))
c.select_by_value("北京市")

t=Select(driver.find_element(By.XPATH,"//div[@class='distpicker-address-wrapper']/label[3]/select"))
t.select_by_value("朝阳区")

driver.find_element(By.XPATH,"//form[@class='el-form']/div[4]/div[1]/div/div/div/div/div/div[1]/div[1]/div/input").send_keys(filepath+'/data/身份证正面.png')
time.sleep(3)
driver.find_element(By.XPATH,"//form[@class='el-form']/div[4]/div[1]/div/div/div/div/div/div[2]/div[1]/div/input").send_keys(filepath+'/data/身份证背面.png')
time.sleep(3)
driver.find_element(By.XPATH,"//input[@placeholder='请输入法人手机号']").send_keys("17785425547")

driver.find_element(By.XPATH,"//form[@class='el-form']/div[6]/div[1]/div/div/div/div/div/div[1]/div[1]/div/input").send_keys(filepath+'/data/身份证正面.png')
time.sleep(3)
driver.find_element(By.XPATH,"//form[@class='el-form']/div[6]/div[1]/div/div/div/div/div/div[2]/div[1]/div/input").send_keys(filepath+'/data/身份证背面.png')
time.sleep(3)
driver.find_element(By.XPATH,"//input[@placeholder='请输入联系人手机号']").send_keys("17785425547")
driver.find_element(By.XPATH,"//input[@placeholder='请选择用户来源']").click()
driver.find_element(By.XPATH,"//span[text()='上海公司']").click()




