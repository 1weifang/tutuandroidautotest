#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/2/27 9:47
# @Author  : Durat
# @Email   : durant.zeng@sunvalley.com.cn
# @File    : addArticle4Fr.py
# @Software: PyCharm


import sys, os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
import json
import requests
from common.Logger import Logger


class addArticle4Fr:

    def __init__(self):
        self.logger = Logger(logger="addArticle4Fr").getlog()

    def get_addArticle4FrURL(self, baseURL, URL, lang, timeStamp, clientVersionInfo, access_token):
        '''
        :param baseURL:
        :param lang:
        :param timeStamp:
        :param clientVersionInfo:
        :param access_token:
        :return:ugc文章-发布
        '''
        ReallyURL = baseURL + URL + "?lang=%s&timeStamp=%s&clientVersionInfo=%s&access_token=%s" % (
        lang, timeStamp, clientVersionInfo, access_token)
        self.logger.info("接口的URL为:%s" % ReallyURL)
        return ReallyURL

    def send_request_addArticle4Fr(self,url, articleType, articleStatus,imagesFallsUrl=None,imagesFallsWidth=None,imagesFallsHeight=None,imagesFallsLitimgUrl=None,imagesUrls=None,imagesLitimgUrls=None,content=None,topicId=None,albumsId=None,longitude=None,latitude=None,address=None,creatorPortrait=None,creatorPortraitLitimg=None):
        '''
        发表笔记或草稿
        :param articleType:
        :param articleStatus:

        '''
        headers = {"Content-Type": "application/json"}

        parameters = {
            "articleType": articleType,
            "articleStatus":articleStatus,
            "imagesFallsUrl":imagesFallsUrl,
            "imagesFallsWidth":imagesFallsWidth,
            "imagesFallsHeight":imagesFallsHeight,
            "imagesFallsLitimgUrl":imagesFallsLitimgUrl,
            "imagesUrls":imagesUrls,
            "imagesLitimgUrls":imagesLitimgUrls,
            # "videoFallsUrl":videoFallsUrl,
            # "videoFallsWidth":videoFallsWidth,
            # "videoFallsHeight":videoFallsHeight,
            # "videoFallsLitimgUrl":videoFallsLitimgUrl,
            # "videoUrl":videoUrl,
            "content":content,
            "topicId":topicId,
            "albumsId":albumsId,
            "longitude":longitude,
            "latitude":latitude,
            "address":address,
            "creatorPortrait":creatorPortrait,
            "creatorPortraitLitimg":creatorPortraitLitimg
            }
        self.logger.info("请求的参数为%s" % parameters)
        r = requests.post(url, data=json.dumps(parameters), headers=headers, timeout=30)
        self.logger.info("返回的参数为:%s" % json.loads(r.text))
        return json.loads(r.text)


