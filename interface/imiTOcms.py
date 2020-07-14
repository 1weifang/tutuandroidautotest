#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/5/21 20:50
# @Author  : Durat
# @Email   : durant.zeng@sunvalley.com.cn
# @File    : test.py
# @Software: PyCharm
import sys,os
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
import json
import requests
from common.FileParsing import FileParser
from common.baseUtil import baseUtils
from interface.base.login.authentication import Authentication
from interface.DataCreate import DataCreate
from common.Logger import Logger
logger = Logger(logger="imi").getlog()


class imi:

    def __init__(self):
        pass

    @classmethod
    def get_AddDiyPicURL(self,baseURL,URL,lang,timeStamp,clientVersionInfo,access_token):
        '''
        :param baseURL:
        :param lang:
        :param timeStamp:
        :param clientVersionInfo:
        :param access_token:
        :return:diy与社区图片上传
        '''
        AddDiyPicURL = baseURL + URL + "?lang=%s&timeStamp=%s&clientVersionInfo=%s&access_token=%s" % (lang, timeStamp, clientVersionInfo,access_token)
        logger.info("diy与社区图片上传的URL为:%s" %AddDiyPicURL)
        return AddDiyPicURL

    @classmethod
    def get_QueryDiyPicURL(self,baseURL,URL,lang,timeStamp,clientVersionInfo,access_token):
        '''
        :param baseURL:
        :param lang:
        :param timeStamp:
        :param clientVersionInfo:
        :param access_token:
        :return:我的上传
        '''
        QueryDiyPicURL = baseURL + URL + "?lang=%s&timeStamp=%s&clientVersionInfo=%s&access_token=%s" % (lang, timeStamp, clientVersionInfo,access_token)
        logger.info("我的上传的URL为:%s" % QueryDiyPicURL)
        return QueryDiyPicURL

    @classmethod
    def get_PicDetailForMiURL(self,baseURL,URL,lang,timeStamp,clientVersionInfo,access_token):
        '''
        :param baseURL:
        :param lang:
        :param timeStamp:
        :param clientVersionInfo:
        :param access_token:
        :return:取单张图详情
        '''
        PicDetailForMiURL = baseURL + URL + "?lang=%s&timeStamp=%s&clientVersionInfo=%s&access_token=%s" % (lang, timeStamp, clientVersionInfo,access_token)
        logger.info("取单张图详情的URL为:%s" % PicDetailForMiURL)
        return PicDetailForMiURL

    @classmethod
    def get_SingelPicCollectionForMiURL(self,baseURL,URL,lang,timeStamp,clientVersionInfo,access_token):
        '''
        :param baseURL:
        :param lang:
        :param timeStamp:
        :param clientVersionInfo:
        :param access_token:
        :return:图片收藏与取消收藏（diy、系统、社区图）
        '''
        SingelPicCollectionForMiURL = baseURL + URL + "?lang=%s&timeStamp=%s&clientVersionInfo=%s&access_token=%s" % (lang, timeStamp, clientVersionInfo,access_token)
        logger.info("图片收藏与取消收藏（diy、系统、社区图）的URL为:%s" % SingelPicCollectionForMiURL)
        return SingelPicCollectionForMiURL

    @classmethod
    def get_PicList4MiByidOrTagURL(self,baseURL,URL,lang,timeStamp,clientVersionInfo,access_token):
        '''
        :param baseURL:
        :param lang:
        :param timeStamp:
        :param clientVersionInfo:
        :param access_token:
        :return:彩绘图库搜索
        '''
        PicList4MiByidOrTagURL = baseURL + URL + "?lang=%s&timeStamp=%s&clientVersionInfo=%s&access_token=%s" % (lang, timeStamp, clientVersionInfo,access_token)
        logger.info("彩绘图库搜索的URL为:%s" % PicList4MiByidOrTagURL)
        return PicList4MiByidOrTagURL

    @classmethod
    def get_MyPicCollectionListIMURL(self,baseURL,URL,lang,timeStamp,clientVersionInfo,access_token):
        '''
        :param baseURL:
        :param lang:
        :param timeStamp:
        :param clientVersionInfo:
        :param access_token:
        :return:个人中心-我的收藏
        '''
        MyPicCollectionListIMURL = baseURL + URL + "?lang=%s&timeStamp=%s&clientVersionInfo=%s&access_token=%s" % (lang, timeStamp, clientVersionInfo,access_token)
        logger.info("个人中心-我的收藏的URL为:%s" % MyPicCollectionListIMURL)
        return MyPicCollectionListIMURL

    @classmethod
    def get_QueryAllTagInfoForMiURL(self,baseURL,URL,lang,timeStamp,clientVersionInfo,access_token):
        '''
        :param baseURL:
        :param lang:
        :param timeStamp:
        :param clientVersionInfo:
        :param access_token:
        :return:彩绘图库-常用标签与标签
        '''
        QueryAllTagInfoForMiURL = baseURL + URL + "?lang=%s&timeStamp=%s&clientVersionInfo=%s&access_token=%s" % (lang, timeStamp, clientVersionInfo,access_token)
        logger.info("彩绘图库-常用标签与标签的URL为:%s" % QueryAllTagInfoForMiURL)
        return QueryAllTagInfoForMiURL

    @classmethod
    def get_AlbumsList4FrontURL(self,baseURL,URL,lang,timeStamp,clientVersionInfo,access_token):
        '''
        :param baseURL:
        :param lang:
        :param timeStamp:
        :param clientVersionInfo:
        :param access_token:
        :return:特辑-列表查询
        '''

        AlbumsList4FrontURL = baseURL + URL + "?lang=%s&timeStamp=%s&clientVersionInfo=%s&access_token=%s" % (lang, timeStamp, clientVersionInfo,access_token)
        logger.info("特辑-列表查询的URL为:%s" % AlbumsList4FrontURL)
        return AlbumsList4FrontURL

    @classmethod
    def get_AlbumsPraise4FrontURL(self,baseURL,URL,lang,timeStamp,clientVersionInfo,access_token):
        '''
        :param baseURL:
        :param lang:
        :param timeStamp:
        :param clientVersionInfo:
        :param access_token:
        :return:特辑-前端专辑点赞
        '''

        AlbumsPraise4FrontURL = baseURL + URL + "?lang=%s&timeStamp=%s&clientVersionInfo=%s&access_token=%s" % (lang, timeStamp, clientVersionInfo,access_token)
        logger.info("特辑-前端专辑点赞的URL为:%s" % AlbumsPraise4FrontURL)
        return AlbumsPraise4FrontURL

    @classmethod
    def get_AlbumsDeatil4FrontURL(self,baseURL,URL,lang,timeStamp,clientVersionInfo,access_token):
        '''
        :param baseURL:
        :param lang:
        :param timeStamp:
        :param clientVersionInfo:
        :param access_token:
        :return:特辑-前端列表详情
        '''

        AlbumsDeatil4FrontURL = baseURL + URL + "?lang=%s&timeStamp=%s&clientVersionInfo=%s&access_token=%s" % (lang, timeStamp, clientVersionInfo,access_token)
        logger.info("特辑-前端列表详情的URL为:%s" % AlbumsDeatil4FrontURL)
        return AlbumsDeatil4FrontURL

    @classmethod
    def get_AlbumsList4FrontURL1(self,baseURL,URL,lang,timeStamp,clientVersionInfo,access_token):
        '''
        :param baseURL:
        :param lang:
        :param timeStamp:
        :param clientVersionInfo:
        :param access_token:
        :return:特辑-列表查询
        '''

        AlbumsList4FrontURL = baseURL + URL + "?lang=%s&timeStamp=%s&clientVersionInfo=%s&access_token=%s" % (lang, timeStamp, clientVersionInfo,access_token)
        logger.info("特辑-列表查询的URL为:%s" % AlbumsList4FrontURL)
        return AlbumsList4FrontURL

    @classmethod
    def get_albumsPraise4FrontURL(self,baseURL,URL,lang,timeStamp,clientVersionInfo,access_token):
        '''
        :param baseURL:
        :param lang:
        :param timeStamp:
        :param clientVersionInfo:
        :param access_token:
        :return:特辑-前端专辑点赞
        '''

        albumsPraise4FrontURL = baseURL + URL + "?lang=%s&timeStamp=%s&clientVersionInfo=%s&access_token=%s" % (lang, timeStamp, clientVersionInfo,access_token)
        logger.info("特辑-前端专辑点赞的URL为:%s" % albumsPraise4FrontURL)
        return albumsPraise4FrontURL

    @classmethod
    def get_AlbumsShare4FrontURL(self,baseURL,URL,lang,timeStamp,clientVersionInfo,access_token):
        '''
        :param baseURL:
        :param lang:
        :param timeStamp:
        :param clientVersionInfo:
        :param access_token:
        :return:特辑-专辑分享
        '''

        AlbumsShare4FrontURL = baseURL + URL + "?lang=%s&timeStamp=%s&clientVersionInfo=%s&access_token=%s" % (lang, timeStamp, clientVersionInfo,access_token)
        logger.info("特辑-专辑分享的URL为:%s" % AlbumsShare4FrontURL)
        return AlbumsShare4FrontURL

    @classmethod
    def get_AlbumsCollection4FrontURL(self,baseURL,URL,lang,timeStamp,clientVersionInfo,access_token):
        '''
        :param baseURL:
        :param lang:
        :param timeStamp:
        :param clientVersionInfo:
        :param access_token:
        :return:专辑图片收藏(分为，一键收藏和单独收藏)
        '''

        AlbumsCollection4FrontURL = baseURL + URL + "?lang=%s&timeStamp=%s&clientVersionInfo=%s&access_token=%s" % (lang, timeStamp, clientVersionInfo,access_token)
        logger.info("专辑图片收藏(分为，一键收藏和单独收藏)的URL为:%s" % AlbumsCollection4FrontURL)
        return AlbumsCollection4FrontURL

    @classmethod
    def get_AlbumsUnCollection4FrontURL(self,baseURL,URL,lang,timeStamp,clientVersionInfo,access_token):
        '''
        :param baseURL:
        :param lang:
        :param timeStamp:
        :param clientVersionInfo:
        :param access_token:
        :return:特辑-专辑图片取消收藏(分为，一键收藏和单独收藏)
        '''
        AlbumsUnCollection4FrontURL = baseURL + URL + "?lang=%s&timeStamp=%s&clientVersionInfo=%s&access_token=%s" % (lang, timeStamp, clientVersionInfo,access_token)
        logger.info("专辑图片取消收藏(分为，一键收藏和单独收藏)的URL为:%s" % AlbumsUnCollection4FrontURL)
        return AlbumsUnCollection4FrontURL

    @classmethod
    def send_request(self, url, parameters=""):
        '''
        :param url:
        :param parameters:
        :return:
        '''
        headers = {"Content-Type": "application/json"}
        if parameters:
            logger.info("传递的参数为:%s"%parameters)
            r = requests.post(url, data=json.dumps(parameters), headers=headers)
            logger.info("返回的数据为:%s" %json.loads(r.text))
            return json.loads(r.text)
        else:
            r = requests.post(url,headers=headers)
            logger.info("返回的数据为:%s" % json.loads(r.text))
            return json.loads(r.text)

    def send_request_addDiyPic(self,url,picture,collectionType):
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
                "galleryName":picture["galleryName"],
                "galleryUrl":picture["galleryUrl"],
                "galleryThumbnailUrl":picture["galleryThumbnailUrl"],
                "collectionType":"2"
            }
            r = requests.post(url, data=json.dumps(parameters), headers=headers)
            logger.info("返回的数据为:%s" % json.loads(r.text))
            return json.loads(r.text)
        elif collectionType == "DIY图库并收藏":
            parameters = {
                "galleryName":picture["galleryName"],
                "galleryUrl":picture["galleryUrl"],
                "galleryThumbnailUrl":picture["galleryThumbnailUrl"],
                "collectionType":"3"}

            r = requests.post(url, data=json.dumps(parameters), headers=headers)
            logger.info("返回的数据为:%s" % json.loads(r.text))
            return json.loads(r.text)

if __name__ == "__main__":
    imi = imi()
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
    PictureUploadURL = config2.get("PictureUploadURL","PictureUploadURL")
    pu = DataCreate()
    PictureUploadURL = pu.get_PictureUploadURL(base_url,PictureUploadURL,lang,currentTime,clientVersionInfo,access_token)

    targetid = "社区"
    filename = r"1.jpg"
    filepath = r"D:\test\1.jpg"
    #
    picture = pu.post_picture_single(PictureUploadURL,targetid,filename,filepath)
    AddDiyPicURL = config2.get("imi_url","AddDiyPicURL")
    AddDiyPicURL = imi.get_AddDiyPicURL(base_url,AddDiyPicURL,lang,currentTime,clientVersionInfo,access_token)
    collectionType = "社区图库"
    imi.send_request_addDiyPic(AddDiyPicURL,picture,collectionType)










