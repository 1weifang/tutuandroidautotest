#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/12/26 14:25
# @Author  : Durat
# @Email   : durant.zeng@sunvalley.com.cn
# @File    : test_case_queryTopicList4Fr.py
# @Software: PyCharm

import sys, os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
import unittest
from common.FileParsing import FileParser
from common.baseUtil import baseUtils
from interface.base.login.authentication import Authentication
from interface.tutu.UGC.topic.queryTopicList4Fr import queryTopicList4Fr
from common.excelUtil import excelUtil


class TestqueryTopicList4FrFunc(unittest.TestCase):
    """Test queryTopicList4Fr.py"""

    def setUp(self):
        self.base = baseUtils()
        self.projectPath = self.base.getProjectPath() + os.sep + "config" + os.sep + "config.ini"
        self.testData = self.base.getProjectPath() + os.sep + "config" + os.sep + "AnjouTestCase.xls"
        self.config = FileParser(self.projectPath)
        self.AC = Authentication()
        self.ex = excelUtil()
        self.queryTopic = queryTopicList4Fr()

    def test_queryTopicList4Fr_Android_ch_001(self):
        '''美甲涂涂端_ugc话题-查列表4Fr_searchTitle不传_zh_Android_正常查询_手机号密码登录'''
        # 账号密码登录
        TestData = self.ex.getDict(2, 29, 7, self.testData)
        currentPage = TestData["currentPage"]
        pageSize = TestData["pageSize"]

        phone = TestData["phone"]
        password = TestData["password"]
        data = self.AC.get_Android_CN_logged_in(phone, password)

        pad_login_url_ch = self.AC.get_AuthenticationURL(self.config.get('imi_base_url_ch', 'base_url_dev_k8s'),self.config.get("imi_login_url","login_url"),self.config.get("lang", "zh"),self.base.getTimeStamp(),self.config.get("clientVersionInfo", "clientVersionInfo_ch_Android"))

        access_token = self.AC.get_Access_token(pad_login_url_ch,data)

        self.assertIsNotNone(access_token)

        #话题列表查询
        queryTopicURL = self.queryTopic.get_queryTopicList4FrURL(self.config.get('imi_base_url_ch', 'base_url_dev_k8s'),
                                                  self.config.get("UGC", "queryTopicList4FrURL"), self.config.get("lang", "zh"),
                                                  self.base.getTimeStamp(),
                                                  self.config.get("clientVersionInfo", "clientVersionInfo_ch_Android"),access_token)


        result_queryTopic = self.queryTopic.send_request_queryTopicList4Fr(queryTopicURL)
        self.assertEqual(result_queryTopic["stateCode"], 200)
        self.assertEqual(result_queryTopic["stateMsg"], "OK")



    def test_queryTopicList4Fr_Android_ch_002(self):
        '''美甲涂涂端_ugc话题-查列表4Fr_searchTitle传_zh_Android_正常查询_手机号密码登录'''
        # 账号密码登录
        TestData = self.ex.getDict(2, 29, 7, self.testData)
        currentPage = TestData["currentPage"]
        pageSize = TestData["pageSize"]

        phone = TestData["phone"]
        password = TestData["password"]
        data = self.AC.get_Android_CN_logged_in(phone, password)

        pad_login_url_ch = self.AC.get_AuthenticationURL(self.config.get('imi_base_url_ch', 'base_url_dev_k8s'),self.config.get("imi_login_url","login_url"),self.config.get("lang", "zh"),self.base.getTimeStamp(),self.config.get("clientVersionInfo", "clientVersionInfo_ch_Android"))

        access_token = self.AC.get_Access_token(pad_login_url_ch,data)

        self.assertIsNotNone(access_token)

        #话题列表查询
        queryTopicURL = self.queryTopic.get_queryTopicList4FrURL(self.config.get('imi_base_url_ch', 'base_url_dev_k8s'),
                                                  self.config.get("UGC", "queryTopicList4FrURL"), self.config.get("lang", "zh"),
                                                  self.base.getTimeStamp(),
                                                  self.config.get("clientVersionInfo", "clientVersionInfo_ch_Android"),access_token)

        searchTitle = self.base.get_random_string(4)
        result_queryTopic = self.queryTopic.send_request_queryTopicList4Fr(queryTopicURL,searchTitle)
        self.assertEqual(result_queryTopic["stateCode"], 200)
        self.assertEqual(result_queryTopic["stateMsg"], "OK")


    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
