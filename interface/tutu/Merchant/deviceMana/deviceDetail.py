#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/10/14 13:36
# @Author  : Durat
# @Email   : durant.zeng@sunvalley.com.cn
# @File    : deviceDetail.py
# @Software: PyCharm

import sys,os
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
import json
import requests
from common.Logger import Logger



class deviceDetail:


    def __init__(self):
        self.logger = Logger(logger="deviceDetail").getlog()


    def get_deviceDetailURL(self,baseURL,URL,lang,timeStamp,access_token):
        '''
        :param baseURL:
        :param lang:
        :param timeStamp:
        :param clientVersionInfo:
        :return:设备列表
        '''
        reallyURL = baseURL + URL + "?lang=%s&timeStamp=%s&access_token=%s" % (lang, timeStamp, access_token)
        self.logger.info("url为:%s" %reallyURL)
        return reallyURL



    def send_request_deviceDetail(self,url,deviceId):
        '''
        :param url:
        :param content:
        :return:
        '''
        headers = {"Content-Type": "application/json"}
        parameters = {
                    "deviceId": deviceId
                }
        self.logger.info("请求的参数为:%s" %parameters)
        r = requests.post(url, data=json.dumps(parameters), headers=headers,timeout=30)
        self.logger.info("返回的参数为:%s" % json.loads(r.text))
        return json.loads(r.text)

if __name__ == "__main__":
    tow = deviceDetail()
    URL= "https://mi-api.nailtutu.com/imi/agent/malfunction/list?&access_token=124737d8-ff17-4d99-b0a7-c64161880285timeStamp=1568613520611lang=zh"
    A = 1
    B = 15
    tow.send_request_deviceDetail(URL,A,B)