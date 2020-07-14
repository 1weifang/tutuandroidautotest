#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/12/26 16:53
# @Author  : Durat
# @Email   : durant.zeng@sunvalley.com.cn
# @File    : queryArticleListOfDiscover4Fr.py
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



class queryArticleListOfDiscover4Fr:

    def __init__(self):
        self.logger = Logger(logger="queryArticleListOfDiscover4Fr").getlog()

    def get_queryArticleListOfDiscover4FrURL(self,baseURL,URL,lang,timeStamp,clientVersionInfo,access_token):
        '''
        :param baseURL:
        :param lang:
        :param timeStamp:
        :param clientVersionInfo:
        :param access_token:
        :return:ugc文章-发现
        '''
        ReallyURL = baseURL + URL + "?lang=%s&timeStamp=%s&clientVersionInfo=%s&access_token=%s" % (lang, timeStamp, clientVersionInfo,access_token)
        self.logger.info("接口的URL为:%s" %ReallyURL)
        return ReallyURL



    @retry(stop_max_attempt_number=5, wait_random_min=1000, wait_random_max=2000, retry_on_result=_result)
    def send_request_queryArticleListOfDiscover4Fr(self,url,orderBy,currentPage,pageSize,userLongitude=None,userLatitude=None):
        '''
        :param url:
        :param orderBy:
        :param currentPage:
        :param pageSize:
        :param userLongitude:
        :param userLatitude:
        :return:
        '''
        headers = {"Content-Type": "application/json"}

        parameters = {
                "orderBy":orderBy,
                "currentPage":currentPage,
                "pageSize":pageSize,
                "userLongitude":userLongitude,
                "userLatitude":userLatitude
        }
        self.logger.info("请求的参数为%s" %parameters)
        r = requests.post(url, data=json.dumps(parameters), headers=headers,timeout=30)
        self.logger.info("返回的参数为:%s" % json.loads(r.text))
        return json.loads(r.text)