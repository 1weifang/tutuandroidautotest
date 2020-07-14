#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/11/18 15:34
# @Author  : Durat
# @Email   : durant.zeng@sunvalley.com.cn
# @File    : test_case_getMyPicAlbumsCollectionDetailMI.py
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
from interface.tutu.Album.albumsCollection4Front import albumsCollection4Front
from interface.tutu.PersonalCenter.myCollection.getMyPicAlbumsCollectionMI import getMyPicAlbumsCollectionMI
from interface.tutu.PersonalCenter.myCollection.getMyPicAlbumsCollectionDetailMI import getMyPicAlbumsCollectionDetailMI
from interface.tutu.PersonalCenter.myCollection.albumsBatchUnCollection4Front import albumsBatchUnCollection4Front
from common.excelUtil import excelUtil


class TestgetMyPicAlbumsCollectionDetailMIFunc(unittest.TestCase):
    """Test getMyPicAlbumsCollectionDetailMI.py"""

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
        self.getMyAlbums = getMyPicAlbumsCollectionMI()
        self.albumsDetail = getMyPicAlbumsCollectionDetailMI()
        self.albumsBatch = albumsBatchUnCollection4Front()


    def test_getMyPicAlbumsCollectionDetailMI_tutu_Android_001(self):
        '''美甲涂涂移动Android端_个人中心--我的收藏--专辑详情_正常查询_001'''
        # 第一步，获取excel中的测试数据
        TestData = self.ex.getDict(2, 27, 7, self.testData)
        currentPage = TestData["currentPage"]
        pageSize = TestData["pageSize"]

        #登录
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
        albumsId = result_ListQuery["data"][1]["albumsId"]

        AlbumsDeatilURL = self.AlbumsDeatil.get_getAlbumsDeatil4FrontURL(self.config.get('imi_base_url_ch', 'base_url_dev_k8s'),
                                                  self.config.get("imi_cms_url", "getAlbumsDeatil4FrontURL"), self.config.get("lang", "zh"),
                                                  self.base.getTimeStamp(),
                                                  self.config.get("clientVersionInfo", "clientVersionInfo_ch_Android"),access_token)
        result_AlbumsDeatil = self.AlbumsDeatil.send_request_getAlbumsDeatil4Front(AlbumsDeatilURL,albumsId)

        self.assertEqual(result_AlbumsDeatil["stateCode"], 200)
        self.assertEqual(result_AlbumsDeatil["stateMsg"], "OK")
        self.assertEqual(result_AlbumsDeatil["data"]["albumsId"],albumsId)

        #对第一张特辑进行一键收藏
        albumsCollectionURL = self.albumsCollection.get_albumsShare4FrontURL(self.config.get('imi_base_url_ch', 'base_url_dev_k8s'),
                                                  self.config.get("imi_cms_url", "albumsCollection4FrontURL"), self.config.get("lang", "zh"),
                                                  self.base.getTimeStamp(),
                                                  self.config.get("clientVersionInfo", "clientVersionInfo_ch_Android"),access_token)
        result_albumsCollection = self.albumsCollection.send_request_albumsCollection4Front_new(albumsCollectionURL,albumsId)

        self.assertEqual(result_albumsCollection["stateCode"], 200)
        self.assertEqual(result_albumsCollection["stateMsg"], "OK")



        #我的收藏（专辑列表）
        getMyAlbumsURL = self.getMyAlbums.get_getMyPicAlbumsCollectionMIURL(self.config.get('imi_base_url_ch', 'base_url_dev_k8s'),
                                                  self.config.get("imi_cms_url", "getMyPicAlbumsCollectionMIURL"), self.config.get("lang", "zh"),
                                                  self.base.getTimeStamp(),
                                                  self.config.get("clientVersionInfo", "clientVersionInfo_ch_Android"),access_token)
        result_getMyAlbums = self.getMyAlbums.send_request_getMyPicAlbumsCollectionMI(getMyAlbumsURL,currentPage,pageSize)

        self.assertEqual(result_getMyAlbums["stateCode"], 200)
        self.assertEqual(result_getMyAlbums["stateMsg"], "OK")

        #特辑详情
        albumsDetailURL = self.albumsDetail.get_getMyPicAlbumsCollectionDetailMIURL(self.config.get('imi_base_url_ch', 'base_url_dev_k8s'),
                                                  self.config.get("imi_cms_url", "getMyPicAlbumsCollectionDetailMIURL"), self.config.get("lang", "zh"),
                                                  self.base.getTimeStamp(),
                                                  self.config.get("clientVersionInfo", "clientVersionInfo_ch_Android"),access_token)
        result_albumsDetail = self.albumsDetail.send_request_getMyPicAlbumsCollectionDetailMI(albumsDetailURL,albumsId)

        self.assertEqual(result_albumsDetail["stateCode"], 200)
        self.assertEqual(result_albumsDetail["stateMsg"], "OK")


        #批量删除特辑
        albumsBatchURL = self.albumsBatch.get_albumsBatchUnCollection4FrontURL(self.config.get('imi_base_url_ch', 'base_url_dev_k8s'),
                                                  self.config.get("imi_cms_url", "albumsBatchUnCollection4FrontURL"), self.config.get("lang", "zh"),
                                                  self.base.getTimeStamp(),
                                                  self.config.get("clientVersionInfo", "clientVersionInfo_ch_Android"),access_token)
        result_albumsBatch = self.albumsBatch.send_request_albumsBatchUnCollection4Front(albumsBatchURL,albumsId)

        self.assertEqual(result_albumsBatch["stateCode"], 200)
        self.assertEqual(result_albumsBatch["stateMsg"], "OK")


    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
