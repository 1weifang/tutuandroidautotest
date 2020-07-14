#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/6/10 18:40
# @Author  : Durat
# @Email   : durant.zeng@sunvalley.com.cn
# @File    : queryDiyPic.py
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
logger = Logger(logger="queryDiyPic").getlog()


class queryDiyPic:

    def __init__(self):
        pass

    def get_queryDiyPicURL(self,baseURL,URL,lang,timeStamp,clientVersionInfo,access_token):
        '''
        :param baseURL:
        :param lang:
        :param timeStamp:
        :param clientVersionInfo:
        :param access_token:
        :return:我的上传
        '''
        queryDiyPicURL = baseURL + URL + "?lang=%s&timeStamp=%s&clientVersionInfo=%s&access_token=%s" % (lang, timeStamp, clientVersionInfo,access_token)
        logger.info("我的上传的URL为:%s" %queryDiyPicURL)
        return queryDiyPicURL



    def send_request_queryDiyPic(self,url,currentPage,pageSize,galleryStatus):
        '''
        :param url:
        :param status:
        :return:
        '''
        headers = {"Content-Type": "application/json"}
        if galleryStatus == "待审核":
            parameters = {
                "galleryStatus":"1",
                "pageSize":pageSize,
                "currentPage":currentPage
            }
            r = requests.post(url, data=json.dumps(parameters), headers=headers)
            logger.info("返回的数据为:%s" % json.loads(r.text))
            return json.loads(r.text)
        elif galleryStatus == "审核不通过":
            parameters = {
                "galleryStatus":"2",
                "pageSize":pageSize,
                "currentPage":currentPage
            }
            r = requests.post(url, data=json.dumps(parameters), headers=headers)
            logger.info("返回的数据为:%s" % json.loads(r.text))
            return json.loads(r.text)
        elif galleryStatus == "审核通过":
            parameters = {
                "galleryStatus":"3",
                "pageSize":pageSize,
                "currentPage":currentPage
            }
            r = requests.post(url, data=json.dumps(parameters), headers=headers)
            logger.info("返回的数据为:%s" % json.loads(r.text))
            return json.loads(r.text)
        elif galleryStatus == "下架":
            parameters = {
                "galleryStatus":"4",
                "pageSize":pageSize,
                "currentPage":currentPage
            }
            r = requests.post(url, data=json.dumps(parameters), headers=headers)
            logger.info("返回的数据为:%s" % json.loads(r.text))
            return json.loads(r.text)
        elif galleryStatus == "删除":
            parameters = {
                "galleryStatus":"5",
                "pageSize":pageSize,
                "currentPage":currentPage
            }
            r = requests.post(url, data=json.dumps(parameters), headers=headers)
            logger.info("返回的数据为:%s" % json.loads(r.text))
            return json.loads(r.text)
        elif galleryStatus == "发布":
            parameters = {
                "galleryStatus":"6",
                "pageSize":pageSize,
                "currentPage":currentPage
            }
            r = requests.post(url, data=json.dumps(parameters), headers=headers)
            logger.info("返回的数据为:%s" % json.loads(r.text))
            return json.loads(r.text)
        elif galleryStatus == "全部":
            parameters = {
                "galleryStatus":"null",
                "pageSize":pageSize,
                "currentPage":currentPage
            }
            r = requests.post(url, data=json.dumps(parameters), headers=headers)
            logger.info("返回的数据为:%s" % json.loads(r.text))
            return json.loads(r.text)
        else:
            logger.error("传的参数有误，请检查！")




if __name__ == "__main__":


    imi = queryDiyPic()
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



    queryDiyPicURL = config2.get("imi_cms_url","queryDiyPicURL")
    queryDiyPicURL = imi.get_queryDiyPicURL(base_url,queryDiyPicURL,lang,currentTime,clientVersionInfo,access_token)
    # print(queryDiyPicURL)

    galleryStatus = "审核通过"
    currentPage = "1"
    pageSize = "10"

    # #
    imi.send_request_queryDiyPic(queryDiyPicURL,currentPage,pageSize,galleryStatus)