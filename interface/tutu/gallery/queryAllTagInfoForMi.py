#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/2/25 15:33
# @Author  : Durat
# @Email   : durant.zeng@sunvalley.com.cn
# @File    : queryAllTagInfoForMi.py
# @Software: PyCharm


import sys,os
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
import json
import requests
from common.Logger import Logger




class queryAllTagInfoForMi:

    def __init__(self):
        self.logger = Logger(logger="queryAllTagInfoForMi").getlog()

    def get_getPicList4MiByidOrTagURL(self,baseURL,URL,lang,timeStamp,clientVersionInfo,access_token):
        '''
        :param baseURL:
        :param lang:
        :param timeStamp:
        :param clientVersionInfo:
        :param access_token:
        :return:彩绘图库-常用标签与标签
        '''
        ReallyURL = baseURL + URL + "?lang=%s&timeStamp=%s&clientVersionInfo=%s&access_token=%s" % (lang, timeStamp, clientVersionInfo,access_token)
        self.logger.info("url为:%s" %ReallyURL)
        return ReallyURL



    def send_request_queryAllTagInfoForMi(self,url,status):
        '''
        :param url:
        :param status:
        :return:
        '''
        headers = {"Content-Type": "application/json"}
        parameters = {
                "status":status
        }
        self.logger.info("请求的参数为:%s" %parameters)
        r = requests.post(url, data=json.dumps(parameters), headers=headers,timeout=30)
        self.logger.info("返回的参数为:%s" % json.loads(r.text))
        return json.loads(r.text)

