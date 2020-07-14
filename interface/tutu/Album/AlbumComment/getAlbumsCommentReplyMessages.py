#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/11/21 16:17
# @Author  : Durat
# @Email   : durant.zeng@sunvalley.com.cn
# @File    : getAlbumsCommentReplyMessages.py
# @Software: PyCharm

import sys,os
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
import json
import requests
from common.Logger import Logger



class getAlbumsCommentReplyMessages:

    def __init__(self):
        self.logger = Logger(logger="getAlbumsCommentReplyMessages").getlog()

    def get_getAlbumsCommentReplyMessagesURL(self,baseURL,URL,lang,timeStamp,clientVersionInfo,access_token):
        '''
        :param baseURL:
        :param lang:
        :param timeStamp:
        :param clientVersionInfo:
        :param access_token:
        :return:个人中心—消息查看
        '''
        ReallyURL = baseURL + URL + "?lang=%s&timeStamp=%s&clientVersionInfo=%s&access_token=%s" % (lang, timeStamp, clientVersionInfo,access_token)
        self.logger.info("url为:%s" %ReallyURL)
        return ReallyURL



    def send_request_getAlbumsCommentReplyMessages(self,url,currentPage,pageSize):
        '''
        :param url:
        :param currentPage:
        :param pageSize:
        :return:
        '''
        headers = {"Content-Type": "application/json"}
        parameters = {
                "pageSize":pageSize,
                "currentPage":currentPage
            }
        self.logger.info("请求的参数为:%s" %parameters)
        r = requests.post(url, data=json.dumps(parameters), headers=headers,timeout=30)
        self.logger.info("返回的参数为:%s" % json.loads(r.text))
        return json.loads(r.text)

