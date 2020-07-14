#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/11/20 10:10
# @Author  : Durat
# @Email   : durant.zeng@sunvalley.com.cn
# @File    : test_case_queryAiNailSuitAgain4Front.py
# @Software: PyCharm

import sys, os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
import unittest
import random
from common.FileParsing import FileParser
from common.baseUtil import baseUtils
from interface.base.login.authentication import Authentication
from interface.base.fileUpload.common import common
from interface.tutu.Album.getAlbumsList4Front import getAlbumsList4Front
from interface.tutu.AITest.v1.app.queryNailSuit4AlbumsCombine import queryNailSuit4AlbumsCombine
from interface.tutu.AITest.v1.app.queryAiNailSuit4Front import queryAiNailSuit4Front
from interface.tutu.AITest.v1.app.queryAiNailSuitAgain4Front import queryAiNailSuitAgain4Front
from common.excelUtil import excelUtil



class TestqueryAiNailSuitAgain4FrontFunc(unittest.TestCase):
    """Test queryAiNailSuitAgain4Front.py"""

    def setUp(self):
        self.base = baseUtils()
        self.projectPath = self.base.getProjectPath() + os.sep + "config" + os.sep + "config.ini"
        self.testData = self.base.getProjectPath() + os.sep + "config" + os.sep + "AnjouTestCase.xls"
        self.file = self.base.getProjectPath()+os.sep+"testPicture"+os.sep+"AITest"+os.sep+"queryAiNailSuit4Front"+os.sep+"queryAiNailSuit4Front.jpg"
        self.config = FileParser(self.projectPath)
        self.AC = Authentication()
        self.ex = excelUtil()
        self.common = common()
        self.getAlbumsList = getAlbumsList4Front()
        self.queryNailSuit = queryNailSuit4AlbumsCombine()
        self.queryAiNailSuit = queryAiNailSuit4Front()
        self.queryAiNailSuitAgain = queryAiNailSuitAgain4Front()

    @unittest.skip("test")
    def test_queryAiNailSuitAgain4Front_app_ch_001(self):
        '''美甲涂涂端_Ai试甲-非首次，查Ai推荐套图+特辑套图(无)+普通套图_zh_Android_正常查询_手机号密码登录'''
        # 安卓app登录
        TestData = self.ex.getDict(2, 25, 7, self.testData)
        currentPage = TestData["currentPage"]
        pageSize = TestData["pageSize"]
        phone = TestData["phone"]
        password = TestData["password"]
        data = self.AC.get_Android_CN_logged_in(phone, password)

        app_login_url_ch = self.AC.get_AuthenticationURL(self.config.get('imi_base_url_ch', 'base_url_prod'),self.config.get("imi_login_url","login_url"),self.config.get("lang", "zh"),self.base.getTimeStamp(),self.config.get("clientVersionInfo", "clientVersionInfo_ch_Android"))
        access_token = self.AC.get_Access_token(app_login_url_ch,data)

        self.assertIsNotNone(access_token)


        #文件上传通用接口
        filename = "queryAiNailSuit4Front.jpg"
        commonURL = self.common.get_commonURL(self.config.get('imi_base_url_ch', 'base_url_prod'),
                                                  self.config.get("fileUpload", "commonURL"), self.config.get("lang", "zh"),
                                                  self.base.getTimeStamp(),
                                                  self.config.get("clientVersionInfo", "clientVersionInfo"),access_token)

        result_common = self.common.send_request_common(commonURL,filename,self.file)
        self.assertEqual(result_common["stateCode"], 200)
        self.assertEqual(result_common["stateMsg"], "OK")

        inputPicName = result_common["data"]["fileName"]
        AI_CDN = "https://cdn-uat.nailtutu.com"
        inputPicUrl = result_common["data"]["fileUrl"]
        really_inputPicUrl = AI_CDN + inputPicUrl

        #queryAiNailSuit4Front接口
        queryAiNailSuitURL = self.queryAiNailSuit.get_queryAiNailSuit4FrontURL(self.config.get('imi_base_url_ch', 'base_url_prod'),
                                                  self.config.get("AI", "queryAiNailSuit4FrontURL"), self.config.get("lang", "zh"),
                                                  self.base.getTimeStamp(),
                                                  self.config.get("clientVersionInfo", "clientVersionInfo"),access_token)

        inputPicHeight = "1162"
        inputPicWidth = "920"

        result_queryAiNailSuit = self.queryAiNailSuit.send_request_queryAiNailSuit4Front(queryAiNailSuitURL,inputPicName,really_inputPicUrl,inputPicWidth,inputPicHeight,currentPage,pageSize)

        self.assertEqual(result_queryAiNailSuit["stateCode"], 200)
        self.assertEqual(result_queryAiNailSuit["stateMsg"], "OK")

        #queryAiNailSuitAgain4Front接口
        queryAiNailSuitAgainURL = self.queryAiNailSuitAgain.get_queryAiNailSuitAgain4FrontURL(self.config.get('imi_base_url_ch', 'base_url_prod'),
                                                  self.config.get("AI", "queryAiNailSuitAgain4FrontURL"), self.config.get("lang", "zh"),
                                                  self.base.getTimeStamp(),self.config.get("clientVersionInfo", "clientVersionInfo"),access_token)

        nailSuitFlag = result_queryAiNailSuit["data"]["nailSuitFlag"]
        tagList = result_queryAiNailSuit["data"]["tagList"]
        result_queryAiNailSuitAgain = self.queryAiNailSuitAgain.send_request_queryAiNailSuitAgain4Front(queryAiNailSuitAgainURL,tagList,nailSuitFlag,currentPage,pageSize)

        self.assertEqual(result_queryAiNailSuitAgain["stateCode"], 200)
        self.assertEqual(result_queryAiNailSuitAgain["stateMsg"], "OK")

    @unittest.skip("调试")
    def test_queryAiNailSuitAgain4Front_app_ch_002(self):
        '''美甲涂涂端_Ai试甲-非首次，查Ai推荐套图+特辑套图(有)+普通套图_zh_Android_正常查询_手机号密码登录'''
        # 安卓app登录
        TestData = self.ex.getDict(2, 25, 7, self.testData)
        currentPage = TestData["currentPage"]
        pageSize = TestData["pageSize"]

        phone = TestData["phone"]
        password = TestData["password"]
        data = self.AC.get_Android_CN_logged_in(phone, password)

        app_login_url_ch = self.AC.get_AuthenticationURL(self.config.get('imi_base_url_ch', 'base_url_prod'),self.config.get("imi_login_url","login_url"),self.config.get("lang", "zh"),self.base.getTimeStamp(),self.config.get("clientVersionInfo", "clientVersionInfo_ch_Android"))
        access_token = self.AC.get_Access_token(app_login_url_ch,data)

        self.assertIsNotNone(access_token)

        #查询特辑列表
        getAlbumsListURL = self.getAlbumsList.get_getAlbumsList4FrontURL(self.config.get('imi_base_url_ch', 'base_url_prod'),
                                                  self.config.get("imi_cms_url", "getAlbumsList4FrontURL"), self.config.get("lang", "zh"),
                                                  self.base.getTimeStamp(),
                                                  self.config.get("clientVersionInfo", "clientVersionInfo_ch_Android"),access_token)

        result_getAlbumsList = self.getAlbumsList.send_request_getAlbumsList4Front(getAlbumsListURL,currentPage,pageSize)

        self.assertEqual(result_getAlbumsList["stateCode"], 200)
        self.assertEqual(result_getAlbumsList["stateMsg"], "OK")
        self.assertIsNotNone(result_getAlbumsList["data"])

        #过滤出套图状态已设置的特辑
        result_list = self.base.get_nailSuitStatus_for_1(result_getAlbumsList)
        #随机取其中一个特辑
        albumsId = random.choice(result_list)

        #文件上传通用接口
        filename = "queryAiNailSuit4Front.jpg"
        commonURL = self.common.get_commonURL(self.config.get('imi_base_url_ch', 'base_url_prod'),
                                                  self.config.get("fileUpload", "commonURL"), self.config.get("lang", "zh"),
                                                  self.base.getTimeStamp(),
                                                  self.config.get("clientVersionInfo", "clientVersionInfo"),access_token)

        result_common = self.common.send_request_common(commonURL,filename,self.file)
        self.assertEqual(result_common["stateCode"], 200)
        self.assertEqual(result_common["stateMsg"], "OK")

        inputPicName = result_common["data"]["fileName"]
        AI_CDN = "https://cdn-uat.nailtutu.com"
        inputPicUrl = result_common["data"]["fileUrl"]
        really_inputPicUrl = AI_CDN + inputPicUrl

        #queryAiNailSuit4Front接口
        queryAiNailSuitURL = self.queryAiNailSuit.get_queryAiNailSuit4FrontURL(self.config.get('imi_base_url_ch', 'base_url_prod'),
                                                  self.config.get("AI", "queryAiNailSuit4FrontURL"), self.config.get("lang", "zh"),
                                                  self.base.getTimeStamp(),
                                                  self.config.get("clientVersionInfo", "clientVersionInfo"),access_token)

        inputPicHeight = "1162"
        inputPicWidth = "920"
        result_queryAiNailSuit = self.queryAiNailSuit.send_request_queryAiNailSuit4Front(queryAiNailSuitURL,inputPicName,really_inputPicUrl,inputPicWidth,inputPicHeight,currentPage,pageSize,albumsId)

        self.assertEqual(result_queryAiNailSuit["stateCode"], 200)
        self.assertEqual(result_queryAiNailSuit["stateMsg"], "OK")


        #queryAiNailSuitAgain4Front接口
        queryAiNailSuitAgainURL = self.queryAiNailSuitAgain.get_queryAiNailSuitAgain4FrontURL(self.config.get('imi_base_url_ch', 'base_url_prod'),
                                                  self.config.get("AI", "queryAiNailSuitAgain4FrontURL"), self.config.get("lang", "zh"),
                                                  self.base.getTimeStamp(),self.config.get("clientVersionInfo", "clientVersionInfo"),access_token)

        nailSuitFlag = result_queryAiNailSuit["data"]["nailSuitFlag"]
        tagList = result_queryAiNailSuit["data"]["tagList"]
        result_queryAiNailSuitAgain = self.queryAiNailSuitAgain.send_request_queryAiNailSuitAgain4Front(queryAiNailSuitAgainURL,tagList,nailSuitFlag,currentPage,pageSize,albumsId)

        self.assertEqual(result_queryAiNailSuitAgain["stateCode"], 200)
        self.assertEqual(result_queryAiNailSuitAgain["stateMsg"], "OK")






    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()


