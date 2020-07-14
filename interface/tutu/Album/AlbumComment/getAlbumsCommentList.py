#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/11/21 9:58
# @Author  : Durat
# @Email   : durant.zeng@sunvalley.com.cn
# @File    : getAlbumsCommentList.py
# @Software: PyCharm


import sys,os
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
import json
import requests
from common.Logger import Logger



class getAlbumsCommentList:

    def __init__(self):
        self.logger = Logger(logger="getAlbumsCommentList").getlog()

    def get_getAlbumsCommentListURL(self,baseURL,URL,lang,timeStamp,clientVersionInfo,access_token):
        '''
        :param baseURL:
        :param lang:
        :param timeStamp:
        :param clientVersionInfo:
        :param access_token:
        :return:专辑评论列表查询
        '''
        ReallyURL = baseURL + URL + "?lang=%s&timeStamp=%s&clientVersionInfo=%s&access_token=%s" % (lang, timeStamp, clientVersionInfo,access_token)
        self.logger.info("url为:%s" %ReallyURL)
        return ReallyURL



    def send_request_getAlbumsCommentList(self,url,albumsId,currentPage,pageSize):
        '''
        :param url:
        :param currentPage:
        :param pageSize:
        :return:
        '''
        headers = {"Content-Type": "application/json"}
        parameters = {
                "albumsId":albumsId,
                "pageSize":pageSize,
                "currentPage":currentPage
            }
        self.logger.info("请求的参数为:%s" %parameters)
        r = requests.post(url, data=json.dumps(parameters), headers=headers,timeout=30)
        self.logger.info("返回的参数为:%s" % json.loads(r.text))
        return json.loads(r.text)




