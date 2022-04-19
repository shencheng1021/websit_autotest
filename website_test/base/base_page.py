from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium import webdriver


class BasePage:

    def __init__(self,driver):
        self.driver=driver

    #定位元素的关键字
    def locator_element(self,loc):
        return self.driver.find_element(*loc)

    #定义单机click的关键字
    def click(self,loc):
        self.locator_element(loc).click()

    #定义输入值的关键字
    def send_keys(self,loc,value):
        self.locator_element(loc).send_keys(value)

    #定义获取指定位置文本的关键字
    def get_text(self,loc):
        return self.locator_element(loc).text

    #定义进入框架的关键字
    def goto_frame(self,frame_name):
        self.driver.switch_to.frame(frame_name)

    #定义退出框架的关键字
    def quit_franme(self):
        self.driver.switch_to.default_content()

    #定义下拉框的关键字
    def chice_select(self,loc,value):
        sel=Select(self.locator_element(loc))
        sel.select_by_value(value)

    #定义切换窗口的关键字
    def switch_handles(self,index):
        handles=self.driver.window_handles
        self.driver.switch_to.new_window(handles[index])

    #定义弹出框确认操作关键字

    def alert_accept(self):
        alert=self.driver.switch_to.alert
        alert.accept()

    #定义弹出框取消的关键字

    def alert_dismiss(self):
        alert=self.driver.switch_to.alert
        alert.dismiss()

















