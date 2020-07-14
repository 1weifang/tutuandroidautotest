#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/9/9 20:37
# @Author  : Durat
# @Email   : durant.zeng@sunvalley.com.cn
# @File    : test_case_addDiyPic.py
# @Software: PyCharm

import sys, os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
import unittest
from common.FileParsing import FileParser
from common.baseUtil import baseUtils
from interface.base.login.authentication import Authentication
from interface.base.fileUpload.single import single
from interface.tutu.gallery.addDiyPic import addDiyPic
from common.excelUtil import excelUtil



class TestaddDiyPicFunc(unittest.TestCase):
    """Test addDiyPic.py"""

    def setUp(self):
        self.base = baseUtils()
        self.projectPath = self.base.getProjectPath() + os.sep + "config" + os.sep + "config.ini"
        self.testData = self.base.getProjectPath() + os.sep + "config" + os.sep + "AnjouTestCase.xls"
        self.filepath = self.base.getProjectPath() + os.sep + "testPicture" + os.sep + "Community" + os.sep + "Community.jpg"
        self.DIYFilepath = self.base.getProjectPath() + os.sep + "testPicture" + os.sep + "DIY" + os.sep + "DIY.jpg"
        self.config = FileParser(self.projectPath)
        self.AC = Authentication()
        self.ex = excelUtil()
        self.single = single()
        self.DIY = addDiyPic()


    def test_addDiyPic_tutu_Android_001(self):
        '''美甲涂涂移动Android端_diy与社区图片上传_上传至美甲涂涂_手机号密码登录_001'''
        # 第一步，获取excel中的测试数据
        TestData = self.ex.getDict(2, 23, 7, self.testData)


        # 第二步，组装要登录的数据
        phone = TestData["phone"]
        password = TestData["password"]
        data = self.AC.get_Android_CN_logged_in(phone, password)

        # 第三步，组装登录的URL
        pad_login_url_ch = self.AC.get_AuthenticationURL(self.config.get('imi_base_url_ch', 'base_url_dev_k8s'),self.config.get("imi_login_url","login_url"),self.config.get("lang", "zh"),self.base.getTimeStamp(),self.config.get("clientVersionInfo", "clientVersionInfo_ch_Android"))


        # 第四步，登录
        access_token = self.AC.get_Access_token(pad_login_url_ch,data)

        # 第五步，断言判断是否登录成功
        self.assertIsNotNone(access_token)

        #第六步，调用单图片上传接口，返回pictureName，pictureUrl，thumbnailPictureUrl，pictureWidth，pictureHeight
        targetid = TestData["targetid"]
        filename = TestData["filename"]

        # 第七步，组装接口的URL
        SingleURL = self.single.get_singleURL(self.config.get('imi_base_url_ch', 'base_url_dev_k8s'),
                                                  self.config.get("imi_cms_url", "singleURL"), self.config.get("lang", "zh"),
                                                  self.base.getTimeStamp(),
                                                  self.config.get("clientVersionInfo", "clientVersionInfo_ch_Android"),access_token)

        # 第八步，发送请求
        result_Single = self.single.send_request_single(SingleURL,targetid,filename,self.filepath)

        # 第九步，断言返回的数据是否正确
        self.assertEqual(result_Single["stateCode"], 200)
        self.assertEqual(result_Single["stateMsg"], "OK")



        #第十步，调用diy与社区图片上传接口，上传至美甲涂涂，到我的上传
        DiyURL = self.DIY.get_AddDiyPicURL(self.config.get('imi_base_url_ch', 'base_url_dev_k8s'),
                                                  self.config.get("imi_cms_url", "AddDiyPicURL"), self.config.get("lang", "zh"),
                                                  self.base.getTimeStamp(),
                                                  self.config.get("clientVersionInfo", "clientVersionInfo_ch_Android"),access_token)
        collectionType = TestData["collectionType"]
        result_Diy = self.DIY.send_request_addDiyPic(DiyURL, result_Single["data"]["pictureName"],result_Single["data"]["thumbnailPictureUrl"], result_Single["data"]["pictureUrl"],collectionType)

        #第十步，断言返回的数据是否正确
        self.assertEqual(result_Diy["stateCode"], 200)
        self.assertEqual(result_Diy["stateMsg"], "OK")
        self.assertIsNotNone(result_Diy["data"]["pictureId"])

    def test_addDiyPic_tutu_Android_002(self):
        '''美甲涂涂移动Android端_diy与社区图片上传_收藏_手机号密码登录_002'''
        # 第一步，获取excel中的测试数据
        TestData = self.ex.getDict(2, 24, 7, self.testData)


        # 第二步，组装要登录的数据
        phone = TestData["phone"]
        password = TestData["password"]
        data = self.AC.get_Android_CN_logged_in(phone, password)

        # 第三步，组装登录的URL
        pad_login_url_ch = self.AC.get_AuthenticationURL(self.config.get('imi_base_url_ch', 'base_url_dev_k8s'),self.config.get("imi_login_url","login_url"),self.config.get("lang", "zh"),self.base.getTimeStamp(),self.config.get("clientVersionInfo", "clientVersionInfo_ch_Android"))


        # 第四步，登录
        access_token = self.AC.get_Access_token(pad_login_url_ch,data)

        # 第五步，断言判断是否登录成功
        self.assertIsNotNone(access_token)

        #第六步，调用单图片上传接口，返回pictureName，pictureUrl，thumbnailPictureUrl，pictureWidth，pictureHeight
        targetid = TestData["targetid"]
        filename = TestData["filename"]

        # 第七步，组装接口的URL
        SingleURL = self.single.get_singleURL(self.config.get('imi_base_url_ch', 'base_url_dev_k8s'),
                                                  self.config.get("imi_cms_url", "singleURL"), self.config.get("lang", "zh"),
                                                  self.base.getTimeStamp(),
                                                  self.config.get("clientVersionInfo", "clientVersionInfo_ch_Android"),access_token)

        # 第八步，发送请求
        result_Single = self.single.send_request_single(SingleURL,targetid,filename,self.DIYFilepath)

        # 第九步，断言返回的数据是否正确
        self.assertEqual(result_Single["stateCode"], 200)
        self.assertEqual(result_Single["stateMsg"], "OK")



        #第十步，调用diy与社区图片上传接口，上传至美甲涂涂，到我的上传
        DiyURL = self.DIY.get_AddDiyPicURL(self.config.get('imi_base_url_ch', 'base_url_dev_k8s'),
                                                  self.config.get("imi_cms_url", "AddDiyPicURL"), self.config.get("lang", "zh"),
                                                  self.base.getTimeStamp(),
                                                  self.config.get("clientVersionInfo", "clientVersionInfo_ch_Android"),access_token)
        collectionType = TestData["collectionType"]
        result_Diy = self.DIY.send_request_addDiyPic(DiyURL, result_Single["data"]["pictureName"],result_Single["data"]["thumbnailPictureUrl"], result_Single["data"]["pictureUrl"],collectionType)

        #第十步，断言返回的数据是否正确
        self.assertEqual(result_Diy["stateCode"], 200)
        self.assertEqual(result_Diy["stateMsg"], "OK")
        self.assertIsNotNone(result_Diy["data"]["pictureId"])

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
