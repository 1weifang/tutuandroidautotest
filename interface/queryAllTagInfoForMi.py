#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/6/10 18:02
# @Author  : Durat
# @Email   : durant.zeng@sunvalley.com.cn
# @File    : queryAllTagInfoForMi.py
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
logger = Logger(logger="queryAllTagInfoForMi").getlog()


class queryAllTagInfoForMi:

    def __init__(self):
        pass

    def get_queryAllTagInfoForMiURL(self,baseURL,URL,lang,timeStamp,clientVersionInfo,access_token):
        '''
        :param baseURL:
        :param lang:
        :param timeStamp:
        :param clientVersionInfo:
        :param access_token:
        :return:彩绘图库-常用标签与标签
        '''
        queryAllTagInfoForMiURL = baseURL + URL + "?lang=%s&timeStamp=%s&clientVersionInfo=%s&access_token=%s" % (lang, timeStamp, clientVersionInfo,access_token)
        logger.info("彩绘图库-常用标签与标签的URL为:%s" %queryAllTagInfoForMiURL)
        return queryAllTagInfoForMiURL



    def send_request_queryAllTagInfoForMi(self,url,status):
        '''
        :param url:
        :param status:
        :return:
        '''
        headers = {"Content-Type": "application/json"}
        if status == "前8条":
            parameters = {
                "status":"1"
            }
            r = requests.post(url, data=json.dumps(parameters), headers=headers)
            logger.info("返回的数据为:%s" % json.loads(r.text))
            return json.loads(r.text)
        elif status == "全部":
            parameters = {
                "status":"2"
            }
            r = requests.post(url, data=json.dumps(parameters), headers=headers)
            logger.info("返回的数据为:%s" % json.loads(r.text))
            return json.loads(r.text)
        else:
            logger.error("传的参数有误，请检查！")



if __name__ == "__main__":


    imi = queryAllTagInfoForMi()
    print(imi)
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



    queryAllTagInfoForMiURL = config2.get("imi_cms_url","queryAllTagInfoForMiURL")
    queryAllTagInfoForMiURL = imi.get_queryAllTagInfoForMiURL(base_url,queryAllTagInfoForMiURL,lang,currentTime,clientVersionInfo,access_token)
    print(queryAllTagInfoForMiURL)

    status = "全部"

    # #
    imi.send_request_queryAllTagInfoForMi(queryAllTagInfoForMiURL,status)