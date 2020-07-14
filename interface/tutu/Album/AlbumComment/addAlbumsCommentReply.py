#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/11/21 10:36
# @Author  : Durat
# @Email   : durant.zeng@sunvalley.com.cn
# @File    : addAlbumsCommentReply.py
# @Software: PyCharm

import sys,os
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
import json
import requests
from common.Logger import Logger



class addAlbumsCommentReply:

    def __init__(self):
        self.logger = Logger(logger="addAlbumsCommentReply").getlog()

    def get_addAlbumsCommentReplyURL(self,baseURL,URL,lang,timeStamp,clientVersionInfo,access_token):
        '''
        :param baseURL:
        :param lang:
        :param timeStamp:
        :param clientVersionInfo:
        :param access_token:
        :return:回复专辑评论
        '''
        ReallyURL = baseURL + URL + "?lang=%s&timeStamp=%s&clientVersionInfo=%s&access_token=%s" % (lang, timeStamp, clientVersionInfo,access_token)
        self.logger.info("url为:%s" %ReallyURL)
        return ReallyURL



    def send_request_addAlbumsCommentReply(self,url,commentId,content,replyId,replyType,toUid=None,toUidNickname=None,toUidHeadPortrait=None):
        '''
        :param url:
        :param albumsId:
        :param content:
        :return:
        '''
        headers = {"Content-Type": "application/json"}
        parameters = {
                "commentId":commentId,
                "content":content,
                "replyId": replyId,
                "replyType": replyType,
                "toUid": toUid,
                "toUidNickname":toUidNickname,
                "toUidHeadPortrait":toUidHeadPortrait

            }
        self.logger.info("请求的参数为:%s" %parameters)
        r = requests.post(url, data=json.dumps(parameters), headers=headers,timeout=30)
        self.logger.info("返回的参数为:%s" % json.loads(r.text))
        return json.loads(r.text)
