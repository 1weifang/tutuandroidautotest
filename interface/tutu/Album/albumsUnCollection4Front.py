#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/6/11 15:05
# @Author  : Durat
# @Email   : durant.zeng@sunvalley.com.cn
# @File    : albumsUnCollection4Front.py
# @Software: PyCharm

import sys,os
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
import json
import requests
from common.FileParsing import FileParser
from common.baseUtil import baseUtils
from interface.base.login.authentication import Authentication
from common.Logger import Logger
from retrying import retry

def _result(result):
    return result is None



class albumsUnCollection4Front:

    def __init__(self):
        self.logger = Logger(logger="albumsUnCollection4Front").getlog()

    def get_albumsUnCollection4FrontURL(self,baseURL,URL,lang,timeStamp,clientVersionInfo,access_token):
        '''
        :param baseURL:
        :param lang:
        :param timeStamp:
        :param clientVersionInfo:
        :param access_token:
        :return:特辑-专辑图片取消收藏(分为，一键收藏和单独收藏)
        '''
        albumsUnCollection4FrontURL = baseURL + URL + "?lang=%s&timeStamp=%s&clientVersionInfo=%s&access_token=%s" % (lang, timeStamp, clientVersionInfo,access_token)
        self.logger.info("url为:%s" %albumsUnCollection4FrontURL)
        return albumsUnCollection4FrontURL



    @retry(stop_max_attempt_number=5, wait_random_min=1000, wait_random_max=2000, retry_on_result=_result)
    def send_request_albumsUnCollection4Front(self,url,albumsId,isallConnectionRemove,galleryId):
        '''
        :param url:
        :param albumsId:
        :param allConnection:
        :param galleryId:
        :return:
        '''

        headers = {"Content-Type": "application/json"}

        allConnectionRemove = True
        NotallConnectionRemove = False
        if isallConnectionRemove == "一键取消收藏":
            parameters = {
                    "albumsId":albumsId,
                    "allConnectionRemove":allConnectionRemove
                }
            self.logger.info("请求的参数为:%s" % parameters)
            r = requests.post(url, data=json.dumps(parameters), headers=headers,timeout=30)
            self.logger.info("返回的参数为:%s" % json.loads(r.text))
            return json.loads(r.text)

        elif isallConnectionRemove == "取消收藏":
            parameters = {
                    "albumsId":albumsId,
                    "allConnectionRemove":NotallConnectionRemove,
                    "galleryId":galleryId
                }
            self.logger.info("请求的参数为:%s" % parameters)
            r = requests.post(url, data=json.dumps(parameters), headers=headers,timeout=30)
            self.logger.info("返回的参数为:%s" % json.loads(r.text))
            return json.loads(r.text)
        else:
            self.logger.error("传的参数有误，请检查！")



    @retry(stop_max_attempt_number=5, wait_random_min=1000, wait_random_max=2000, retry_on_result=_result)
    def send_request_albumsUnCollection4Front_new(self,url,albumsId):
        '''
        :param url:
        :param albumsId:
        :param allConnection:
        :return:
        '''

        headers = {"Content-Type": "application/json"}

        parameters = {
                    "albumsId":albumsId,
                    "allConnectionRemove":True,
                    "collectVersion": "2.0"
                }
        self.logger.info("请求的参数为:%s" % parameters)
        r = requests.post(url, data=json.dumps(parameters), headers=headers,timeout=30)
        self.logger.info("返回的参数为:%s" % json.loads(r.text))
        return json.loads(r.text)


if __name__ == "__main__":
    imi = albumsUnCollection4Front()
    # print(imi)
    phone = "13723746965"
    config0 = FileParser(r'D:\anjouAutoTest\config\Authentication_url.ini')
    dev_AC_URL = config0.get('Authentication', 'dev')
    print(dev_AC_URL)
    config1 = FileParser(r'D:\anjouAutoTest\config\env.ini')
    base = baseUtils()
    clientVersionInfo = config1.get("clientVersionInfo", "clientVersionInfo")
    lang = config1.get("lang", "zh")
    currentTime = base.getTimeStamp()
    AC = Authentication()
    DATA = AC.get_Android_CN_logged_in(phone)
    url = AC.get_AuthenticationURL(dev_AC_URL, lang, currentTime, clientVersionInfo)

    access_token = AC.get_Access_token(url, DATA)

    config2 = FileParser(r'D:\anjouAutoTest\config\api_url.ini')
    base_url = config2.get("base_url","base_url_dev")



    albumsUnCollection4FrontURL = config2.get("imi_cms_url","albumsUnCollection4FrontURL")
    albumsUnCollection4FrontURL = imi.get_albumsShare4FrontURL(base_url,albumsUnCollection4FrontURL,lang,currentTime,clientVersionInfo,access_token)


    # # print(queryDiyPicURL)
    #
    #
    albumsId = "0055358489bb44e8b40b41706fd0b6d6"
    allConnectionRemove = "一键取消收藏"
    galleryId = "0ab076b4fe274fbc8a1b30949bdb8236"
    # #
    # # # #
    imi.send_request_albumsUnCollection4Front(albumsUnCollection4FrontURL,albumsId,allConnectionRemove,galleryId)