#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/5/21 20:58
# @Author  : Durat
# @Email   : durant.zeng@sunvalley.com.cn
# @File    : mysqlUtils.py
# @Software: PyCharm

import sys,os
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from pymysql import connect,cursors
from pymysql.err import OperationalError
from builtins import int
import time
from common.FileParsing import FileParser
from common.Logger import Logger
logger = Logger(logger="mysqlUtils").getlog()



class mysqlUtils:

    #构造函数
    def __init__(self,host,port,user,password,db):
        '''
        :param host:
        :param port:
        :param user:
        :param password:
        :param db:
        '''
        try:
            self.conn = connect(host=host,
                                port=int(port),
                                user=user,
                                password=password,
                                db=db,
                                charset='utf8mb4',
                                cursorclass=cursors.DictCursor
                                )
        except OperationalError as e:
            print(e)

    def cursor(self):
        '''
        获得游标
        '''
        self.conn.cursor()

    def getDict(self):
        '''
        公共方法，获取id的字典
        '''
        with self.conn.cursor() as cursor:
            cursor.execute("select *  from t_oc_tag_info ")
        Dict = cursor.fetchone()
        self.conn.commit()
        logger.info("成功")
        return Dict

    def delete_user_info(self,mobile):
        '''
        :param mobile:
        :return:
        '''
        type = "mobile"
        with self.conn.cursor() as cursor:
            cursor.execute("delete from user_auth_info WHERE type = %s  and uniqueid = %s ",(type,mobile))
            logger.info("在user_auth_info表中删除mobile为%s的记录" % mobile)
            time.sleep(2)
            cursor.execute("delete FROM user_info WHERE mobile = %s ", (mobile))
            logger.info("在user_info表中删除mobile为%s的记录" % mobile)
        self.conn.commit()

    # def get_Total_Recommend(self):
    #     '''
    #     :return: 获取热门推荐标签中已发布的总数
    #     '''
    #     with self.conn.cursor() as cursor:
    #         cursor.execute("SELECT id from t_oc_tag_info where tag_name = %s", (tagName))

    def get_tagId(self,tagName):
        '''
        :param tagName:
        :return: 获取标签ID,str
        '''
        with self.conn.cursor() as cursor:
            cursor.execute("SELECT id from t_oc_tag_info where tag_name = %s",(tagName))
        Dict = cursor.fetchone()
        self.conn.commit()
        logger.info("获取标签【%s】的id成功,ID为%s" %(tagName,Dict["id"]))
        return Dict["id"]

    def get_tagName_totalNum(self,tag_id):
        '''
        :param tag_id:
        :return:
        '''
        gallery_status = "6"
        with self.conn.cursor() as cursor:
            cursor.execute("SELECT * from t_oc_gallery_info a,(SELECT * FROM t_oc_gallery_tag_rel  WHERE tag_id = %s ) as b WHERE a.id = b.gallery_id  and a.gallery_status =%s",(tag_id,gallery_status))
        Dict = cursor.fetchall()
        tag_totalNum = len(Dict)
        self.conn.commit()
        return tag_totalNum



    def get_lastest_galleryINFO(self):
        '''
        :return: 获取最近一张照片的ID和galleryStatus
        '''
        with self.conn.cursor() as cursor:
            cursor.execute("SELECT id,gallery_status from t_oc_gallery_info ORDER BY create_time desc ")
        Dict = cursor.fetchone()
        self.conn.commit()
        logger.info(Dict)
        return Dict

    def get_t_oc_gallery_INFO(self,id):
        '''
        :param id:
        :return: 根据图片ID去获取图片信息
        '''
        with self.conn.cursor() as cursor:
            cursor.execute("SELECT * from t_oc_gallery_info where id = %s",(id))
        Dict = cursor.fetchone()
        self.conn.commit()
        logger.info(Dict)
        return Dict

    def get_t_oc_gallery_info_collect_INFO(self,id):
        '''
        :param id:
        :return: 根据图片ID去获取图片信息
        '''
        with self.conn.cursor() as cursor:
            cursor.execute("SELECT * from t_oc_gallery_info_collect where gallery_id = %s",(id))
        Dict = cursor.fetchone()
        self.conn.commit()
        logger.info(Dict)
        return Dict


    def delete_gallery(self,id):
        '''
        :param id:
        :return: 根据图片ID去删除图片
        '''
        with self.conn.cursor() as cursor:
            cursor.execute("delete from t_oc_gallery_info where id = %s",(id))
            logger.info("在t_oc_gallery_info表中删除id为%s的记录" %id)
        self.conn.commit()


    def delete_gallery_collection(self,id):
        '''
        :param id:
        :return: 根据图片ID去删除图片
        '''
        with self.conn.cursor() as cursor:
            cursor.execute("delete from  t_oc_gallery_info_collect where gallery_id = %s",(id))
            logger.info("在 t_oc_gallery_info_collect表中删除gallery_id为%s的记录" %id)
        self.conn.commit()

    def get_userUpload_totalNumber(self):
        '''
        :return: 获取用户上传的总数
        '''
        gallery_type ="2"
        gallery_status = "3"
        with self.conn.cursor() as cursor:
            cursor.execute("SELECT * FROM t_oc_gallery_info  WHERE gallery_type = %s AND gallery_status = %s ORDER BY create_time desc",(gallery_type,gallery_status))
        list_result = cursor.fetchall()
        Total = len(list_result)
        self.conn.commit()
        return Total


    def get_gallery_userUpload_first(self):
        '''
        :return: 获取用户上传的彩绘图案的第一条
        '''
        gallery_type ="2"
        gallery_status = "3"
        with self.conn.cursor() as cursor:
            cursor.execute("SELECT * FROM t_oc_gallery_info  WHERE gallery_type = %s AND gallery_status = %s ORDER BY create_time desc",(gallery_type,gallery_status))
        list_result = cursor.fetchall()
        self.conn.commit()
        return list_result[0]["id"]


    def get_gallery_userUpload_second(self):
        '''
        :return: 获取用户上传的彩绘图案的第二条
        '''
        gallery_type ="2"
        gallery_status = "3"
        with self.conn.cursor() as cursor:
            cursor.execute("SELECT * FROM t_oc_gallery_info  WHERE gallery_type = %s AND gallery_status = %s ORDER BY create_time desc",(gallery_type,gallery_status))
        list_result = cursor.fetchall()
        self.conn.commit()
        return list_result[1]["id"]


    def insertInto_autoTest_record(self,area,system_type,business_type,task_name,start_time,end_time,exe_result,create_time,duration,exe_result_content):
        '''
        每次执行任务，都往表里插入一条执行记录
        :param taskName:
        :param startTime:
        :param endTime:
        :param exe_result:
        :return:
        '''
        with self.conn.cursor() as cursor:
            cursor.execute("INSERT INTO t_auto_test_exe_record (area,system_type,business_type,task_name,start_time,end_time,exe_result,create_time,duration,exe_result_content) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(area,system_type,business_type,task_name,start_time,end_time,exe_result,create_time,duration,exe_result_content))
        print("往表【t_auto_test_exe_record】插入记录成功")
        self.conn.commit()
        self.conn.close()


    def is_exist_gallery_id_in_collection(self):
        '''检查图片在t_oc_gallery_info_collect表是否存在'''
        pass


    #
    # def AttentionLibraryDelete(self, system_id, merchant_id):
    #         '''非正常删除数据,即直接操作数据库删除'''
    #
    #     with self.conn.cursor() as cursor:
    #         cursor.execute("delete  from tableName where system_id = %s and merchant_id = %s;",
    #                        (system_id, merchant_id))
    #     self.conn.commit()
    #



    def close(self):
        '''
        关闭mysql数据库
        '''

        self.conn.close()

if __name__ == "__main__":
    config = FileParser(r'D:\anjouAutoTest\config\config.ini')
    host = config.get('mysql_dev', 'host')
    port = config.get('mysql_dev', 'port')
    user = config.get('mysql_dev', 'user')
    password = config.get('mysql_dev', 'password')
    db_platform = config.get('mysql_dev', 'db_platform')

    # tableName = "t_oc_tag_info"
    mysql = mysqlUtils(host,port,user,password,db_platform)

    print(mysql)
    #
    # task_name = "Anjou接口自动化测试"
    # start_time = "2020-02-18 18:52:12"
    # end_time = "2020-02-18 18:58:12"
    #
    # exe_result = 1
    #
    # mysql.insertInto_autoTest_record(task_name,start_time,end_time,exe_result)


    # tag_name = "热门推荐"
    # re = mysql.get_tagId(tag_name)
    # print(re)

    # re1 = mysql.get_hot_totalNum(re)
    # print(type(re1))



    # mobile = "13417335080"
    # mysql.delete_user_info(mobile)



    # print(mysql)
    # print(mysql.getDict())

    # tagName = "几何色块"
    # re = mysql.get_tagId(tagName)

    # id = "46e513ff4901405db30ca3c66563905b"
    # re = mysql.get_t_oc_gallery_info_collect_INFO(id)
    # print(type(re))

    # test = mysql.get_gallery_userUpload_totalNumber()
    # print(test)

    # re = mysql.get_gallery_userUpload_first()
    # print(type(re))









