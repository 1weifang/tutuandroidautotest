#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/11/19 10:33
# @Author  : Durat
# @Email   : durant.zeng@sunvalley.com.cn
# @File    : test_case_queryNailSuit4AlbumsCombine.py
# @Software: PyCharm

import sys, os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
import random
import unittest
from common.FileParsing import FileParser
from common.baseUtil import baseUtils
from interface.base.login.authentication import Authentication
from interface.tutu.Album.getAlbumsList4Front import getAlbumsList4Front
from interface.tutu.AITest.v1.app.queryNailSuit4AlbumsCombine import queryNailSuit4AlbumsCombine
from common.excelUtil import excelUtil


class TestqueryNailSuit4AlbumsCombineFunc(unittest.TestCase):
    """Test queryNailSuit4AlbumsCombine.py"""

    def setUp(self):
        self.base = baseUtils()
        self.projectPath = self.base.getProjectPath() + os.sep + "config" + os.sep + "config.ini"
        self.testData = self.base.getProjectPath() + os.sep + "config" + os.sep + "AnjouTestCase.xls"
        self.config = FileParser(self.projectPath)
        self.AC = Authentication()
        self.ex = excelUtil()
        self.getAlbumsList = getAlbumsList4Front()
        self.queryNailSuit = queryNailSuit4AlbumsCombine()

    @unittest.skip("调试")
    def test_queryNailSuit4AlbumsCombine_tutu_Android_001(self):
        '''美甲涂涂移动Android端_v1_Ai试甲-查指定特辑套图和普通套图列表_正常查询_手机号密码登录_001'''
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


        #Ai试甲-查指定特辑套图和普通套图列表
        queryNailSuitURL = self.queryNailSuit.get_queryNailSuit4AlbumsCombineURL(self.config.get('imi_base_url_ch', 'base_url_prod'),
                                                  self.config.get("AI", "queryNailSuit4AlbumsCombineURL"), self.config.get("lang", "zh"),
                                                  self.base.getTimeStamp(),
                                                  self.config.get("clientVersionInfo", "clientVersionInfo_ch_Android"),access_token)


        result_queryNailSuit = self.queryNailSuit.send_request_queryNailSuit4AlbumsCombine(queryNailSuitURL,albumsId,currentPage,pageSize)


        self.assertEqual(result_queryNailSuit["stateCode"], 200)
        self.assertEqual(result_queryNailSuit["stateMsg"], "OK")
        self.assertEqual(result_queryNailSuit["data"]["nailSuit4Ablums"]["albumsId"],albumsId)


    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()

