#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/9/16 21:52
# @Author  : Durat
# @Email   : durant.zeng@sunvalley.com.cn
# @File    : getdetails.py
# @Software: PyCharm

import sys,os
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
import json
import requests
from common.Logger import Logger



class getdetails:

    def __init__(self):
        self.logger = Logger(logger="getdetails").getlog()

    def get_getdetailsURL(self,baseURL,URL,lang,timeStamp,access_token):
        '''
        :param baseURL:
        :param lang:
        :param timeStamp:
        :param clientVersionInfo:
        :return:查看租购订单详情
        '''
        getdetailsURL = baseURL + URL + "?lang=%s&timeStamp=%s&access_token=%s" % (lang, timeStamp, access_token)
        self.logger.info("url为:%s" %getdetailsURL)
        return getdetailsURL



    def send_request_getdetails(self,url,orderNo):
        '''
        :param url:
        :param content:
        :return:
        '''
        headers = {"Content-Type": "application/json"}
        parameters = {
                        "orderNo": orderNo
                            }
        self.logger.info("请求的参数为:%s" %parameters)
        r = requests.post(url, data=json.dumps(parameters), headers=headers,timeout=30)
        self.logger.info("返回的参数为:%s" % json.loads(r.text))
        return json.loads(r.text)