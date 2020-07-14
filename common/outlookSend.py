#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/8/19 20:11
# @Author  : Durat
# @Email   : durant.zeng@sunvalley.com.cn
# @File    : outlookSend.py
# @Software: PyCharm


import sys,os
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
import win32com.client as win32
from common.Logger import Logger
logger = Logger(logger="outlookSend").getlog()

cc = 'durant.zeng@sunvalley.com.cn'
receivers = 'durant.zeng@sunvalley.com.cn'

# receivers = 'durant.zeng@sunvalley.com.cn'+';'+'ning.ou@sunvalley.com.cn'




class outlookSend:

    def __init__(self):
        pass


    def send(self,receivers,cc,fileName):

        outlook = win32.Dispatch('outlook.application')
        mail = outlook.CreateItem(0)
        mail.To = receivers
        logger.info("收件人为：%s" %receivers)
        mail.CC = cc
        logger.info("抄送人为：%s" % cc)
        mail.Subject ='【prod_自动化测试报告】'
        mail.Body = 'Anjou接口自动化测试报告'
        mail.Attachments.Add(fileName)
        logger.info("发送的邮件为：%s" % fileName)
        mail.Send()
        logger.info("邮件发送成功")


if __name__ == "__main__":
    outlook= outlookSend()
    cc = 'durant.zeng@sunvalley.com.cn'
    # receivers = 'durant.zeng@sunvalley.com.cn' + ';' + 'ning.ou@sunvalley.com.cn'
    receivers = 'durant.zeng@sunvalley.com.cn'

    fileName = r'D:\anjouAutoTest\report\result_2019-08-19-20_25_02.html'

    print(type(fileName))
    outlook.send(receivers,cc,fileName)








