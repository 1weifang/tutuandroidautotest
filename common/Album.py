#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/7/16 16:21
# @Author  : Durat
# @Email   : durant.zeng@sunvalley.com.cn
# @File    : Album.py
# @Software: PyCharm


import sys,os
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
import requests
import json
import time
from interface.base.login.authentication import Authentication
from common.FileParsing import FileParser
from common.baseUtil import baseUtils
from common.Logger import Logger

logger = Logger(logger="AlbumInfo").getlog()



class AlbumInfo:
    def __init__(self):
        pass

    def get_addAlbumsInfo_URL(self,baseURL,URL,lang,timeStamp,clientVersionInfo,access_token):
        '''
        :param baseURL:
        :param lang:
        :param timeStamp:
        :param clientVersionInfo:
        :param access_token:
        :return:
        '''
        addAlbumsInfoURL = baseURL + URL + "?lang=%s&timeStamp=%s&clientVersionInfo=%s&access_token=%s" % (lang, timeStamp, clientVersionInfo,access_token)
        logger.info("添加特辑的URL为:%s" %addAlbumsInfoURL)
        return addAlbumsInfoURL


    def send_request_addTagInfo(self,url,tagName,tagDescribe,sortNumber):
        '''
        :param url:
        :param tagName:
        :param tagDescribe:
        :param sortNumber:
        :return:创建标签
        '''
        data = {
            "tagName":tagName,
            "tagDescribe":tagDescribe,
            "sortNumber":sortNumber
        }
        headers = {"Content-Type": "application/json"}
        try:
            requests.post(url, data=json.dumps(data), headers=headers)
        except:
            logger.error("创建标签失败！")
        else:
            logger.info("创建标签[%s]成功" % tagName)


    def get_tagSystemPic4Back_URL(self,baseURL,URL,lang,timeStamp,clientVersionInfo,access_token):
        '''
        :param baseURL:
        :param lang:
        :param timeStamp:
        :param clientVersionInfo:
        :param access_token:
        :return:
        '''
        tagSystemPic4BackURL = baseURL + URL + "?lang=%s&timeStamp=%s&clientVersionInfo=%s&access_token=%s" % (lang, timeStamp, clientVersionInfo,access_token)
        logger.info("系统图库关联标签的URL为:%s" %tagSystemPic4BackURL)
        return tagSystemPic4BackURL


    def send_request_tagSystemPic4Back(self,url,galleryId,tagId):
        '''
        :param url:
        :param tagName:
        :param tagDescribe:
        :param sortNumber:
        :return:系统图库关联标签
        '''
        #默认为0，不提醒
        tagIdsList = []
        tagIdsList.append(tagId)
        data = {
            "galleryId": galleryId,
            "isReleaseRemind": 0,
            "tagIds":tagIdsList
        }
        headers = {"Content-Type": "application/json"}
        try:
            requests.post(url, data=json.dumps(data), headers=headers)
        except:
            logger.error("系统图库关联标签失败！")
        else:
            logger.info("系统图库[%s]关联标签[%s]成功" % (galleryId,tagId))


    def get_deleteGalleryTagRel_URL(self,baseURL,URL,lang,timeStamp,clientVersionInfo,access_token):
        '''
        :param baseURL:
        :param lang:
        :param timeStamp:
        :param clientVersionInfo:
        :param access_token:
        :return:
        '''
        deleteGalleryTagRelURL = baseURL + URL + "?lang=%s&timeStamp=%s&clientVersionInfo=%s&access_token=%s" % (lang, timeStamp, clientVersionInfo,access_token)
        logger.info("删除标签关联的系统图库的URL为:%s" %deleteGalleryTagRelURL)
        return deleteGalleryTagRelURL


    def send_request_deleteGalleryTagRel(self,url,tagId,galleryId):
        '''
        :param url:
        :param tagId:
        :return:
        '''
        galleryIdsList = []
        galleryIdsList.append(galleryId)
        data = {
            "tagId": tagId,
            "galleryIds": galleryIdsList
        }
        logger.info(data)
        headers = {"Content-Type": "application/json"}
        try:
            requests.post(url, data=json.dumps(data), headers=headers)
        except:
            logger.error("删除标签关联的系统图库失败！")
        else:
            logger.info("删除标签ID[%s]关联的系统图库ID[%s]成功" % (tagId,galleryId))



    def get_delTagOC_URL(self,baseURL,URL,lang,timeStamp,clientVersionInfo,access_token):
        '''
        :param baseURL:
        :param lang:
        :param timeStamp:
        :param clientVersionInfo:
        :param access_token:
        :return:
        '''
        addTagInfoURL = baseURL + URL + "?lang=%s&timeStamp=%s&clientVersionInfo=%s&access_token=%s" % (lang, timeStamp, clientVersionInfo,access_token)
        logger.info("删除标签的URL为:%s" %addTagInfoURL)
        return addTagInfoURL


    def send_request_delTagOC(self,url,tagId):
        '''
        :param url:
        :param tagId:
        :return:
        '''
        data = {
            "tagId":tagId
        }
        headers = {"Content-Type": "application/json"}
        try:
            requests.post(url, data=json.dumps(data), headers=headers)
        except:
            logger.error("删除失败！")
        else:
            logger.info("删除标签ID[%s]成功" % tagId)








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
    oc_web_data = AC.get_oc_web(userName,password)


    print(oc_web_data)


    access_token_oc = AC.get_Access_token(url, oc_web_data)
    print(access_token_oc)

    tag= TagInfo()
    tagName = "autoTest3"
    tagDescribe = "this is a test"
    sortNumber = 10
    #

    # addTagInfo_url = tag.get_addTagInfo_URL(base_url_dev,addTagInfoURL,lang,currentTime,clientVersionInfo,access_token_oc)
    # print(addTagInfo_url)
    #
    # tag.send_request_addTagInfo(addTagInfo_url,tagName,tagDescribe,sortNumber)





    #删除便签
    # currentTime1  = base.getTimeStamp()
    # delTagOCURL = config.get("imi_oc_url", "delTagOC")
    # delTagOC_URL = tag.get_delTagOC_URL(base_url_dev,delTagOCURL,lang,currentTime,clientVersionInfo,access_token_oc)




    # host = config.get('mysql_dev', 'host')
    # port = config.get('mysql_dev', 'port')
    # user = config.get('mysql_dev', 'user')
    # password = config.get('mysql_dev', 'password')
    # db_cms = config.get('mysql_dev', 'db_cms')
    # mysql = mysqlUtils(host,port,user,password,db_cms)
    # tag_id = mysql.get_tagId(tagName)
    #
    #
    # time.sleep(20)
    # tag.send_request_delTagOC(delTagOC_URL,tag_id)


    #系统图库关联标签
    galleryId = "a99658f753fa4891b58a7a43b805b780"
    tagId = "df773295f3ce4927a981566c31c28848"
    #
    #
    # currentTime1  = base.getTimeStamp()
    # tagSystemPic4BackURL = config.get("imi_oc_url", "tagSystemPic4Back")
    # tagSystemPic4Back_URL = tag.get_tagSystemPic4Back_URL(base_url_dev,tagSystemPic4BackURL,lang,currentTime,clientVersionInfo,access_token_oc)
    #
    # time.sleep(20)
    # tag.send_request_tagSystemPic4Back(tagSystemPic4Back_URL,galleryId,tagId)




    #系统图库解解绑标签

    currentTime2  = base.getTimeStamp()
    deleteGalleryTagRelURL = config.get("imi_oc_url", "deleteGalleryTagRel")
    deleteGalleryTagRel_URL = tag.get_deleteGalleryTagRel_URL(base_url_dev,deleteGalleryTagRelURL,lang,currentTime,clientVersionInfo,access_token_oc)

    time.sleep(10)
    tag.send_request_deleteGalleryTagRel(deleteGalleryTagRel_URL,tagId,galleryId)