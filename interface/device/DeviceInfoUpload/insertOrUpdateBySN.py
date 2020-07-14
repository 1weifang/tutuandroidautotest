#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/9/6 13:57
# @Author  : Durat
# @Email   : durant.zeng@sunvalley.com.cn
# @File    : insertOrUpdateBySN.py
# @Software: PyCharm


import sys,os
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
import json
import requests
from common.baseUtil import baseUtils
from common.Logger import Logger
base = baseUtils()

class insertOrUpdateBySN:

    def __init__(self):
        self.logger = Logger(logger="insertOrUpdateBySN").getlog()

    def get_insertOrUpdateBySNURL(self,baseURL,URL,lang,timeStamp,clientVersionInfo):
        '''
        :param baseURL:
        :param lang:
        :param timeStamp:
        :param clientVersionInfo:
        :return:设备信息上传
        '''
        insertOrUpdateBySNURL = baseURL + URL + "?lang=%s&timeStamp=%s&clientVersionInfo=%s" % (lang, timeStamp, clientVersionInfo)
        self.logger.info("url为:%s" %insertOrUpdateBySNURL)
        return insertOrUpdateBySNURL



    def send_request_insertOrUpdateBySN(self,url,sn):
        '''
        :param url:
        :param sn:
        :return:
        '''
        headers = {"Content-Type": "application/json"}
        parameters = {

                "appVersion": "cn:1.0.34_df275d3,en:1.0.34_",
                "cpu": "1.10_0.71_0.31",
                "deviceVersion": "1.0.34_2df3b8d8f3",
                "hardVersion": "4",
                "ipAddr": "Server obtain",
                "latitude": "22.604299",
                "longitude": "114.057696",
                "memory": "1.68GB",
                "sn": sn,
                "stm32Version": "47",
                "storage": "11.57GB",
                "temperature": "54240"

                }
        self.logger.info("请求的参数为:%s" %parameters)
        r = requests.post(url, data=json.dumps(parameters), headers=headers,timeout=30)
        self.logger.info("返回的参数为:%s" % json.loads(r.text))
        return json.loads(r.text)


if __name__ == "__main__":
    ota = insertOrUpdateBySN()
    URL = "https://env-proxy.nailtutu.com/api/platformDeviceInfo/insertOrUpdateBySN?&timeStamp=20190906135132&clientVersionInfo=android_1.0.0&lang=zh"
    sn = "e4937a14f91c05a3"

    result = ota.send_request_insertOrUpdateBySN(URL,sn)
    # print(result["data"])
    # print(type(result["data"]))