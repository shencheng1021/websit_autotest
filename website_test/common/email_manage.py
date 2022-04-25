#coding=utf-8
"""
@author:shencheng
@data:2022年1月21日
@description:发送邮件的脚本
"""
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class EmailManage:
    #发送邮件
    def send_email(self,report_name):
        #定义smtp的服务器是什么
        smtpserver='smtp.163.com'
        #定义发送邮件的用户名和客户端密码
        username='sc13730870086@163.com'
        password='OOYHXNKTVGAFDAPM'
        #定义接收邮件的邮箱，多个用逗号隔开
        receiver='565072153@qq.com'
        #创建邮件对象
        message=MIMEMultipart('related')
        subject='砼金服自动化测试报告'
        fujian=MIMEText(open('../report/'+report_name,'rb').read(),'html','utf-8')   #附件
        #把邮件的信息组装到邮件的对象中去
        message['from']=username
        message['to']=receiver
        message['subject']=subject
        message.attach(fujian)
        #登录smtp服务器并发送邮件
        smtp=smtplib.SMTP()
        smtp.connect(smtpserver)
        smtp.login(username,password)
        smtp.sendmail(username,receiver,message.as_string())
        smtp.quit()


