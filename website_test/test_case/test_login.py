import time

from website_test.base.base_util import BaseUtil
from website_test.common.excel_util import ExcelUtil
from website_test.common.logger_util import Logger
from website_test.pageobject.login_page import LoginPage
from ddt import ddt, data, unpack


mylogger = Logger(logger='TestMyLog').getlog()

@ddt
class Testcase(BaseUtil):
    @data(*ExcelUtil().read_excel('login_data','login'))
    @unpack
    def test_01_login(self,index,username,password,result):
        '''
        登录官网成功
        :return:
        '''
        mylogger.info('******登录测试开始，输入账号'+username+'，输入密码：'+password+'.******')
        self.driver.implicitly_wait(10)
        lg=LoginPage(self.driver)
        lg.login_eshop(username,password)
        time.sleep(1)
        if index==1:
            self.assertEqual(lg.checkpoint(),str(result))
        else:
            self.assertEqual(lg.checkpoint_loginfail(),result)
        mylogger.info('****************************登录测试结束*************************')

    def test_02_logout(self):
        '''
        注销登录
        :return:
        '''
        mylogger.info('************注销登录测试开始************')
        lg = LoginPage(self.driver)
        lg.login_eshop('13565656787', '656787')
        self.assertEqual(lg.checkpoint(), '13565656787')
        lg.logout_eshop()
        self.assertEqual(lg.checkpoint_login(),'用户登录')
        mylogger.info('************注销登录测试结束************')










