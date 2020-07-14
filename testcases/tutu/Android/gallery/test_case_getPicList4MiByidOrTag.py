#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/9/9 11:20
# @Author  : Durat
# @Email   : durant.zeng@sunvalley.com.cn
# @File    : test_case_getPicList4MiByidOrTag.py
# @Software: PyCharm

import sys, os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
import unittest
import random
from common.FileParsing import FileParser
from common.baseUtil import baseUtils
from interface.base.login.authentication import Authentication
from interface.tutu.gallery.getPicList4MiByidOrTag import getPicList4MiByidOrTag
from interface.tutu.gallery.getPicList4HotMi import getPicList4HotMi
from interface.tutu.gallery.getPicDetailForMi import getPicDetailForMi

from common.excelUtil import excelUtil


class TestgetPicList4MiByidOrTagFunc(unittest.TestCase):
    """Test getPicList4MiByidOrTag.py"""

    def setUp(self):
        self.base = baseUtils()
        self.projectPath = self.base.getProjectPath() + os.sep + "config" + os.sep + "config.ini"
        self.testData = self.base.getProjectPath() + os.sep + "config" + os.sep + "AnjouTestCase.xls"
        self.config = FileParser(self.projectPath)
        self.AC = Authentication()
        self.ex = excelUtil()
        self.search = getPicList4MiByidOrTag()
        self.Recommendations = getPicList4HotMi()
        self.getPicDetail = getPicDetailForMi()


    def test_getPicList4MiByidOrTag_tutu_Android_001(self):
        '''美甲涂涂移动Android端_彩绘图库搜索_标签名查询_手机号密码登录_001'''
        # 登录
        TestData = self.ex.getDict(2, 5, 7, self.testData)
        currentPage = TestData["currentPage"]
        pageSize = TestData["pageSize"]
        name = TestData["name"]

        phone = TestData["phone"]
        password = TestData["password"]
        data = self.AC.get_Android_CN_logged_in(phone, password)

        pad_login_url_ch = self.AC.get_AuthenticationURL(self.config.get('imi_base_url_ch', 'base_url_dev_k8s'),self.config.get("imi_login_url","login_url"),self.config.get("lang", "zh"),self.base.getTimeStamp(),self.config.get("clientVersionInfo", "clientVersionInfo_ch_Android"))

        access_token = self.AC.get_Access_token(pad_login_url_ch,data)

        self.assertIsNotNone(access_token)

        #彩绘图库搜索
        searchURL = self.search.get_getPicList4MiByidOrTagURL(self.config.get('imi_base_url_ch', 'base_url_dev_k8s'),
                                                  self.config.get("imi_cms_url", "getPicList4MiByidOrTagURL"), self.config.get("lang", "zh"),
                                                  self.base.getTimeStamp(),
                                                  self.config.get("clientVersionInfo", "clientVersionInfo_ch_Android"),access_token)


        result = self.search.send_request_getPicList4MiByidOrTag(searchURL,currentPage,pageSize,name)

        self.assertEqual(result["stateCode"], 200)
        self.assertEqual(result["stateMsg"], "OK")



    def test_getPicList4MiByidOrTag_tutu_Android_002(self):
        '''美甲涂涂移动Android端_彩绘图库搜索_ID查询_手机号密码登录_002'''
        #登录
        TestData = self.ex.getDict(2, 17, 7, self.testData)
        currentPage = TestData["currentPage"]
        pageSize = TestData["pageSize"]

        phone = TestData["phone"]
        password = TestData["password"]
        data = self.AC.get_Android_CN_logged_in(phone, password)
        pad_login_url_ch = self.AC.get_AuthenticationURL(self.config.get('imi_base_url_ch', 'base_url_dev_k8s'),self.config.get("imi_login_url","login_url"),self.config.get("lang", "zh"),self.base.getTimeStamp(),self.config.get("clientVersionInfo", "clientVersionInfo_ch_Android"))
        access_token = self.AC.get_Access_token(pad_login_url_ch,data)

        self.assertIsNotNone(access_token)

        #热门推荐
        RecommendationsURL = self.Recommendations.get_getPicList4HotMiURL(self.config.get('imi_base_url_ch', 'base_url_dev_k8s'),
                                                  self.config.get("imi_cms_url", "getPicList4HotMiURL"), self.config.get("lang", "zh"),
                                                  self.base.getTimeStamp(),
                                                  self.config.get("clientVersionInfo", "clientVersionInfo_ch_Android"),access_token)
        result_Recommendations = self.Recommendations.send_request_getPicList4HotMi(RecommendationsURL,currentPage,pageSize)

        self.assertEqual(result_Recommendations["stateCode"], 200)
        self.assertEqual(result_Recommendations["stateMsg"], "OK")

        #随机取热门推荐返回的一张图片的ID
        ID = random.choice(result_Recommendations["data"])["id"]
        #定义为系统图库类型
        collectionType = "系统图库"

        #取单张图片详情
        getPicDetailURL = self.getPicDetail.get_getPicDetailForMiURL(self.config.get('imi_base_url_ch', 'base_url_dev_k8s'),
                                                  self.config.get("imi_cms_url", "getPicDetailForMiURL"), self.config.get("lang", "zh"),
                                                  self.base.getTimeStamp(),
                                                  self.config.get("clientVersionInfo", "clientVersionInfo_ch_Android"),access_token)
        result_getPicDetail = self.getPicDetail.send_request_getPicDetailForMi(getPicDetailURL,ID,collectionType)

        self.assertEqual(result_getPicDetail["stateCode"], 200)
        self.assertEqual(result_getPicDetail["stateMsg"], "OK")


        #彩绘图库搜索
        galleryOutId = result_getPicDetail["data"]["galleryOutId"]
        searchURL = self.search.get_getPicList4MiByidOrTagURL(self.config.get('imi_base_url_ch', 'base_url_dev_k8s'),
                                                  self.config.get("imi_cms_url", "getPicList4MiByidOrTagURL"), self.config.get("lang", "zh"),
                                                  self.base.getTimeStamp(),
                                                  self.config.get("clientVersionInfo", "clientVersionInfo_ch_Android"),access_token)


        result_search = self.search.send_request_getPicList4MiByidOrTag(searchURL,currentPage,pageSize,galleryOutId)


        self.assertEqual(result_search["stateCode"], 200)
        self.assertEqual(result_search["stateMsg"], "OK")
        # self.assertEqual(result_search["totalNum"], 1)



    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()


