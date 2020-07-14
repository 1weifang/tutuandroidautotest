#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/6/11 19:44
# @Author  : Durat
# @Email   : durant.zeng@sunvalley.com.cn
# @File    : calibrationSetting.py
# @Software: PyCharm
import sys,os
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
import json
import requests
from common.baseUtil import baseUtils
from common.Logger import Logger



class calibrationSetting:

    def __init__(self):
        self.logger = Logger(logger="calibrationSetting").getlog()

    def get_calibrationSettingURL(self,baseURL,URL,lang,timeStamp,clientVersionInfo):
        '''
        :param baseURL:
        :param lang:
        :param timeStamp:
        :param clientVersionInfo:
        :return:机器校准设置接口
        '''
        calibrationSettingURL = baseURL + URL + "?lang=%s&timeStamp=%s&clientVersionInfo=%s" % (lang, timeStamp, clientVersionInfo)
        self.logger.info("url为:%s" %calibrationSettingURL)
        return calibrationSettingURL



    def send_request_calibrationSetting(self,url,miniRectWidth):
        '''
        :param url:
        :param content:
        :return:
        '''
        headers = {"Content-Type": "application/json"}
        parameters = {
                    "calibrationRect": "{\"bottom\":340,\"left\":221,\"right\":413,\"top\":52}",
                    "cameraRotate": "0.0",
                    "cameraScale": "0.3225",
                    "lineAgnles": "{\"bottom\":129.00,\"left\":104.00,\"right\":104.00,\"top\":129.00}",
                    "miniRectWidth": miniRectWidth,
                    "moreData": "",
                    "sn": "e4937a14f91c05a3",
                    "whRate": "0.8062016",
                    "xaxleStartPos": "575",
                    "yaxleStartPos": "1700"
                }
        self.logger.info("请求的参数为:%s" %parameters)
        r = requests.post(url, data=json.dumps(parameters), headers=headers,timeout=30)
        self.logger.info("返回的参数为:%s" % json.loads(r.text))
        return json.loads(r.text)

if __name__ == "__main__":


    imi = calibrationSetting()
    base = baseUtils()
    miniRectWidth = base.get_miniRectWidth()
    print(type(miniRectWidth))
    url = "https://env-proxy.nailtutu.com/api/cms/machine/calibrationSetting?&timeStamp=20190906103623&clientVersionInfo=android_1.0.0&lang=zh"
    imi.send_request_calibrationSetting(url,miniRectWidth)

    # print(imi)
    # phone = "13723746965"
    # config0 = FileParser(r'D:\anjouAutoTest\config\Authentication_url.ini')
    # dev_AC_URL = config0.get('Authentication', 'dev')
    # print(dev_AC_URL)
    # config1 = FileParser(r'D:\anjouAutoTest\config\env.ini')
    # base = baseUtils()
    # clientVersionInfo = config1.get("clientVersionInfo", "clientVersionInfo")
    # lang = config1.get("lang", "zh")
    # currentTime = base.getTimeStamp()
    # AC = Authentication()
    # DATA = AC.get_PAD_CN_logged_in(phone)
    # url = AC.get_AuthenticationURL(dev_AC_URL, lang, currentTime, clientVersionInfo)
    #
    # access_token = AC.get_Access_token(url, DATA)
    #
    # config2 = FileParser(r'D:\anjouAutoTest\config\api_url.ini')
    # base_url = config2.get("env_base_url","base_url_dev")
    #
    #
    #
    # calibrationSettingURL = config2.get("env_url","calibrationSettingURL")
    # calibrationSettingURL = imi.get_calibrationSettingURL(base_url,calibrationSettingURL,lang,currentTime,clientVersionInfo,access_token)
    #
    # sn = "e4937a14f91c05a3"
    # whRate = "0.79849416"
    # cameraScale = "0.32595325"
    # xaxleStartPos = "575"
    # yaxleStartPos = "1700"
    # cameraRotate = "0.0"
    # miniRectWidth = "0"
    # moreData = ""
    #
    # bottom = 343
    # left = 217
    # right = 413
    # top = 51
    #
    # calibrationRect = {
    #                 "bottom":bottom,
    #                 "left":left,
    #                 "right":right,
    #                 "top":top
    #                 }
    #
    #
    # lineAgnles = ""







    # content ="星河world星河world星河world"
    #
    # imi.send_request_addCmsUserQuestion(addCmsUserQuestionURL,content)