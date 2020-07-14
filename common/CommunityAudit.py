#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/7/16 19:27
# @Author  : Durat
# @Email   : durant.zeng@sunvalley.com.cn
# @File    : CommunityAudit.py
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
logger = Logger(logger="CommunityAudit").getlog()



class CommunityAudit:
    def __init__(self):
        pass

    def get_auditDiyPic4Back_URL(self,baseURL,URL,lang,timeStamp,clientVersionInfo,access_token):
        '''
        :param baseURL:
        :param lang:
        :param timeStamp:
        :param clientVersionInfo:
        :param access_token:
        :return:
        '''
        auditDiyPic4BackURL = baseURL + URL + "?lang=%s&timeStamp=%s&clientVersionInfo=%s&access_token=%s" % (lang, timeStamp, clientVersionInfo,access_token)
        logger.info("社区图库-审核的URL为:%s" %auditDiyPic4BackURL)
        return auditDiyPic4BackURL


    def send_request_auditDiyPic4Back(self,url,galleryID,galleryStatus_will):
        '''
        :param url:
        :param tagName:
        :param tagDescribe:
        :param sortNumber:
        :return:社区图库-审核
        '''

        if galleryStatus_will == "审核通过":
            pictureDict = {
                "id": galleryID,
                "galleryStatus": 1
            }
            pictureList = []
            pictureList.append(pictureDict)

            data = {
                "galleryStatus":3,
                "pictureList":pictureList
            }
            headers = {"Content-Type": "application/json"}
            try:
                requests.post(url, data=json.dumps(data), headers=headers)
            except:
                logger.error("社区图库[%s]审核失败！" %galleryID)
            else:
                logger.info("社区图库[%s]审核通过！" %galleryID)
        elif galleryStatus_will == "审核不通过":
            pictureDict = {
                "id": galleryID,
                "galleryStatus": 1
            }
            pictureList = []
            pictureList.append(pictureDict)

            data = {
                "galleryStatus":2,
                "pictureList":pictureList
            }
            headers = {"Content-Type": "application/json"}
            try:
                requests.post(url, data=json.dumps(data), headers=headers)
            except:
                logger.error("社区图库[%s]审核失败！" %galleryID)
            else:
                logger.info("社区图库[%s]审核不通过！" %galleryID)
        elif galleryStatus_will == "下架":
            pictureDict = {
                "id": galleryID,
                "galleryStatus": 3
            }
            pictureList = []
            pictureList.append(pictureDict)

            data = {
                "galleryStatus":4,
                "pictureList":pictureList
            }
            headers = {"Content-Type": "application/json"}
            try:
                requests.post(url, data=json.dumps(data), headers=headers)
            except:
                logger.error("社区图库[%s]下架失败！" %galleryID)
            else:
                logger.info("社区图库[%s]下架成功！" %galleryID)
        elif galleryStatus_will == "删除":
            pictureDict = {
                "id": galleryID,
                "galleryStatus": 4
            }
            pictureList = []
            pictureList.append(pictureDict)

            data = {
                "galleryStatus":5,
                "pictureList":pictureList
            }
            headers = {"Content-Type": "application/json"}
            try:
                requests.post(url, data=json.dumps(data), headers=headers)
            except:
                logger.error("社区图库[%s]删除失败！" %galleryID)
            else:
                logger.info("社区图库[%s]删除成功！" %galleryID)
        else:
            logger.info("传入的参数不对，请检查配置！")


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


    auditDiyPic4BackURL = config.get("imi_oc_url","auditDiyPic4Back")

    userName = "durant.zeng@sunvalley.com.cn"
    password = "123456"
    oc_web_data = AC.get_oc_web(userName,password)



    access_token_oc = AC.get_Access_token(url, oc_web_data)
    print(access_token_oc)

    Community= CommunityAudit()
    galleryID = "220aabb11e89464481bb40624a441eaa"
    galleryStatus_will = "删除"

    auditDiyPic4Back_URL = Community.get_auditDiyPic4Back_URL(base_url_dev,auditDiyPic4BackURL,lang,currentTime,clientVersionInfo,access_token_oc)
    Community.send_request_auditDiyPic4Back(auditDiyPic4Back_URL,galleryID,galleryStatus_will)



