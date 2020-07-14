#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/6/10 20:11
# @Author  : Durat
# @Email   : durant.zeng@sunvalley.com.cn
# @File    : getAlbumsDeatil4Front.py
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



class getAlbumsDeatil4Front:

    def __init__(self):
        self.logger = Logger(logger="getAlbumsDeatil4Front").getlog()

    def get_getAlbumsDeatil4FrontURL(self,baseURL,URL,lang,timeStamp,clientVersionInfo,access_token):
        '''
        :param baseURL:
        :param lang:
        :param timeStamp:
        :param clientVersionInfo:
        :param access_token:
        :return:特辑-前端列表详情
        '''
        getAlbumsDeatil4FrontURL = baseURL + URL + "?lang=%s&timeStamp=%s&clientVersionInfo=%s&access_token=%s" % (lang, timeStamp, clientVersionInfo,access_token)
        self.logger.info("url为:%s" %getAlbumsDeatil4FrontURL)
        return getAlbumsDeatil4FrontURL


    @retry(stop_max_attempt_number=5, wait_random_min=1000, wait_random_max=2000, retry_on_result=_result)
    def send_request_getAlbumsDeatil4Front(self,url,albumsId):
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



if __name__ == "__main__":


    imi = getAlbumsDeatil4Front()
    albumsId = "24cbd164926b4cfd9f2fdc62e6415326"
    url = "https://mi-api.nailtutu.com/imi/tOcAlbumsInfo/getAlbumsDeatil4Front?lang=zh&timeStamp=20190911090313&clientVersionInfo=android_app_ch_1.0.4&access_token=5d7cb718-38d3-48e6-9435-ec49dcb1985e"
    imi.send_request_getAlbumsDeatil4Front(url,albumsId)