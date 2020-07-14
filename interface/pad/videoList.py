#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/2/24 15:46
# @Author  : Durat
# @Email   : durant.zeng@sunvalley.com.cn
# @File    : videoList.py
# @Software: PyCharm

import sys,os
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
import json
import requests
from common.Logger import Logger


class videoList:

    def __init__(self):
        self.logger = Logger(logger="videoList").getlog()

    def get_videoListURL(self,baseURL,URL,lang,timeStamp,clientVersionInfo,access_token):
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



    def send_request_videoList(self,url,columnId,currentPage,pageSize):
        '''
        视频列表
        :param url:
        :param columnId:
        :param currentPage:
        :param pageSize:
        :return:
        '''
        headers = {"Content-Type": "application/json"}
        parameters = {
                    "columnId":columnId,
                    "currentPage":currentPage,
                    "pageSize":pageSize
                }
        self.logger.info("请求的参数为:%s" %parameters)
        r = requests.post(url, data=json.dumps(parameters), headers=headers,timeout=30)
        self.logger.info("返回的参数为:%s" % json.loads(r.text))
        return json.loads(r.text)

