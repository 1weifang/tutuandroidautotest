#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/6/12 14:53
# @Author  : Durat
# @Email   : durant.zeng@sunvalley.com.cn
# @File    : single.py
# @Software: PyCharm
import sys,os
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
import requests
import json
from common.Logger import Logger
import warnings
from retrying import retry

def _result(result):
    return result is None




class single:
    def __init__(self):
        self.logger = Logger(logger="single").getlog()
        warnings.simplefilter("ignore",ResourceWarning)

    def get_singleURL(self, baseurl,url, lang, timeStamp, clientVersionInfo,access_token):
        '''
        :param url:
        :param lang:
        :param timeStamp:
        :param clientVersionInfo:
        :return:
        '''
        singleURL = baseurl+ url + "?lang=%s&timeStamp=%s&clientVersionInfo=%s&access_token=%s" % (lang, timeStamp, clientVersionInfo,access_token)
        self.logger.info("单图片上传接口的URL为:%s" % singleURL)
        return singleURL



    @retry(stop_max_attempt_number=5, wait_random_min=1000, wait_random_max=2000, retry_on_result=_result)
    def send_request_single(self,url,targetid,filename,filepath):
        '''
        :param url:
        :param targetid:
        :param filename:
        :param filepath:
        :return:
        '''
        proportion = False
        files = {"file":(filename,open(filepath,"rb"),"multipart/form-data",{})}
        if targetid == "社区":
            data = {"targetid":"48d1cd1ef8d846d98897cf68f12dba01",
                "sizes":"240x360",
                "proportion":proportion}
        elif targetid == "头像":
            data = {"targetid":"329ad03f9c6c4db59caffbbe3b02e1e6",
                "sizes":"240x360",
                "proportion":proportion}
        elif targetid =="甲面":
            data = {"targetid":"6e9800a33d364c298a9e515ac3a2a9bc",
                "sizes":"240x360",
                "proportion":proportion}
        elif targetid == "DIY":
            data = {"targetid":"cb8b8835e5f84249958f01d1b2f47b07",
                "sizes":"240x360",
                "proportion":proportion}
        elif targetid == "系统":
            data = {"targetid":"4305685b17aa11e9b53f005056ad4128",
                "sizes":"240x360",
                "proportion":proportion}
        else:
            self.logger.error("targetid不存在，请检查配置！")
        self.logger.info("单图片上传的请求参数为%s" %data)
        r = requests.request("post",url,data = data,files=files,timeout=30)
        re = r.text
        josnre = json.loads(re)
        self.logger.info("单图片上传接口的返回值为：%s" %josnre)
        return json.loads(re)
        # pictureDict= {
        #             "galleryName" :josnre["data"]["pictureName"],
        #             "galleryThumbnailUrl" :josnre["data"]["thumbnailPictureUrl"],
        #             "galleryUrl" :josnre["data"]["pictureUrl"]
        #         }
        # return pictureDict



if __name__ == "__main__":
    a = single()

    url = "https://mi-api.nailtutu.com/file/picture-upload/single?lang=zh&timeStamp=20190909200353&clientVersionInfo=android_app_ch_1.0.4&access_token=5d7cb718-38d3-48e6-9435-ec49dcb1985e"

    targetid = "社区"

    filename = "Community.jpg"
    filepath = r"D:\testPicture\Community\Community.jpg"

    a.send_request_single(url,targetid,filename,filepath)
