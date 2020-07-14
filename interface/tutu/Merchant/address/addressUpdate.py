#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/9/16 20:04
# @Author  : Durat
# @Email   : durant.zeng@sunvalley.com.cn
# @File    : addressUpdate.py
# @Software: PyCharm


import sys,os
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
import json
import requests
from common.Logger import Logger


class addressUpdate:

    def __init__(self):
        self.logger = Logger(logger="addressUpdate").getlog()

    def get_addressUpdateURL(self,baseURL,URL,lang,timeStamp,access_token):
        '''
        :param baseURL:
        :param lang:
        :param timeStamp:
        :param clientVersionInfo:
        :return:修改收货地址
        '''
        addressUpdateURL = baseURL + URL + "?lang=%s&timeStamp=%s&access_token=%s" % (lang, timeStamp, access_token)
        self.logger.info("url为:%s" %addressUpdateURL)
        return addressUpdateURL



    def send_request_addressUpdate(self,url,addressId,userId,uid):
        '''
        :param url:
        :param content:
        :return:
        '''
        headers = {"Content-Type": "application/json"}
        parameters = {
                    "id":addressId,
                    "userId": userId,
                    "uid": uid,
                    "name": "曾先生",
                    "mobile": "13417335080",
                    "provinceName": "上海市",
                    "postCode": "",
                    "cityName": "上海市",
                    "areaName": "黄浦区",
                    "address": "现在我",
                    "isDefault": 0
                    }
        self.logger.info("请求的参数为:%s" % parameters)
        r = requests.post(url, data=json.dumps(parameters), headers=headers,timeout=30)
        self.logger.info("返回的参数为:%s" % json.loads(r.text))
        return json.loads(r.text)

