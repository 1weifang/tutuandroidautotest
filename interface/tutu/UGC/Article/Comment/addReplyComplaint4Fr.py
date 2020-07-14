#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/2/28 10:57
# @Author  : Durat
# @Email   : durant.zeng@sunvalley.com.cn
# @File    : addReplyComplaint4Fr.py
# @Software: PyCharm


import sys,os
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
import json
import requests
from common.Logger import Logger
from retrying import retry

def _result(result):
    return result is None



class addReplyComplaint4Fr:

    def __init__(self):
        self.logger = Logger(logger="addReplyComplaint4Fr").getlog()

    def get_addReplyComplaint4FrURL(self,baseURL,URL,lang,timeStamp,clientVersionInfo,access_token):
        '''
        :param baseURL:
        :param lang:
        :param timeStamp:
        :param clientVersionInfo:
        :param access_token:
        :return:
        '''
        ReallyURL = baseURL + URL + "?lang=%s&timeStamp=%s&clientVersionInfo=%s&access_token=%s" % (lang, timeStamp, clientVersionInfo,access_token)
        self.logger.info("url为:%s" %ReallyURL)
        return ReallyURL


    @retry(stop_max_attempt_number=5, wait_random_min=1000, wait_random_max=2000, retry_on_result=_result)
    def send_request_addReplyComplaint4Fr(self,url,complaintType,articleId,commentId,replyId,replyType,content,uid,toUid,uidNickname=None,uidThumbnail=None,toUidNickname=None,toUidThumbnail=None,complaintUid=None,complaintUidNickname=None,complaintUidThumbnail=None):
        '''
        -投诉-对回复的投诉
        :param url:
        :param complaintType:
        :param articleId:
        :param commentId:
        :param replyId:
        :param replyType:
        :param content:
        :param uid:
        :param toUid:
        :param uidNickname:
        :param uidThumbnail:
        :param toUidNickname:
        :param toUidThumbnail:
        :param complaintUid:
        :param complaintUidNickname:
        :param complaintUidThumbnail:
        :return:
        '''
        headers = {"Content-Type": "application/json"}
        parameters = {
                "complaintType":complaintType,
                "articleId":articleId,
                "commentId":commentId,
                "replyId":replyId,
                "replyType":replyType,
                "content":content,
                "uid":uid,
                "toUid":toUid,
                "uidNickname":uidNickname,
                "uidThumbnail":uidThumbnail,
                "toUidNickname":toUidNickname,
                "toUidThumbnail":toUidThumbnail,
                "complaintUid":complaintUid,
                "complaintUidNickname":complaintUidNickname,
                "complaintUidThumbnail":complaintUidThumbnail

            }
        self.logger.info("请求的参数为:%s" %parameters)
        r = requests.post(url, data=json.dumps(parameters), headers=headers,timeout=30)
        self.logger.info("返回的参数为:%s" % json.loads(r.text))
        return json.loads(r.text)

