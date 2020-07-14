#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/6/10 20:31
# @Author  : Durat
# @Email   : durant.zeng@sunvalley.com.cn
# @File    : albumsShare4Front.py
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



class albumsShare4Front:

    def __init__(self):
        self.logger = Logger(logger="albumsShare4Front").getlog()

    def get_albumsShare4FrontURL(self,baseURL,URL,lang,timeStamp,clientVersionInfo,access_token):
        '''
        :param baseURL:
        :param lang:
        :param timeStamp:
        :param clientVersionInfo:
        :param access_token:
        :return:特辑-专辑分享
        '''
        albumsShare4FrontURL = baseURL + URL + "?lang=%s&timeStamp=%s&clientVersionInfo=%s&access_token=%s" % (lang, timeStamp, clientVersionInfo,access_token)
        self.logger.info("url为:%s" %albumsShare4FrontURL)
        return albumsShare4FrontURL



    @retry(stop_max_attempt_number=5, wait_random_min=1000, wait_random_max=2000, retry_on_result=_result)
    def send_request_albumsShare4Front(self,url,shareType,shareWay,sharedId):
        '''
        :param url:
        :param shareType:
        :param shareWay:
        :param sharedId:
        :return:
        '''

        headers = {"Content-Type": "application/json"}
        if shareType == "专辑" and shareWay == "微信":
            parameters = {
                    "shareType":"1",
                    "shareWay":"1",
                    "sharedId":sharedId
                }
            self.logger.info("请求的参数为:%s" %parameters)
            r = requests.post(url, data=json.dumps(parameters), headers=headers,timeout=30)
            self.logger.info("返回的参数为:%s" % json.loads(r.text))
            return json.loads(r.text)
        elif shareType == "专辑" and shareWay == "微信朋友圈":
            parameters = {
                    "shareType":"1",
                    "shareWay":"0",
                    "sharedId":sharedId
                }
            self.logger.info("请求的参数为:%s" %parameters)
            r = requests.post(url, data=json.dumps(parameters), headers=headers,timeout=30)
            self.logger.info("返回的参数为:%s" % json.loads(r.text))
            return json.loads(r.text)
        elif shareType == "专辑" and shareWay == "微博":
            parameters = {
                    "shareType":"1",
                    "shareWay":"2",
                    "sharedId":sharedId
                }
            self.logger.info("请求的参数为:%s" %parameters)
            r = requests.post(url, data=json.dumps(parameters), headers=headers,timeout=30)
            self.logger.info("返回的参数为:%s" % json.loads(r.text))
            return json.loads(r.text)

        elif shareType == "专辑" and shareWay == "QQ":
            parameters = {
                    "shareType":"1",
                    "shareWay":"3",
                    "sharedId":sharedId
                }
            self.logger.info("请求的参数为:%s" %parameters)
            r = requests.post(url, data=json.dumps(parameters), headers=headers,timeout=30)
            self.logger.info("返回的参数为:%s" % json.loads(r.text))
            return json.loads(r.text)
        elif shareType == "社区" and shareWay == "微信":
            parameters = {
                    "shareType":"2",
                    "shareWay":"1",
                    "sharedId":sharedId
                }
            self.logger.info("请求的参数为:%s" %parameters)
            r = requests.post(url, data=json.dumps(parameters), headers=headers,timeout=30)
            self.logger.info("返回的参数为:%s" % json.loads(r.text))
            return json.loads(r.text)
        elif shareType == "社区" and shareWay == "微博":
            parameters = {
                    "shareType":"2",
                    "shareWay":"2",
                    "sharedId":sharedId
                }
            self.logger.info("请求的参数为:%s" %parameters)
            r = requests.post(url, data=json.dumps(parameters), headers=headers,timeout=30)
            self.logger.info("返回的参数为:%s" % json.loads(r.text))
            return json.loads(r.text)
        elif shareType == "社区" and shareWay == "QQ":
            parameters = {
                    "shareType":"2",
                    "shareWay":"3",
                    "sharedId":sharedId
                }
            self.logger.info("请求的参数为:%s" %parameters)
            r = requests.post(url, data=json.dumps(parameters), headers=headers,timeout=30)
            self.logger.info("返回的参数为:%s" % json.loads(r.text))
            return json.loads(r.text)
        elif shareType == "系统" and shareWay == "微信":
            parameters = {
                    "shareType":"3",
                    "shareWay":"1",
                    "sharedId":sharedId
                }
            self.logger.info("请求的参数为:%s" %parameters)
            r = requests.post(url, data=json.dumps(parameters), headers=headers,timeout=30)
            self.logger.info("返回的参数为:%s" % json.loads(r.text))
            return json.loads(r.text)
        elif shareType == "系统" and shareWay == "微博":
            parameters = {
                    "shareType":"3",
                    "shareWay":"2",
                    "sharedId":sharedId
                }
            self.logger.info("请求的参数为:%s" %parameters)
            r = requests.post(url, data=json.dumps(parameters), headers=headers,timeout=30)
            self.logger.info("返回的参数为:%s" % json.loads(r.text))
            return json.loads(r.text)
        elif shareType == "系统" and shareWay == "QQ":
            parameters = {
                    "shareType":"3",
                    "shareWay":"3",
                    "sharedId":sharedId
                }
            self.logger.info("请求的参数为:%s" %parameters)
            r = requests.post(url, data=json.dumps(parameters), headers=headers,timeout=30)
            self.logger.info("返回的参数为:%s" % json.loads(r.text))
            return json.loads(r.text)
        else:
            self.logger.error("传的参数有误，请检查！")



if __name__ == "__main__":


    imi = albumsShare4Front()
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



    albumsShare4FrontURL = config2.get("imi_cms_url","albumsShare4FrontURL")
    albumsShare4FrontURL = imi.get_albumsShare4FrontURL(base_url,albumsShare4FrontURL,lang,currentTime,clientVersionInfo,access_token)


    # print(queryDiyPicURL)


    sharedId = "0055358489bb44e8b40b41706fd0b6d6"
    shareType = "专辑"
    shareWay = "微信"
    # #
    # # # #
    imi.send_request_albumsShare4Front(albumsShare4FrontURL,shareType,shareWay,sharedId)


