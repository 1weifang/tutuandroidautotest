#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/12/26 15:04
# @Author  : Durat
# @Email   : durant.zeng@sunvalley.com.cn
# @File    : queryArticleListByTag4Fr.py
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


class queryArticleListByTag4Fr:

    def __init__(self):
        self.logger = Logger(logger="queryArticleListByTag4Fr").getlog()

    def get_queryArticleListByTag4FrURL(self,baseURL,URL,lang,timeStamp,clientVersionInfo,access_token):
        '''
        :param baseURL:
        :param lang:
        :param timeStamp:
        :param clientVersionInfo:
        :param access_token:
        :return:ugc搜索出列表by标签4Fr
        '''
        ReallyURL = baseURL + URL + "?lang=%s&timeStamp=%s&clientVersionInfo=%s&access_token=%s" % (lang, timeStamp, clientVersionInfo,access_token)
        self.logger.info("接口的URL为:%s" %ReallyURL)
        return ReallyURL



    @retry(stop_max_attempt_number=5, wait_random_min=1000, wait_random_max=2000, retry_on_result=_result)
    def send_request_queryArticleListByTag4Fr(self,url,searchContent,currentPage,pageSize,searchType=None):
        '''
        :param url:
        :param searchContent:
        :param searchType:
        :param currentPage:
        :param pageSize:
        :return:
        '''
        headers = {"Content-Type": "application/json"}

        parameters = {
                "searchContent":searchContent,
                "currentPage": currentPage,
                "pageSize": pageSize,
                "searchType": searchType

        }
        self.logger.info("请求的参数为%s" %parameters)
        r = requests.post(url, data=json.dumps(parameters), headers=headers,timeout=30)
        self.logger.info("返回的参数为:%s" % json.loads(r.text))
        return json.loads(r.text)