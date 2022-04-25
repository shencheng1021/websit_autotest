#coding=utf-8
import unittest

import os
import time

from HTMLTestRunner.HTMLTestRunner import HTMLTestRunner

from email_manage import EmailManage

report_path= '../report/'
t=time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
report_file=report_path+t+'report.html'
#如果路径不存在就创建一个文件夹
if not os.path.exists(report_path):
    os.mkdir(report_path)
else:
    pass
report_title='砼金服运管台自动化测试报告'
report_desc='砼金服运管台自动化测试报告'

with open(report_file,'wb') as report:
    #方法一，给出文件名何类名，就能测试所有的测试用例
    #suit.addTest(unittest.TestLoader().loadTestsFromName('for_douyu.te'))
    #方法二，给出类名，就能测试所有的测试用例
    #suit.addTest(unittest.TestLoader().loadTestsFromTestCase(te))
    #方法三，start_dir参数指定文件路径，pattern执行规则，‘s*.py’表示以s开头，‘.py’结尾的都加入到测试套件中
    test_dir= '../test_case'
    discover=unittest.defaultTestLoader.discover(start_dir=test_dir,pattern='test_login.py')
    #套件结合TextTestRunner对象进行相当于unittest.main()
    #如果结合HTMLTestRunner使用，则需要调用HTMLTestRunner中的运行器
    runner=HTMLTestRunner(stream=report,title=report_title,description=report_desc)
    runner.run(discover)
    report.close()   #发送邮件之前一定要关闭文件流
    #发送邮件
    time.sleep(3)
    EmailManage().send_email(report.name)

