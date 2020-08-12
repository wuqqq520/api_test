#!/usr/bin/python
# -*- coding: UTF-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.header import Header
import configure



def sendmail(mail_host,mail_user,mail_pass,receivers,subject,html_content):    
    message = MIMEText(html_content, 'html', 'utf-8')
    message['From'] = mail_user
    message['To'] =  ";".join(receivers)
    message['Subject'] = subject
    try:
        smtpObj = smtplib.SMTP() 
        smtpObj.connect(mail_host, 25)    # 25 为 SMTP 端口号
        smtpObj.login(mail_user,mail_pass)  
        smtpObj.sendmail(mail_user, receivers, message.as_string())
        print ("邮件发送成功")    
    except smtplib.SMTPException:
        print ("Error: 无法发送邮件")    
        
sendmail(configure.mail_host,configure.mail_user,configure.mail_pass,configure.receivers,configure.subject,"<a>sssss</a>")
        

        