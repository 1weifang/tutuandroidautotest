#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/6/10 16:40
# @Author  : Durat
# @Email   : durant.zeng@sunvalley.com.cn
# @File    : getPicList4MiByidOrTag.py
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





class getPicList4MiByidOrTag:

    def __init__(self):
        self.logger = Logger(logger="getPicList4MiByidOrTag").getlog()

    def get_getPicList4MiByidOrTagURL(self,baseURL,URL,lang,timeStamp,clientVersionInfo,access_token):
        '''
        :param baseURL:
        :param lang:
        :param timeStamp:
        :param clientVersionInfo:
        :param access_token:
        :return:彩绘图库搜索
        '''
        getPicList4MiByidOrTagURL = baseURL + URL + "?lang=%s&timeStamp=%s&clientVersionInfo=%s&access_token=%s" % (lang, timeStamp, clientVersionInfo,access_token)
        self.logger.info("url为:%s" %getPicList4MiByidOrTagURL)
        return getPicList4MiByidOrTagURL



    @retry(stop_max_attempt_number=5, wait_random_min=1000, wait_random_max=2000, retry_on_result=_result)
    def send_request_getPicList4MiByidOrTag(self,url,currentPage,pageSize,name=None):
        '''

        :param name:
        :param url:
        :param currentPage:
        :param pageSize:
        :return:
        '''
        headers = {"Content-Type": "application/json"}
        parameters = {
                "currentPage":currentPage,
                "pageSize":pageSize,
                "name": name
        }
        self.logger.info("请求的参数为:%s" %parameters)
        r = requests.post(url, data=json.dumps(parameters), headers=headers,timeout=30)
        self.logger.info("返回的参数为:%s" % json.loads(r.text))
        return json.loads(r.text)




if __name__ == "__main__":


    imi = getPicList4MiByidOrTag()
    print(imi)
    phone = "13723746965"
    config = FileParser(r'D:\anjouAutoTest\config\config.ini')
    dev_AC_URL = config.get('Authentication', 'dev')
    base = baseUtils()
    clientVersionInfo = config.get("clientVersionInfo", "clientVersionInfo")
    lang = config.get("lang", "zh")
    currentTime = base.getTimeStamp()
    AC = Authentication()
    DATA = AC.get_Android_CN_logged_in(phone)
    url = AC.get_AuthenticationURL(dev_AC_URL, lang, currentTime, clientVersionInfo)

    access_token = AC.get_Access_token(url, DATA)

    base_url = config.get("imi_base_url","base_url_dev")



    getPicList4MiByidOrTagURL = config.get("imi_cms_url","getPicList4MiByidOrTagURL")
    getPicList4MiByidOrTagURL = imi.get_getPicList4MiByidOrTagURL(base_url,getPicList4MiByidOrTagURL,lang,currentTime,clientVersionInfo,access_token)
    # print(getPicList4MiByidOrTagURL)

    name = "00000950"
    currentPage = 1
    pageSize = 10

    imi.send_request_getPicList4MiByidOrTag(getPicList4MiByidOrTagURL,name,currentPage,pageSize)





