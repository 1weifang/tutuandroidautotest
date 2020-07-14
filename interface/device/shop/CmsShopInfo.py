#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/6/11 15:22
# @Author  : Durat
# @Email   : durant.zeng@sunvalley.com.cn
# @File    : CmsShopInfo.py
# @Software: PyCharm

import sys,os
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
import json
import requests
from common.Logger import Logger


class CmsShopInfo:

    def __init__(self):
        self.logger = Logger(logger="CmsShopInfo").getlog()

    def get_CmsShopInfoURL(self,baseURL,URL,lang,timeStamp,clientVersionInfo,access_token):
        '''
        :param baseURL:
        :param lang:
        :param timeStamp:
        :param clientVersionInfo:
        :param access_token:
        :return:增加附近店铺信息
        '''
        CmsShopInfoURL = baseURL + URL + "?lang=%s&timeStamp=%s&clientVersionInfo=%s&access_token=%s" % (lang, timeStamp, clientVersionInfo,access_token)
        self.logger.info("url为:%s" %CmsShopInfoURL)
        return CmsShopInfoURL


    def send_request_deleteCmsShopInfoBySN(self,url,sn):
        '''
        :param sn: 
        :return: 
        '''
        headers = {"Content-Type": "application/json"}
        parameters = {
                "sn": sn
                }
        self.logger.info("请求的参数为:%s" % parameters)
        r = requests.post(url, data=json.dumps(parameters), headers=headers,timeout=30)
        self.logger.info("返回的参数为:%s" % json.loads(r.text))
        return json.loads(r.text)



    def send_request_addCmsShopInfo(self,url,sn):
        '''
        :param url:
        :param sn:
        :return:
        '''
        headers = {"Content-Type": "application/json"}
        parameters = {
                "address": "五和大道",
                "area": "宝安区",
                "city": "深圳市",
                "province": "广东省",
                "shopName": "官方版本不同",
                "sn": sn,
                "tel": "778888",
                "x": "114.064241",
                "y": "22.60995"
                }
        self.logger.info("请求的参数为:%s" % parameters)
        r = requests.post(url, data=json.dumps(parameters), headers=headers)
        self.logger.info("返回的参数为:%s" % json.loads(r.text))
        return json.loads(r.text)



    def send_request_queryCmsShopInfoBySN(self,url,sn):
        '''
        :param url:
        :param sn:
        :return:
        '''
        headers = {"Content-Type": "application/json"}
        parameters = {
                "sn": sn
                }
        self.logger.info("请求的参数为:%s" % parameters)
        r = requests.post(url, data=json.dumps(parameters), headers=headers)
        self.logger.info("返回的参数为:%s" % json.loads(r.text))
        return json.loads(r.text)


    def send_request_updateCmsShopInfo(self,url,sn):
        '''
        :param url:
        :param sn:
        :return:
        '''
        headers = {"Content-Type": "application/json"}
        parameters = {
                "address": "五和大道",
                "area": "宝安区",
                "city": "深圳市",
                "province": "广东省",
                "shopName": "官方版本不同",
                "sn": sn,
                "tel": "778888",
                "x": "114.064241",
                "y": "22.60995"
                }
        self.logger.info("请求的参数为:%s" % parameters)
        r = requests.post(url, data=json.dumps(parameters), headers=headers)
        self.logger.info("返回的参数为:%s" % json.loads(r.text))
        return json.loads(r.text)


if __name__ == "__main__":

    ota = CmsShopInfo()
    URL = "https://mi-api.nailtutu.com/imi/cmsShopInfo/deleteCmsShopInfoBySN?&access_token=6883cbe9-c40a-4e4d-83e9-f737a582bce6&timeStamp=20190906141905&clientVersionInfo=android_1.0.34&lang=zh"
    sn = "e4937a14f91c05a3"

    result = ota.send_request_deleteCmsShopInfoBySN(URL,sn)