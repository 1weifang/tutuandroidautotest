#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/11/20 10:05
# @Author  : Durat
# @Email   : durant.zeng@sunvalley.com.cn
# @File    : queryAiNailSuitAgain4Front.py
# @Software: PyCharm

import sys,os
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
import json
import requests
from common.Logger import Logger



class queryAiNailSuitAgain4Front:

    def __init__(self):
        self.logger = Logger(logger="queryAiNailSuitAgain4Front").getlog()

    def get_queryAiNailSuitAgain4FrontURL(self,baseURL,URL,lang,timeStamp,clientVersionInfo,access_token):
        '''
        :param baseURL:
        :param lang:
        :param timeStamp:
        :param clientVersionInfo:
        :param access_token:
        :return:Ai试甲-非首次，查Ai推荐套图+特辑套图(如果有)+普通套图4Front
        '''
        ReallyURL = baseURL + URL + "?lang=%s&timeStamp=%s&clientVersionInfo=%s&access_token=%s" % (lang, timeStamp, clientVersionInfo,access_token)
        self.logger.info("url为:%s" %ReallyURL)
        return ReallyURL



    def send_request_queryAiNailSuitAgain4Front(self,url,tagList,nailSuitFlag,currentPage,pageSize,albumsId=None):
        '''
        :param url:
        :param currentPage:
        :param pageSize:
        :return:
        '''
        headers = {"Content-Type": "application/json"}
        parameters = {
                "tagList":tagList,
                "nailSuitFlag":nailSuitFlag,
                "currentPage": currentPage,
                "pageSize":pageSize,
                "albumsId":albumsId

            }
        self.logger.info("请求的参数为:%s" %parameters)
        r = requests.post(url, data=json.dumps(parameters), headers=headers,timeout=30)
        self.logger.info("返回的参数为:%s" % json.loads(r.text))
        return json.loads(r.text)