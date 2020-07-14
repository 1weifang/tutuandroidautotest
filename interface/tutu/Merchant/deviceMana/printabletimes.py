#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/10/15 16:03
# @Author  : Durat
# @Email   : durant.zeng@sunvalley.com.cn
# @File    : printabletimes.py
# @Software: PyCharm

import sys,os
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
import json
import requests
from common.Logger import Logger



class printabletimes:


    def __init__(self):
        self.logger = Logger(logger="printabletimes").getlog()


    def get_printabletimesURL(self,baseURL,URL,lang,timeStamp,clientVersionInfo,access_token):
        '''
        :param baseURL:
        :param lang:
        :param timeStamp:
        :param clientVersionInfo:
        :return:查看设备可打印次数
        '''
        reallyURL = baseURL + URL + "?lang=%s&timeStamp=%s&clientVersionInfo=%s&access_token=%s" % (lang, timeStamp,clientVersionInfo,access_token)
        self.logger.info("url为:%s" %reallyURL)
        return reallyURL



    def send_request_printabletimes(self,url,printerModel,sn):
        '''
        :param url:
        :param content:
        :return:
        '''
        headers = {"Content-Type": "application/json"}
        parameters = {
                "printerModel":str(printerModel),
                "sn":sn
                }
        self.logger.info("请求的参数为:%s" %parameters)
        r = requests.post(url, data=json.dumps(parameters), headers=headers,timeout=30)
        self.logger.info("返回的参数为:%s" % json.loads(r.text))
        return json.loads(r.text)