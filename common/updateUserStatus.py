#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/8/21 11:41
# @Author  : Durat
# @Email   : durant.zeng@sunvalley.com.cn
# @File    : updateUserStatus.py
# @Software: PyCharm


import requests
import json
from interface.base.login.authentication import Authentication
from common.FileParsing import FileParser
from common.baseUtil import baseUtils
from common.Logger import Logger

logger = Logger(logger="TagInfo").getlog()



class updateUserStatus:
    def __init__(self):
        pass

    def get_updateUserStatus_URL(self,baseURL,URL,lang,timeStamp,clientVersionInfo,access_token):
        '''
        :param baseURL:
        :param lang:
        :param timeStamp:
        :param clientVersionInfo:
        :param access_token:
        :return:
        '''
        updateUserStatusURL = baseURL + URL + "?lang=%s&timeStamp=%s&clientVersionInfo=%s&access_token=%s" % (lang, timeStamp, clientVersionInfo,access_token)
        logger.info("更新用户状态的URL为:%s" %updateUserStatusURL)
        return updateUserStatusURL


    def send_request_updateUserStatus(self,url,id,userStatus):
        '''
        :param url:
        :param id:
        :param userStatus:
        :return:
        '''
        data = {
            "id":id,
            "userStatus":userStatus
        }
        headers = {"Content-Type": "application/json"}
        try:
            requests.post(url, data=json.dumps(data), headers=headers)
        except:
            logger.error("更新用户状态失败！")
        else:
            logger.info("更新用户[%s]状态成功" % id)


if __name__ == "__main__":
    # phone = "13723746965"
    config = FileParser(r'D:\anjouAutoTest\config\config.ini')
    AC = Authentication()
    base = baseUtils()
    lang = config.get("lang","zh")
    clientVersionInfo = config.get("clientVersionInfo","clientVersionInfo")
    currentTime = base.getTimeStamp()
    base_url_dev = config.get('oc_web_base_url', 'base_url_dev')
    login_url = config.get("imi_login_url", "login_url")
    url = AC.get_AuthenticationURL_OC(base_url_dev, login_url,lang, currentTime, clientVersionInfo)


    addTagInfoURL = config.get("imi_oc_url","addTagInfo")

    userName = "durant.zeng@sunvalley.com.cn"
    password = "123456"


    # userName = "admin@sunvalley.com.cn"
    # password = "danya@123"


    oc_web_data = AC.get_oc_web(userName,password)


    print(oc_web_data)


    access_token_oc = AC.get_Access_token(url, oc_web_data)
    print(access_token_oc)

    tag= TagInfo()
    # tagName = "autoTest4"
    # tagDescribe = "this is a test"
    # sortNumber = 10
    # #
    #
    # addTagInfo_url = tag.get_addTagInfo_URL(base_url_dev,addTagInfoURL,lang,currentTime,clientVersionInfo,access_token_oc)
    # print(addTagInfo_url)
    #
    # tag.send_request_addTagInfo(addTagInfo_url,tagName,tagDescribe,sortNumber)