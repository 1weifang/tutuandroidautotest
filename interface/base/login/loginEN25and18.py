#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/9/3 14:00
# @Author  : Durat
# @Email   : durant.zeng@sunvalley.com.cn
# @File    : loginEN25.py
# @Software: PyCharm


import sys,os
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
import json
import requests
from common.baseUtil import baseUtils
from common.Logger import Logger
base = baseUtils()

class loginEN25and18:

    def __init__(self):
        self.logger = Logger(logger="loginEN25and18").getlog()

    def get_appauth_loginEN25URL(self,timeStamp,version):
        '''
        :param timeStamp:
        :param clientVersionInfo:
        :return:
        '''
        appauthURL = "https://mi-api-uat.sunvalleycloud.com/auth/app-auth" + "?&timeStamp=%s&clientVersionInfo=%s&requestToken=0&lang=EN" % (timeStamp,version)
        self.logger.info("url为:%s" %appauthURL)
        return appauthURL


    def get_get_appauth_data(self):

        pad_EN_Not_logged_in = {
            "appKey": "b773f52c25a041bfa1318607616b1011",
            "appSecret": "ed6ac5d3726d4fe59ed5f2a83c928cf1"
        }
        return pad_EN_Not_logged_in

    def send_request_getrequestToken(self,url,data):
        '''
        :param url:
        :param data:
        :return:
        '''
        headers = {"Content-Type": "application/json"}

        self.logger.info("请求的参数为:%s" %data)
        r = requests.post(url, data=json.dumps(data), headers=headers,timeout=30)
        self.logger.info("返回的参数为:%s" % json.loads(r.text))
        return json.loads(r.text)


    def get_login_25_en_URL(self,timestamp,version,requestToken):
        '''
        :param timestamp:
        :param requestToken:
        :return:
        '''
        loginURL = "https://mi-api-uat.sunvalleycloud.com/auth/email-password-login" + "?&timeStamp=%s&clientVersionInfo=%s&requestToken=%s&lang=EN" % (timestamp,version,requestToken)
        self.logger.info("url为:%s" %loginURL)
        return loginURL

    def send_request_email_password_login(self,url,email,password):
        '''
        :param url:
        :param sn:
        :return:
        '''
        headers = {"Content-Type": "application/json"}
        parameters = {
            "clientType": "A602",
            "email": email,
            "password": base.MD5(password)
                }
        self.logger.info("请求的参数为:%s" %parameters)
        r = requests.post(url, data=json.dumps(parameters), headers=headers,timeout=30)
        self.logger.info("返回的参数为:%s" % json.loads(r.text))
        return json.loads(r.text)


if __name__ == "__main__":
    ota = loginEN25and18()
    timestamp1 = base.getTimeStamp()
    version = "android_1.0.18"
    URL1 = ota.get_appauth_loginEN25URL(timestamp1,version)
    data = ota.get_get_appauth_data()
    re = ota.send_request_getrequestToken(URL1,data)
    requestToken = re["data"]["requestToken"]
    print(requestToken)

    timestamp2 = base.getTimeStamp()
    emalil = "durant.zeng@sunvalley.com.cn"
    password = "123456"
    loginURL = ota.get_login_25_en_URL(timestamp2,version,requestToken)
    ota.send_request_email_password_login(loginURL,emalil,password)


