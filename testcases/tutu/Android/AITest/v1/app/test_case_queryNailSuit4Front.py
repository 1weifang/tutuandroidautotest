#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/11/19 9:54
# @Author  : Durat
# @Email   : durant.zeng@sunvalley.com.cn
# @File    : test_case_queryNailSuit4Front.py
# @Software: PyCharm

import sys, os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
import unittest
from common.FileParsing import FileParser
from common.baseUtil import baseUtils
from interface.base.login.authentication import Authentication
from interface.tutu.AITest.v1.app.queryNailSuit4Front import queryNailSuit4Front
from common.excelUtil import excelUtil


class TestqueryNailSuit4FrontFunc(unittest.TestCase):
    """Test queryNailSuit4Front.py"""

    def setUp(self):
        self.base = baseUtils()
        self.projectPath = self.base.getProjectPath() + os.sep + "config" + os.sep + "config.ini"
        self.testData = self.base.getProjectPath() + os.sep + "config" + os.sep + "AnjouTestCase.xls"
        self.config = FileParser(self.projectPath)
        self.AC = Authentication()
        self.ex = excelUtil()
        self.queryNailSuit = queryNailSuit4Front()


    def test_queryNailSuit4Front_tutu_Android_001(self):
        '''美甲涂涂移动Android端_v1_AI试甲-查发布的普通套图列表_正常查询_手机号密码登录_001'''
        # 登录
        # TestData = self.ex.getDict(2, 25, 7, self.testData)
        currentPage = "1"
        pageSize = "15"

        phone = "13417335080"
        password = "123456"
        data = self.AC.get_Android_CN_logged_in(phone, password)

        test = self.config.get('imi_base_url_ch', 'base_url_dev_k8s')
        print(test)
        app_login_url_ch = self.AC.get_AuthenticationURL(self.config.get('imi_base_url_ch', 'base_url_dev_k8s'),self.config.get("imi_login_url","login_url"),self.config.get("lang", "zh"),self.base.getTimeStamp(),self.config.get("clientVersionInfo", "clientVersionInfo_ch_Android"))
        access_token = self.AC.get_Access_token(app_login_url_ch,data)

        self.assertIsNotNone(access_token)

        #AI试甲-查发布的普通套图列表
        queryNailSuitURL = self.queryNailSuit.get_queryNailSuit4FrontURL(self.config.get('imi_base_url_ch', 'base_url_dev_k8s'),
                                                  self.config.get("AI", "queryNailSuit4FrontURL"), self.config.get("lang", "zh"),
                                                  self.base.getTimeStamp(),
                                                  self.config.get("clientVersionInfo", "clientVersionInfo_ch_Android"),access_token)


        result_queryNailSuit = self.queryNailSuit.send_request_queryNailSuit4Front(queryNailSuitURL,currentPage,pageSize)


        self.assertEqual(result_queryNailSuit["stateCode"], 200)
        self.assertEqual(result_queryNailSuit["stateMsg"], "OK")


    def test_queryNailSuit4Front_tutu_Android_002(self):
        '''美甲涂涂移动Android端_v1_AI试甲-查发布的普通套图列表_正常查询_鉴权登录_002'''
        # 登录
        # TestData = self.ex.getDict(2, 25, 7, self.testData)
        currentPage = "1"
        pageSize = "15"

        phone = "13417335080"
        password = "123456"
        data = self.AC.get_Android_CN_Not_logged_in()

        app_login_url_ch = self.AC.get_AuthenticationURL(self.config.get('imi_base_url_ch', 'base_url_dev_k8s'),self.config.get("imi_login_url","login_url"),self.config.get("lang", "zh"),self.base.getTimeStamp(),self.config.get("clientVersionInfo", "clientVersionInfo_ch_Android"))
        access_token = self.AC.get_Access_token(app_login_url_ch,data)

        self.assertIsNotNone(access_token)

        #AI试甲-查发布的普通套图列表
        queryNailSuitURL = self.queryNailSuit.get_queryNailSuit4FrontURL(self.config.get('imi_base_url_ch', 'base_url_dev_k8s'),
                                                  self.config.get("AI", "queryNailSuit4FrontURL"), self.config.get("lang", "zh"),
                                                  self.base.getTimeStamp(),
                                                  self.config.get("clientVersionInfo", "clientVersionInfo_ch_Android"),access_token)


        result_queryNailSuit = self.queryNailSuit.send_request_queryNailSuit4Front(queryNailSuitURL,currentPage,pageSize)


        self.assertEqual(result_queryNailSuit["stateCode"], 200)
        self.assertEqual(result_queryNailSuit["stateMsg"], "OK")


    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()