#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/6/11 17:02
# @Author  : Durat
# @Email   : durant.zeng@sunvalley.com.cn
# @File    : addCmsUserQuestion.py
# @Software: PyCharm
import sys,os
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
import json
import requests
from common.Logger import Logger


class addCmsUserQuestion:

    def __init__(self):
        self.logger = Logger(logger="addCmsUserQuestion").getlog()

    def get_addCmsShopInfoURL(self,baseURL,URL,lang,timeStamp,clientVersionInfo,access_token):
        '''
        :param baseURL:
        :param lang:
        :param timeStamp:
        :param clientVersionInfo:
        :param access_token:
        :return:增加用户反馈
        '''
        addCmsUserQuestionURL = baseURL + URL + "?lang=%s&timeStamp=%s&clientVersionInfo=%s&access_token=%s" % (lang, timeStamp, clientVersionInfo,access_token)
        self.logger.info("url为:%s" %addCmsUserQuestionURL)
        return addCmsUserQuestionURL



    def send_request_addCmsUserQuestion(self,url,content):
        '''
        :param url:
        :param content:
        :return:
        '''
        headers = {"Content-Type": "application/json"}
        parameters = {
                    "content":content
                }
        self.logger.info("请求的参数为:%s" %parameters)
        r = requests.post(url, data=json.dumps(parameters), headers=headers,timeout=30)
        self.logger.info("返回的参数为:%s" % json.loads(r.text))
        return json.loads(r.text)

if __name__ == "__main__":


    imi = addCmsUserQuestion()
    # # print(imi)
    # phone = "13723746965"
    # config = FileParser(r'D:\anjouAutoTest\config\config.ini')
    # dev_AC_URL = config.get('Authentication', 'dev')
    # print(dev_AC_URL)
    # base = baseUtils()
    # lang = config.get("lang", "zh")
    # clientVersionInfo = config.get("clientVersionInfo", "clientVersionInfo")
    # currentTime = base.getTimeStamp()
    # AC = Authentication()
    # DATA = AC.get_PAD_CN_logged_in(phone)
    # url = AC.get_AuthenticationURL(dev_AC_URL, lang, currentTime, clientVersionInfo)
    #
    # access_token = AC.get_Access_token(url, DATA)
    #
    # base_url = config.get("imi_base_url","base_url_dev")
    #
    #
    #
    # addCmsUserQuestionURL = config.get("imi_cms_url","addCmsUserQuestionURL")
    # addCmsUserQuestionURL = imi.get_addCmsShopInfoURL(base_url,addCmsUserQuestionURL,lang,currentTime,clientVersionInfo,access_token)
    #

    URL = "https://mi-api.nailtutu.com/imi/cmsUserQuestion/addCmsUserQuestion?&access_token=ea631474-203b-4a60-b923-498b766d00eb&timeStamp=20190821180749&clientVersionInfo=android_1.0.0&lang=zh"

    content ="星河行的的多大阿萨"

    imi.send_request_addCmsUserQuestion(URL,content)