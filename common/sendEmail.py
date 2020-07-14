#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/8/16 9:24
# @Author  : Durat
# @Email   : durant.zeng@sunvalley.com.cn
# @File    : sendEmail.py
# @Software: PyCharm

import smtplib
from email.mime.text import MIMEText
from email.header import Header
import unittest
import HTMLTestRunner
import time,os
from common.Logger import Logger
logger = Logger(logger="sendEamil").getlog()



class sendEamil:

    def __init__(self):
        pass

    def new_report(self,test_report):
        lists = os.listdir(test_report)
        # print(lists)
        file_path = os.path.join(test_report, lists[-1])
        return file_path


    def send_mail(self,last_file):
        # 发信邮箱
        # mail_from = '1350129201@qq.com'
        # # 收信邮箱
        # mail_to = '1350129201@qq.com'
        # # 定义正文
        # f = open(last_file, 'rb')
        # mail_body = f.read()
        # f.close()
        # msg = MIMEText(mail_body, _subtype='html', _charset='utf-8')
        # # 定义标题
        # msg['Subject'] = u"自动化测试报告"
        # # 定义发送时间（不定义的可能有的邮件客户端会不显示发送时间）
        # msg['date'] = time.strftime('%a, %d %b %Y %H:%M:%S %z')
        #
        # smtp = smtplib.SMTP()
        # # 连接 SMTP 服务器，此处用的 126 的 SMTP 服务器
        # smtp.connect('smtp.126.com')
        # # 用户名密码
        # smtp.login('durant.zeng@sunvalley.com.cn', '2wsx@WSX2')
        # smtp.sendmail(mail_from, mail_to, msg.as_string())
        # smtp.quit()
        # logger.info('email has send out !')

        # 第三方 SMTP 服务
        mail_host = "smtp.qq.com"  # 设置服务器
        mail_user = "1350129201@qq.com"  # 用户名
        mail_pass = "ytncwhwzfxttbace"  # 口令,QQ邮箱是输入授权码，在qq邮箱设置 里用验证过的手机发送短信获得，不含空格

        sender = '1350129201@qq.com'
        receivers = ['1350129201@qq.com', 'durant.zeng@sunvalley.com.cn']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱




    def send_report(self,testreport):
        result_dir = testreport
        logger.info(result_dir)
        lists = os.listdir(result_dir)
        lists.sort(key=lambda fn: os.path.getmtime(result_dir + "\\" + fn))
        # print (u'最新测试生成的报告： '+lists[-1])
        # 找到最新生成的文件
        file_new = os.path.join(result_dir, lists[-1])
        logger.info(file_new)
        # 调用发邮件模块
        self.send_mail(file_new)


if __name__ == "__main__":
	ac = sendEamil()




