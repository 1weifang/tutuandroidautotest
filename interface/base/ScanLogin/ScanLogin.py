#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/7/10 10:00
# @Author  : Durat
# @Email   : durant.zeng@sunvalley.com.cn
# @File    : ScanLogin.py
# @Software: PyCharm

import sys,os
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
import json
import requests
from common.Logger import Logger


class ScanLogin:

    def __init__(self):
        self.logger = Logger(logger="ScanLogin").getlog()


    def get_code_URL(self,baseURL,URL,lang,timeStamp,clientVersionInfo,access_token):
        '''
        :param baseURL:
        :param lang:
        :param timeStamp:
        :param clientVersionInfo:
        :param access_token:
        :return:
        '''
        codeURL = baseURL + URL + "?lang=%s&timeStamp=%s&clientVersionInfo=%s&access_token=%s" % (lang, timeStamp, clientVersionInfo,access_token)
        self.logger.info("url为:%s" %codeURL)
        return codeURL



    def send_request_code(self,url):
        '''
        :param url:
        :param mobile:
        :return:获得pad端产生的二维码
        '''
        headers = {"Content-Type": "application/json"}
        parameters = {
                    }
        self.logger.info("请求的参数为:%s" %parameters)
        r = requests.post(url, data=json.dumps(parameters), headers=headers,timeout=30)
        re = json.loads(r.text)
        self.logger.info("返回的参数为:%s" % json.loads(r.text))
        return re


    def get_build_connect_URL(self,baseURL,URL,lang,timeStamp,clientVersionInfo,access_token):
        '''
        :param baseURL:
        :param lang:
        :param timeStamp:
        :param clientVersionInfo:
        :param access_token:
        :return:
        '''
        scanURL = baseURL + URL + "?lang=%s&timeStamp=%s&clientVersionInfo=%s&access_token=%s" % (lang, timeStamp, clientVersionInfo,access_token)
        self.logger.info("url为:%s" %scanURL)
        return scanURL



    def send_request_build_connect(self,url,qrCode):
        '''
        :param url:
        :param mobile:
        :return:APP或小程序获取扫码登陆
        '''
        headers = {"Content-Type": "application/json"}
        parameters = {
                        "qrCode": qrCode
                    }
        self.logger.info("请求的参数为:%s" %parameters)
        r = requests.post(url, data=json.dumps(parameters), headers=headers,timeout=30)
        self.logger.info("返回的参数为:%s" % json.loads(r.text))
        return json.loads(r.text)


    def get_get_connect_URL(self,baseURL,URL,lang,timeStamp,clientVersionInfo,access_token):
        '''
        :param baseURL:
        :param lang:
        :param timeStamp:
        :param clientVersionInfo:
        :param access_token:
        :return:
        '''
        codeURL = baseURL + URL + "?lang=%s&timeStamp=%s&clientVersionInfo=%s&access_token=%s" % (lang, timeStamp, clientVersionInfo,access_token)
        self.logger.info("url为:%s" %codeURL)
        return codeURL



    def send_request_get_connect(self,url,qrCode):
        '''
        :param url:
        :param mobile:
        :return:pad端判断是否有扫码
        '''
        headers = {"Content-Type": "application/json"}
        parameters = {
                        "qrCode":qrCode
                    }
        self.logger.info("请求的参数为:%s" %parameters)
        r = requests.post(url, data=json.dumps(parameters), headers=headers,timeout=30)
        self.logger.info("返回的参数为:%s" % json.loads(r.text))
        return json.loads(r.text)

    def get_app_confirm_login_URL(self, baseURL, URL, lang, timeStamp, clientVersionInfo, access_token):
        '''
        :param baseURL:
        :param lang:
        :param timeStamp:
        :param clientVersionInfo:
        :param access_token:
        :return:
        '''
        codeURL = baseURL + URL + "?lang=%s&timeStamp=%s&clientVersionInfo=%s&access_token=%s" % (
        lang, timeStamp, clientVersionInfo, access_token)
        self.logger.info("url为:%s" %codeURL)
        return codeURL

    def send_request_app_confirm_login(self, url):
        '''
        :param url:
        :param mobile:
        :return:APP或小程序获取扫码登陆
        '''
        headers = {"Content-Type": "application/json"}
        parameters = {

        }
        self.logger.info("请求的参数为:%s" %parameters)
        r = requests.post(url, data=json.dumps(parameters), headers=headers, timeout=30)
        self.logger.info("返回的参数为:%s" % json.loads(r.text))
        return json.loads(r.text)



if __name__ == "__main__":
    scan = ScanLogin()



    url = "https://mi-api-dev.nailtutu.com/oauth/generate-qr-code?lang=zh&timeStamp=20190710105800&clientVersionInfo=android_app_ch_1.0.2&access_token=e6b64ab3-513a-4182-a9c0-9a217ed94c27"


    re = scan.send_request_code(url)

    print(type(re))




