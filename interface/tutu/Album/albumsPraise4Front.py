#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/6/10 20:18
# @Author  : Durat
# @Email   : durant.zeng@sunvalley.com.cn
# @File    : albumsPraise4Front.py
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


class albumsPraise4Front:

    def __init__(self):
        self.logger = Logger(logger="albumsPraise4Front").getlog()

    def get_albumsPraise4FrontURL(self,baseURL,URL,lang,timeStamp,clientVersionInfo,access_token):
        '''
        :param baseURL:
        :param lang:
        :param timeStamp:
        :param clientVersionInfo:
        :param access_token:
        :return:特辑-前端列表点赞
        '''
        albumsPraise4FrontURL = baseURL + URL + "?lang=%s&timeStamp=%s&clientVersionInfo=%s&access_token=%s" % (lang, timeStamp, clientVersionInfo,access_token)
        self.logger.info("url为:%s" %albumsPraise4FrontURL)
        return albumsPraise4FrontURL



    def send_request_albumsPraise4Front(self,url,praiseType,praisedId):
        '''
        :param url:
        :param praiseType:
        :param praisedId:
        :return:
        '''

        headers = {"Content-Type": "application/json"}
        if praiseType == "专辑":
            parameters = {
                    "praiseType":"1",
                    "praisedId":praisedId
                }
            self.logger.info("请求的参数为:%s" % parameters)
            r = requests.post(url, data=json.dumps(parameters), headers=headers,timeout=30)
            self.logger.info("返回的参数为:%s" % json.loads(r.text))
            return json.loads(r.text)
        elif praiseType == "社区":
            parameters = {
                    "praiseType":"2",
                    "praisedId":praisedId
                }
            self.logger.info("请求的参数为:%s" % parameters)
            r = requests.post(url, data=json.dumps(parameters), headers=headers,timeout=30)
            self.logger.info("返回的参数为:%s" % json.loads(r.text))
            return json.loads(r.text)
        elif praiseType == "系统":
            parameters = {
                    "praiseType":"3",
                    "praisedId":praisedId
                }
            self.logger.info("请求的参数为:%s" % parameters)
            r = requests.post(url, data=json.dumps(parameters), headers=headers,timeout=30)
            self.logger.info("返回的参数为:%s" % json.loads(r.text))
            return json.loads(r.text)
        else:
            self.logger.error("传的参数有误，请检查！")



if __name__ == "__main__":


    imi = albumsPraise4Front()
    # print(imi)
    phone = "13723746965"
    config = FileParser(r'D:\anjouAutoTest\config\config.ini')
    dev_AC_URL = config.get('Authentication', 'dev')

    base = baseUtils()
    clientVersionInfo = config.get("clientVersionInfo", "clientVersionInfo")
    lang = config.get("lang", "en")
    currentTime = base.getTimeStamp()
    AC = Authentication()
    DATA = AC.get_Android_CN_logged_in(phone)
    url = AC.get_AuthenticationURL(dev_AC_URL, lang, currentTime, clientVersionInfo)

    access_token = AC.get_Access_token(url, DATA)

    config2 = FileParser(r'D:\anjouAutoTest\config\api_url.ini')
    base_url = config.get("imi_base_url","base_url_dev")



    albumsPraise4FrontURL = config.get("imi_cms_url","albumsPraise4FrontURL")
    albumsPraise4FrontURL = imi.get_albumsPraise4FrontURL(base_url,albumsPraise4FrontURL,lang,currentTime,clientVersionInfo,access_token)


    # print(queryDiyPicURL)


    praisedId = "91b14a6ab8ed4e91bb0fa698e1d7a7d6"
    praiseType = "专辑"
    # #
    # # # #
    imi.send_request_albumsPraise4Front(albumsPraise4FrontURL,praiseType,praisedId)