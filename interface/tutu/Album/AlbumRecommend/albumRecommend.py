#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/9/10 10:57
# @Author  : Durat
# @Email   : durant.zeng@sunvalley.com.cn
# @File    : albumRecommend.py
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




class albumRecommend:

    def __init__(self):
        self.logger = Logger(logger="albumRecommend").getlog()

    def get_albumRecommendURL(self,baseURL,URL,lang,timeStamp,clientVersionInfo,access_token):
        '''
        :param baseURL:
        :param lang:
        :param timeStamp:
        :param clientVersionInfo:
        :param access_token:
        :return:特辑推荐列表查询
        '''
        albumRecommendURL = baseURL + URL + "?lang=%s&timeStamp=%s&clientVersionInfo=%s&access_token=%s" % (lang, timeStamp, clientVersionInfo,access_token)
        self.logger.info("特辑推荐列表列表接口的URL为:%s" %albumRecommendURL)
        return albumRecommendURL



    @retry(stop_max_attempt_number=5, wait_random_min=1000, wait_random_max=2000, retry_on_result=_result)
    def send_request_albumRecommend(self,url,albumsId):
        '''
        :param url:
        :param albumsId:
        :return:
        '''
        headers = {"Content-Type": "application/json"}

        parameters = {
                "albumsId":albumsId
            }
        self.logger.info("请求的参数为%s" %parameters)
        r = requests.post(url, data=json.dumps(parameters), headers=headers,timeout=30)
        self.logger.info("返回的参数为:%s" % json.loads(r.text))
        return json.loads(r.text)

