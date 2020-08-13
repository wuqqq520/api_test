#!/usr/bin/python
# -*- coding: UTF-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.header import Header
import configure



def sendmail(html_content):    
    message = MIMEText(html_content, 'html', 'utf-8')
    message['From'] = configure.mail_user
    message['To'] =  ";".join(configure.receivers)
    message['Subject'] = configure.subject
    try:
        smtpObj = smtplib.SMTP() 
        smtpObj.connect(configure.mail_host, 25)    # 25 为 SMTP 端口号
        smtpObj.login(configure.mail_user,configure.mail_pass)  
        smtpObj.sendmail(configure.mail_user, configure.receivers, message.as_string())
        print ("邮件发送成功")    
    except smtplib.SMTPException:
        print ("Error: 无法发送邮件")    
        
        

        