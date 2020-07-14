#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/2/24 13:53
# @Author  : Durat
# @Email   : durant.zeng@sunvalley.com.cn
# @File    : getPicList4MiByidOrTag.py
# @Software: PyCharm


import sys,os
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
import json
import requests
from common.Logger import Logger


class getPicList4MiByidOrTag:

    def __init__(self):
        self.logger = Logger(logger="getPicList4MiByidOrTag").getlog()

    def get_getPicList4MiByidOrTagURL(self,baseURL,URL,lang,timeStamp,clientVersionInfo,access_token):
        '''
        :param baseURL:
        :param lang:
        :param timeStamp:
        :param clientVersionInfo:
        :return:
        '''
        ReallyURL = baseURL + URL + "?access_token=%s&lang=%s&timeStamp=%s&clientVersionInfo=%s" % (access_token,lang, timeStamp, clientVersionInfo)
        self.logger.info("url为:%s" %ReallyURL)
        return ReallyURL



    def send_request_getPicList4MiByidOrTag(self,url,currentPage,name,pageSize):
        '''
        获取特定标签下的所有图片
        :param url:
        :param currentPage:
        :param name:
        :param pageSize:
        :return:
        '''
        headers = {"Content-Type": "application/json"}
        parameters = {
                    "currentPage":currentPage,
                    "name":name,
                    "pageSize":pageSize
                }
        self.logger.info("请求的参数为:%s" %parameters)
        r = requests.post(url, data=json.dumps(parameters), headers=headers,timeout=30)
        self.logger.info("返回的参数为:%s" % json.loads(r.text))
        return json.loads(r.text)

