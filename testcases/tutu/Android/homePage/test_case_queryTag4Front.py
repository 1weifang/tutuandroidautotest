#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/3/4 16:02
# @Author  : Durat
# @Email   : durant.zeng@sunvalley.com.cn
# @File    : test_case_queryTag4Front.py
# @Software: PyCharm


import sys,os
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
import unittest
from common.FileParsing import FileParser
from common.baseUtil import baseUtils
from interface.base.login.authentication import Authentication
from interface.tutu.homePage.queryTag4Front import queryTag4Front
from common.excelUtil import excelUtil


class TestqueryTag4FrontFunc(unittest.TestCase):
    """Test queryTag4Front.py"""

    def setUp(self):
        self.base = baseUtils()
        self.projectPath = self.base.getProjectPath() + os.sep + "config" + os.sep + "config.ini"
        self.testData = self.base.getProjectPath() + os.sep + "config" + os.sep + "AnjouTestCase.xls"
        self.config = FileParser(self.projectPath)
        self.AC = Authentication()
        self.ex = excelUtil()
        self.queryTag = queryTag4Front()


    def test_queryTag4Front_tutu_Android_001(self):
        '''美甲涂涂移动Android端_queryTag4Front_获取特辑标签列表_001'''

        #账号密码登录
        TestData = self.ex.getDict(2, 29, 7, self.testData)
        currentPage = TestData["currentPage"]
        pageSize = TestData["pageSize"]

        phone = "13417335080"
        password = TestData["password"]
        data = self.AC.get_Android_CN_logged_in(phone,password)

        anjou_login_url = self.AC.get_AuthenticationURL(self.config.get('imi_base_url_ch', 'base_url_dev_k8s'),self.config.get("imi_login_url","login_url"),self.config.get("lang", "en"),self.base.getTimeStamp(),self.config.get("clientVersionInfo", "clientVersionInfo_en_ios"))

        access_token = self.AC.get_Access_token(anjou_login_url,data)

        self.assertIsNotNone(access_token)

        #queryTag接口
        queryTagURL = self.queryTag.get_queryTag4FrontURL(self.config.get('imi_base_url_ch', 'base_url_dev_k8s'),
                                                  self.config.get("homePage", "queryTag4FrontURL"), self.config.get("lang", "en"),
                                                  self.base.getTimeStamp(),
                                                  self.config.get("clientVersionInfo", "clientVersionInfo_en_ios"),access_token)

        result_coverBanner = self.queryTag.send_request_queryTag4Front(queryTagURL)
        self.assertEqual(result_coverBanner["stateCode"], 200)
        self.assertEqual(result_coverBanner["stateMsg"], "OK")


    def tearDown(self):
            pass

if __name__ == '__main__':
    unittest.main()
