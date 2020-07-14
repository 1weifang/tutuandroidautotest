#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/10/14 13:48
# @Author  : Durat
# @Email   : durant.zeng@sunvalley.com.cn
# @File    : changeDeviceName.py
# @Software: PyCharm

import sys,os
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
import json
import requests
from common.Logger import Logger



class changeDeviceName:


    def __init__(self):
        self.logger = Logger(logger="changeDeviceName").getlog()


    def get_changeDeviceNameURL(self,baseURL,URL,lang,timeStamp,access_token):
        '''
        :param baseURL:
        :param lang:
        :param timeStamp:
        :param clientVersionInfo:
        :return:设备别名修改接口
        '''
        reallyURL = baseURL + URL + "?lang=%s&timeStamp=%s&access_token=%s" % (lang, timeStamp, access_token)
        self.logger.info("url为:%s" %reallyURL)
        return reallyURL



    def send_request_changeDeviceName(self,url,deviceId,deviceName):
        '''
        :param url:
        :param content:
        :return:
        '''
        headers = {"Content-Type": "application/json"}
        parameters = {
                    "deviceId": deviceId,
                    "deviceName":deviceName
                }
        self.logger.info("请求的参数为:%s" %parameters)
        r = requests.post(url, data=json.dumps(parameters), headers=headers,timeout=30)
        self.logger.info("返回的参数为:%s" % json.loads(r.text))
        return json.loads(r.text)