#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/2/25 13:51
# @Author  : Durat
# @Email   : durant.zeng@sunvalley.com.cn
# @File    : test_case_coverBanner.py
# @Software: PyCharm

import sys,os
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
import unittest
from common.FileParsing import FileParser
from common.baseUtil import baseUtils
from interface.base.login.authentication import Authentication
from interface.anjou.IOS.coverBanner import coverBanner
from common.excelUtil import excelUtil


class TestcoverBannerFunc(unittest.TestCase):
    """Test coverBanner.py"""

    def setUp(self):
        self.base = baseUtils()
        self.projectPath = self.base.getProjectPath() + os.sep + "config" + os.sep + "config.ini"
        self.testData = self.base.getProjectPath() + os.sep + "config" + os.sep + "AnjouTestCase.xls"
        self.config = FileParser(self.projectPath)
        self.AC = Authentication()
        self.ex = excelUtil()
        self.coverBanner = coverBanner()


    def test_coverBanner_tutu_Android_001(self):
        '''美甲涂涂移动Android端_coverBanner_获取banner列表_001'''

        #账号密码登录
        TestData = self.ex.getDict(2, 29, 7, self.testData)
        currentPage = TestData["currentPage"]
        pageSize = TestData["pageSize"]

        phone = "13417335080"
        password = TestData["password"]
        data = self.AC.get_Android_CN_logged_in(phone,password)

        anjou_login_url = self.AC.get_AuthenticationURL(self.config.get('imi_base_url_ch', 'base_url_dev_k8s'),self.config.get("imi_login_url","login_url"),self.config.get("lang", "en"),self.base.getTimeStamp(),self.config.get("clientVersionInfo", "clientVersionInfo_en_ios"))

        access_token = self.AC.get_Access_token(anjou_login_url,data)

        self.assertIsNotNone(access_token)

        #coverBanner接口
        coverBannerURL = self.coverBanner.get_coverBannerURL(self.config.get('imi_base_url_ch', 'base_url_dev_k8s'),
                                                  self.config.get("anjou", "coverBannerURL"), self.config.get("lang", "en"),
                                                  self.base.getTimeStamp(),
                                                  self.config.get("clientVersionInfo", "clientVersionInfo_en_ios"),access_token)
        #标识当前请求是哪一端：1、android 2、ios 3、小程序
        appType = 1
        bannerModel = "B03B11"
        result_coverBanner = self.coverBanner.send_request_coverBanner(coverBannerURL,appType,bannerModel)
        self.assertEqual(result_coverBanner["stateCode"], 200)
        self.assertEqual(result_coverBanner["stateMsg"], "OK")


    def tearDown(self):
            pass

if __name__ == '__main__':
    unittest.main()


