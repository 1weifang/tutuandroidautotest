#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/8/21 14:32
# @Author  : Durat
# @Email   : durant.zeng@sunvalley.com.cn
# @File    : getPadAppVersion.py
# @Software: PyCharm

import sys,os
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
import json
import requests
from common.Logger import Logger

class getPadAppVersion:

    def __init__(self):
        self.logger = Logger(logger="getPadAppVersion").getlog()

    def get_getPadAppVersionURL(self,baseURL,URL,lang,timeStamp,clientVersionInfo,access_token):
        '''
        :param baseURL:
        :param lang:
        :param timeStamp:
        :param clientVersionInfo:
        :param access_token:
        :return:pad应用-获取包
        '''
        getPadAppVersionURL = baseURL + URL + "?lang=%s&timeStamp=%s&clientVersionInfo=%s&access_token=%s" % (lang, timeStamp, clientVersionInfo,access_token)
        self.logger.info("url为:%s" %getPadAppVersionURL)
        return getPadAppVersionURL



    def send_request_getPadAppVersion(self,url,location,sn):
        '''
        :param url:
        :param location:
        :param sn:
        :return:
        '''
        headers = {"Content-Type": "application/json"}
        parameters = {
                    "location":location,
                    "sn":sn
                }
        self.logger.info("请求的参数为:%s" %parameters)
        r = requests.post(url, data=json.dumps(parameters), headers=headers,timeout=30)
        self.logger.info("返回的参数为:%s" % json.loads(r.text))
        return json.loads(r.text)

# if __name__ == "__main__":
#
#
#     imi = getPadAppVersion()
#     # print(imi)
#     phone = "13417335080"
#     config = FileParser(r'D:\anjouAutoTest\config\config.ini')
#     dev_AC_URL = config.get('Authentication', 'dev')
#     base = baseUtils()
#     clientVersionInfo = )config1.get("clientVersionInfo", "clientVersionInfo_ch_pad_1.0.34")
#     lang = config1.get("lang", "zh")
#     currentTime = base.getTimeStamp()
#     AC = Authentication()
#     DATA = AC.get_PAD_CN_logged_in(phone)
#     url = AC.get_AuthenticationURL(dev_AC_URL, lang, currentTime, clientVersionInfo)
#
#     access_token = AC.get_Access_token(url, DATA)
#
#     config2 = FileParser(r'D:\anjouAutoTest\config\api_url.ini')
#     base_url = config2.get("base_url","base_url_dev")


