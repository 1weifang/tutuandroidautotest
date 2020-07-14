#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/6/11 16:29
# @Author  : Durat
# @Email   : durant.zeng@sunvalley.com.cn
# @File    : queryCmsShopInfoBySN.py
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



class queryCmsShopInfoBySN:

    def __init__(self):
        self.logger = Logger(logger="queryCmsShopInfoBySN").getlog()

    def get_queryCmsShopInfoListURL(self,baseURL,URL,lang,timeStamp,clientVersionInfo,access_token):
        '''
        :param baseURL:
        :param lang:
        :param timeStamp:
        :param clientVersionInfo:
        :param access_token:
        :return:查询当前用户店铺信息
        '''
        queryCmsShopInfoBySNURL = baseURL + URL + "?lang=%s&timeStamp=%s&clientVersionInfo=%s&access_token=%s" % (lang, timeStamp, clientVersionInfo,access_token)
        self.logger.info("url为:%s" %queryCmsShopInfoBySNURL)
        return queryCmsShopInfoBySNURL



    def send_request_queryCmsShopInfoBySN(self,url,sn):
        '''
        :param url:
        :param sn:
        :return:
        '''
        headers = {"Content-Type": "application/json"}
        parameters = {
                    "sn":sn
                }
        self.logger.info("请求的参数为:%s" % parameters)
        r = requests.post(url, data=json.dumps(parameters), headers=headers,timeout=30)
        self.logger.info("返回的参数为:%s" % json.loads(r.text))
        return json.loads(r.text)

if __name__ == "__main__":


    imi = queryCmsShopInfoBySN()
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
    DATA = AC.get_PAD_CN_logged_in(phone)
    url = AC.get_AuthenticationURL(dev_AC_URL, lang, currentTime, clientVersionInfo)

    access_token = AC.get_Access_token(url, DATA)

    config2 = FileParser(r'D:\anjouAutoTest\config\api_url.ini')
    base_url = config2.get("base_url","base_url_dev")



    queryCmsShopInfoBySNURL = config2.get("imi_cms_url","queryCmsShopInfoBySNURL")
    queryCmsShopInfoBySNURL = imi.get_queryCmsShopInfoListURL(base_url,queryCmsShopInfoBySNURL,lang,currentTime,clientVersionInfo,access_token)


    # lat = "114.057737"
    # lnt = "22.604453"
    # distance = 100
    # shopName = "星星美甲店"
    # pageSize = "10"
    sn = "e4937a14f91c05a3"

    imi.send_request_queryCmsShopInfoBySN(queryCmsShopInfoBySNURL,sn)