#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/6/10 17:06
# @Author  : Durat
# @Email   : durant.zeng@sunvalley.com.cn
# @File    : getPicList4UserUpLoadMi.py
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



class getPicList4UserUpLoadMi:

    def __init__(self):
        self.logger = Logger(logger="getPicList4UserUpLoadMi").getlog()

    def get_getPicList4UserUpLoadMiURL(self,baseURL,URL,lang,timeStamp,clientVersionInfo,access_token):
        '''
        :param baseURL:
        :param lang:
        :param timeStamp:
        :param clientVersionInfo:
        :param access_token:
        :return:用户上传
        '''
        getPicList4UserUpLoadMiURL = baseURL + URL + "?lang=%s&timeStamp=%s&clientVersionInfo=%s&access_token=%s" % (lang, timeStamp, clientVersionInfo,access_token)
        self.logger.info("url为:%s" %getPicList4UserUpLoadMiURL)
        return getPicList4UserUpLoadMiURL


    def send_request_getPicList4UserUpLoadMi(self,url,allNailSuitFlag,currentPage,pageSize):
        '''
        :param url:
        :param currentPage:
        :param pageSize:
        :return:
        '''
        headers = {"Content-Type": "application/json"}
        parameters = {
                "allNailSuitFlag":allNailSuitFlag,
                "currentPage":currentPage,
                "pageSize":pageSize
        }
        self.logger.info("请求的参数为:%s" %parameters)
        r = requests.post(url, data=json.dumps(parameters), headers=headers,timeout=30)
        self.logger.info("返回的参数为:%s" % json.loads(r.text))
        return json.loads(r.text)




if __name__ == "__main__":


    imi = getPicList4UserUpLoadMi()
    print(imi)
    phone = "13417335080"
    password = "123456"
    config = FileParser(r'D:\anjouAutoTest\config\config.ini')
    dev_AC_URL = config.get('Authentication', 'prod')
    base = baseUtils()
    clientVersionInfo = config.get("clientVersionInfo", "clientVersionInfo")
    lang = config.get("lang", "zh")
    currentTime = base.getTimeStamp()
    AC = Authentication()
    DATA = AC.get_Android_CN_logged_in(phone,password)
    url = AC.get_AuthenticationURL(dev_AC_URL, lang, currentTime, clientVersionInfo)
    access_token = AC.get_Access_token(url, DATA)
    base_url = config.get("imi_base_url","base_url_prod")

    getPicList4UserUpLoadMiURL = config.get("imi_cms_url","getPicList4UserUpLoadMiURL")
    getPicList4UserUpLoadMiURL = imi.get_getPicList4UserUpLoadMiURL(base_url,getPicList4UserUpLoadMiURL,lang,currentTime,clientVersionInfo,access_token)
    currentPage = "1"
    pageSize = "1"
    re = imi.send_request_getPicList4UserUpLoadMi(getPicList4UserUpLoadMiURL,currentPage,pageSize)
    print(re["data"][0]["id"])
