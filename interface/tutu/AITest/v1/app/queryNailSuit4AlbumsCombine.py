#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/11/19 10:15
# @Author  : Durat
# @Email   : durant.zeng@sunvalley.com.cn
# @File    : queryNailSuit4AlbumsCombine.py
# @Software: PyCharm


import sys,os
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
import json
import requests
from common.Logger import Logger



class queryNailSuit4AlbumsCombine:

    def __init__(self):
        self.logger = Logger(logger="queryNailSuit4AlbumsCombine").getlog()

    def get_queryNailSuit4AlbumsCombineURL(self,baseURL,URL,lang,timeStamp,clientVersionInfo,access_token):
        '''
        :param baseURL:
        :param lang:
        :param timeStamp:
        :param clientVersionInfo:
        :param access_token:
        :return:Ai试甲-查指定特辑套图和普通套图列表
        '''
        ReallyURL = baseURL + URL + "?lang=%s&timeStamp=%s&clientVersionInfo=%s&access_token=%s" % (lang, timeStamp, clientVersionInfo,access_token)
        self.logger.info("url为:%s" %ReallyURL)
        return ReallyURL



    def send_request_queryNailSuit4AlbumsCombine(self,url,albumsId,currentPage,pageSize):
        '''
        :param url:
        :param currentPage:
        :param pageSize:
        :return:
        '''
        headers = {"Content-Type": "application/json"}
        parameters = {
                "albumsId":albumsId,
                "currentPage": currentPage,
                "pageSize":pageSize

            }
        self.logger.info("请求的参数为:%s" %parameters)
        r = requests.post(url, data=json.dumps(parameters), headers=headers,timeout=30)
        self.logger.info("返回的参数为:%s" % json.loads(r.text))
        return json.loads(r.text)
