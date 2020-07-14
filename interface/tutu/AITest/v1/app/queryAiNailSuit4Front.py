#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/11/19 11:22
# @Author  : Durat
# @Email   : durant.zeng@sunvalley.com.cn
# @File    : queryAiNailSuit4Front.py
# @Software: PyCharm

import sys,os
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
import json
import requests
from common.Logger import Logger



class queryAiNailSuit4Front:

    def __init__(self):
        self.logger = Logger(logger="queryAiNailSuit4Front").getlog()

    def get_queryAiNailSuit4FrontURL(self,baseURL,URL,lang,timeStamp,clientVersionInfo,access_token):
        '''
        :param baseURL:
        :param lang:
        :param timeStamp:
        :param clientVersionInfo:
        :param access_token:
        :return:Ai试甲-查Ai推荐套图+特辑套图(如果有)+普通套图
        '''
        ReallyURL = baseURL + URL + "?lang=%s&timeStamp=%s&clientVersionInfo=%s&access_token=%s" % (lang, timeStamp, clientVersionInfo,access_token)
        self.logger.info("url为:%s" %ReallyURL)
        return ReallyURL



    def send_request_queryAiNailSuit4Front(self,url,inputPicName,inputPicUrl,inputPicWidth,inputPicHeight,currentPage,pageSize,albumsId=None):
        '''
        :param url:
        :param currentPage:
        :param pageSize:
        :return:
        '''
        headers = {"Content-Type": "application/json"}
        parameters = {
                "inputPicName": inputPicName,
                "inputPicUrl": inputPicUrl,
                "inputPicWidth": inputPicWidth,
                "inputPicHeight": inputPicHeight,
                "albumsId":albumsId,
                "currentPage": currentPage,
                "pageSize":pageSize,
                "arithVersion":"2.0"

            }
        self.logger.info("请求的参数为:%s" %parameters)
        r = requests.post(url, data=json.dumps(parameters), headers=headers,timeout=30)
        self.logger.info("返回的参数为:%s" % json.loads(r.text))
        return json.loads(r.text)