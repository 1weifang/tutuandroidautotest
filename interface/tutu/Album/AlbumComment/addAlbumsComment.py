#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/11/21 10:13
# @Author  : Durat
# @Email   : durant.zeng@sunvalley.com.cn
# @File    : addAlbumsComment.py
# @Software: PyCharm


import sys,os
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
import json
import requests
from common.Logger import Logger



class addAlbumsComment:

    def __init__(self):
        self.logger = Logger(logger="addAlbumsComment").getlog()

    def get_addAlbumsCommentURL(self,baseURL,URL,lang,timeStamp,clientVersionInfo,access_token):
        '''
        :param baseURL:
        :param lang:
        :param timeStamp:
        :param clientVersionInfo:
        :param access_token:
        :return:发表专辑评论
        '''
        ReallyURL = baseURL + URL + "?lang=%s&timeStamp=%s&clientVersionInfo=%s&access_token=%s" % (lang, timeStamp, clientVersionInfo,access_token)
        self.logger.info("url为:%s" %ReallyURL)
        return ReallyURL



    def send_request_addAlbumsComment(self,url,albumsId,content):
        '''
        :param url:
        :param albumsId:
        :param content:
        :return:
        '''
        headers = {"Content-Type": "application/json"}
        parameters = {
                "albumsId":albumsId,
                "content":content
            }
        self.logger.info("请求的参数为:%s" %parameters)
        r = requests.post(url, data=json.dumps(parameters), headers=headers,timeout=30)
        self.logger.info("返回的参数为:%s" % json.loads(r.text))
        return json.loads(r.text)
