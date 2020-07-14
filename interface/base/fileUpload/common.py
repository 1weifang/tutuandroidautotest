#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/10/16 9:57
# @Author  : Durat
# @Email   : durant.zeng@sunvalley.com.cn
# @File    : common.py
# @Software: PyCharm

import sys,os
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
import json
import requests
from common.Logger import Logger
import warnings


class common:


    def __init__(self):
        self.logger = Logger(logger="common").getlog()
        warnings.simplefilter("ignore",ResourceWarning)


    def get_commonURL(self,baseURL,URL,lang,timeStamp,clientVersionInfo,access_token):
        '''
        :param baseURL:
        :param lang:
        :param timeStamp:
        :param clientVersionInfo:
        :return:文件上传（通用版）
        '''
        reallyURL = baseURL + URL + "?lang=%s&timeStamp=%s&clientVersionInfo=%s&access_token=%s" % (lang, timeStamp, clientVersionInfo,access_token)
        self.logger.info("url为:%s" %reallyURL)
        return reallyURL


    def get_commonURL_new(self,baseURL,URL):
        '''
        :param baseURL:
        :param lang:
        :param timeStamp:
        :param clientVersionInfo:
        :return:文件上传（通用版）
        '''
        reallyURL = baseURL + URL
        self.logger.info("url为:%s" %reallyURL)
        return reallyURL


    def send_request_common(self,url,fileName,filepath,directory=None,autoWithContentType=None):
        '''
        :param url:
        :param content:
        :return:
        '''

        custom_headers = {

        }
        files = {"file": (fileName, open(filepath, "rb"), "multipart/form-data", custom_headers)}

        upload_data = {
                "directory":directory,
                "autoWithContentType":autoWithContentType}

        self.logger.info("请求参数为%s" %upload_data)
        r = requests.request("post",url,data = upload_data,files=files,timeout=30)
        re = r.text
        josnre = json.loads(re)
        self.logger.info("返回值为：%s" %josnre)
        return json.loads(re)


