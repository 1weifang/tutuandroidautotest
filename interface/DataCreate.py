#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/6/4 14:08
# @Author  : Durat
# @Email   : durant.zeng@sunvalley.com.cn
# @File    : pictureUpload.py
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
logger = Logger(logger="PictureUpload").getlog()



class DataCreate:
    def __init__(self):
        pass

    def get_PictureUploadURL(self, baseurl,url, lang, timeStamp, clientVersionInfo,access_token):
        '''
        :param url:
        :param lang:
        :param timeStamp:
        :param clientVersionInfo:
        :return:
        '''
        PictureUploadURL = baseurl+ url + "?lang=%s&timeStamp=%s&clientVersionInfo=%s&access_token=%s" % (lang, timeStamp, clientVersionInfo,access_token)
        logger.info("PictureUploadURL为:%s" % PictureUploadURL)
        return PictureUploadURL


    def post_picture_single(self,url,targetid,filename,filepath):
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
            logger.error("targetid不存在，请检查配置！")

        r = requests.request("post",url,data = data,files=files)
        re = r.text
        josnre = json.loads(re)
        logger.info("单图片上传的返回值为：%s" %josnre)
        pictureDict= {
                    "galleryName" :josnre["data"]["pictureName"],
                    "galleryThumbnailUrl" :josnre["data"]["thumbnailPictureUrl"],
                    "galleryUrl" :josnre["data"]["pictureUrl"]
                }
        logger.info(pictureDict)
        return pictureDict


    def get_addTagInfo_url(self,baseURL,addTagInfoURL,lang,timeStamp,access_token):


        addTagInfoURL = baseURL + addTagInfoURL + "?lang=%s&timeStamp=%s&access_token=%s" % (lang, timeStamp,access_token)
        logger.info("addTagInfoURL的值为:%s" % addTagInfoURL)
        return addTagInfoURL


    def addTagInfo(self,url,tagName,tagDescribe,sortNumber):
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
            logger.info("创建标签[%s]成功" % tagName )

    def get_addSystemPic_url(self, baseURL, addSystemPicURL, lang, timeStamp, access_token):

        addSystemPicURL = baseURL + addSystemPicURL + "?lang=%s&timeStamp=%s&access_token=%s" % (lang, timeStamp, access_token)
        logger.info("addSystemPicURL的值为:%s" % addSystemPicURL)
        return addSystemPicURL

    def addSystemPic(self, url, picture, isReleaseRemind,tagIds):

        headers = {"Content-Type": "application/json"}
        logger.info("保存系统图库的url为:%s" %url)
        parameters = {
                    "galleryName": picture["galleryName"],
                    "galleryUrl": picture["galleryUrl"],
                    "galleryThumbnailUrl": picture["galleryThumbnailUrl"],
                    "isReleaseRemind":isReleaseRemind,
                    "tagIds":tagIds
                    }
        pictureList = []
        pictureList.append(parameters)
        data = {}
        data["pictureList"] = pictureList
        r = requests.post(url, data=json.dumps(data), headers=headers)
        logger.info("返回的数据为:%s" % json.loads(r.text))
        return json.loads(r.text)

    def get_auditSystemPic4Back_url(self, baseURL, auditSystemPic4BackURL, lang, timeStamp, access_token):

        auditSystemPic4BackURL = baseURL + auditSystemPic4BackURL + "?lang=%s&timeStamp=%s&access_token=%s" % (lang, timeStamp, access_token)
        logger.info("addSystemPicURL的值为:%s" % auditSystemPic4BackURL)
        return auditSystemPic4BackURL

    def auditSystemPic4Back(self, url, picture, isReleaseRemind,tagIds):

        headers = {"Content-Type": "application/json"}
        logger.info("保存系统图库的url为:%s" %url)
        parameters = {
                    "galleryName": picture["galleryName"],
                    "galleryUrl": picture["galleryUrl"],
                    "galleryThumbnailUrl": picture["galleryThumbnailUrl"],
                    "isReleaseRemind":isReleaseRemind,
                    "tagIds":tagIds
                    }
        pictureList = []
        pictureList.append(parameters)
        data = {}
        data["pictureList"] = pictureList
        r = requests.post(url, data=json.dumps(data), headers=headers)
        logger.info("返回的数据为:%s" % json.loads(r.text))
        return json.loads(r.text)









if __name__ == "__main__":
    # phone = "13723746965"
    config0 = FileParser(r'D:\anjouAutoTest\config\Authentication_url.ini')
    dev_AC_URL = config0.get('Authentication', 'dev')
    print(dev_AC_URL)
    config1 = FileParser(r'D:\anjouAutoTest\config\env.ini')
    base = baseUtils()
    clientVersionInfo = config1.get("clientVersionInfo", "clientVersionInfo")
    lang = config1.get("lang", "zh")
    currentTime = base.getTimeStamp()
    AC = Authentication()
    # DATA = AC.get_Android_CN_logged_in(phone)
    url = AC.get_AuthenticationURL(dev_AC_URL, lang, currentTime, clientVersionInfo)

    # access_token = AC.get_Access_token(url, DATA)

    config2 = FileParser(r'D:\anjouAutoTest\config\api_url.ini')
    base_url = config2.get("base_url","base_url_dev")
    PictureUploadURL = config2.get("PictureUploadURL","PictureUploadURL")
    pu = DataCreate()

    base_url_oc = config2.get("oc_web_base_url","base_url_dev")
    addTagInfoURL = config2.get("imi_oc_url","addTagInfo")

    userName = "admin@sunvalley.com.cn"
    oc_web_data = AC.get_oc_web(userName)
    login_url = config2.get("mi_login_url","login")

    OC_URL = oc_web_usl = AC.get_AuthenticationURL_OC(base_url_oc,login_url,lang,currentTime)

    print(OC_URL)


    access_token_oc = AC.get_Access_token(OC_URL, oc_web_data)
    print(access_token_oc)



    # tagName = "autoTest"
    # tagDescribe = "this is a test"
    # sortNumber = 10
    #
    # addTagInfo_url = pu.get_addTagInfo_url(base_url_oc,addTagInfoURL,lang,currentTime,access_token_oc)
    # print(addTagInfo_url)
    #
    # pu.addTagInfo(addTagInfo_url,tagName,tagDescribe,sortNumber)
    #

    addSystemPicURL = config2.get("imi_oc_url","addSystemPic")

    addSystemPic_url = pu.get_addSystemPic_url(base_url_oc,addSystemPicURL,lang,currentTime,access_token_oc)

    isReleaseRemind = 0
    tagIds = ["1"]








    PictureUploadURL = pu.get_PictureUploadURL(base_url_oc,PictureUploadURL,lang,currentTime,clientVersionInfo,access_token_oc)

    targetid = "系统"
    filename = r"1.jpg"
    filepath = r"D:\test\1.jpg"
    #
    pictureDict = pu.post_picture_single(PictureUploadURL,targetid,filename,filepath)


    pu.addSystemPic(addSystemPic_url,pictureDict,isReleaseRemind,tagIds)

    pu.get_auditSystemPic4Back_url()







