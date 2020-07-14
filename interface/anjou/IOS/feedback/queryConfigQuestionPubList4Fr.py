#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/2/26 9:39
# @Author  : Durat
# @Email   : durant.zeng@sunvalley.com.cn
# @File    : queryConfigQuestionPubList4Fr.py
# @Software: PyCharm

import sys,os
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
import json
import requests
from common.Logger import Logger


class queryConfigQuestionPubList4Fr:

    def __init__(self):
        self.logger = Logger(logger="queryConfigQuestionPubList4Fr").getlog()

    def get_queryConfigQuestionPubList4FrURL(self,baseURL,URL,lang,timeStamp,clientVersionInfo,access_token):
        '''
        :param baseURL:
        :param lang:
        :param timeStamp:
        :param clientVersionInfo:
        :return:
        '''
        ReallyURL = baseURL + URL + "?access_token=%s&lang=%s&timeStamp=%s&clientVersionInfo=%s" % (access_token,lang, timeStamp, clientVersionInfo)
        self.logger.info("url为:%s" %ReallyURL)
        return ReallyURL



    def send_request_queryConfigQuestionPubList4Fr(self,url):
        '''
        用户反馈问题分类&发布的信息4Fr-查询
        :param url:
        :return:
        '''
        headers = {"Content-Type": "application/json"}
        parameters = {
                }
        self.logger.info("请求的参数为:%s" %parameters)
        r = requests.post(url, data=json.dumps(parameters), headers=headers,timeout=30)
        self.logger.info("返回的参数为:%s" % json.loads(r.text))
        return json.loads(r.text)