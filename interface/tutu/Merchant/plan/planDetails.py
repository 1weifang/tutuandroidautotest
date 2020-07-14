#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/9/16 21:01
# @Author  : Durat
# @Email   : durant.zeng@sunvalley.com.cn
# @File    : planDetails.py
# @Software: PyCharm

import sys,os
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
import json
import requests
from common.Logger import Logger



class planDetails:

    def __init__(self):
        self.logger = Logger(logger="planDetails").getlog()

    def get_planDetailsURL(self,baseURL,URL,lang,timeStamp,access_token):
        '''
        :param baseURL:
        :param lang:
        :param timeStamp:
        :param clientVersionInfo:
        :return:查看方案详情
        '''
        planDetailsURL = baseURL + URL + "?lang=%s&timeStamp=%s&access_token=%s" % (lang, timeStamp, access_token)
        self.logger.info("url为:%s" %planDetailsURL)
        return planDetailsURL



    def send_request_planDetails(self,url,rentProgramId):
        '''
        :param url:
        :param content:
        :return:
        '''
        headers = {"Content-Type": "application/json"}
        parameters = {
                    "rentProgramId": rentProgramId
                }
        self.logger.info("请求的参数为:%s" %parameters)
        r = requests.post(url, data=json.dumps(parameters), headers=headers,timeout=30)
        self.logger.info("返回的参数为:%s" % json.loads(r.text))
        return json.loads(r.text)