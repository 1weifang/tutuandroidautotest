#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/3/3 16:23
# @Author  : Durat
# @Email   : durant.zeng@sunvalley.com.cn
# @File    : test_case_UGC_ProcessTesting.py
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
from interface.tutu.Album.getAlbumsDeatil4Front import getAlbumsDeatil4Front
from interface.tutu.UGC.NailShow.queryAlbumsRelArticleList4Fr import queryAlbumsRelArticleList4Fr
from interface.tutu.Album.getAlbumsList4Front import getAlbumsList4Front
from interface.tutu.UGC.Article.addArticle4Fr import addArticle4Fr
from interface.tutu.UGC.Article.deleteArticle4Fr import deleteArticle4Fr
from interface.tutu.UGC.Article.queryArticleListOfHomePub4Fr import queryArticleListOfHomePub4Fr
from interface.tutu.UGC.Article.Comment.addComment4Fr import addComment4Fr
from interface.tutu.UGC.Article.updateArticle4Fr import updateArticle4Fr
from interface.tutu.UGC.Article.Comment.getCommentList4Fr import getCommentList4Fr
from interface.tutu.UGC.Article.Comment.addReply4Fr import addReply4Fr
from interface.tutu.UGC.Article.Comment.getReplySimpleList4Fr import getReplySimpleList4Fr
from interface.tutu.UGC.Article.staticUserLog4Fr import staticUserLog4Fr
from interface.tutu.UGC.topic.queryTopicList4Fr import queryTopicList4Fr
from interface.tutu.UGC.topic.queryTopicDetail4Fr import queryTopicDetail4Fr
from interface.tutu.UGC.Tag.querySearchTagList4Fr import querySearchTagList4Fr
from interface.tutu.UGC.Tag.queryArticleListByTag4Fr import queryArticleListByTag4Fr
from interface.tutu.UGC.Article.queryArticleListOfDiscover4Fr import queryArticleListOfDiscover4Fr
from interface.tutu.UGC.Article.queryArticleDetail4Fr import queryArticleDetail4Fr
from interface.tutu.UGC.Article.queryArticleListOfRecommend4Fr import queryArticleListOfRecommend4Fr
from common.excelUtil import excelUtil


class TestgetReplySimpleList4FrFunc(unittest.TestCase):
    """Test UGC_ProcessTesting.py"""

    def setUp(self):
        self.base = baseUtils()
        self.projectPath = self.base.getProjectPath() + os.sep + "config" + os.sep + "config.ini"
        self.testData = self.base.getProjectPath() + os.sep + "config" + os.sep + "AnjouTestCase.xls"
        self.config = FileParser(self.projectPath)
        self.AC = Authentication()
        self.ex = excelUtil()
        self.batch = batch()
        self.ListQuery = getAlbumsList4Front()
        self.AlbumsDeatil = getAlbumsDeatil4Front()
        self.NailShow = queryAlbumsRelArticleList4Fr()
        self.addArticle = addArticle4Fr()
        self.updateArticle = updateArticle4Fr()
        self.Home = queryArticleListOfHomePub4Fr()
        self.deleteArticle = deleteArticle4Fr()
        self.addComment = addComment4Fr()
        self.getCommentList = getCommentList4Fr()
        self.addReply = addReply4Fr()
        self.Detail = queryArticleDetail4Fr()
        self.ArticleRecommend = queryArticleListOfRecommend4Fr()
        self.TagList = querySearchTagList4Fr()
        self.queryArticleListByTag = queryArticleListByTag4Fr()
        self.static = staticUserLog4Fr()
        self.queryTopic = queryTopicList4Fr()
        self.Discover = queryArticleListOfDiscover4Fr()
        self.queryTopicDetail = queryTopicDetail4Fr()
        self.getReplySimpleList = getReplySimpleList4Fr()
        self.filepath = self.base.getProjectPath() + os.sep + "testPicture" + os.sep + "printerOrder" + os.sep + "printTargetImg" + os.sep + "printTargetImg.jpg"
        self.file = self.base.getProjectPath() + os.sep + "testPicture" + os.sep + "AITest" + os.sep + "queryAiNailSuit4Front" + os.sep + "queryAiNailSuit4Front.jpg"


    def test_UGC_ProcessTesting_tutu_IOS_001(self):
        '''美甲涂涂移动IOS端_UGC流程化测试_001'''
        #登录
        TestData = self.ex.getDict(2, 29, 7, self.testData)
        currentPage = TestData["currentPage"]
        pageSize = TestData["pageSize"]
        phone = TestData["phone"]
        password = TestData["password"]
        data = self.AC.get_IOS_CN_logged_in(phone,password)
        tutu_login_url = self.AC.get_AuthenticationURL(self.config.get('imi_base_url_ch', 'base_url_uat'),self.config.get("imi_login_url","login_url"),self.config.get("lang", "zh"),self.base.getTimeStamp(),self.config.get("clientVersionInfo", "clientVersionInfo_en_ios"))

        access_token = self.AC.get_Access_token(tutu_login_url,data)
        self.assertIsNotNone(access_token)

        time.sleep(0.3)
        #ugc文章-发现
        ArticleListURL = self.Discover.get_queryArticleListOfDiscover4FrURL(self.config.get('imi_base_url_ch', 'base_url_uat'),
                                                  self.config.get("UGC", "queryArticleListOfDiscover4FrURL"), self.config.get("lang", "zh"),
                                                  self.base.getTimeStamp(),
                                                  self.config.get("clientVersionInfo", "clientVersionInfo_ch_Android"),access_token)
        #文章排序方式：1-发现，2-附近
        orderBy = 2
        userLongitude = 114.064611
        userLatitude = 22.610561
        result_ArticleList = self.Discover.send_request_queryArticleListOfDiscover4Fr(ArticleListURL,orderBy,currentPage,pageSize,userLongitude,userLatitude)

        self.assertEqual(result_ArticleList["stateCode"], 200)
        self.assertEqual(result_ArticleList["stateMsg"], "OK")

        #ugc笔记-查详情
        DetailURL = self.Detail.get_queryArticleDetail4FrURL(self.config.get('imi_base_url_ch', 'base_url_uat'),
                                                  self.config.get("UGC", "queryArticleDetail4FrURL"), self.config.get("lang", "zh"),
                                                  self.base.getTimeStamp(),
                                                  self.config.get("clientVersionInfo", "clientVersionInfo_ch_Android"),access_token)
        #取第一篇笔记的已经存在的ID
        existing_id = result_ArticleList["data"][0]["id"]
        time.sleep(0.3)
        result_Detail = self.Detail.send_request_queryArticleDetail4Fr(DetailURL,existing_id)

        self.assertEqual(result_Detail["stateCode"], 200)
        self.assertEqual(result_Detail["stateMsg"], "OK")


        #ugc笔记-查推荐
        #是随机的
        ArticleRecommendURL = self.ArticleRecommend.get_queryArticleListOfRecommend4FrURL(self.config.get('imi_base_url_ch', 'base_url_uat'),
                                                  self.config.get("UGC", "queryArticleListOfRecommend4FrURL"), self.config.get("lang", "zh"),
                                                  self.base.getTimeStamp(),
                                                  self.config.get("clientVersionInfo", "clientVersionInfo_ch_Android"),access_token)
        time.sleep(0.3)
        result_ArticleRecommend = self.ArticleRecommend.send_request_queryArticleListOfRecommend4Fr(ArticleRecommendURL)

        self.assertEqual(result_ArticleRecommend["stateCode"], 200)
        self.assertEqual(result_ArticleRecommend["stateMsg"], "OK")

        time.sleep(0.3)
        #特辑列表
        ListQueryURL = self.ListQuery.get_getAlbumsList4FrontURL(self.config.get('imi_base_url_ch', 'base_url_uat'),
                                                  self.config.get("imi_cms_url", "getAlbumsList4FrontURL"), self.config.get("lang", "zh"),
                                                  self.base.getTimeStamp(),
                                                  self.config.get("clientVersionInfo", "clientVersionInfo_ch_Android"),access_token)


        result_ListQuery = self.ListQuery.send_request_getAlbumsList4Front(ListQueryURL,currentPage,pageSize)

        #
        self.assertEqual(result_ListQuery["stateCode"], 200)
        self.assertEqual(result_ListQuery["stateMsg"], "OK")
        self.assertIsNotNone(result_ListQuery["data"])

        #随机获取一张特辑ID,作为特辑详情的参数
        albumsId = random.choice(result_ListQuery["data"])["albumsId"]

        time.sleep(0.3)
        #特辑详情
        AlbumsDeatilURL = self.AlbumsDeatil.get_getAlbumsDeatil4FrontURL(self.config.get('imi_base_url_ch', 'base_url_uat'),
                                                  self.config.get("imi_cms_url", "getAlbumsDeatil4FrontURL"), self.config.get("lang", "zh"),
                                                  self.base.getTimeStamp(),
                                                  self.config.get("clientVersionInfo", "clientVersionInfo_ch_Android"),access_token)
        result_AlbumsDeatil = self.AlbumsDeatil.send_request_getAlbumsDeatil4Front(AlbumsDeatilURL,albumsId)

        self.assertEqual(result_AlbumsDeatil["stateCode"], 200)
        self.assertEqual(result_AlbumsDeatil["stateMsg"], "OK")
        self.assertEqual(result_AlbumsDeatil["data"]["albumsId"],albumsId)

        time.sleep(0.3)
        #同款美甲秀
        NailShowURL = self.NailShow.get_queryAlbumsRelArticleList4FrURL(self.config.get('imi_base_url_ch', 'base_url_uat'),
                                                  self.config.get("UGC", "queryAlbumsRelArticleList4FrURL"), self.config.get("lang", "zh"),
                                                  self.base.getTimeStamp(),
                                                  self.config.get("clientVersionInfo", "clientVersionInfo_ch_Android"),access_token)
        result_NailShow = self.NailShow.send_request_queryAlbumsRelArticleList4Fr(NailShowURL,albumsId,currentPage,pageSize)

        self.assertEqual(result_NailShow["stateCode"], 200)
        self.assertEqual(result_NailShow["stateMsg"], "OK")

        #batch上传接口
        filename = "queryAiNailSuit4Front.jpg"
        batchURL = self.batch.get_batchURL(self.config.get('imi_base_url_ch', 'base_url_uat'),
                                                  self.config.get("fileUpload", "batchURL"), self.config.get("lang", "zh"),
                                                  self.base.getTimeStamp(),
                                                  self.config.get("clientVersionInfo", "clientVersionInfo_ch_Android"),access_token)
        filepath = self.file
        filename = filename
        dictory = "ugc/article/pic"
        result_batch = self.batch.send_request_batch(batchURL,filename,filepath,dictory)

        self.assertEqual(result_batch["stateCode"], 200)
        self.assertEqual(result_batch["stateMsg"], "OK")


        #话题列表查询
        queryTopicURL = self.queryTopic.get_queryTopicList4FrURL(self.config.get('imi_base_url_ch', 'base_url_uat'),
                                                  self.config.get("UGC", "queryTopicList4FrURL"), self.config.get("lang", "zh"),
                                                  self.base.getTimeStamp(),
                                                  self.config.get("clientVersionInfo", "clientVersionInfo_ch_Android"),access_token)

        time.sleep(0.3)
        result_queryTopic = self.queryTopic.send_request_queryTopicList4Fr(queryTopicURL)

        self.assertEqual(result_queryTopic["stateCode"], 200)
        self.assertEqual(result_queryTopic["stateMsg"], "OK")

        time.sleep(0.3)
        #随机获取话题ID
        topicID = random.choice(result_queryTopic["data"])["id"]
        #话题详情查询
        queryTopicDetailURL = self.queryTopicDetail.get_queryTopicDetail4FrURL(self.config.get('imi_base_url_ch', 'base_url_uat'),
                                                  self.config.get("UGC", "queryTopicDetail4FrURL"), self.config.get("lang", "zh"),
                                                  self.base.getTimeStamp(),
                                                  self.config.get("clientVersionInfo", "clientVersionInfo_ch_Android"),access_token)
        time.sleep(0.3)
        orderBy = 1
        result_queryTopicDetail = self.queryTopicDetail.send_request_queryTopicDetail4Fr(queryTopicDetailURL,topicID,currentPage,pageSize,orderBy)

        self.assertEqual(result_queryTopicDetail["stateCode"], 200)
        self.assertEqual(result_queryTopicDetail["stateMsg"], "OK")


        #获取一个话题ID
        topicId = topicID
        time.sleep(0.3)
        #addArticle4Fr接口
        addArticleURL = self.addArticle.get_addArticle4FrURL(self.config.get('imi_base_url_ch', 'base_url_uat'),
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

        content = self.base.get_random_string(10)*20

        result_addArticle = self.addArticle.send_request_addArticle4Fr(addArticleURL,articleType,articleStatus,topicId,albumsId,imagesFallsUrl,imagesFallsWidth,imagesFallsHeight,imagesFallsLitimgUrl,imagesUrlsList,imagesLitimgUrlsList,content)
        self.assertEqual(result_addArticle["stateCode"], 200)
        self.assertEqual(result_addArticle["stateMsg"], "OK")

        time.sleep(0.3)
        #ugc文章-查主页发布的文章列表/我的发布
        HomeURL = self.Home.get_queryArticleListOfHomePub4FrURL(self.config.get('imi_base_url_ch', 'base_url_uat'),
                                                  self.config.get("UGC", "queryArticleListOfHomePub4FrURL"), self.config.get("lang", "zh"),
                                                  self.base.getTimeStamp(),
                                                  self.config.get("clientVersionInfo", "clientVersionInfo_ch_Android"),access_token)

        homeType = 1
        result_Home = self.Home.send_request_queryArticleListOfHomePub4Fr(HomeURL,homeType,currentPage,pageSize)

        self.assertEqual(result_Home["stateCode"], 200)
        self.assertEqual(result_Home["stateMsg"], "OK")

        #获取当前发布笔记的ID
        created_id = result_Home["data"][0]["id"]

        time.sleep(0.3)
        #updateArticle接口
        updateArticle4URL = self.updateArticle.get_updateArticle4FrURL(self.config.get('imi_base_url_ch', 'base_url_uat'),
                                                  self.config.get("UGC", "updateArticle4FrURL"), self.config.get("lang", "zh"),
                                                  self.base.getTimeStamp(),

                                                 self.config.get("clientVersionInfo", "clientVersionInfo_ch_Android"),access_token)

        content1 = self.base.get_random_string(10)*20

        result_addArticle = self.updateArticle.send_request_updateArticle4Fr(updateArticle4URL,created_id,articleType,articleStatus,imagesFallsUrl,imagesFallsWidth,imagesFallsHeight,imagesFallsLitimgUrl,imagesUrlsList,imagesLitimgUrlsList,content1)
        self.assertEqual(result_addArticle["stateCode"], 200)
        self.assertEqual(result_addArticle["stateMsg"], "OK")


        #ugc搜索的标签-查列表4F
        TagListURL = self.TagList.get_querySearchTagList4FrURL(self.config.get('imi_base_url_ch', 'base_url_uat'),
                                                  self.config.get("UGC", "querySearchTagList4FrURL"), self.config.get("lang", "zh"),
                                                  self.base.getTimeStamp(),
                                                  self.config.get("clientVersionInfo", "clientVersionInfo_ch_Android"),access_token)
        time.sleep(0.3)
        result_TagList = self.TagList.send_request_querySearchTagList4Fr(TagListURL)

        self.assertEqual(result_TagList["stateCode"], 200)
        self.assertEqual(result_TagList["stateMsg"], "OK")

        #ugc搜索出列表by标签4Fr
        queryArticleListByTagURL = self.queryArticleListByTag.get_queryArticleListByTag4FrURL(self.config.get('imi_base_url_ch', 'base_url_uat'),
                                                  self.config.get("UGC", "queryArticleListByTag4FURL"), self.config.get("lang", "zh"),
                                                  self.base.getTimeStamp(),
                                                 self.config.get("clientVersionInfo", "clientVersionInfo_ch_Android"),access_token)
        #搜索类型：1-内容，2-用户
        searchType = 1
        time.sleep(0.3)
        searchContent = content1[0:30]
        result_queryArticleListByTag = self.queryArticleListByTag.send_request_queryArticleListByTag4Fr(queryArticleListByTagURL,searchContent,currentPage,pageSize,searchType)

        self.assertEqual(result_queryArticleListByTag["stateCode"], 200)
        self.assertEqual(result_queryArticleListByTag["stateMsg"], "OK")

        #ugc笔记-统计点赞/转发
        #点赞
        staticURL = self.static.get_staticUserLog4FrURL(self.config.get('imi_base_url_ch', 'base_url_uat'),
                                                  self.config.get("UGC", "staticUserLog4FrURL"), self.config.get("lang", "zh"),
                                                  self.base.getTimeStamp(),
                                                  self.config.get("clientVersionInfo", "clientVersionInfo_ch_Android"),access_token)
        time.sleep(0.3)
        staticType = 2
        result_static = self.static.send_request_staticUserLog4Fr(staticURL,staticType,created_id)
        self.assertEqual(result_static["stateCode"], 200)
        self.assertEqual(result_static["stateMsg"], "OK")


        #分别对微信，QQ和微博进行转发
        staticType = 3
        shareWayList = [1,2,3]
        for shareWay in shareWayList:
            time.sleep(0.3)
            result_static = self.static.send_request_staticUserLog4Fr(staticURL,staticType,created_id,shareWay)
            self.assertEqual(result_static["stateCode"], 200)
            self.assertEqual(result_static["stateMsg"], "OK")


        #addComment4Fr接口
        addCommentURL = self.addComment.get_addComment4FrURL(self.config.get('imi_base_url_ch', 'base_url_uat'),
                                                  self.config.get("UGC", "addComment4FrURL"), self.config.get("lang", "zh"),
                                                  self.base.getTimeStamp(),

                                                 self.config.get("clientVersionInfo", "clientVersionInfo_ch_Android"),access_token)

        content = self.base.get_random_string(10)*10
        result_addComment = self.addComment.send_request_addComment4Fr(addCommentURL,created_id,content)
        self.assertEqual(result_addComment["stateCode"], 200)
        self.assertEqual(result_addComment["stateMsg"], "OK")

        time.sleep(0.3)
        #getCommentList4Fr接口
        getCommentListURL = self.getCommentList.get_getCommentList4FrURL(self.config.get('imi_base_url_ch', 'base_url_uat'),
                                                  self.config.get("UGC", "getCommentList4FrURL"), self.config.get("lang", "zh"),
                                                  self.base.getTimeStamp(),
                                                 self.config.get("clientVersionInfo", "clientVersionInfo_ch_Android"),access_token)


        result_getCommentList = self.getCommentList.send_request_getCommentList4Fr(getCommentListURL,created_id,currentPage,pageSize)
        self.assertEqual(result_getCommentList["stateCode"], 200)
        self.assertEqual(result_getCommentList["stateMsg"], "OK")


        time.sleep(0.3)
        #addReply4Fr接口
        addReplyURL = self.addReply.get_addReply4FrURL(self.config.get('imi_base_url_ch', 'base_url_uat'),
                                                  self.config.get("UGC", "addReply4FrURL"), self.config.get("lang", "zh"),
                                                  self.base.getTimeStamp(),
                                                 self.config.get("clientVersionInfo", "clientVersionInfo_ch_Android"),access_token)

        commentId = result_getCommentList["data"][0]["id"]
        replyId = commentId
        replyType = 2
        content = self.base.get_random_string(10)*5
        uid = result_getCommentList["data"][0]["uid"]
        toUid = ""
        result_addReply = self.addReply.send_request_addReply4Fr(addReplyURL,commentId,replyId,replyType,content,toUid,uid)
        self.assertEqual(result_addReply["stateCode"], 200)
        self.assertEqual(result_addReply["stateMsg"], "OK")


        time.sleep(0.3)
        #getReplySimpleList4Fr接口
        getReplySimpleListURL = self.getReplySimpleList.get_getCommentList4FrURL(self.config.get('imi_base_url_ch', 'base_url_uat'),
                                                  self.config.get("UGC", "getReplySimpleList4FrURL"), self.config.get("lang", "zh"),
                                                  self.base.getTimeStamp(),
                                                 self.config.get("clientVersionInfo", "clientVersionInfo_ch_Android"),access_token)

        commentId = result_getCommentList["data"][0]["id"]
        result_getReplySimpleList = self.getReplySimpleList.send_request_getReplySimpleList4Fr(getReplySimpleListURL,commentId,currentPage,pageSize)
        self.assertEqual(result_getReplySimpleList["stateCode"], 200)
        self.assertEqual(result_getReplySimpleList["stateMsg"], "OK")

        time.sleep(0.3)
        #deleteArticle4Fr接口
        deleteArticleURL = self.deleteArticle.get_deleteArticle4FrURL(self.config.get('imi_base_url_ch', 'base_url_uat'),
                                                  self.config.get("UGC", "deleteArticle4FrURL"), self.config.get("lang", "zh"),
                                                  self.base.getTimeStamp(),

                                                 self.config.get("clientVersionInfo", "clientVersionInfo_ch_Android"),access_token)
        articleIdList = []
        articleIdList.append(created_id)
        result_deleteArticle = self.deleteArticle.send_request_deleteArticle4Fr(deleteArticleURL,articleIdList)
        self.assertEqual(result_deleteArticle["stateCode"], 200)
        self.assertEqual(result_deleteArticle["stateMsg"], "OK")

    def tearDown(self):
            pass

if __name__ == '__main__':
    unittest.main()



