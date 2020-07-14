#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/6/11 16:46
# @Author  : Durat
# @Email   : durant.zeng@sunvalley.com.cn
# @File    : updateCmsShopInfo.py
# @Software: PyCharm
import sys,os
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
import json
import requests
from common.FileParsing import FileParser
from common.baseUtil import baseUtils
from interface.base.login.authentication import Authentication
from common.Logger import Logger



class updateCmsShopInfo:

    def __init__(self):
        self.logger = Logger(logger="updateCmsShopInfo").getlog()

    def get_updateCmsShopInfoURL(self,baseURL,URL,lang,timeStamp,clientVersionInfo,access_token):
        '''
        :param baseURL:
        :param lang:
        :param timeStamp:
        :param clientVersionInfo:
        :param access_token:
        :return:更新附近店铺信息
        '''
        updateCmsShopInfoURL = baseURL + URL + "?lang=%s&timeStamp=%s&clientVersionInfo=%s&access_token=%s" % (lang, timeStamp, clientVersionInfo,access_token)
        self.logger.info("url为:%s" %updateCmsShopInfoURL)
        return updateCmsShopInfoURL



    def send_request_updateCmsShopInfo(self,url,id,shopName,sn,tel,x,y,province,city,area,address):
        '''
        :param url:
        :param id:
        :param shopName:
        :param sn:
        :param tel:
        :param x:
        :param y:
        :param province:
        :param city:
        :param area:
        :param address:
        :return:
        '''
        headers = {"Content-Type": "application/json"}
        parameters = {
                    "id":id,
                    "shopName":shopName,
                    "sn":sn,
                    "tel": tel,
                    "x": x,
                    "y":y,
                    "province": province,
                    "city": city,
                    "area": area,
                    "address": address
                }
        self.logger.info("请求的参数为:%s" % parameters)
        r = requests.post(url, data=json.dumps(parameters), headers=headers,timeout=30)
        self.logger.info("返回的参数为:%s" % json.loads(r.text))

if __name__ == "__main__":


    imi = updateCmsShopInfo()
    # print(imi)
    phone = "13723746965"
    config0 = FileParser(r'D:\anjouAutoTest\config\Authentication_url.ini')
    dev_AC_URL = config0.get('Authentication', 'dev')
    print(dev_AC_URL)
    config1 = FileParser(r'D:\anjouAutoTest\config\env.ini')
    base = baseUtils()
    clientVersionInfo = config1.get("clientVersionInfo", "clientVersionInfo")
    lang = config1.get("lang", "zh")
    currentTime = base.getTimeStamp()
    AC = Authentication()
    DATA = AC.get_PAD_CN_logged_in(phone)
    url = AC.get_AuthenticationURL(dev_AC_URL, lang, currentTime, clientVersionInfo)

    access_token = AC.get_Access_token(url, DATA)

    config2 = FileParser(r'D:\anjouAutoTest\config\api_url.ini')
    base_url = config2.get("base_url","base_url_dev")



    updateCmsShopInfoURL = config2.get("imi_cms_url","updateCmsShopInfoURL")
    updateCmsShopInfoURL = imi.get_updateCmsShopInfoURL(base_url,updateCmsShopInfoURL,lang,currentTime,clientVersionInfo,access_token)


    id = "155365168c634f9a9a2aae9d9de7fdd7"
    address ="星河world1"
    area = "龙华区"
    city= "深圳市"
    province= "广东省"
    shopName = "星星美甲店1"
    sn= "e4937a14f91c05a3"
    tel="13417335081"
    x = "114.057737 "
    y = "22.604453"

    imi.send_request_updateCmsShopInfo(updateCmsShopInfoURL,id,shopName,sn,tel,x,y,province,city,area,address)