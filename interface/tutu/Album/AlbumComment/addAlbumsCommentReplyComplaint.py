#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/11/21 14:06
# @Author  : Durat
# @Email   : durant.zeng@sunvalley.com.cn
# @File    : addAlbumsCommentComplaint.py
# @Software: PyCharm

import sys,os
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
import json
import requests
from common.Logger import Logger



class addAlbumsCommentReplyComplaint:

    def __init__(self):
        self.logger = Logger(logger="addAlbumsCommentReplyComplaint").getlog()

    def get_addAlbumsCommentReplyComplaintURL(self,baseURL,URL,lang,timeStamp,clientVersionInfo,access_token):
        '''
        :param baseURL:
        :param lang:
        :param timeStamp:
        :param clientVersionInfo:
        :param access_token:
        :return:专辑评论--回复投诉
        '''
        ReallyURL = baseURL + URL + "?lang=%s&timeStamp=%s&clientVersionInfo=%s&access_token=%s" % (lang, timeStamp, clientVersionInfo,access_token)
        self.logger.info("url为:%s" %ReallyURL)
        return ReallyURL



    def send_request_addAlbumsCommentReplyComplaint(self,url,albumsId,commentId,complaintType,content,replyType,uid,replyId=None,toUid=None):
        '''
        :param url:
        :param albumsId:
        :param commentId:
        :param complaintType:
        :param content:
        :param replyType:
        :param uid:
        :param replyId:
        :param toUid:
        :return:
        '''
        headers = {"Content-Type": "application/json"}
        parameters = {
                "albumsId":albumsId,
                "commentId":commentId,
                "complaintType":complaintType,
                "content":content,
                "replyType":replyType,
                "uid":uid,
                "replyId":replyId,
                "toUid":toUid
            }
        self.logger.info("请求的参数为:%s" %parameters)
        r = requests.post(url, data=json.dumps(parameters), headers=headers,timeout=30)
        self.logger.info("返回的参数为:%s" % json.loads(r.text))
        return json.loads(r.text)

