#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/6/10 14:25
# @Author  : Durat
# @Email   : durant.zeng@sunvalley.com.cn
# @File    : getPicDetailForMi.py
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




class getPicDetailForMi:

    def __init__(self):
        self.logger = Logger(logger="getPicDetailForMi").getlog()

    def get_getPicDetailForMiURL(self,baseURL,URL,lang,timeStamp,clientVersionInfo,access_token):
        '''
        :param baseURL:
        :param lang:
        :param timeStamp:
        :param clientVersionInfo:
        :param access_token:
        :return:取单张图详情
        '''
        getPicDetailForMiURL = baseURL + URL + "?lang=%s&timeStamp=%s&clientVersionInfo=%s&access_token=%s" % (lang, timeStamp, clientVersionInfo,access_token)
        self.logger.info("url为:%s" %getPicDetailForMiURL)
        return getPicDetailForMiURL



    @retry(stop_max_attempt_number=5, wait_random_min=1000, wait_random_max=2000, retry_on_result=_result)
    def send_request_getPicDetailForMi(self,url,id,collectionType):
        '''
        :param galleryName:
        :param galleryUrl:
        :param galleryThumbnailUrl:
        :param collectionType:
        :return:
        '''
        headers = {"Content-Type": "application/json"}
        if collectionType == "系统图库":
            parameters = {
                "id":id,
                "collectionType":"1"
            }
            self.logger.info("请求的参数为:%s" %parameters)
            r = requests.post(url, data=json.dumps(parameters), headers=headers,timeout=30)
            self.logger.info("返回的参数为:%s" % json.loads(r.text))
            return json.loads(r.text)

        elif collectionType == "社区图库":
            parameters = {
                "id":id,
                "collectionType":"2"
            }
            self.logger.info("请求的参数为:%s" %parameters)
            r = requests.post(url, data=json.dumps(parameters), headers=headers,timeout=30)
            self.logger.info("返回的参数为:%s" % json.loads(r.text))
            return json.loads(r.text)

        elif collectionType == "DIY图库":
            parameters = {
                "id":id,
                "collectionType":"3"
            }
            self.logger.info("请求的参数为:%s" %parameters)
            r = requests.post(url, data=json.dumps(parameters), headers=headers,timeout=30)
            self.logger.info("返回的参数为:%s" % json.loads(r.text))

        elif collectionType == "专辑图库":
            parameters = {
                "id":id,
                "collectionType":"4"
            }
            self.logger.info("请求的参数为:%s" %parameters)
            r = requests.post(url, data=json.dumps(parameters), headers=headers,timeout=30)
            self.logger.info("返回的参数为:%s" % json.loads(r.text))
        else:
            self.logger.error("collectionType不存在,请检查！")



if __name__ == "__main__":


    imi = getPicDetailForMi()
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



    getPicDetailForMiURL = config.get("imi_cms_url","getPicDetailForMiURL")
    getPicDetailForMiURL = imi.get_getPicDetailForMiURL(base_url,getPicDetailForMiURL,lang,currentTime,clientVersionInfo,access_token)
    print(getPicDetailForMiURL)

    id = "1302e3f89d594d67a2a5fab34aa6fdf7"
    collectionType = "专辑图库"
    imi.send_request_getPicDetailForMi(getPicDetailForMiURL,id,collectionType)


    # collectionType = "社区图库"
    # imi.send_request_addDiyPic(AddDiyPicURL,picture,collectionType)

