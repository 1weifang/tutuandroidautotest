#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/11/18 15:31
# @Author  : Durat
# @Email   : durant.zeng@sunvalley.com.cn
# @File    : getMyPicAlbumsCollectionDetailMI.py
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





class getMyPicAlbumsCollectionDetailMI:

    def __init__(self):
        self.logger = Logger(logger="getMyPicAlbumsCollectionDetailMI").getlog()



    def get_getMyPicAlbumsCollectionDetailMIURL(self,baseURL,URL,lang,timeStamp,clientVersionInfo,access_token):
        '''
        :param baseURL:
        :param lang:
        :param timeStamp:
        :param clientVersionInfo:
        :param access_token:
        :return:个人中心--我的收藏--专辑详情
        '''
        reallyURL = baseURL + URL + "?lang=%s&timeStamp=%s&clientVersionInfo=%s&access_token=%s" % (lang, timeStamp, clientVersionInfo,access_token)
        self.logger.info("url为:%s" %reallyURL)
        return reallyURL


    @retry(stop_max_attempt_number=5, wait_random_min=1000, wait_random_max=2000, retry_on_result=_result)
    def send_request_getMyPicAlbumsCollectionDetailMI(self,url,albumsId):
        '''
        :param url:
        :param albumsId:
        :return:
        '''
        headers = {"Content-Type": "application/json"}
        parameters = {

            "albumsId":albumsId
            }
        self.logger.info("请求的参数为:%s" %parameters)
        r = requests.post(url, data=json.dumps(parameters), headers=headers,timeout=30)
        self.logger.info("返回的参数为:%s" % json.loads(r.text))
        return json.loads(r.text)