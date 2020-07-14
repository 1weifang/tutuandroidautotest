#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/11/15 9:36
# @Author  : Durat
# @Email   : durant.zeng@sunvalley.com.cn
# @File    : loadBySn.py
# @Software: PyCharm

import sys,os
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
import json
import requests
from common.Logger import Logger



class loadBySn:

    def __init__(self):
        self.logger = Logger(logger="loadBySn").getlog()

    def get_loadBySnURL(self,baseURL,URL,lang,timeStamp,clientVersionInfo,access_token):
        '''
        :param baseURL:
        :param lang:
        :param timeStamp:
        :param clientVersionInfo:
        :param access_token:
        :return:获取设备模式接口
        '''
        ReallyURL = baseURL + URL + "?lang=%s&timeStamp=%s&clientVersionInfo=%s&access_token=%s" % (lang, timeStamp, clientVersionInfo,access_token)
        self.logger.info("url为:%s" %ReallyURL)
        return ReallyURL



    def send_request_loadBySn(self,url,sn):
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
    ota = loadBySn()
    URL = "https://mi-api.nailtutu.com/imi/agent/getDeviceModel?lang=zh&timeStamp=20191114163736&clientVersionInfo=android_1.0.30&access_token=3247d3b9-750d-455f-b9a4-0449d6d07c7e"
    sn = "e4937a14f91c05a3"

    result = ota.send_request_getDeviceModel(URL,sn)
    # print(result["data"])
    # print(type(result["data"]))