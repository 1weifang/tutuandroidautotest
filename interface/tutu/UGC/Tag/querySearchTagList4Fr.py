#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/12/26 15:03
# @Author  : Durat
# @Email   : durant.zeng@sunvalley.com.cn
# @File    : querySearchTagList4Fr.py
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



class querySearchTagList4Fr:

    def __init__(self):
        self.logger = Logger(logger="querySearchTagList4Fr").getlog()

    def get_querySearchTagList4FrURL(self,baseURL,URL,lang,timeStamp,clientVersionInfo,access_token):
        '''
        :param baseURL:
        :param lang:
        :param timeStamp:
        :param clientVersionInfo:
        :param access_token:
        :return:标签列表
        '''
        ReallyURL = baseURL + URL + "?lang=%s&timeStamp=%s&clientVersionInfo=%s&access_token=%s" % (lang, timeStamp, clientVersionInfo,access_token)
        self.logger.info("接口的URL为:%s" %ReallyURL)
        return ReallyURL


    @retry(stop_max_attempt_number=5, wait_random_min=1000, wait_random_max=2000, retry_on_result=_result)
    def send_request_querySearchTagList4Fr(self,url):
        '''
        :param url
        :return:
        '''
        headers = {"Content-Type": "application/json"}

        parameters = {
        }
        self.logger.info("请求的参数为%s" %parameters)
        r = requests.post(url, data=json.dumps(parameters), headers=headers,timeout=30)
        self.logger.info("返回的参数为:%s" % json.loads(r.text))
        return json.loads(r.text)
