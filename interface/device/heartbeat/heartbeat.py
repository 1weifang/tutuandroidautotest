#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/9/6 9:28
# @Author  : Durat
# @Email   : durant.zeng@sunvalley.com.cn
# @File    : heartbeat.py
# @Software: PyCharm

import sys,os
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
import json
import requests
from common.baseUtil import baseUtils
from common.Logger import Logger
base = baseUtils()

class heartbeat:

    def __init__(self):
        self.logger = Logger(logger="heartbeat").getlog()

    def get_heartbeatURL(self,baseURL,URL,lang,timeStamp,clientVersionInfo):
        '''
        :param baseURL:
        :param lang:
        :param timeStamp:
        :param clientVersionInfo:
        :return:心跳接口
        '''
        heartbeatURL = baseURL + URL + "?lang=%s&timeStamp=%s&clientVersionInfo=%s" % (lang, timeStamp, clientVersionInfo)
        self.logger.info("url为:%s" %heartbeatURL)
        return heartbeatURL



    def send_request_heartbeat(self,url,sn,client_time):
        '''
        :param url:
        :param sn:
        :return:
        '''
        headers = {"Content-Type": "application/json"}
        parameters = {
                    "sn":sn,
                    "client_time":client_time
                }
        self.logger.info("请求的参数为:%s" %parameters)
        r = requests.post(url, data=json.dumps(parameters), headers=headers,timeout=30)
        self.logger.info("返回的参数为:%s" % json.loads(r.text))
        return json.loads(r.text)


if __name__ == "__main__":
    ota = heartbeat()
    URL = "https://env-proxy.nailtutu.com/api/heartbeat?&timeStamp=20190905161417&clientVersionInfo=android_1.0.0&lang=zh"
    sn = "e4937a14f91c05a3"
    verifyStr = "SuBl3sIzSqCHUDltwBYRMz75aABTxPCpvvoowlKzLinCbTkhjotQLn1Yr4yxL3feSUQOtAVRA6Bt4PO+G8zXf0MtcHFEyHrw3YElxSKolG7ehMcRQGI9ozjRQdXEHi/LN5lY/16SGdbdNp4lYPsvd/93CyfIdLZ0HPgnBrfim08="

    result = ota.send_request_heartbeat(URL,sn,base.get_millisecond())
    # print(result["data"])
    # print(type(result["data"]))

