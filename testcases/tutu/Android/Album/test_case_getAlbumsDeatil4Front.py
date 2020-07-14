#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/9/10 10:25
# @Author  : Durat
# @Email   : durant.zeng@sunvalley.com.cn
# @File    : test_case_getAlbumsDeatil4Front.py
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
from common.excelUtil import excelUtil




class TestgetAlbumsDeatil4FrontFunc(unittest.TestCase):
    """Test getAlbumsDeatil4Front.py"""

    def setUp(self):
        self.base = baseUtils()
        self.projectPath = self.base.getProjectPath() + os.sep + "config" + os.sep + "config.ini"
        self.testData = self.base.getProjectPath() + os.sep + "config" + os.sep + "AnjouTestCase.xls"
        self.config = FileParser(self.projectPath)
        self.AC = Authentication()
        self.ex = excelUtil()
        self.ListQuery = getAlbumsList4Front()
        self.AlbumsDeatil = getAlbumsDeatil4Front()


    def test_getAlbumsDeatil4Front_tutu_Android_001(self):
        '''美甲涂涂移动Android端_特辑详情_正常查询_手机号密码登录_001'''
        # 登录
        TestData = self.ex.getDict(2, 27, 7, self.testData)
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

        #随机获取一个特辑ID，作为特辑详情的参数
        albumsId = random.choice(result_ListQuery["data"])["albumsId"]

        AlbumsDeatilURL = self.AlbumsDeatil.get_getAlbumsDeatil4FrontURL(self.config.get('imi_base_url_ch', 'base_url_dev_k8s'),
                                                  self.config.get("imi_cms_url", "getAlbumsDeatil4FrontURL"), self.config.get("lang", "zh"),
                                                  self.base.getTimeStamp(),
                                                  self.config.get("clientVersionInfo", "clientVersionInfo_ch_Android"),access_token)

        result_AlbumsDeatil = self.AlbumsDeatil.send_request_getAlbumsDeatil4Front(AlbumsDeatilURL,albumsId)

        self.assertEqual(result_AlbumsDeatil["stateCode"], 200)
        self.assertEqual(result_AlbumsDeatil["stateMsg"], "OK")
        self.assertEqual(result_AlbumsDeatil["data"]["albumsId"],albumsId)


    def test_getAlbumsDeatil4Front_tutu_Android_002(self):
        '''美甲涂涂移动Android端_特辑详情_正常查询_鉴权登录_002'''
        # 第一步，获取excel中的测试数据
        TestData = self.ex.getDict(2, 28, 7, self.testData)
        currentPage = TestData["currentPage"]
        pageSize = TestData["pageSize"]


        # 第二步，组装要登录的数据
        data = self.AC.get_Android_CN_Not_logged_in()

        # 第三步，组装登录的URL
        pad_login_url_ch = self.AC.get_AuthenticationURL(self.config.get('imi_base_url_ch', 'base_url_dev_k8s'),self.config.get("imi_login_url","login_url"),self.config.get("lang", "zh"),self.base.getTimeStamp(),self.config.get("clientVersionInfo", "clientVersionInfo_ch_Android"))


        # 第四步，登录
        access_token = self.AC.get_Access_token_not_login(pad_login_url_ch,data)

        # 第五步，断言判断是否登录成功
        self.assertIsNotNone(access_token)

        # 第六步，组装接口的URL
        ListQueryURL = self.ListQuery.get_getAlbumsList4FrontURL(self.config.get('imi_base_url_ch', 'base_url_dev_k8s'),
                                                  self.config.get("imi_cms_url", "getAlbumsList4FrontURL"), self.config.get("lang", "zh"),
                                                  self.base.getTimeStamp(),
                                                  self.config.get("clientVersionInfo", "clientVersionInfo_ch_Android"),access_token)

        # 第七步，发送请求
        result_ListQuery = self.ListQuery.send_request_getAlbumsList4Front(ListQueryURL,currentPage,pageSize)

        # 第八步，断言返回的数据是否正确
        self.assertEqual(result_ListQuery["stateCode"], 200)
        self.assertEqual(result_ListQuery["stateMsg"], "OK")
        self.assertIsNotNone(result_ListQuery["data"])

        #获取第一个特辑ID，作为特辑详情的参数
        albumsId = random.choice(result_ListQuery["data"])["albumsId"]

        AlbumsDeatilURL = self.AlbumsDeatil.get_getAlbumsDeatil4FrontURL(self.config.get('imi_base_url_ch', 'base_url_dev_k8s'),
                                                  self.config.get("imi_cms_url", "getAlbumsDeatil4FrontURL"), self.config.get("lang", "zh"),
                                                  self.base.getTimeStamp(),
                                                  self.config.get("clientVersionInfo", "clientVersionInfo_ch_Android"),access_token)
        # 第七步，发送请求
        result_AlbumsDeatil = self.AlbumsDeatil.send_request_getAlbumsDeatil4Front(AlbumsDeatilURL,albumsId)

        self.assertEqual(result_AlbumsDeatil["stateCode"], 200)
        self.assertEqual(result_AlbumsDeatil["stateMsg"], "OK")
        self.assertEqual(result_AlbumsDeatil["data"]["albumsId"],albumsId)

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()


