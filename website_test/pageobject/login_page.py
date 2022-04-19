import time

from selenium.webdriver.common.by import By

from website_test.base.base_page import BasePage


class LoginPage(BasePage):
    #页面的元素
    login_button_loc=(By.XPATH, '//*[@id="login-box"]/div')
    username_loc=(By.XPATH, '//input[@placeholder="请输入注册手机号"]')
    password_loc=(By.XPATH, '//input[@placeholder="请输入密码"]')
    submit_loc=(By.XPATH, '//button[@class="el-button el-button--primary"]')
    text_loc=(By.XPATH,'//*[@id="login-box"]/div[1]/strong')
    #退出按钮
    logout_button_loc=(By.XPATH,'//*[@id="login-box"]/div[2]')
    #确定退出按钮
    sure_logout_loc=(By.XPATH,'//div[@class="el-message-box__btns"]/button[2]')
    yonghudenglu_loc=(By.XPATH,'//div[@class="title"]')
    #登录界面提示文本框定位
    prompt_text_loc=(By.XPATH,'//p[@class="el-message__content"]')

    #页面的动作
    def login_eshop(self,username,password):
        self.click(LoginPage.login_button_loc)
        self.send_keys(LoginPage.username_loc,username)
        self.send_keys(LoginPage.password_loc,password)
        self.click(LoginPage.submit_loc)

    def logout_eshop(self):
        self.click(LoginPage.logout_button_loc)
        self.click(LoginPage.sure_logout_loc)

    #检查是否登录成功
    def checkpoint(self):
        return self.get_text(LoginPage.text_loc)

    #登录失败界面提示信息检查
    def checkpoint_loginfail(self):
        return self.get_text(LoginPage.prompt_text_loc)

    #退出成功登录页面检查
    def checkpoint_login(self):
        return self.get_text(LoginPage.yonghudenglu_loc)

