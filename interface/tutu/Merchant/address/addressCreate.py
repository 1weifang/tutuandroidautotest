#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/9/16 16:11
# @Author  : Durat
# @Email   : durant.zeng@sunvalley.com.cn
# @File    : addressCreate.py
# @Software: PyCharm

import sys,os
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
import json
import requests
from common.Logger import Logger


class addressCreate:

    def __init__(self):
        self.logger = Logger(logger="addressCreate").getlog()

    def get_addressCreateURL(self,baseURL,URL,lang,timeStamp,access_token):
        '''
        :param baseURL:
        :param lang:
        :param timeStamp:
        :param clientVersionInfo:
        :return:创建收货地址
        '''
        addressCreateURL = baseURL + URL + "?lang=%s&timeStamp=%s&access_token=%s" % (lang, timeStamp, access_token)
        self.logger.info("url为:%s" %addressCreateURL)
        return addressCreateURL



    def send_request_addressCreate(self,url):
        '''
        :param url:
        :param content:
        :return:
        '''
        headers = {"Content-Type": "application/json"}
        parameters = {
                        "name": "曾先生",
                        "mobile": "13417335080",
                        "provinceName": "上海市",
                        "postCode": "",
                        "cityName": "上海市",
                        "areaName": "黄浦区",
                        "address": "现在我",
                        "isDefault": 1
                            }
        self.logger.info("请求的参数为:%s" %parameters)
        r = requests.post(url, data=json.dumps(parameters), headers=headers,timeout=30)
        self.logger.info("返回的参数为:%s" % json.loads(r.text))
        return json.loads(r.text)