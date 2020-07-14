#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/7/9 18:57
# @Author  : Durat
# @Email   : durant.zeng@sunvalley.com.cn
# @File    : register.py
# @Software: PyCharm

import sys,os
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
import json
import requests
from common.baseUtil import baseUtils
from common.Logger import Logger
logger = Logger(logger="register").getlog()

class Register:

    def __init__(self):
        pass

    def get_mobile_URL(self,baseURL,URL,lang,timeStamp,clientVersionInfo,access_token):
        '''
        :param baseURL:
        :param lang:
        :param timeStamp:
        :param clientVersionInfo:
        :param access_token:
        :return:
        '''
        mobileURL = baseURL + URL + "?lang=%s&timeStamp=%s&clientVersionInfo=%s&access_token=%s" % (lang, timeStamp, clientVersionInfo,access_token)
        logger.info("注册的短信验证码的URL为:%s" %mobileURL)
        return mobileURL



    def send_request_mobile(self,url,mobile):
        '''
        :param url:
        :param mobile:
        :return:获取注册的短信验证码
        '''
        headers = {"Content-Type": "application/json"}
        parameters = {
                        "mobile":mobile
                    }
        r = requests.post(url, data=json.dumps(parameters), headers=headers)
        logger.info("返回的数据为:%s" % json.loads(r.text))
        return json.loads(r.text)


    def get_mobile_code_URL(self,baseURL,URL,lang,timeStamp,clientVersionInfo,access_token):
        '''
        :param baseURL:
        :param lang:
        :param timeStamp:
        :param clientVersionInfo:
        :param access_token:
        :return:
        '''
        mobilecodeURL = baseURL + URL + "?lang=%s&timeStamp=%s&clientVersionInfo=%s&access_token=%s" % (lang, timeStamp, clientVersionInfo,access_token)
        logger.info("注册_手机号_验证码的URL为:%s" %mobilecodeURL)
        return mobilecodeURL



    def send_request_mobile_code(self,url,mobile,code):
        '''
        :param url:
        :param mobile:
        :param code:
        :return:
        '''
        headers = {"Content-Type": "application/json"}
        parameters = {
                    "mobile":mobile,
                    "verifyCode":code
                }
        r = requests.post(url, data=json.dumps(parameters), headers=headers)
        logger.info("返回的数据为:%s" % json.loads(r.text))
        return json.loads(r.text)



    def get_mobile_code_password_URL(self,baseURL,URL,lang,timeStamp,clientVersionInfo,access_token):
        '''
        :param baseURL:
        :param lang:
        :param timeStamp:
        :param clientVersionInfo:
        :param access_token:
        :return:获取短信验证码
        '''
        mobilecodepasswordURL = baseURL + URL + "?lang=%s&timeStamp=%s&clientVersionInfo=%s&access_token=%s" % (lang, timeStamp, clientVersionInfo,access_token)
        logger.info("注册_手机号_验证码_密码的URL为:%s" %mobilecodepasswordURL)
        return mobilecodepasswordURL



    def send_request_mobile_code_password(self,url,mobile,code,password):
        '''
        :param url:
        :param mobile:
        :param code:
        :param password:
        :return:
        '''
        headers = {"Content-Type": "application/json"}
        parameters = {
                    "mobile":mobile,
                    "verifyCode":code,
                    "password":baseUtils.MD5(password),
                    "productLineId":"b74ba81ad5de48dd9fab250f911b9157"
                }
        r = requests.post(url, data=json.dumps(parameters), headers=headers)
        logger.info("返回的数据为:%s" % json.loads(r.text))
        return json.loads(r.text)

