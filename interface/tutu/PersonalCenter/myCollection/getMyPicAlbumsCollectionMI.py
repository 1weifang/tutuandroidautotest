#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/11/15 14:48
# @Author  : Durat
# @Email   : durant.zeng@sunvalley.com.cn
# @File    : getMyPicAlbumsCollectionMI.py
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



class getMyPicAlbumsCollectionMI:

    def __init__(self):
        self.logger = Logger(logger="getMyPicAlbumsCollectionMI").getlog()



    def get_getMyPicAlbumsCollectionMIURL(self,baseURL,URL,lang,timeStamp,clientVersionInfo,access_token):
        '''
        :param baseURL:
        :param lang:
        :param timeStamp:
        :param clientVersionInfo:
        :param access_token:
        :return:特辑-列表查询
        '''
        reallyURL = baseURL + URL + "?lang=%s&timeStamp=%s&clientVersionInfo=%s&access_token=%s" % (lang, timeStamp, clientVersionInfo,access_token)
        self.logger.info("url为:%s" %reallyURL)
        return reallyURL


    @retry(stop_max_attempt_number=5, wait_random_min=1000, wait_random_max=2000, retry_on_result=_result)
    def send_request_getMyPicAlbumsCollectionMI(self,url,currentPage,pageSize):
        '''
        :param url:
        :param currentPage:
        :param pageSize:
        :return:
        '''
        headers = {"Content-Type": "application/json"}
        parameters = {

            "currentPage":currentPage,
            "pageSize": pageSize
            }
        self.logger.info("请求的参数为:%s" %parameters)
        r = requests.post(url, data=json.dumps(parameters), headers=headers,timeout=30)
        self.logger.info("返回的参数为:%s" % json.loads(r.text))
        return json.loads(r.text)