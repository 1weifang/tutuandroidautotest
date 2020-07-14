#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/9/9 9:56
# @Author  : Durat
# @Email   : durant.zeng@sunvalley.com.cn
# @File    : test_case_getPicList4UserUpLoadMi.py
# @Software: PyCharm


import sys, os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
import unittest
from common.FileParsing import FileParser
from common.baseUtil import baseUtils
from interface.base.login.authentication import Authentication
from interface.tutu.gallery.getPicList4UserUpLoadMi import getPicList4UserUpLoadMi
from common.excelUtil import excelUtil


class TestgetPicList4UserUpLoadMiFunc(unittest.TestCase):
    """Test getPicList4UserUpLoadMi.py"""

    def setUp(self):
        self.base = baseUtils()
        self.projectPath = self.base.getProjectPath() + os.sep + "config" + os.sep + "config.ini"
        self.testData = self.base.getProjectPath() + os.sep + "config" + os.sep + "AnjouTestCase.xls"
        self.config = FileParser(self.projectPath)
        self.AC = Authentication()
        self.ex = excelUtil()
        self.userUpload = getPicList4UserUpLoadMi()

    @unittest.skip("跳过")
    def test_getPicList4UserUpLoadMi_Android_ch_001(self):
        '''美甲涂涂端_用户上传_zh_Android_正常查询_手机号密码登录'''
        # 第一步，获取excel中的测试数据
        TestData = self.ex.getDict(2, 1, 7, self.testData)
        currentPage = TestData["currentPage"]
        pageSize = TestData["pageSize"]
        allNailSuitFlag = TestData["allNailSuitFlag"]

        # 第二步，组装要登录的数据
        phone = TestData["phone"]
        password = TestData["password"]
        data = self.AC.get_Android_CN_logged_in(phone, password)

        # 第三步，组装登录的URL
        pad_login_url_ch = self.AC.get_AuthenticationURL(self.config.get('imi_base_url_ch', 'base_url_prod'),self.config.get("imi_login_url","login_url"),self.config.get("lang", "zh"),self.base.getTimeStamp(),self.config.get("clientVersionInfo", "clientVersionInfo_ch_Android"))


        # 第四步，登录
        access_token = self.AC.get_Access_token(pad_login_url_ch,data)

        # 第五步，断言判断是否登录成功
        self.assertIsNotNone(access_token)

        # 第六步，组装接口的URL
        userUploadURL = self.userUpload.get_getPicList4UserUpLoadMiURL(self.config.get('imi_base_url_ch', 'base_url_prod'),
                                                  self.config.get("imi_cms_url", "getPicList4UserUpLoadMiURL"), self.config.get("lang", "zh"),
                                                  self.base.getTimeStamp(),
                                                  self.config.get("clientVersionInfo", "clientVersionInfo_ch_Android"),access_token)

        # 第七步，发送请求
        result = self.userUpload.send_request_getPicList4UserUpLoadMi(userUploadURL,allNailSuitFlag,currentPage,pageSize)

        # 第八步，断言返回的数据是否正确
        self.assertEqual(result["stateCode"], 200)
        self.assertEqual(result["stateMsg"], "OK")

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()


