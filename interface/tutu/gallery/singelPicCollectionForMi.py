#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/6/10 15:09
# @Author  : Durat
# @Email   : durant.zeng@sunvalley.com.cn
# @File    : singelPicCollectionForMi.py
# @Software: PyCharm
import sys,os
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
import json
import requests
from common.Logger import Logger
from retrying import retry

def _result(result):
    return result is None





class singelPicCollectionForMi:

    def __init__(self):
        self.logger = Logger(logger="singelPicCollectionForMi").getlog()

    def get_singelPicCollectionForMiURL(self,baseURL,URL,lang,timeStamp,clientVersionInfo,access_token):
        '''
        :param baseURL:
        :param lang:
        :param timeStamp:
        :param clientVersionInfo:
        :param access_token:
        :return:图片收藏与取消收藏（diy、系统、社区图）
        '''
        singelPicCollectionForMiURL = baseURL + URL + "?lang=%s&timeStamp=%s&clientVersionInfo=%s&access_token=%s" % (lang, timeStamp, clientVersionInfo,access_token)
        self.logger.info("url为:%s" %singelPicCollectionForMiURL)
        return singelPicCollectionForMiURL



    @retry(stop_max_attempt_number=5, wait_random_min=1000, wait_random_max=2000, retry_on_result=_result)
    def send_request_singelPicCollectionForMi(self,url,galleryId,collectionType,collectStatus):
        '''
        :param url:
        :param galleryId:
        :param collectionType:
        :param collectStatus:
        :return:
        '''
        headers = {"Content-Type": "application/json"}
        if collectionType == "系统图库" and collectStatus == "收藏":
            parameters = {
                "galleryId":galleryId,
                "collectionType":"1"
            }
            pictureList = []
            pictureList.append(parameters)
            data = {"collectStatus":"1"}
            data["picList"] = pictureList
            self.logger.info("请求的参数为:%s" %parameters)
            r = requests.post(url, data=json.dumps(data), headers=headers,timeout=30)
            self.logger.info("返回的参数为:%s" % json.loads(r.text))
            return json.loads(r.text)

        elif collectionType == "系统图库" and collectStatus == "取消收藏":
            parameters = {
                "galleryId":galleryId,
                "collectionType":"1"
            }
            pictureList = []
            pictureList.append(parameters)
            data = {"collectStatus":"0"}
            data["picList"] = pictureList
            self.logger.info("请求的参数为:%s" %parameters)
            r = requests.post(url, data=json.dumps(data), headers=headers,timeout=30)
            self.logger.info("返回的参数为:%s" % json.loads(r.text))
            return json.loads(r.text)

        elif collectionType == "社区图库" and collectStatus == "收藏":
            parameters = {
                "galleryId":galleryId,
                "collectionType":"2"
            }
            pictureList = []
            pictureList.append(parameters)
            data = {"collectStatus":"1"}
            data["picList"] = pictureList
            self.logger.info("请求的参数为:%s" %parameters)
            r = requests.post(url, data=json.dumps(data), headers=headers,timeout=30)
            self.logger.info("返回的参数为:%s" % json.loads(r.text))
            return json.loads(r.text)

        elif collectionType == "社区图库" and collectStatus == "取消收藏":
            parameters = {
                "galleryId":galleryId,
                "collectionType":"2"
            }
            pictureList = []
            pictureList.append(parameters)
            data = {"collectStatus":"0"}
            data["picList"] = pictureList
            self.logger.info("请求的参数为:%s" %parameters)
            r = requests.post(url, data=json.dumps(data), headers=headers,timeout=30)
            self.logger.info("返回的参数为:%s" % json.loads(r.text))
            return json.loads(r.text)

        elif collectionType == "DIY图库" and collectStatus == "收藏":
            parameters = {
                "galleryId":galleryId,
                "collectionType":"3"
            }
            pictureList = []
            pictureList.append(parameters)
            data = {"collectStatus":"1"}
            data["picList"] = pictureList
            self.logger.info("请求的参数为:%s" %parameters)
            r = requests.post(url, data=json.dumps(data), headers=headers,timeout=30)
            self.logger.info("返回的参数为:%s" % json.loads(r.text))
            return json.loads(r.text)

        elif collectionType == "社区图库" and collectStatus == "取消收藏":
            parameters = {
                "galleryId":galleryId,
                "collectionType":"3"
            }
            pictureList = []
            pictureList.append(parameters)
            data = {"collectStatus":"0"}
            data["picList"] = pictureList
            self.logger.info("请求的参数为:%s" %parameters)
            r = requests.post(url, data=json.dumps(data), headers=headers,timeout=30)
            self.logger.info("返回的参数为:%s" % json.loads(r.text))
            return json.loads(r.text)
        else:
            self.logger.error("传值有误,请检查！")



    @retry(stop_max_attempt_number=5, wait_random_min=1000, wait_random_max=2000, retry_on_result=_result)
    def send_request_singelPicCollectionForMi_new(self,url,collectStatus,collectionType,galleryId):
        '''
        :param url:
        :param galleryId:
        :param collectionType:
        :param collectStatus:
        :return:
        '''
        headers = {"Content-Type": "application/json"}

        parameters = {
            "collectStatus": collectStatus,
            "collectVersion": "2.0",
            "picList": [{
                "collectionType": collectionType,
                "galleryId": galleryId
            }]
            }
        self.logger.info("请求的参数为:%s" %parameters)
        r = requests.post(url, data=json.dumps(parameters), headers=headers,timeout=30)
        self.logger.info("返回的参数为:%s" % json.loads(r.text))
        return json.loads(r.text)




