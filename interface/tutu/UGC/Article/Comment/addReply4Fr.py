#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/2/27 17:03
# @Author  : Durat
# @Email   : durant.zeng@sunvalley.com.cn
# @File    : addReply4Fr.py
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




class addReply4Fr:

    def __init__(self):
        self.logger = Logger(logger="addReply4Fr").getlog()

    def get_addReply4FrURL(self,baseURL,URL,lang,timeStamp,clientVersionInfo,access_token):
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
    def send_request_addReply4Fr(self,url,commentId,replyId,replyType,content,toUid,uid=None,uidNickname=None,uidHeadPortrait=None,uidThumbnail=None,toUidNickname=None,toUidHeadPortrait=None,toUidThumbnail=None):
        '''

        :param url:
        :param articleId:
        :param content:
        :param uid:
        :param uidNickname:
        :param uidHeadPortrait:
        :param uidThumbnail:
        :return:
        '''
        headers = {"Content-Type": "application/json"}
        parameters = {
                "commentId":commentId,
                "replyId":replyId,
                "replyType":replyType,
                "content":content,
                "toUid": toUid,
                "uid":uid,
                "uidNickname":uidNickname,
                "uidHeadPortrait":uidHeadPortrait,
                "uidThumbnail":uidThumbnail,
                "toUidNickname":toUidNickname,
                "toUidHeadPortrait":toUidHeadPortrait,
                "toUidThumbnail":toUidThumbnail
            }
        self.logger.info("请求的参数为:%s" %parameters)
        r = requests.post(url, data=json.dumps(parameters), headers=headers,timeout=30)
        self.logger.info("返回的参数为:%s" % json.loads(r.text))
        return json.loads(r.text)
