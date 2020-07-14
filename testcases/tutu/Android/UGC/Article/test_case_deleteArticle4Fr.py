#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/2/27 15:03
# @Author  : Durat
# @Email   : durant.zeng@sunvalley.com.cn
# @File    : test_case_deleteArticle4Fr.py
# @Software: PyCharm

import sys,os
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
import unittest
import random
import time
from common.FileParsing import FileParser
from common.baseUtil import baseUtils
from interface.base.login.authentication import Authentication
from interface.base.fileUpload.batch import batch
from interface.tutu.UGC.Article.addArticle4Fr import addArticle4Fr
from interface.tutu.UGC.Article.deleteArticle4Fr import deleteArticle4Fr
from interface.tutu.UGC.Article.queryArticleListOfHomePub4Fr import queryArticleListOfHomePub4Fr
from common.excelUtil import excelUtil


class TestdeleteArticle4FrFunc(unittest.TestCase):
    """Test deleteArticle4Fr.py"""

    def setUp(self):
        self.base = baseUtils()
        self.projectPath = self.base.getProjectPath() + os.sep + "config" + os.sep + "config.ini"
        self.testData = self.base.getProjectPath() + os.sep + "config" + os.sep + "AnjouTestCase.xls"
        self.config = FileParser(self.projectPath)
        self.AC = Authentication()
        self.ex = excelUtil()
        self.batch = batch()
        self.addArticle = addArticle4Fr()
        self.Home = queryArticleListOfHomePub4Fr()
        self.deleteArticle = deleteArticle4Fr()
        self.filepath = self.base.getProjectPath() + os.sep + "testPicture" + os.sep + "printerOrder" + os.sep + "printTargetImg" + os.sep + "printTargetImg.jpg"
        self.file = self.base.getProjectPath() + os.sep + "testPicture" + os.sep + "AITest" + os.sep + "queryAiNailSuit4Front" + os.sep + "Android" + os.sep + "queryAiNailSuit4Front.jpg"

    def test_deleteArticle_tutu_Android_001(self):
        '''美甲涂涂移动Android端_deleteArticle_UGC删除笔记_图片_001'''
        #账号密码登录
        TestData = self.ex.getDict(2, 29, 7, self.testData)
        currentPage = TestData["currentPage"]
        pageSize = TestData["pageSize"]

        phone = TestData["phone"]
        password = TestData["password"]

        data = self.AC.get_Android_CN_logged_in(phone,password)
        tutu_login_url = self.AC.get_AuthenticationURL(self.config.get('imi_base_url_ch', 'base_url_dev_k8s'),self.config.get("imi_login_url","login_url"),self.config.get("lang", "zh"),self.base.getTimeStamp(),self.config.get("clientVersionInfo", "clientVersionInfo_en_ios"))

        access_token = self.AC.get_Access_token(tutu_login_url,data)
        self.assertIsNotNone(access_token)



        #batch上传接口
        filename = "queryAiNailSuit4Front.jpg"
        batchURL = self.batch.get_batchURL(self.config.get('imi_base_url_ch', 'base_url_dev_k8s'),
                                                  self.config.get("fileUpload", "batchURL"), self.config.get("lang", "zh"),
                                                  self.base.getTimeStamp(),
                                                  self.config.get("clientVersionInfo", "clientVersionInfo_ch_Android"),access_token)
        filepath = self.file
        filename = filename
        dictory = "ugc/article/pic"
        result_batch = self.batch.send_request_batch(batchURL,filename,filepath,dictory)

        self.assertEqual(result_batch["stateCode"], 200)
        self.assertEqual(result_batch["stateMsg"], "OK")


        try:
            #addArticle4Fr接口
            addArticleURL = self.addArticle.get_addArticle4FrURL(self.config.get('imi_base_url_ch', 'base_url_dev_k8s'),
                                                      self.config.get("UGC", "addArticle4FrURL"), self.config.get("lang", "zh"),
                                                      self.base.getTimeStamp(),

                                                     self.config.get("clientVersionInfo", "clientVersionInfo_ch_Android"),access_token)
            articleType = 1
            articleStatus = 3
            imagesFallsHeight = result_batch["data"][0]["pictureHeight"]
            imagesFallsWidth = result_batch["data"][0]["pictureWidth"]
            imagesFallsLitimgUrl = result_batch["data"][0]["thumbnailPictureUrl"]
            imagesFallsUrl = result_batch["data"][0]["pictureUrl"]
            imagesLitimgUrlsList = []
            imagesLitimgUrlsList.append(imagesFallsLitimgUrl)
            imagesUrlsList = []
            imagesUrlsList.append(imagesFallsUrl)

            content = self.base.get_random_content()

            result_addArticle = self.addArticle.send_request_addArticle4Fr(addArticleURL,articleType,articleStatus,imagesFallsUrl,imagesFallsWidth,imagesFallsHeight,imagesFallsLitimgUrl,imagesUrlsList,imagesLitimgUrlsList,content)
            self.assertEqual(result_addArticle["stateCode"], 200)
            self.assertEqual(result_addArticle["stateMsg"], "OK")

            #ugc文章-查主页发布的文章列表/我的发布
            HomeURL = self.Home.get_queryArticleListOfHomePub4FrURL(self.config.get('imi_base_url_ch', 'base_url_dev_k8s'),
                                                      self.config.get("UGC", "queryArticleListOfHomePub4FrURL"), self.config.get("lang", "zh"),
                                                      self.base.getTimeStamp(),
                                                      self.config.get("clientVersionInfo", "clientVersionInfo_ch_Android"),access_token)

            time.sleep(0.5)
            homeType = 1
            result_Home = self.Home.send_request_queryArticleListOfHomePub4Fr(HomeURL,homeType,currentPage,pageSize)

            self.assertEqual(result_Home["stateCode"], 200)
            self.assertEqual(result_Home["stateMsg"], "OK")

            #获取任意一篇笔记的ID
            id = result_Home["data"][0]["id"]

        finally:
            time.sleep(0.5)
            #deleteArticle4Fr接口
            deleteArticleURL = self.deleteArticle.get_deleteArticle4FrURL(self.config.get('imi_base_url_ch', 'base_url_dev_k8s'),
                                                      self.config.get("UGC", "deleteArticle4FrURL"), self.config.get("lang", "zh"),
                                                      self.base.getTimeStamp(),

                                                     self.config.get("clientVersionInfo", "clientVersionInfo_ch_Android"),access_token)
            articleIdList = []
            articleIdList.append(id)
            result_deleteArticle = self.deleteArticle.send_request_deleteArticle4Fr(deleteArticleURL,articleIdList)
            self.assertEqual(result_deleteArticle["stateCode"], 200)
            self.assertEqual(result_deleteArticle["stateMsg"], "OK")



    def tearDown(self):
            pass

if __name__ == '__main__':
    unittest.main()

