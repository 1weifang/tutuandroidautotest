#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/9/16 21:26
# @Author  : Durat
# @Email   : durant.zeng@sunvalley.com.cn
# @File    : create.py
# @Software: PyCharm


import sys,os
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
import json
import requests
from common.Logger import Logger



class create:

    def __init__(self):
        self.logger = Logger(logger="create").getlog()

    def get_createURL(self,baseURL,URL,lang,timeStamp,access_token):
        '''
        :param baseURL:
        :param lang:
        :param timeStamp:
        :param clientVersionInfo:
        :return:租购订下单
        '''
        reallyURL = baseURL + URL + "?lang=%s&timeStamp=%s&access_token=%s" % (lang, timeStamp, access_token)
        self.logger.info("url为:%s" %reallyURL)
        return reallyURL



    def send_request_create(self,url,primaryAgentId,primaryAgentLoginName,twoAgentId,twoAgentLoginName,goodId,amount,orderType,source,receivedId):
        '''
        :param url:
        :param content:
        :return:
        '''
        headers = {"Content-Type": "application/json"}
        parameters = {
                    "primaryAgentId":primaryAgentId,
                    "primaryAgentLoginName": primaryAgentLoginName,
                    "twoAgentId": twoAgentId,
                    "twoAgentLoginName": twoAgentLoginName,
                    "goodId": goodId,
                    "amount": amount,
                    "orderType": orderType,
                    "source":source,
                    "receivedId":receivedId,
                    "remark": "没有备注"
                            }
        self.logger.info("请求的参数为:%s" %parameters)
        r = requests.post(url, data=json.dumps(parameters), headers=headers,timeout=30)
        self.logger.info("返回的参数为:%s" % json.loads(r.text))
        return json.loads(r.text)
