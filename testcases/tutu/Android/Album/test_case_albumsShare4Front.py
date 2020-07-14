#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/9/10 11:27
# @Author  : Durat
# @Email   : durant.zeng@sunvalley.com.cn
# @File    : test_case_albumsShare4Front.py
# @Software: PyCharm

import sys, os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
import unittest
import random
from common.FileParsing import FileParser
from common.baseUtil import baseUtils
from interface.base.login.authentication import Authentication
from interface.tutu.Album.getAlbumsList4Front import getAlbumsList4Front
from interface.tutu.Album.albumsShare4Front import albumsShare4Front
from common.excelUtil import excelUtil


class TestalbumsShare4FrontFunc(unittest.TestCase):
    """Test albumsShare4Front.py"""

    def setUp(self):
        self.base = baseUtils()
        self.projectPath = self.base.getProjectPath() + os.sep + "config" + os.sep + "config.ini"
        self.testData = self.base.getProjectPath() + os.sep + "config" + os.sep + "AnjouTestCase.xls"
        self.config = FileParser(self.projectPath)
        self.AC = Authentication()
        self.ex = excelUtil()
        self.ListQuery = getAlbumsList4Front()
        self.share = albumsShare4Front()



    def test_albumsShare4Front_tutu_Android_001(self):
        '''美甲涂涂移动Android端_特辑分享_微信_手机号密码登录_001'''
        #登录
        TestData = self.ex.getDict(2, 31, 7, self.testData)
        currentPage = TestData["currentPage"]
        pageSize = TestData["pageSize"]

        phone = TestData["phone"]
        password = TestData["password"]
        data = self.AC.get_Android_CN_logged_in(phone, password)

        pad_login_url_ch = self.AC.get_AuthenticationURL(self.config.get('imi_base_url_ch', 'base_url_dev_k8s'),self.config.get("imi_login_url","login_url"),self.config.get("lang", "zh"),self.base.getTimeStamp(),self.config.get("clientVersionInfo", "clientVersionInfo_ch_Android"))

        access_token = self.AC.get_Access_token(pad_login_url_ch,data)

        self.assertIsNotNone(access_token)

        #特辑列表
        ListQueryURL = self.ListQuery.get_getAlbumsList4FrontURL(self.config.get('imi_base_url_ch', 'base_url_dev_k8s'),
                                                  self.config.get("imi_cms_url", "getAlbumsList4FrontURL"), self.config.get("lang", "zh"),
                                                  self.base.getTimeStamp(),
                                                  self.config.get("clientVersionInfo", "clientVersionInfo_ch_Android"),access_token)


        result_ListQuery = self.ListQuery.send_request_getAlbumsList4Front(ListQueryURL,currentPage,pageSize)


        self.assertEqual(result_ListQuery["stateCode"], 200)
        self.assertEqual(result_ListQuery["stateMsg"], "OK")
        self.assertIsNotNone(result_ListQuery["data"])

        # 随机获取一个特辑ID，作为特辑详情的参数
        albumsId = random.choice(result_ListQuery["data"])["albumsId"]
        shareType = TestData["shareType"]
        shareWay = TestData["shareWay"]
        shareURL = self.share.get_albumsShare4FrontURL(self.config.get('imi_base_url_ch', 'base_url_dev_k8s'),
                                                  self.config.get("imi_cms_url", "albumsShare4FrontURL"), self.config.get("lang", "zh"),
                                                  self.base.getTimeStamp(),
                                                  self.config.get("clientVersionInfo", "clientVersionInfo_ch_Android"),access_token)

        result_share = self.share.send_request_albumsShare4Front(shareURL,shareType,shareWay,albumsId)

        self.assertEqual(result_share["stateCode"], 200)
        self.assertEqual(result_share["stateMsg"], "OK")




    def test_albumsShare4Front_tutu_Android_002(self):
        '''美甲涂涂移动Android端_特辑分享_微博_手机号密码登录_002'''
        # 登录
        TestData = self.ex.getDict(2, 32, 7, self.testData)
        currentPage = TestData["currentPage"]
        pageSize = TestData["pageSize"]

        phone = TestData["phone"]
        password = TestData["password"]
        data = self.AC.get_Android_CN_logged_in(phone, password)

        pad_login_url_ch = self.AC.get_AuthenticationURL(self.config.get('imi_base_url_ch', 'base_url_dev_k8s'),self.config.get("imi_login_url","login_url"),self.config.get("lang", "zh"),self.base.getTimeStamp(),self.config.get("clientVersionInfo", "clientVersionInfo_ch_Android"))

        access_token = self.AC.get_Access_token(pad_login_url_ch,data)

        self.assertIsNotNone(access_token)

        # 特辑列表
        ListQueryURL = self.ListQuery.get_getAlbumsList4FrontURL(self.config.get('imi_base_url_ch', 'base_url_dev_k8s'),
                                                  self.config.get("imi_cms_url", "getAlbumsList4FrontURL"), self.config.get("lang", "zh"),
                                                  self.base.getTimeStamp(),
                                                  self.config.get("clientVersionInfo", "clientVersionInfo_ch_Android"),access_token)


        result_ListQuery = self.ListQuery.send_request_getAlbumsList4Front(ListQueryURL,currentPage,pageSize)

        # 第八步，断言返回的数据是否正确
        self.assertEqual(result_ListQuery["stateCode"], 200)
        self.assertEqual(result_ListQuery["stateMsg"], "OK")
        self.assertIsNotNone(result_ListQuery["data"])

        # 获取第一个特辑ID，作为特辑详情的参数
        albumsId = random.choice(result_ListQuery["data"])["albumsId"]
        shareType = TestData["shareType"]
        shareWay = TestData["shareWay"]
        shareURL = self.share.get_albumsShare4FrontURL(self.config.get('imi_base_url_ch', 'base_url_dev_k8s'),
                                                  self.config.get("imi_cms_url", "albumsShare4FrontURL"), self.config.get("lang", "zh"),
                                                  self.base.getTimeStamp(),
                                                  self.config.get("clientVersionInfo", "clientVersionInfo_ch_Android"),access_token)
        result_share = self.share.send_request_albumsShare4Front(shareURL,shareType,shareWay,albumsId)

        self.assertEqual(result_share["stateCode"], 200)
        self.assertEqual(result_share["stateMsg"], "OK")



    def test_albumsShare4Front_tutu_Android_003(self):
        '''美甲涂涂移动Android端_特辑分享_QQ_手机号密码登录_003'''
        #登录
        TestData = self.ex.getDict(2, 33, 7, self.testData)
        currentPage = TestData["currentPage"]
        pageSize = TestData["pageSize"]

        phone = TestData["phone"]
        password = TestData["password"]
        data = self.AC.get_Android_CN_logged_in(phone, password)

        pad_login_url_ch = self.AC.get_AuthenticationURL(self.config.get('imi_base_url_ch', 'base_url_dev_k8s'),self.config.get("imi_login_url","login_url"),self.config.get("lang", "zh"),self.base.getTimeStamp(),self.config.get("clientVersionInfo", "clientVersionInfo_ch_Android"))

        access_token = self.AC.get_Access_token(pad_login_url_ch,data)

        self.assertIsNotNone(access_token)

        #特辑列表
        ListQueryURL = self.ListQuery.get_getAlbumsList4FrontURL(self.config.get('imi_base_url_ch', 'base_url_dev_k8s'),
                                                  self.config.get("imi_cms_url", "getAlbumsList4FrontURL"), self.config.get("lang", "zh"),
                                                  self.base.getTimeStamp(),
                                                  self.config.get("clientVersionInfo", "clientVersionInfo_ch_Android"),access_token)

        result_ListQuery = self.ListQuery.send_request_getAlbumsList4Front(ListQueryURL,currentPage,pageSize)

        self.assertEqual(result_ListQuery["stateCode"], 200)
        self.assertEqual(result_ListQuery["stateMsg"], "OK")
        self.assertIsNotNone(result_ListQuery["data"])

        # 随机获取一个特辑ID，作为特辑详情的参数
        albumsId = random.choice(result_ListQuery["data"])["albumsId"]
        shareType = TestData["shareType"]
        shareWay = TestData["shareWay"]
        shareURL = self.share.get_albumsShare4FrontURL(self.config.get('imi_base_url_ch', 'base_url_dev_k8s'),
                                                  self.config.get("imi_cms_url", "albumsShare4FrontURL"), self.config.get("lang", "zh"),
                                                  self.base.getTimeStamp(),
                                                  self.config.get("clientVersionInfo", "clientVersionInfo_ch_Android"),access_token)

        result_share = self.share.send_request_albumsShare4Front(shareURL,shareType,shareWay,albumsId)

        self.assertEqual(result_share["stateCode"], 200)
        self.assertEqual(result_share["stateMsg"], "OK")


    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
