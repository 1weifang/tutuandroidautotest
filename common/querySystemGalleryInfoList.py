#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/7/10 16:06
# @Author  : Durat
# @Email   : durant.zeng@sunvalley.com.cn
# @File    : querySystemGalleryInfoList.py
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
logger = Logger(logger="querySystemGalleryInfoList").getlog()


class querySystemGalleryInfoList:

    def __init__(self):
        pass

    def get_querySystemGalleryInfoListURL(self,baseURL,URL,lang,timeStamp,clientVersionInfo,access_token):
        '''
        :param baseURL:
        :param lang:
        :param timeStamp:
        :param clientVersionInfo:
        :param access_token:
        :return:系统图库-查询列表
        '''
        querySystemGalleryInfoListURL = baseURL + URL + "?lang=%s&timeStamp=%s&clientVersionInfo=%s&access_token=%s" % (lang, timeStamp, clientVersionInfo,access_token)
        logger.info("系统图库-查询列表的URL为:%s" %querySystemGalleryInfoListURL)
        return querySystemGalleryInfoListURL



    def send_request_querySystemGalleryInfoList(self,url,galleryName,galleryStatus,tagId,currentPage,pageSize):
        '''
        :param url:
        :param galleryName:
        :param galleryStatus:
        :param tagId:
        :param currentPage:
        :param pageSize:
        :return:系统图库-查询列表
        '''
        headers = {"Content-Type": "application/json"}
        parameters = {
                    "currentPage": currentPage,
                    "galleryName": galleryName,
                    "galleryStatus": galleryStatus,
                    "pageSize": pageSize,
                    "tagId": tagId
                }
        r = requests.post(url, data=json.dumps(parameters), headers=headers)
        logger.info("返回的数据为:%s" % json.loads(r.text))
        return json.loads(r.text)

if __name__ == "__main__":
    imi = querySystemGalleryInfoList()
    userName = "durant.zeng@sunvalley.com.cn"
    passWord = "123456"
    config = FileParser(r'D:\anjouAutoTest\config\config.ini')
    dev_AC_URL = config.get('Authentication', 'dev')
    print(dev_AC_URL)
    base = baseUtils()
    clientVersionInfo = config.get("clientVersionInfo", "clientVersionInfo_ch_Android")
    lang = config.get("lang", "zh")
    currentTime = base.getTimeStamp()
    AC = Authentication()


    DATA = AC.get_oc_web(userName,passWord)
    url = AC.get_AuthenticationURL_OC(dev_AC_URL, lang, currentTime, clientVersionInfo)

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

