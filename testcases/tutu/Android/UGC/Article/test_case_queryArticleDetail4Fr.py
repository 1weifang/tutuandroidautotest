#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/2/18 10:54
# @Author  : Durat
# @Email   : durant.zeng@sunvalley.com.cn
# @File    : test_case_queryArticleDetail4Fr.py
# @Software: PyCharm

import sys, os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
import unittest
import time
import random
from common.FileParsing import FileParser
from common.baseUtil import baseUtils
from interface.base.login.authentication import Authentication
from interface.tutu.UGC.Article.queryArticleListOfDiscover4Fr import queryArticleListOfDiscover4Fr
from interface.tutu.UGC.Article.queryArticleDetail4Fr import queryArticleDetail4Fr

from common.excelUtil import excelUtil


class TestqueryArticleDetail4FrFunc(unittest.TestCase):
    """Test queryArticleDetail4Fr"""

    def setUp(self):
        self.base = baseUtils()
        self.projectPath = self.base.getProjectPath() + os.sep + "config" + os.sep + "config.ini"
        self.testData = self.base.getProjectPath() + os.sep + "config" + os.sep + "AnjouTestCase.xls"
        self.config = FileParser(self.projectPath)
        self.AC = Authentication()
        self.ex = excelUtil()
        self.Discover = queryArticleListOfDiscover4Fr()
        self.Detail = queryArticleDetail4Fr()

    def test_queryArticleDetail4Fr_tutu_Android_001(self):
        '''美甲涂涂移动Android端_queryArticleDetail4Fr_ugc笔记-查详情_正常查询_手机号密码登录_001'''
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



        #ugc笔记-发现
        ArticleListURL = self.Discover.get_queryArticleListOfDiscover4FrURL(self.config.get('imi_base_url_ch', 'base_url_dev_k8s'),
                                                  self.config.get("UGC", "queryArticleListOfDiscover4FrURL"), self.config.get("lang", "zh"),
                                                  self.base.getTimeStamp(),
                                                  self.config.get("clientVersionInfo", "clientVersionInfo_ch_Android"),access_token)
        time.sleep(0.5)
        orderBy = 1
        result_ArticleList = self.Discover.send_request_queryArticleListOfDiscover4Fr(ArticleListURL,orderBy,currentPage,pageSize)

        self.assertEqual(result_ArticleList["stateCode"], 200)
        self.assertEqual(result_ArticleList["stateMsg"], "OK")



        #ugc笔记-查详情
        DetailURL = self.Detail.get_queryArticleDetail4FrURL(self.config.get('imi_base_url_ch', 'base_url_dev_k8s'),
                                                  self.config.get("UGC", "queryArticleDetail4FrURL"), self.config.get("lang", "zh"),
                                                  self.base.getTimeStamp(),
                                                 self.config.get("clientVersionInfo", "clientVersionInfo_ch_Android"),access_token)
        #随机获取一篇笔记的ID
        id = random.choice(result_ArticleList["data"])["id"]
        time.sleep(0.5)
        result_Detail = self.Detail.send_request_queryArticleDetail4Fr(DetailURL,id)

        self.assertEqual(result_Detail["stateCode"], 200)
        self.assertEqual(result_Detail["stateMsg"], "OK")


    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()