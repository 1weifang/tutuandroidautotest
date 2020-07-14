#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/9/16 14:08
# @Author  : Durat
# @Email   : durant.zeng@sunvalley.com.cn
# @File    : twoAgentList.py
# @Software: PyCharm

import sys,os
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
import json
import requests
from common.Logger import Logger



class twoAgentList:


    def __init__(self):
        self.logger = Logger(logger="twoAgentList").getlog()

    def get_twoAgentListURL(self,baseURL,URL,lang,timeStamp,access_token):
        '''
        :param baseURL:
        :param lang:
        :param timeStamp:
        :param clientVersionInfo:
        :return:前端服务商列表
        '''
        twoAgentListURL = baseURL + URL + "?lang=%s&timeStamp=%s&access_token=%s" % (lang, timeStamp, access_token)
        self.logger.info("url为:%s" %twoAgentListURL)
        return twoAgentListURL



    def send_request_twoAgentList(self,url,currentPage,pageSize):
        '''
        :param url:
        :param content:
        :return:
        '''
        headers = {"Content-Type": "application/json"}
        parameters = {
                    "currentPage": currentPage,
                    "pageSize": pageSize

                }
        self.logger.info("请求的参数为:%s" %parameters)
        r = requests.post(url, data=json.dumps(parameters), headers=headers,timeout=30)
        self.logger.info("返回的参数为:%s" % json.loads(r.text))
        return json.loads(r.text)

if __name__ == "__main__":
    tow = twoAgentList()
    URL= "https://mi-api.nailtutu.com/agent/twoAgentList?&access_token=7d1f3989-7d42-44a1-af09-658b33175c20timeStamp=1568613520611lang=zh"
    A = 1
    B = 15
    tow.send_request_twoAgentList(URL,A,B)