#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/9/9 11:01
# @Author  : Durat
# @Email   : durant.zeng@sunvalley.com.cn
# @File    : test_case_getPicList4HotMi.py
# @Software: PyCharm

import sys, os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
import unittest
from common.FileParsing import FileParser
from common.baseUtil import baseUtils
from interface.base.login.authentication import Authentication
from interface.tutu.gallery.getPicList4HotMi import getPicList4HotMi
from common.excelUtil import excelUtil




class TestgetPicList4HotMiFunc(unittest.TestCase):
    """Test getPicList4HotMi.py"""

    def setUp(self):
        self.base = baseUtils()
        self.projectPath = self.base.getProjectPath() + os.sep + "config" + os.sep + "config.ini"
        self.testData = self.base.getProjectPath() + os.sep + "config" + os.sep + "AnjouTestCase.xls"
        self.config = FileParser(self.projectPath)
        self.AC = Authentication()
        self.ex = excelUtil()
        self.Recommendations = getPicList4HotMi()


    def test_getPicList4HotMi_tutu_Android_001(self):
        '''美甲涂涂移动Android端_热门推荐_正常查询_手机号密码登录_001'''
        # 登录
        TestData = self.ex.getDict(2, 3, 7, self.testData)
        currentPage = TestData["currentPage"]
        pageSize = TestData["pageSize"]
        allNailSuitFlag = TestData["allNailSuitFlag"]

        phone = TestData["phone"]
        password = TestData["password"]
        data = self.AC.get_Android_CN_logged_in(phone, password)

        pad_login_url_ch = self.AC.get_AuthenticationURL(self.config.get('imi_base_url_ch', 'base_url_dev_k8s'),self.config.get("imi_login_url","login_url"),self.config.get("lang", "zh"),self.base.getTimeStamp(),self.config.get("clientVersionInfo", "clientVersionInfo_ch_Android"))
        access_token = self.AC.get_Access_token(pad_login_url_ch,data)

        self.assertIsNotNone(access_token)

        # 热门推荐
        RecommendationsURL = self.Recommendations.get_getPicList4HotMiURL(self.config.get('imi_base_url_ch', 'base_url_dev_k8s'),
                                                  self.config.get("imi_cms_url", "getPicList4HotMiURL"), self.config.get("lang", "zh"),
                                                  self.base.getTimeStamp(),
                                                  self.config.get("clientVersionInfo", "clientVersionInfo_ch_Android"),access_token)


        result = self.Recommendations.send_request_getPicList4HotMi(RecommendationsURL,currentPage,pageSize,allNailSuitFlag)

        self.assertEqual(result["stateCode"], 200)
        self.assertEqual(result["stateMsg"], "OK")


    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
