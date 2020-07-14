#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/6/11 13:49
# @Author  : Durat
# @Email   : durant.zeng@sunvalley.com.cn
# @File    : albumsCollection4Front.py
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




class albumsCollection4Front:

    def __init__(self):
        self.logger = Logger(logger="albumsCollection4Front").getlog()

    def get_albumsShare4FrontURL(self,baseURL,URL,lang,timeStamp,clientVersionInfo,access_token):
        '''
        :param baseURL:
        :param lang:
        :param timeStamp:
        :param clientVersionInfo:
        :param access_token:
        :return:专辑图片收藏(分为，一键收藏和单独收藏)
        '''
        albumsCollection4FrontURL = baseURL + URL + "?lang=%s&timeStamp=%s&clientVersionInfo=%s&access_token=%s" % (lang, timeStamp, clientVersionInfo,access_token)
        self.logger.info("url为:%s" %albumsCollection4FrontURL)
        return albumsCollection4FrontURL


    @retry(stop_max_attempt_number=5, wait_random_min=1000, wait_random_max=2000, retry_on_result=_result)
    def send_request_albumsCollection4Front(self,url,albumsId,allConnection,galleryId=None,galleryType=None):
        '''
        :param url:
        :param albumsId:
        :param allConnection:
        :param galleryId:
        :return:
        '''

        headers = {"Content-Type": "application/json"}
        parameters = {
                    "albumsId":albumsId,
                    "allConnection":allConnection,
                    "galleryId":galleryId,
                    "galleryType":galleryType
                        }
        self.logger.info("请求的参数为:%s" % parameters)
        r = requests.post(url, data=json.dumps(parameters), headers=headers,timeout=30)
        self.logger.info("返回的参数为:%s" % json.loads(r.text))
        return json.loads(r.text)



    @retry(stop_max_attempt_number=5, wait_random_min=1000, wait_random_max=2000, retry_on_result=_result)
    def send_request_albumsCollection4Front_new(self,url,albumsId):
        '''
        :param url:
        :param albumsId:
        :param allConnection:
        :return:
        '''

        headers = {"Content-Type": "application/json"}
        parameters = {
                    "albumsId":albumsId,
                    "allConnection":True,
                    "collectVersion":"2.0"
                        }
        self.logger.info("请求的参数为:%s" % parameters)
        r = requests.post(url, data=json.dumps(parameters), headers=headers,timeout=30)
        self.logger.info("返回的参数为:%s" % json.loads(r.text))
        return json.loads(r.text)


if __name__ == "__main__":


    imi = albumsCollection4Front()
    url = "https://mi-api.nailtutu.com/imi/tOcAlbumsInfo/albumsCollection4Front?lang=zh&timeStamp=20190911092104&clientVersionInfo=android_1.0.30&access_token=be970c5d-f75c-4de9-b4c1-da0beb5e5787"
    albumsId = "24cbd164926b4cfd9f2fdc62e6415326"
    allConnection = False
    galleryId = "f591e2bd193443469d2c7ed0fd6600cc"
    imi.send_request_albumsCollection4Front(url,albumsId,allConnection,galleryId)