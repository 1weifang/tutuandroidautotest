#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/10/15 20:29
# @Author  : Durat
# @Email   : durant.zeng@sunvalley.com.cn
# @File    : balance.py
# @Software: PyCharm

import sys,os
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
import json
import requests
from common.Logger import Logger



class balance:


    def __init__(self):
        self.logger = Logger(logger="balance").getlog()


    def get_balanceURL(self,baseURL,URL,lang,timeStamp,clientVersionInfo,access_token):
        '''
        :param baseURL:
        :param lang:
        :param timeStamp:
        :param clientVersionInfo:
        :return:打印下单-余额支付
        '''
        reallyURL = baseURL + URL + "?lang=%s&timeStamp=%s&clientVersionInfo=%s&access_token=%s" % (lang, timeStamp, clientVersionInfo,access_token)
        self.logger.info("url为:%s" %reallyURL)
        return reallyURL



    def send_request_balance(self,url,orderNum):
        '''
        :param url:
        :param content:
        :return:
        '''
        headers = {"Content-Type": "application/json"}
        parameters = {
            "orderNum": orderNum
                 }
        self.logger.info("请求的参数为:%s" %parameters)
        r = requests.post(url, data=json.dumps(parameters), headers=headers,timeout=30)
        self.logger.info("返回的参数为:%s" % json.loads(r.text))
        return json.loads(r.text)
