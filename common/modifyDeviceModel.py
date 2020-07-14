#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/9/5 14:10
# @Author  : Durat
# @Email   : durant.zeng@sunvalley.com.cn
# @File    : modifyDeviceModel.py
# @Software: PyCharm

import sys,os
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
import json
import requests
from common.Logger import Logger
from common.baseUtil import baseUtils

base = baseUtils()


class modifyDeviceModel:

    def __init__(self):
        self.logger = Logger(logger="modifyDeviceModel").getlog()

    def get_modifyDeviceModel_url(self,env,access_token,lang,timeStamp):
        '''
        :param access_token:
        :param lang:
        :param timeStamp:
        :return:
        '''
        if env == "prod":
            modifyDeviceModelURL = "https://oc-api.nailtutu.com" +"/api/deviceModel/edit?access_token=%s&lang=%s&timeStamp=%s" % (access_token, lang,timeStamp)
            self.logger.info("修改设备模式的URL为:%s" %modifyDeviceModelURL)
            return modifyDeviceModelURL
        elif env == "uat":
            modifyDeviceModelURL = "https://oc-api-uat.nailtutu.com" + "/api/deviceModel/edit?access_token=%s&lang=%s&timeStamp=%s" % (access_token, lang, timeStamp)
            self.logger.info("修改设备模式的URL为:%s" % modifyDeviceModelURL)
            return modifyDeviceModelURL
        elif env == "dev":
            modifyDeviceModelURL = "https://oc-api-dev.nailtutu.com" + "/api/deviceModel/edit?access_token=%s&lang=%s&timeStamp=%s" % (access_token, lang, timeStamp)
            self.logger.info("修改设备模式的URL为:%s" % modifyDeviceModelURL)
            return modifyDeviceModelURL


    def get_data_modifyDeviceModel(self,sn,deviceModel):
        '''
        :param sn:
        :param deviceModel:
        :return:
        '''
        para = {
                "id": "488bd8f4744048ea9c69dd350fbe014a",
                "sn": sn,
                "deviceModel": 0,
                "sku":"49-03000-007-b"
                }

        #线上的id
        #488bd8f4744048ea9c69dd350fbe014a
        #uat
        #fde1248e6a524ff9a956b90acdc7d1f4
        if deviceModel == "出租":
            para["deviceModel"] = 0
            self.logger.info("%s的设备模式修改为%s" %(sn,deviceModel))
            return para
        elif deviceModel == "共享":
            para["deviceModel"] = 1
            para["sku"] = "49-03000-007-a"
            self.logger.info("%s的设备模式修改为%s" % (sn, deviceModel))
            return para
        elif deviceModel == "购买":
            para["deviceModel"] = 2
            para["sku"] = "49-03000-007"
            self.logger.info("%s的设备模式修改为%s" % (sn, deviceModel))
            return para
        else:
            self.logger.error("参数错误，请检查配置！")

    def send_request_modifyDeviceModel(self,url,data):
        '''
        :param url:
        :param data:
        :return:
        '''
        headers = {"Content-Type": "application/json"}
        self.logger.info("请求的参数为:%s" %data)
        r = requests.post(url, data=json.dumps(data), headers=headers)
        self.logger.info("返回的数据为:%s" % json.loads(r.text))
        return json.loads(r.text)

if __name__ == "__main__":
    oc = modifyDeviceModel()
    time = base.get_millisecond()
    env = "uat"
    lang = "zh"
    token = "487d7821-2ef3-427c-91ed-3ddd3e5e8ef7"
    sn = "e4937a14f91c05a3"
    DeviceModel = "购买"

    url = oc.get_modifyDeviceModel_url(env,token,lang,time)

    data = oc.get_data_modifyDeviceModel(sn,DeviceModel)
    oc.send_request_modifyDeviceModel(url,data)

    # print(result["data"])
    # print(type(result["data"]))

