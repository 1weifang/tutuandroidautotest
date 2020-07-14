#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/11/20 14:44
# @Author  : Durat
# @Email   : durant.zeng@sunvalley.com.cn
# @File    : queryAiNailSuit4Applet.py
# @Software: PyCharm

import sys,os
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
import json
import requests
from common.Logger import Logger


class queryAiNailSuit4Applet:

    def __init__(self):
        self.logger = Logger(logger="queryAiNailSuit4Applet").getlog()

    def get_queryAiNailSuit4AppletURL(self,baseURL,URL,lang,timeStamp,clientVersionInfo,access_token):
        '''
        :param baseURL:
        :param lang:
        :param timeStamp:
        :param clientVersionInfo:
        :param access_token:
        :return:Ai试甲-小程序-查询小程序的推荐套图
        '''
        ReallyURL = baseURL + URL + "?lang=%s&timeStamp=%s&clientVersionInfo=%s&access_token=%s" % (lang, timeStamp, clientVersionInfo,access_token)
        self.logger.info("url为:%s" %ReallyURL)
        return ReallyURL



    def send_request_queryAiNailSuit4Applet(self,url,suitType,currentPage,pageSize,fingers,inputPicName,nailSuitList,inputPicUrl,modelHand,nailShapeList,tagList,actionType,albumsPutFront,albumsId=None):
        '''
        :param url:
        :param currentPage:
        :param pageSize:
        :return:
        '''
        headers = {"Content-Type": "application/json"}
        parameters = {
                "suitType": suitType,
                "currentPage": currentPage,
                "pageSize":pageSize,
                "fingers":fingers,
                "inputPicHeight": 892,
                "inputPicWidth":750,
                "inputPicName":inputPicName,
                "nailSuitList": nailSuitList,
                "inputPicUrl":inputPicUrl,
                "modelHand":modelHand,
                "nailShapeList":nailShapeList,
                "tagList":tagList,
                "actionType":actionType,
                "albumsPutFront":albumsPutFront,
                "albumsId":albumsId
            }
        self.logger.info("请求的参数为:%s" %parameters)
        r = requests.post(url, data=json.dumps(parameters), headers=headers,timeout=30)
        self.logger.info("返回的参数为:%s" % json.loads(r.text))
        return json.loads(r.text)