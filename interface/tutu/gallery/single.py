#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/6/12 14:53
# @Author  : Durat
# @Email   : durant.zeng@sunvalley.com.cn
# @File    : single.py
# @Software: PyCharm
import sys,os
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
import requests
import json
from interface.base.login.authentication import Authentication
from common.FileParsing import FileParser
from common.baseUtil import baseUtils
from common.Logger import Logger




class single:
    def __init__(self):
        self.logger = Logger(logger="single").getlog()

    def get_singleURL(self, baseurl,url, lang, timeStamp, clientVersionInfo,access_token):
        '''
        :param url:
        :param lang:
        :param timeStamp:
        :param clientVersionInfo:
        :return:
        '''
        singleURL = baseurl+ url + "?lang=%s&timeStamp=%s&clientVersionInfo=%s&access_token=%s" % (lang, timeStamp, clientVersionInfo,access_token)
        self.logger.info("url为:%s" %singleURL)
        return singleURL


    def send_request_single(self,url,targetid,filename,filepath):
        '''
        :param url:
        :param targetid:
        :param filename:
        :param filepath:
        :return:
        '''
        proportion = False
        files = {"file":(filename,open(filepath,"rb"),"multipart/form-data",{})}
        if targetid == "社区":
            data = {"targetid":"48d1cd1ef8d846d98897cf68f12dba01",
                "sizes":"240x360",
                "proportion":proportion}
        elif targetid == "头像":
            data = {"targetid":"329ad03f9c6c4db59caffbbe3b02e1e6",
                "sizes":"240x360",
                "proportion":proportion}
        elif targetid =="甲面":
            data = {"targetid":"6e9800a33d364c298a9e515ac3a2a9bc",
                "sizes":"240x360",
                "proportion":proportion}
        elif targetid == "DIY":
            data = {"targetid":"cb8b8835e5f84249958f01d1b2f47b07",
                "sizes":"240x360",
                "proportion":proportion}
        elif targetid == "系统":
            data = {"targetid":"4305685b17aa11e9b53f005056ad4128",
                "sizes":"240x360",
                "proportion":proportion}
        else:
            self.logger.error("targetid不存在，请检查配置！")
        self.logger.info("请求的参数为:%s" % data)
        r = requests.request("post",url,data = data,files=files,timeout=30)
        re = r.text
        josnre = json.loads(re)
        self.logger.info("返回的参数为:%s" % json.loads(r.text))
        pictureDict= {
                    "galleryName" :josnre["data"]["pictureName"],
                    "galleryThumbnailUrl" :josnre["data"]["thumbnailPictureUrl"],
                    "galleryUrl" :josnre["data"]["pictureUrl"]
                }
        return pictureDict



if __name__ == "__main__":
    imi = single()
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
    singleURL = config.get("imi_cms_url","singleURL")

    singleURL = imi.get_singleURL(base_url,singleURL,lang,currentTime,clientVersionInfo,access_token)

    targetid = "社区"
    filename = "Community.jpg"
    filepath = r"D:\testPicture\Community\Community.jpg"


    #
    imi.send_request_single(singleURL,targetid,filename,filepath)








