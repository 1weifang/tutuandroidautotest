#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/6/10 19:49
# @Author  : Durat
# @Email   : durant.zeng@sunvalley.com.cn
# @File    : getAlbumsList4Front.py
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



class getAlbumsList4Front:

    def __init__(self):
        self.logger = Logger(logger="getAlbumsList4Front").getlog()

    def get_getAlbumsList4FrontURL(self,baseURL,URL,lang,timeStamp,clientVersionInfo,access_token):
        '''
        :param baseURL:
        :param lang:
        :param timeStamp:
        :param clientVersionInfo:
        :param access_token:
        :return:特辑-列表查询
        '''
        getAlbumsList4FrontURL = baseURL + URL + "?lang=%s&timeStamp=%s&clientVersionInfo=%s&access_token=%s" % (lang, timeStamp, clientVersionInfo,access_token)
        self.logger.info("url为:%s" %getAlbumsList4FrontURL)
        return getAlbumsList4FrontURL


    @retry(stop_max_attempt_number=5, wait_random_min=1000, wait_random_max=2000, retry_on_result=_result)
    def send_request_getAlbumsList4Front(self,url,currentPage,pageSize,albumsTagId=None):
        '''
        :param url:
        :param currentPage:
        :param pageSize:
        :return:
        '''
        headers = {"Content-Type": "application/json"}
        allNailSuitFlag = False
        parameters = {
                "allNailSuitFlag":allNailSuitFlag,
                "pageSize":pageSize,
                "currentPage":currentPage,
                "albumsTagId":albumsTagId
            }
        self.logger.info("请求的参数为:%s" %parameters)
        r = requests.post(url, data=json.dumps(parameters), headers=headers,timeout=30)
        self.logger.info("返回的参数为:%s" % json.loads(r.text))
        return json.loads(r.text)



if __name__ == "__main__":


    imi = getAlbumsList4Front()
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



    getAlbumsList4FrontURL = config2.get("imi_cms_url","getAlbumsList4FrontURL")
    getAlbumsList4FrontURL = imi.get_getAlbumsList4FrontURL(base_url,getAlbumsList4FrontURL,lang,currentTime,clientVersionInfo,access_token)
    # print(queryDiyPicURL)


    currentPage = "1"
    pageSize = "10"
    #
    # # #
    imi.send_request_getAlbumsList4Front(getAlbumsList4FrontURL,currentPage,pageSize)

