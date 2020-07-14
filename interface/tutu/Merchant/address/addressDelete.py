#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/9/16 20:09
# @Author  : Durat
# @Email   : durant.zeng@sunvalley.com.cn
# @File    : addressDelete.py
# @Software: PyCharm

import sys,os
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
import json
import requests
from common.Logger import Logger



class addressDelete:

    def __init__(self):
        self.logger = Logger(logger="addressDelete").getlog()

    def get_addressDeleteURL(self,baseURL,URL,lang,timeStamp,access_token):
        '''
        :param baseURL:
        :param lang:
        :param timeStamp:
        :param clientVersionInfo:
        :return:删除收货地址
        '''
        addressDeleteURL = baseURL + URL + "?lang=%s&timeStamp=%s&access_token=%s" % (lang, timeStamp, access_token)
        self.logger.info("url为:%s" %addressDeleteURL)
        return addressDeleteURL



    def send_request_addressDelete(self,url,addressId):
        '''
        :param url:
        :param content:
        :return:
        '''
        headers = {"Content-Type": "application/json"}
        parameters = {
                    "addressId":addressId
                    }
        self.logger.info("请求的参数为:%s" %parameters)
        r = requests.post(url, data=json.dumps(parameters), headers=headers,timeout=30)
        self.logger.info("返回的参数为:%s" % json.loads(r.text))
        return json.loads(r.text)

