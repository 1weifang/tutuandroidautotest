#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/6/10 11:23
# @Author  : Durat
# @Email   : durant.zeng@sunvalley.com.cn
# @File    : addDiyPic.py
# @Software: PyCharm
import sys,os
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
import json
import requests
from common.FileParsing import FileParser
from common.baseUtil import baseUtils
from interface.base.login.authentication import Authentication
from interface.tutu.gallery.single import single
from common.Logger import Logger
from retrying import retry

def _result(result):
    return result is None



class addDiyPic:

    def __init__(self):
        self.logger = Logger(logger="addDiyPic").getlog()

    def get_AddDiyPicURL(self,baseURL,URL,lang,timeStamp,clientVersionInfo,access_token):
        '''
        :param baseURL:
        :param URL:
        :param lang:
        :param timeStamp:
        :param clientVersionInfo:
        :param access_token:
        :return:
        '''
        AddDiyPicURL = baseURL + URL + "?lang=%s&timeStamp=%s&clientVersionInfo=%s&access_token=%s" % (lang, timeStamp, clientVersionInfo,access_token)
        self.logger.info("url为:%s" %AddDiyPicURL)
        return AddDiyPicURL



    @retry(stop_max_attempt_number=5, wait_random_min=1000, wait_random_max=2000, retry_on_result=_result)
    def send_request_addDiyPic(self,url,galleryName,galleryUrl,galleryThumbnailUrl,collectionType):
        '''
        :param galleryName:
        :param galleryUrl:
        :param galleryThumbnailUrl:
        :param collectionType:
        :return:
        '''
        headers = {"Content-Type": "application/json"}
        if collectionType == "社区图库":
            parameters = {
                "galleryName":galleryName,
                "galleryUrl":galleryUrl,
                "galleryThumbnailUrl":galleryThumbnailUrl,
                "collectionType":"2"
            }
            self.logger.info("请求的参数为:%s" %parameters)
            r = requests.post(url, data=json.dumps(parameters), headers=headers,timeout=30)
            self.logger.info("返回的参数为:%s" % json.loads(r.text))
            return json.loads(r.text)
        elif collectionType == "DIY图库并收藏":
            parameters = {
                "galleryName":galleryName,
                "galleryUrl":galleryUrl,
                "galleryThumbnailUrl":galleryThumbnailUrl,
                "collectionType":"3"}
            self.logger.info("请求的参数为:%s" %parameters)
            r = requests.post(url, data=json.dumps(parameters), headers=headers,timeout=30)
            self.logger.info("返回的参数为:%s" % json.loads(r.text))
            return json.loads(r.text)

if __name__ == "__main__":
    imi = addDiyPic()
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
    PictureUploadURL = config.get("PictureUploadURL","PictureUploadURL")
    pu = single()
    PictureUploadURL = pu.get_singleURL(base_url,PictureUploadURL,lang,currentTime,clientVersionInfo,access_token)

    targetid = "社区"
    filename = r"1.jpg"
    filepath = r"D:\testPicture\1.jpg"
    #
    picture = pu.send_request_single(PictureUploadURL,targetid,filename,filepath)
    AddDiyPicURL = config.get("imi_cms_url","AddDiyPicURL")
    AddDiyPicURL = imi.get_AddDiyPicURL(base_url,AddDiyPicURL,lang,currentTime,clientVersionInfo,access_token)
    collectionType = "社区图库"
    re = imi.send_request_addDiyPic(AddDiyPicURL,picture,collectionType)
    print(type(re))

