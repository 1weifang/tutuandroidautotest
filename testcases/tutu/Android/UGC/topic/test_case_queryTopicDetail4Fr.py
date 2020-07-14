#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/12/26 14:39
# @Author  : Durat
# @Email   : durant.zeng@sunvalley.com.cn
# @File    : test_case_queryTopicDetail4Fr.py
# @Software: PyCharm

import sys, os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
import unittest
import time
from common.FileParsing import FileParser
from common.baseUtil import baseUtils
from interface.base.login.authentication import Authentication
from interface.tutu.UGC.topic.queryTopicList4Fr import queryTopicList4Fr
from interface.tutu.UGC.topic.queryTopicDetail4Fr import queryTopicDetail4Fr
from common.excelUtil import excelUtil


class TestqueryTopicDetail4FrFunc(unittest.TestCase):
    """Test queryTopicDetail4Fr.py"""

    def setUp(self):
        self.base = baseUtils()
        self.projectPath = self.base.getProjectPath() + os.sep + "config" + os.sep + "config.ini"
        self.testData = self.base.getProjectPath() + os.sep + "config" + os.sep + "AnjouTestCase.xls"
        self.config = FileParser(self.projectPath)
        self.AC = Authentication()
        self.ex = excelUtil()
        self.queryTopic = queryTopicList4Fr()
        self.queryTopicDetail = queryTopicDetail4Fr()

    def test_queryTopicDetail4Fr_tutu_Android_001(self):
        '''美甲涂涂移动Android端_queryTopicDetail4Fr_ugc话题-查详情4Fr_1-最热_001'''
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

        time.sleep(0.3)
        result_queryTopic = self.queryTopic.send_request_queryTopicList4Fr(queryTopicURL)

        self.assertEqual(result_queryTopic["stateCode"], 200)
        self.assertEqual(result_queryTopic["stateMsg"], "OK")

        #取第一个话题ID
        topicID = result_queryTopic["data"][0]["id"]
        #话题详情查询
        queryTopicDetailURL = self.queryTopicDetail.get_queryTopicDetail4FrURL(self.config.get('imi_base_url_ch', 'base_url_dev_k8s'),
                                                  self.config.get("UGC", "queryTopicDetail4FrURL"), self.config.get("lang", "zh"),
                                                  self.base.getTimeStamp(),
                                                  self.config.get("clientVersionInfo", "clientVersionInfo_ch_Android"),access_token)
        time.sleep(0.3)
        orderBy = 1
        result_queryTopicDetail = self.queryTopicDetail.send_request_queryTopicDetail4Fr(queryTopicDetailURL,topicID,currentPage,pageSize,orderBy)

        self.assertEqual(result_queryTopicDetail["stateCode"], 200)
        self.assertEqual(result_queryTopicDetail["stateMsg"], "OK")


    def test_queryTopicDetail4Fr_tutu_Android_002(self):
        '''美甲涂涂移动Android端_queryTopicDetail4Fr_ugc话题-查详情4Fr_2-最新_002'''
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

        time.sleep(0.3)
        result_queryTopic = self.queryTopic.send_request_queryTopicList4Fr(queryTopicURL)

        self.assertEqual(result_queryTopic["stateCode"], 200)
        self.assertEqual(result_queryTopic["stateMsg"], "OK")

        #取第一个话题ID
        topicID = result_queryTopic["data"][0]["id"]
        #话题详情查询
        queryTopicDetailURL = self.queryTopicDetail.get_queryTopicDetail4FrURL(self.config.get('imi_base_url_ch', 'base_url_dev_k8s'),
                                                  self.config.get("UGC", "queryTopicDetail4FrURL"), self.config.get("lang", "zh"),
                                                  self.base.getTimeStamp(),
                                                  self.config.get("clientVersionInfo", "clientVersionInfo_ch_Android"),access_token)
        time.sleep(0.3)
        orderBy = 2
        result_queryTopicDetail = self.queryTopicDetail.send_request_queryTopicDetail4Fr(queryTopicDetailURL,topicID,currentPage,pageSize,orderBy)

        self.assertEqual(result_queryTopicDetail["stateCode"], 200)
        self.assertEqual(result_queryTopicDetail["stateMsg"], "OK")


    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()