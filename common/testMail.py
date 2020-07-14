#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/8/16 10:27
# @Author  : Durat
# @Email   : durant.zeng@sunvalley.com.cn
# @File    : testMail.py
# @Software: PyCharm


# coding:utf-8
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

# 第三方 SMTP 服务
mail_host = "smtp.qq.com"  # 设置服务器
mail_user = "1350129201@qq.com"  # 用户名
mail_pass = "ytncwhwzfxttbace"  # 口令,QQ邮箱是输入授权码，在qq邮箱设置 里用验证过的手机发送短信获得，不含空格

sender = '1350129201@qq.com'
receivers = ['1350129201@qq.com', 'durant.zeng@sunvalley.com.cn']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

message = MIMEText('a test for python', 'plain', 'utf-8')
message['From'] = Header("ppyy", 'utf-8')
message['To'] = Header("you", 'utf-8')

subject = 'my test'
message['Subject'] = Header(subject, 'utf-8')


smtpObj = smtplib.SMTP_SSL(mail_host, 465)
smtpObj.login(mail_user, mail_pass)
smtpObj.sendmail(sender, receivers, message.as_string())
smtpObj.quit()
print("邮件发送成功")



