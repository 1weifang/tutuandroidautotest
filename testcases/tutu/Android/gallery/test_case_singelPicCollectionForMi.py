#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/9/9 15:04
# @Author  : Durat
# @Email   : durant.zeng@sunvalley.com.cn
# @File    : test_case_singelPicCollectionForMi.py
# @Software: PyCharm


import sys, os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
import unittest
import time
import random
from common.FileParsing import FileParser
from common.baseUtil import baseUtils
from interface.base.login.authentication import Authentication
from interface.tutu.gallery.getPicList4HotMi import getPicList4HotMi
from interface.tutu.gallery.getPicDetailForMi import getPicDetailForMi
from interface.tutu.gallery.singelPicCollectionForMi import singelPicCollectionForMi
from interface.tutu.PersonalCenter.myCollection.getMyPicCollectionListIM import getMyPicCollectionListIM
from common.excelUtil import excelUtil


class TestsingelPicCollectionForMiFunc(unittest.TestCase):
    """Test singelPicCollectionForMi.py"""

    def setUp(self):
        self.base = baseUtils()
        self.projectPath = self.base.getProjectPath() + os.sep + "config" + os.sep + "config.ini"
        self.testData = self.base.getProjectPath() + os.sep + "config" + os.sep + "AnjouTestCase.xls"
        self.config = FileParser(self.projectPath)
        self.AC = Authentication()
        self.ex = excelUtil()
        self.Recommendations = getPicList4HotMi()
        self.getPicDetail = getPicDetailForMi()
        self.singelColl = singelPicCollectionForMi()
        self.getMyPicCollectionList = getMyPicCollectionListIM()


    def test_singelPicCollectionForMi_tutu_Android_001(self):
        '''美甲涂涂移动Android端_图片收藏与取消收藏(version2.0)_系统图库_图片收藏_001'''
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
        allNailSuitFlag = ""
        result_Recommendations = self.Recommendations.send_request_getPicList4HotMi(RecommendationsURL,currentPage,pageSize,allNailSuitFlag)

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

        #单图片收藏
        time.sleep(0.3)
        collectStatus = "1"
        collectionType_coll = "1"
        singelCollURL = self.singelColl.get_singelPicCollectionForMiURL(self.config.get('imi_base_url_ch', 'base_url_dev_k8s'),
                                                  self.config.get("imi_cms_url", "singelPicCollectionForMiURL"), self.config.get("lang", "zh"),
                                                  self.base.getTimeStamp(),
                                                  self.config.get("clientVersionInfo", "clientVersionInfo_ch_Android"),access_token)
        result_Collection = self.singelColl.send_request_singelPicCollectionForMi_new(singelCollURL,collectStatus,collectionType_coll,ID)
        self.assertEqual(result_Collection["stateCode"],200)
        self.assertEqual(result_Collection["stateMsg"], "OK")

        #我的收藏-单图列表查询
        collectVersion = "2.0"
        getMyPicCollectionListURL = self.getMyPicCollectionList.get_getMyPicCollectionListIMURL(self.config.get('imi_base_url_ch', 'base_url_dev_k8s'),
                                                  self.config.get("imi_cms_url", "getMyPicCollectionListIMUR"), self.config.get("lang", "zh"),
                                                  self.base.getTimeStamp(),
                                                  self.config.get("clientVersionInfo", "clientVersionInfo_ch_Android"),access_token)
        result_getMyPicCollectionList = self.getMyPicCollectionList.send_request_getMyPicCollectionListIM(getMyPicCollectionListURL,currentPage,pageSize,collectVersion)

        self.assertEqual(result_getMyPicCollectionList["stateCode"],200)
        self.assertEqual(result_getMyPicCollectionList["stateMsg"], "OK")

        time.sleep(0.3)
        #单图片取消收藏
        collectStatus = "0"
        collectionType_coll = "1"
        singelCollURL = self.singelColl.get_singelPicCollectionForMiURL(self.config.get('imi_base_url_ch', 'base_url_dev_k8s'),
                                                  self.config.get("imi_cms_url", "singelPicCollectionForMiURL"), self.config.get("lang", "zh"),
                                                  self.base.getTimeStamp(),
                                                  self.config.get("clientVersionInfo", "clientVersionInfo_ch_Android"),access_token)
        result_Collection = self.singelColl.send_request_singelPicCollectionForMi_new(singelCollURL,collectStatus,collectionType_coll,ID)
        self.assertEqual(result_Collection["stateCode"],200)
        self.assertEqual(result_Collection["stateMsg"], "OK")


    def test_singelPicCollectionForMi_tutu_Android_002(self):
        '''美甲涂涂移动Android端_图片收藏与取消收藏(version2.0)_系统图库_图片取消收藏_002'''
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
        allNailSuitFlag = ""
        result_Recommendations = self.Recommendations.send_request_getPicList4HotMi(RecommendationsURL,currentPage,pageSize,allNailSuitFlag)

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

        #单图片收藏
        time.sleep(0.3)
        collectStatus = "1"
        collectionType_coll = "1"
        singelCollURL = self.singelColl.get_singelPicCollectionForMiURL(self.config.get('imi_base_url_ch', 'base_url_dev_k8s'),
                                                  self.config.get("imi_cms_url", "singelPicCollectionForMiURL"), self.config.get("lang", "zh"),
                                                  self.base.getTimeStamp(),
                                                  self.config.get("clientVersionInfo", "clientVersionInfo_ch_Android"),access_token)
        result_Collection = self.singelColl.send_request_singelPicCollectionForMi_new(singelCollURL,collectStatus,collectionType_coll,ID)
        self.assertEqual(result_Collection["stateCode"],200)
        self.assertEqual(result_Collection["stateMsg"], "OK")

        #我的收藏-单图列表查询
        collectVersion = "2.0"
        getMyPicCollectionListURL = self.getMyPicCollectionList.get_getMyPicCollectionListIMURL(self.config.get('imi_base_url_ch', 'base_url_dev_k8s'),
                                                  self.config.get("imi_cms_url", "getMyPicCollectionListIMUR"), self.config.get("lang", "zh"),
                                                  self.base.getTimeStamp(),
                                                  self.config.get("clientVersionInfo", "clientVersionInfo_ch_Android"),access_token)
        result_getMyPicCollectionList = self.getMyPicCollectionList.send_request_getMyPicCollectionListIM(getMyPicCollectionListURL,currentPage,pageSize,collectVersion)

        self.assertEqual(result_getMyPicCollectionList["stateCode"],200)
        self.assertEqual(result_getMyPicCollectionList["stateMsg"], "OK")

        time.sleep(0.3)
        #单图片取消收藏
        collectStatus = "0"
        collectionType_coll = "1"
        singelCollURL = self.singelColl.get_singelPicCollectionForMiURL(self.config.get('imi_base_url_ch', 'base_url_dev_k8s'),
                                                  self.config.get("imi_cms_url", "singelPicCollectionForMiURL"), self.config.get("lang", "zh"),
                                                  self.base.getTimeStamp(),
                                                  self.config.get("clientVersionInfo", "clientVersionInfo_ch_Android"),access_token)
        result_Collection = self.singelColl.send_request_singelPicCollectionForMi_new(singelCollURL,collectStatus,collectionType_coll,ID)
        self.assertEqual(result_Collection["stateCode"],200)
        self.assertEqual(result_Collection["stateMsg"], "OK")

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()