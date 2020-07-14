#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/12/26 15:35
# @Author  : Durat
# @Email   : durant.zeng@sunvalley.com.cn
# @File    : test_case_queryArticleListByTag4Fr.py
# @Software: PyCharm


import sys, os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
import unittest
import time
from random import choice
from common.FileParsing import FileParser
from common.baseUtil import baseUtils
from interface.base.login.authentication import Authentication
from interface.tutu.UGC.Tag.querySearchTagList4Fr import querySearchTagList4Fr
from interface.tutu.UGC.Tag.queryArticleListByTag4Fr import queryArticleListByTag4Fr
from common.excelUtil import excelUtil


class TestqueryArticleListByTag4FrFunc(unittest.TestCase):
    """Test queryArticleListByTag4Fr.py"""

    def setUp(self):
        self.base = baseUtils()
        self.projectPath = self.base.getProjectPath() + os.sep + "config" + os.sep + "config.ini"
        self.testData = self.base.getProjectPath() + os.sep + "config" + os.sep + "AnjouTestCase.xls"
        self.config = FileParser(self.projectPath)
        self.AC = Authentication()
        self.ex = excelUtil()
        self.TagList = querySearchTagList4Fr()
        self.queryArticleListByTag = queryArticleListByTag4Fr()


    def test_queryArticleListByTag4Fr_tutu_Android_001(self):
        '''美甲涂涂移动Android端_queryArticleListByTag4Fr_ugc搜索出列表by标签4Fr_搜内容_已有标签随机查询_001'''
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


        #标签列表查询
        TagListURL = self.TagList.get_querySearchTagList4FrURL(self.config.get('imi_base_url_ch', 'base_url_dev_k8s'),
                                                  self.config.get("UGC", "querySearchTagList4FrURL"), self.config.get("lang", "zh"),
                                                  self.base.getTimeStamp(),
                                                  self.config.get("clientVersionInfo", "clientVersionInfo_ch_Android"),access_token)
        time.sleep(0.5)
        result_TagList = self.TagList.send_request_querySearchTagList4Fr(TagListURL)

        self.assertEqual(result_TagList["stateCode"], 200)
        self.assertEqual(result_TagList["stateMsg"], "OK")

        #随机选取标签名字
        searchContent = choice(result_TagList["data"])["tagName"]

        #ugc搜索出列表by标签4Fr
        queryArticleListByTagURL = self.queryArticleListByTag.get_queryArticleListByTag4FrURL(self.config.get('imi_base_url_ch', 'base_url_dev_k8s'),
                                                  self.config.get("UGC", "queryArticleListByTag4FURL"), self.config.get("lang", "zh"),
                                                  self.base.getTimeStamp(),
                                                self.config.get("clientVersionInfo", "clientVersionInfo_ch_Android"),access_token)
        searchType = 1
        time.sleep(1)
        result_queryArticleListByTag = self.queryArticleListByTag.send_request_queryArticleListByTag4Fr(queryArticleListByTagURL,searchContent,currentPage,pageSize,searchType)

        self.assertEqual(result_queryArticleListByTag["stateCode"], 200)
        self.assertEqual(result_queryArticleListByTag["stateMsg"], "OK")


    def test_queryArticleListByTag4Fr_tutu_Android_002(self):
        '''美甲涂涂移动Android端_queryArticleListByTag4Fr_ugc搜索出列表by标签4Fr_搜内容_随机产生字符串_002'''
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


        #标签列表查询
        TagListURL = self.TagList.get_querySearchTagList4FrURL(self.config.get('imi_base_url_ch', 'base_url_dev_k8s'),
                                                  self.config.get("UGC", "querySearchTagList4FrURL"), self.config.get("lang", "zh"),
                                                  self.base.getTimeStamp(),
                                                  self.config.get("clientVersionInfo", "clientVersionInfo_ch_Android"),access_token)
        time.sleep(0.5)
        result_TagList = self.TagList.send_request_querySearchTagList4Fr(TagListURL)

        self.assertEqual(result_TagList["stateCode"], 200)
        self.assertEqual(result_TagList["stateMsg"], "OK")

        #随机生成字符串
        searchContent = self.base.get_random_string(4)

        #ugc搜索出列表by标签4Fr
        queryArticleListByTagURL = self.queryArticleListByTag.get_queryArticleListByTag4FrURL(self.config.get('imi_base_url_ch', 'base_url_dev_k8s'),
                                                  self.config.get("UGC", "queryArticleListByTag4FURL"), self.config.get("lang", "zh"),
                                                  self.base.getTimeStamp(),
                                                  self.config.get("clientVersionInfo", "clientVersionInfo_ch_Android"),access_token)
        searchType = 1
        time.sleep(1)
        result_queryArticleListByTag = self.queryArticleListByTag.send_request_queryArticleListByTag4Fr(queryArticleListByTagURL,searchContent,currentPage,pageSize,searchType)

        self.assertEqual(result_queryArticleListByTag["stateCode"], 200)
        self.assertEqual(result_queryArticleListByTag["stateMsg"], "OK")


    def test_queryArticleListByTag4Fr_tutu_Android_003(self):
        '''美甲涂涂移动Android端_queryArticleListByTag4Fr_ugc搜索出列表by标签4Fr_搜用户_随机产生字符串_003'''
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


        #标签列表查询
        TagListURL = self.TagList.get_querySearchTagList4FrURL(self.config.get('imi_base_url_ch', 'base_url_dev_k8s'),
                                                  self.config.get("UGC", "querySearchTagList4FrURL"), self.config.get("lang", "zh"),
                                                  self.base.getTimeStamp(),
                                                  self.config.get("clientVersionInfo", "clientVersionInfo_ch_Android"),access_token)
        time.sleep(0.5)
        result_TagList = self.TagList.send_request_querySearchTagList4Fr(TagListURL)

        self.assertEqual(result_TagList["stateCode"], 200)
        self.assertEqual(result_TagList["stateMsg"], "OK")

        #随机生成字符串
        searchContent = self.base.get_random_string(4)

        #ugc搜索出列表by标签4Fr
        queryArticleListByTagURL = self.queryArticleListByTag.get_queryArticleListByTag4FrURL(self.config.get('imi_base_url_ch', 'base_url_dev_k8s'),
                                                  self.config.get("UGC", "queryArticleListByTag4FURL"), self.config.get("lang", "zh"),
                                                  self.base.getTimeStamp(),
                                                  self.config.get("clientVersionInfo", "clientVersionInfo_ch_Android"),access_token)
        searchType = 2
        time.sleep(1)
        result_queryArticleListByTag = self.queryArticleListByTag.send_request_queryArticleListByTag4Fr(queryArticleListByTagURL,searchContent,currentPage,pageSize,searchType)

        self.assertEqual(result_queryArticleListByTag["stateCode"], 200)
        self.assertEqual(result_queryArticleListByTag["stateMsg"], "OK")

    def test_queryArticleListByTag4Fr_Android_ch_004(self):
        '''美甲涂涂移动Android端_queryArticleListByTag4Frugc搜索出列表by标签4Fr_搜内容_字符串不能大于30_004'''
        # 账号密码登录
        TestData = self.ex.getDict(2, 29, 7, self.testData)
        currentPage = TestData["currentPage"]
        pageSize = TestData["pageSize"]

        phone = TestData["phone"]
        password = TestData["password"]
        data = self.AC.get_Android_CN_logged_in(phone, password)

        pad_login_url_ch = self.AC.get_AuthenticationURL(self.config.get('imi_base_url_ch', 'base_url_dev_k8s'),
                                                         self.config.get("imi_login_url", "login_url"),
                                                         self.config.get("lang", "zh"), self.base.getTimeStamp(),
                                                         self.config.get("clientVersionInfo",
                                                                         "clientVersionInfo_ch_Android"))

        access_token = self.AC.get_Access_token(pad_login_url_ch, data)

        self.assertIsNotNone(access_token)

        # 标签列表查询
        TagListURL = self.TagList.get_querySearchTagList4FrURL(self.config.get('imi_base_url_ch', 'base_url_dev_k8s'),
                                                               self.config.get("UGC", "querySearchTagList4FrURL"),
                                                               self.config.get("lang", "zh"),
                                                               self.base.getTimeStamp(),
                                                               self.config.get("clientVersionInfo",
                                                                               "clientVersionInfo_ch_Android"),
                                                               access_token)
        time.sleep(0.5)
        result_TagList = self.TagList.send_request_querySearchTagList4Fr(TagListURL)

        self.assertEqual(result_TagList["stateCode"], 200)
        self.assertEqual(result_TagList["stateMsg"], "OK")

        # 31字符串
        searchContent = self.base.get_random_string(10)*3 + "1"

        # ugc搜索出列表by标签4Fr
        queryArticleListByTagURL = self.queryArticleListByTag.get_queryArticleListByTag4FrURL(
            self.config.get('imi_base_url_ch', 'base_url_dev_k8s'),
            self.config.get("UGC", "queryArticleListByTag4FURL"), self.config.get("lang", "zh"),
            self.base.getTimeStamp(),
            self.config.get("clientVersionInfo", "clientVersionInfo_ch_Android"), access_token)
        searchType = 1
        time.sleep(1)
        result_queryArticleListByTag = self.queryArticleListByTag.send_request_queryArticleListByTag4Fr(
            queryArticleListByTagURL, searchContent, currentPage, pageSize, searchType)

        self.assertEqual(result_queryArticleListByTag["status"], 400)




    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()

