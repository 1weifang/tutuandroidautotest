#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/9/16 21:34
# @Author  : Durat
# @Email   : durant.zeng@sunvalley.com.cn
# @File    : pagelist4fornt.py
# @Software: PyCharm

import sys,os
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
import json
import requests
from common.Logger import Logger



class pagelist4fornt:

    def __init__(self):
        self.logger = Logger(logger="pagelist4fornt").getlog()

    def get_pagelist4forntURL(self,baseURL,URL,lang,timeStamp,access_token):
        '''
        :param baseURL:
        :param lang:
        :param timeStamp:
        :param clientVersionInfo:
        :return:租购订单列表
        '''
        pagelist4forntURL = baseURL + URL + "?lang=%s&timeStamp=%s&access_token=%s" % (lang, timeStamp, access_token)
        self.logger.info("url为:%s" %pagelist4forntURL)
        return pagelist4forntURL



    def send_request_pagelist4fornt(self,url,currentPage,pageSize):
        '''
        :param url:
        :param content:
        :return:
        '''
        headers = {"Content-Type": "application/json"}
        parameters = {
                        "currentPage": currentPage,
                        "pageSize": pageSize,
                            }
        self.logger.info("请求的参数为:%s" %parameters)
        r = requests.post(url, data=json.dumps(parameters), headers=headers,timeout=30)
        self.logger.info("返回的参数为:%s" % json.loads(r.text))
        return json.loads(r.text)