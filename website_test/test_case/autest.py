import time

from selenium import webdriver
from selenium.webdriver.common.by import By


driver=webdriver.Chrome()
driver.get('http://172.24.100.2:22222/tjf-website/#')
driver.implicitly_wait(10)
driver.maximize_window()
driver.find_element(By.XPATH,'//*[@id="login-box"]/div').click()
driver.find_element(By.XPATH,'//input[@placeholder="请输入注册手机号"]').send_keys('13565656787')
driver.find_element(By.XPATH, '//input[@placeholder="请输入密码"]').send_keys('123123123')
driver.find_element(By.XPATH,'//button[@class="el-button el-button--primary"]').click()
time.sleep(1)
text=driver.find_element(By.XPATH,'//p[@class="el-message__content"]').text
print(text)


