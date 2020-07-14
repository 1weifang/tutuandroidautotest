#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/10/15 14:31
# @Author  : Durat
# @Email   : durant.zeng@sunvalley.com.cn
# @File    : RefundOrderList.py
# @Software: PyCharm

import sys,os
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
import json
import requests
from common.Logger import Logger



class RefundOrderList:

    def __init__(self):
        self.logger = Logger(logger="RefundOrderList").getlog()

    def get_RefundOrderListURL(self,baseURL,URL,lang,timeStamp,access_token):
        '''
        :param baseURL:
        :param lang:
        :param timeStamp:
        :param clientVersionInfo:
        :return:出租退货退款-交易端退货退款列表
        '''
        reallyURL = baseURL + URL + "?lang=%s&timeStamp=%s&access_token=%s" % (lang, timeStamp, access_token)
        self.logger.info("url为:%s" %reallyURL)
        return reallyURL



    def send_request_RefundOrderList(self,url,currentPage,pageSize):
        '''
        :param url:
        :param content:
        :return:
        '''
        headers = {"Content-Type": "application/json"}
        parameters = {
                        "currentPage": currentPage,
                        "pageSize": pageSize,
                            }
        self.logger.info("请求的参数为:%s" %parameters)
        r = requests.post(url, data=json.dumps(parameters), headers=headers,timeout=30)
        self.logger.info("返回的参数为:%s" % json.loads(r.text))
        return json.loads(r.text)

