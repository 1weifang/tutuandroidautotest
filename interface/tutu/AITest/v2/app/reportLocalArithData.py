#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/11/20 13:40
# @Author  : Durat
# @Email   : durant.zeng@sunvalley.com.cn
# @File    : reportLocalArithData.py
# @Software: PyCharm

import sys,os
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
import json
import requests
from common.Logger import Logger



class reportLocalArithData:

    def __init__(self):
        self.logger = Logger(logger="reportLocalArithData").getlog()

    def get_reportLocalArithDataURL(self,baseURL,URL,lang,timeStamp,clientVersionInfo,access_token):
        '''
        :param baseURL:
        :param lang:
        :param timeStamp:
        :param clientVersionInfo:
        :param access_token:
        :return:Ai试甲-上报本地算法数据
        '''
        ReallyURL = baseURL + URL + "?lang=%s&timeStamp=%s&clientVersionInfo=%s&access_token=%s" % (lang, timeStamp, clientVersionInfo,access_token)
        self.logger.info("url为:%s" %ReallyURL)
        return ReallyURL


    #暂时先写死
    def send_request_reportLocalArithData(self,url,id):
        '''
        :param url:
        :param currentPage:
        :param pageSize:
        :return:
        '''
        headers = {"Content-Type": "application/json"}
        parameters = {
                "id": id,
                "inputPicUrl": "/tutu/ai/nail/danyaAi/local/20191120142031428_326473.png",
                "inputPicWidth":920,
                "inputPicHeight": 1162,
                "inputPicName":"1574230821470_cropbeauty.jpg",
                "binaryPicUrl": "/tutu/ai/nail/danyaAi/binaryPic/20191120142027269_842205.png"
            }
        self.logger.info("请求的参数为:%s" %parameters)
        r = requests.post(url, data=json.dumps(parameters), headers=headers,timeout=30)
        self.logger.info("返回的参数为:%s" % json.loads(r.text))
        return json.loads(r.text)