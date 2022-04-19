from selenium.webdriver.common.by import By

from website_test.base.base_page import BasePage


class RegisteredPage(BasePage):
    #页面的元素
    #登录按钮元素定位
    login_button_loc=(By.XPATH, '//*[@id="login-box"]/div')
    #立即注册按钮元素定位
    registered_loc=(By.XPATH,'//span[text()="立即注册"]')
    #输入企业名称编辑框元素定位
    enterprise_name_loc=(By.XPATH,'//input[@placeholder="请输入企业名称"]')
    #输入企业证件号输入框元素定位
    id_no_loc=(By.XPATH,'//input[@placeholder="请输入企业证件号"]')
    #输入手机号输入框元素定位
    phone_no_loc = (By.XPATH, '//input[@placeholder="请输入手机号"]')
    #登录密码设置输入框元素定位
    password_loc = (By.XPATH, '//input[@placeholder="请输入密码"]')
    #登录密码确认输入框元素定位
    password_sure_loc = (By.XPATH, '//input[@placeholder="请再次输入密码"]')
    #确定注册按钮元素定位
    registered_button_loc = (By.XPATH, '//span[text()="确定注册"]')


    #页面的动作
    def registered_eshop(self):
        self.click(RegisteredPage.login_button_loc)
        self.click(RegisteredPage.registered_loc)
        self.send_keys(RegisteredPage.enterprise_name_loc,'核心企业注册_autotest_001')
        self.send_keys(RegisteredPage.id_no_loc,'674567412587468354')
        self.send_keys(RegisteredPage.phone_no_loc,'18154756685')
        self.send_keys(RegisteredPage.password_loc,'Ganjue,22')
        self.send_keys(RegisteredPage.password_sure_loc,'Ganjue,22')
        self.click(RegisteredPage.registered_button_loc)