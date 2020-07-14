#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/11/21 13:50
# @Author  : Durat
# @Email   : durant.zeng@sunvalley.com.cn
# @File    : getAlbumsCommentReplySimpleList.py
# @Software: PyCharm


import sys,os
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
import json
import requests
from common.Logger import Logger



class getAlbumsCommentReplySimpleList:

    def __init__(self):
        self.logger = Logger(logger="getAlbumsCommentReplySimpleList").getlog()

    def get_getAlbumsCommentReplySimpleListURL(self,baseURL,URL,lang,timeStamp,clientVersionInfo,access_token):
        '''
        :param baseURL:
        :param lang:
        :param timeStamp:
        :param clientVersionInfo:
        :param access_token:
        :return:回复—列表查询(简单形)
        '''
        ReallyURL = baseURL + URL + "?lang=%s&timeStamp=%s&clientVersionInfo=%s&access_token=%s" % (lang, timeStamp, clientVersionInfo,access_token)
        self.logger.info("url为:%s" %ReallyURL)
        return ReallyURL



    def send_request_getAlbumsCommentReplySimpleList(self,url,commentId,currentPage,pageSize):
        '''
        :param url:
        :param currentPage:
        :param pageSize:
        :return:
        '''
        headers = {"Content-Type": "application/json"}
        parameters = {
                "commentId":commentId,
                "pageSize":pageSize,
                "currentPage":currentPage
            }
        self.logger.info("请求的参数为:%s" %parameters)
        r = requests.post(url, data=json.dumps(parameters), headers=headers,timeout=30)
        self.logger.info("返回的参数为:%s" % json.loads(r.text))
        return json.loads(r.text)

