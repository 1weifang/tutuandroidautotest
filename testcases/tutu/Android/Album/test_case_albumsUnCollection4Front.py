#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/11/15 14:32
# @Author  : Durat
# @Email   : durant.zeng@sunvalley.com.cn
# @File    : test_case_albumsUnCollection4Front.py
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
from interface.tutu.Album.getAlbumsDeatil4Front import getAlbumsDeatil4Front
from interface.tutu.Album.albumsCollection4Front import albumsCollection4Front
from interface.tutu.Album.albumsUnCollection4Front import albumsUnCollection4Front
from common.excelUtil import excelUtil


class TestalbumsUnCollection4FrontFunc(unittest.TestCase):
    """Test albumsUnCollection4Front.py"""

    def setUp(self):
        self.base = baseUtils()
        self.projectPath = self.base.getProjectPath() + os.sep + "config" + os.sep + "config.ini"
        self.testData = self.base.getProjectPath() + os.sep + "config" + os.sep + "AnjouTestCase.xls"
        self.config = FileParser(self.projectPath)
        self.AC = Authentication()
        self.ex = excelUtil()
        self.ListQuery = getAlbumsList4Front()
        self.AlbumsDeatil = getAlbumsDeatil4Front()
        self.albumsCollection = albumsCollection4Front()
        self.albumsUnCollection = albumsUnCollection4Front()


    def test_albumsUnCollection4Front_tutu_Android_001(self):
        '''美甲涂涂移动Android端_特辑取消收藏(2.0)_正常取消收藏_手机号密码登录_001'''
        #登录
        TestData = self.ex.getDict(2, 27, 7, self.testData)
        currentPage = TestData["currentPage"]
        pageSize = TestData["pageSize"]

        phone = TestData["phone"]
        password = TestData["password"]
        data = self.AC.get_Android_CN_logged_in(phone, password)
        pad_login_url_ch = self.AC.get_AuthenticationURL(self.config.get('imi_base_url_ch', 'base_url_dev_k8s'),self.config.get("imi_login_url","login_url"),self.config.get("lang", "zh"),self.base.getTimeStamp(),self.config.get("clientVersionInfo", "clientVersionInfo_ch_Android"))
        access_token = self.AC.get_Access_token(pad_login_url_ch,data)
        self.assertIsNotNone(access_token)

        #获取特辑列表
        ListQueryURL = self.ListQuery.get_getAlbumsList4FrontURL(self.config.get('imi_base_url_ch', 'base_url_dev_k8s'),
                                                  self.config.get("imi_cms_url", "getAlbumsList4FrontURL"), self.config.get("lang", "zh"),
                                                  self.base.getTimeStamp(),
                                                  self.config.get("clientVersionInfo", "clientVersionInfo_ch_Android"),access_token)

        result_ListQuery = self.ListQuery.send_request_getAlbumsList4Front(ListQueryURL,currentPage,pageSize)

        self.assertEqual(result_ListQuery["stateCode"], 200)
        self.assertEqual(result_ListQuery["stateMsg"], "OK")
        self.assertIsNotNone(result_ListQuery["data"])

        # 获取第一个特辑ID，作为特辑详情的参数
        albumsId = random.choice(result_ListQuery["data"])["albumsId"]

        AlbumsDeatilURL = self.AlbumsDeatil.get_getAlbumsDeatil4FrontURL(self.config.get('imi_base_url_ch', 'base_url_dev_k8s'),
                                                  self.config.get("imi_cms_url", "getAlbumsDeatil4FrontURL"), self.config.get("lang", "zh"),
                                                  self.base.getTimeStamp(),
                                                  self.config.get("clientVersionInfo", "clientVersionInfo_ch_Android"),access_token)
        result_AlbumsDeatil = self.AlbumsDeatil.send_request_getAlbumsDeatil4Front(AlbumsDeatilURL,albumsId)

        self.assertEqual(result_AlbumsDeatil["stateCode"], 200)
        self.assertEqual(result_AlbumsDeatil["stateMsg"], "OK")
        self.assertEqual(result_AlbumsDeatil["data"]["albumsId"],albumsId)

        #进行一键收藏
        albumsCollectionURL = self.albumsCollection.get_albumsShare4FrontURL(self.config.get('imi_base_url_ch', 'base_url_dev_k8s'),
                                                  self.config.get("imi_cms_url", "albumsCollection4FrontURL"), self.config.get("lang", "zh"),
                                                  self.base.getTimeStamp(),
                                                  self.config.get("clientVersionInfo", "clientVersionInfo_ch_Android"),access_token)
        result_albumsCollection = self.albumsCollection.send_request_albumsCollection4Front_new(albumsCollectionURL,albumsId)

        self.assertEqual(result_albumsCollection["stateCode"], 200)
        self.assertEqual(result_albumsCollection["stateMsg"], "OK")



        #进行一键取消收藏
        albumsUnCollectionURL = self.albumsUnCollection.get_albumsUnCollection4FrontURL(self.config.get('imi_base_url_ch', 'base_url_dev_k8s'),
                                                  self.config.get("imi_cms_url", "albumsUnCollection4FrontURL"), self.config.get("lang", "zh"),
                                                  self.base.getTimeStamp(),
                                                  self.config.get("clientVersionInfo", "clientVersionInfo_ch_Android"),access_token)
        result_albumsUnCollection = self.albumsUnCollection.send_request_albumsUnCollection4Front_new(albumsUnCollectionURL,albumsId)

        self.assertEqual(result_albumsUnCollection["stateCode"], 200)
        self.assertEqual(result_albumsUnCollection["stateMsg"], "OK")

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
