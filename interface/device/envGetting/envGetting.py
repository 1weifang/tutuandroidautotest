#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/9/5 16:31
# @Author  : Durat
# @Email   : durant.zeng@sunvalley.com.cn
# @File    : envGetting.py
# @Software: PyCharm


import sys,os
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
import json
import requests
from common.Logger import Logger

class envGetting:

    def __init__(self):
        self.logger = Logger(logger="envGetting").getlog()

    def get_envGettingURL(self,baseURL,URL,lang,timeStamp,clientVersionInfo):
        '''
        :param baseURL:
        :param lang:
        :param timeStamp:
        :param clientVersionInfo:
        :return:获取环境接口
        '''
        envGettingURL = baseURL + URL + "?lang=%s&timeStamp=%s&clientVersionInfo=%s" % (lang, timeStamp, clientVersionInfo)
        self.logger.info("url为:%s" %envGettingURL)
        return envGettingURL



    def send_request_envGetting(self,url,sn,verifyStr):
        '''
        :param url:
        :param sn:
        :return:
        '''
        headers = {"Content-Type": "application/json"}
        parameters = {
                    "sn":sn,
                    "verifyStr":verifyStr
                }
        self.logger.info("请求的参数为:%s" %parameters)
        r = requests.post(url, data=json.dumps(parameters), headers=headers,timeout=30)
        self.logger.info("返回的参数为:%s" % json.loads(r.text))
        return json.loads(r.text)


if __name__ == "__main__":
    ota = envGetting()
    URL = "https://env-proxy.nailtutu.com/api/envGetting?&timeStamp=20190905161420&clientVersionInfo=android_1.0.0&lang=zh"
    sn = "e4937a14f91c05a3"
    verifyStr = "SuBl3sIzSqCHUDltwBYRMz75aABTxPCpvvoowlKzLinCbTkhjotQLn1Yr4yxL3feSUQOtAVRA6Bt4PO+G8zXf0MtcHFEyHrw3YElxSKolG7ehMcRQGI9ozjRQdXEHi/LN5lY/16SGdbdNp4lYPsvd/93CyfIdLZ0HPgnBrfim08="

    result = ota.send_request_envGetting(URL,sn,verifyStr)
    # print(result["data"])
    # print(type(result["data"]))