#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/9/6 9:57
# @Author  : Durat
# @Email   : durant.zeng@sunvalley.com.cn
# @File    : calibrationGetting.py
# @Software: PyCharm

import sys,os
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
import json
import requests
from common.baseUtil import baseUtils
from common.Logger import Logger
base = baseUtils()

class calibrationGetting:

    def __init__(self):
        self.logger = Logger(logger="calibrationGetting").getlog()

    def get_calibrationGettingURL(self,baseURL,URL,lang,timeStamp,clientVersionInfo):
        '''
        :param baseURL:
        :param lang:
        :param timeStamp:
        :param clientVersionInfo:
        :return:校准参数获取
        '''
        calibrationGettingURL = baseURL + URL + "?lang=%s&timeStamp=%s&clientVersionInfo=%s" % (lang, timeStamp, clientVersionInfo)
        self.logger.info("url为:%s" %calibrationGettingURL)
        return calibrationGettingURL



    def send_request_calibrationGetting(self,url,sn):
        '''
        :param url:
        :param sn:
        :return:
        '''
        headers = {"Content-Type": "application/json"}
        parameters = {
                    "sn":sn
                }
        self.logger.info("请求的参数为:%s" %parameters)
        r = requests.post(url, data=json.dumps(parameters), headers=headers,timeout=30)
        self.logger.info("返回的参数为:%s" % json.loads(r.text))
        return json.loads(r.text)


if __name__ == "__main__":
    ota = calibrationGetting()
    URL = "https://env-proxy.nailtutu.com/api/cms/machine/calibrationGetting?&timeStamp=20190905161449&clientVersionInfo=android_1.0.0&lang=zh"
    sn = "e4937a14f91c05a3"

    result = ota.send_request_calibrationGetting(URL,sn)
    # print(result["data"])
    # print(type(result["data"]))