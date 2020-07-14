#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/8/23 10:34
# @Author  : Durat
# @Email   : durant.zeng@sunvalley.com.cn
# @File    : firmwareUpgrade.py
# @Software: PyCharm

import sys,os
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
import json
import requests
from common.Logger import Logger
from common.baseUtil import baseUtils



class firmwareUpgrade:

    def __init__(self):
        self.logger = Logger(logger="firmwareUpgrade").getlog()

    def get_firmwareUpgradeURL(self,baseURL,URL,lang,timeStamp,clientVersionInfo,access_token):
        '''
        :param baseURL:
        :param lang:
        :param timeStamp:
        :param clientVersionInfo:
        :param access_token:
        :return:固件检索升级
        '''
        addCmsShopInfoURL = baseURL + URL + "?lang=%s&timeStamp=%s&clientVersionInfo=%s&access_token=%s" % (lang, timeStamp, clientVersionInfo,access_token)
        self.logger.info("url为:%s" %addCmsShopInfoURL)
        return addCmsShopInfoURL

    def send_request_firmwareUpgrade(self,url,version,sn):
        '''
        :param url:
        :param version:
        :param sn:
        :return:
        '''
        headers = {"Content-Type": "application/json"}
        parameters = {
                    "client_id":"d00a9260baff4ad386939a7baf22b799",
                    "client_secret":"8236dc7b20ed484c830aabc5643717e9",
                    "version": version,
                    "sn":sn
                }
        self.logger.info("请求的参数为:%s" %parameters)
        r = requests.post(url, data=json.dumps(parameters), headers=headers,timeout=30)
        self.logger.info("返回的参数为:%s" % json.loads(r.text))
        return json.loads(r.text)



    def get_18_login_url(self,timeStamp,version,lang):
        '''
        :param timeStamp:
        :param version:
        :return:
        '''
        loginURL = "https://iot-api.nailtutu.com/oauth/login" + "?&timeStamp=%s&clientVersionInfo=%s&lang=%s" % (timeStamp,version,lang)
        self.logger.info("url为:%s" %loginURL)
        return loginURL

    def get_login_data(self):
        '''
        :return:
        '''
        pad_en_auth_login ={
                                    "auth_type": "sn_password",
                                    "client_id": "d00a9260baff4ad386939a7baf22b799",
                                    "client_secret": "8236dc7b20ed484c830aabc5643717e9",
                                    "grant_type": "password",
                                    "scope": "all",
                                    "sn": "R225T8E7B003F7837B77E5B49"
                            }
        return pad_en_auth_login

    def send_request_18_auth_login(self,url,data):
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


    def get_18_firmware_url(self,access_token,timeStamp,version,lang):
        '''
        :param access_token:
        :param timeStamp:
        :param version:
        :return:
        '''
        fiemwareURL = "https://iot-api.nailtutu.com/firmware/ota/upgrade/task/latest/rule" + "?&access_token=%s&timeStamp=%s&clientVersionInfo=%s&lang=%s" % (access_token,timeStamp,version,lang)
        self.logger.info("url为:%s" %fiemwareURL)
        return fiemwareURL



    def send_request_18_firmwareUpgrade(self,url,version):
        '''
        :param url:
        :param version:
        :return:
        '''
        headers = {"Content-Type": "application/json"}
        parameters = {
                    "version": version
                }
        self.logger.info("请求的参数为:%s" %parameters)
        r = requests.post(url, data=json.dumps(parameters), headers=headers,timeout=30)
        self.logger.info("返回的参数为:%s" % json.loads(r.text))
        return json.loads(r.text)



if __name__ == "__main__":
    ota = firmwareUpgrade()
    base = baseUtils()
    # URL = "https://mi-api.nailtutu.com/imi/firmware/ota/upgrade/task/latest/rule?&access_token=13daabfd-467c-49ba-bf08-7f386d034117&timeStamp=20190821180749&clientVersionInfo=android_1.0.0&lang=zh"
    # version = "010030"
    # sn = "R225T8E7B003F7837B77E5B49"
    #
    # result = ota.send_request_firmwareUpgrade(URL,version,sn)
    # print(result["data"])
    # # print(type(result["data"]))

    appVersion = "android_1.0.21"
    lang = "EN"
    timeStamp1 = base.getTimeStamp()
    loginURL = ota.get_18_login_url(timeStamp1,appVersion,lang)
    login_data = ota.get_login_data()
    re = ota.send_request_18_auth_login(loginURL,login_data)

    token = re["data"]["access_token"]
    timeStamp2 = base.getTimeStamp()
    firmwareVersion = "010018"
    firmwareUpgradeURL = ota.get_18_firmware_url(token,timeStamp2,appVersion,lang)
    ota.send_request_18_firmwareUpgrade(firmwareUpgradeURL,firmwareVersion)


