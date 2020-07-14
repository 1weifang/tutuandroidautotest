#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/9/16 14:59
# @Author  : Durat
# @Email   : durant.zeng@sunvalley.com.cn
# @File    : PlanList.py
# @Software: PyCharm

import sys,os
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
import json
import requests
from common.Logger import Logger



class PlanList:

    def __init__(self):
        self.logger = Logger(logger="PlanList").getlog()

    def get_PlanListURL(self,baseURL,URL,lang,timeStamp,access_token):
        '''
        :param baseURL:
        :param lang:
        :param timeStamp:
        :param clientVersionInfo:
        :return:服务商方案列表
        '''
        planListURL = baseURL + URL + "?lang=%s&timeStamp=%s&access_token=%s" % (lang, timeStamp, access_token)
        self.logger.info("url为:%s" %planListURL)
        return planListURL



    def send_request_planList(self,url,twoAgentId,currentPage,pageSize):
        '''
        :param url:
        :param content:
        :return:
        '''
        headers = {"Content-Type": "application/json"}
        parameters = {
                    "currentPage": currentPage,
                    "pageSize": pageSize,
                    "twoAgentId":twoAgentId

                }
        self.logger.info("请求的参数为:%s" %parameters)
        r = requests.post(url, data=json.dumps(parameters), headers=headers,timeout=30)
        self.logger.info("返回的参数为:%s" % json.loads(r.text))
        return json.loads(r.text)

# if __name__ == "__main__":
#     tow = PlanList()
#     URL= "https://mi-api.nailtutu.com/agent/twoAgentList?&access_token=7d1f3989-7d42-44a1-af09-658b33175c20timeStamp=1568613520611lang=zh"
#     A = 1
#     B = 15
#     tow.send_request_twoAgentList(URL,A,B)