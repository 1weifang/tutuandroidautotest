#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/7/9 11:34
# @Author  : Durat
# @Email   : durant.zeng@sunvalley.com.cn
# @File    : send-login-sms-verify-code.py
# @Software: PyCharm
import sys,os
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
import json
import requests
from common.Logger import Logger
logger = Logger(logger="sendCode").getlog()


class sendCode:
    def __init__(self):
        pass

    def get_sendCodeURL(self,baseURL,URL,lang,timeStamp,clientVersionInfo,access_token):
        '''
        :param baseURL:
        :param lang:
        :param timeStamp:
        :param clientVersionInfo:
        :param access_token:
        :return:获取短信验证码
        '''
        sendCodeURL = baseURL + URL + "?lang=%s&timeStamp=%s&clientVersionInfo=%s&access_token=%s" % (lang, timeStamp, clientVersionInfo,access_token)
        logger.info("获取短信验证码的URL为:%s" %sendCodeURL)
        return sendCodeURL



    def send_request_sendCode(self,url,mobile):
        '''
        :param url:
        :param mobile:
        :return:
        '''
        headers = {"Content-Type": "application/json"}
        parameters = {
                    "mobile":mobile
                }
        r = requests.post(url, data=json.dumps(parameters), headers=headers)
        logger.info("返回的数据为:%s" % json.loads(r.text))
        return json.loads(r.text)


