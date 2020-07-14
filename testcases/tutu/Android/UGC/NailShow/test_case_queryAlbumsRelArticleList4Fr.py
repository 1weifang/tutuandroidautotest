#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/2/18 11:25
# @Author  : Durat
# @Email   : durant.zeng@sunvalley.com.cn
# @File    : test_case_queryAlbumsRelArticleList4Fr.py
# @Software: PyCharm

import sys, os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
import unittest
from common.FileParsing import FileParser
from common.baseUtil import baseUtils
from interface.base.login.authentication import Authentication
from interface.tutu.Album.getAlbumsList4Front import getAlbumsList4Front
from interface.tutu.Album.getAlbumsDeatil4Front import getAlbumsDeatil4Front
from interface.tutu.UGC.NailShow.queryAlbumsRelArticleList4Fr import queryAlbumsRelArticleList4Fr
from common.excelUtil import excelUtil


class TestqueryAlbumsRelArticleList4FrFunc(unittest.TestCase):
    """Test queryAlbumsRelArticleList4Fr.py"""

    def setUp(self):
        self.base = baseUtils()
        self.projectPath = self.base.getProjectPath() + os.sep + "config" + os.sep + "config.ini"
        self.testData = self.base.getProjectPath() + os.sep + "config" + os.sep + "AnjouTestCase.xls"
        self.config = FileParser(self.projectPath)
        self.AC = Authentication()
        self.ex = excelUtil()
        self.ListQuery = getAlbumsList4Front()
        self.AlbumsDeatil = getAlbumsDeatil4Front()
        self.NailShow = queryAlbumsRelArticleList4Fr()


    def test_queryAlbumsRelArticleList4Fr_tutu_Android_001(self):
        '''美甲涂涂移动Android端_queryAlbumsRelArticleList4Fr_特辑-特辑详情-查同款特辑的美甲文章_正常查询_001'''
        #登录
        TestData = self.ex.getDict(2, 27, 7, self.testData)
        currentPage = TestData["currentPage"]
        pageSize = TestData["pageSize"]

        phone = TestData["phone"]
        password = TestData["password"]
        data = self.AC.get_Android_CN_logged_in(phone, password)

        login_url_ch = self.AC.get_AuthenticationURL(self.config.get('imi_base_url_ch', 'base_url_dev_k8s'),self.config.get("imi_login_url","login_url"),self.config.get("lang", "zh"),self.base.getTimeStamp(),self.config.get("clientVersionInfo", "clientVersionInfo_ch_Android"))
        access_token = self.AC.get_Access_token(login_url_ch,data)
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

        # 获取第一个特辑ID，作为特辑详情的参数
        albumsId = result_ListQuery["data"][0]["albumsId"]

        #特辑详情
        AlbumsDeatilURL = self.AlbumsDeatil.get_getAlbumsDeatil4FrontURL(self.config.get('imi_base_url_ch', 'base_url_dev_k8s'),
                                                  self.config.get("imi_cms_url", "getAlbumsDeatil4FrontURL"), self.config.get("lang", "zh"),
                                                  self.base.getTimeStamp(),
                                                  self.config.get("clientVersionInfo", "clientVersionInfo_ch_Android"),access_token)
        result_AlbumsDeatil = self.AlbumsDeatil.send_request_getAlbumsDeatil4Front(AlbumsDeatilURL,albumsId)

        self.assertEqual(result_AlbumsDeatil["stateCode"], 200)
        self.assertEqual(result_AlbumsDeatil["stateMsg"], "OK")
        self.assertEqual(result_AlbumsDeatil["data"]["albumsId"],albumsId)

        #同款美甲秀
        NailShowURL = self.NailShow.get_queryAlbumsRelArticleList4FrURL(self.config.get('imi_base_url_ch', 'base_url_dev_k8s'),
                                                  self.config.get("UGC", "queryAlbumsRelArticleList4FrURL"), self.config.get("lang", "zh"),
                                                  self.base.getTimeStamp(),
                                                  self.config.get("clientVersionInfo", "clientVersionInfo_ch_Android"),access_token)
        result_NailShow = self.NailShow.send_request_queryAlbumsRelArticleList4Fr(NailShowURL,albumsId,currentPage,pageSize)

        self.assertEqual(result_NailShow["stateCode"], 200)
        self.assertEqual(result_NailShow["stateMsg"], "OK")


    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()