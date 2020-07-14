#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/2/25 13:46
# @Author  : Durat
# @Email   : durant.zeng@sunvalley.com.cn
# @File    : coverBanner.py
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



class coverBanner:

    def __init__(self):
        self.logger = Logger(logger="coverBanner").getlog()

    def get_coverBannerURL(self,baseURL,URL,lang,timeStamp,clientVersionInfo,access_token):
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


    @retry(stop_max_attempt_number=5, wait_random_min=1000, wait_random_max=2000, retry_on_result=_result)
    def send_request_coverBanner(self,url,appType,bannerModel):
        '''
        获取banner列表
        :param url:
        :param appType:
        :param bannerModel:
        :return:
        '''
        headers = {"Content-Type": "application/json"}
        parameters = {
                    "appType":appType,
                    "bannerModel":bannerModel
                }
        self.logger.info("请求的参数为:%s" %parameters)
        r = requests.post(url, data=json.dumps(parameters), headers=headers,timeout=30)
        self.logger.info("返回的参数为:%s" % json.loads(r.text))
        return json.loads(r.text)


