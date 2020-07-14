#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/5/21 20:50
# @Author  : Durat
# @Email   : durant.zeng@sunvalley.com.cn
# @File    : redisUtils.py
# @Software: PyCharm

import sys,os
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
import redis
import time
from common.Logger import Logger
logger = Logger(logger="redisUtils").getlog()
from common.FileParsing import FileParser


class redisUtils:

    def __init__(self,host,port,password):
        try:
            self.pool = redis.ConnectionPool(host=host, port=port,password=password,db=0)
            self.conn = redis.Redis(connection_pool=self.pool)
        except redis.ConnectionError as e:
            logger.exception('Connected failed:%s'%e)

    def set(self,key,value):
        self.conn.set(key, value)

    def get(self,key):
        pipe = self.conn.pipeline(transaction=True)
        return self.conn.get(key)
        pipe.execute()

    def delete(self,key):
        return self.conn.delete(key)

    def isKeyExists(self,name):
        '''判断key是否存在'''
        return self.conn.exists(name)

    def bitcount(self,key):
        return self.conn.bitcount(key)

    def get_value(self,Key):
        '''60秒拿特定key的值'''
        # redisValue = {}
        seconds = 60
        count = 0
        while (count < seconds):
            count += 1
            n = seconds - count
            logger.info('remain %s seconds' % n)
            time.sleep(1)
            redisValue = self.get(Key.strip())
            if redisValue:
                break
        if redisValue:
            logger.info('此规则的key为:%s,值为: %s' % (Key, redisValue))
        else:
            logger.exception('此规则的key为:%s,值为: %s' % (Key, redisValue))
        return redisValue


if __name__ == "__main__":
    config = FileParser(r'D:\anjouAutoTest\config\config.ini')
    host = config.get('redis_dev', 'host')
    port = config.get('redis_dev', 'port')
    password = config.get('redis_dev', 'password')


    print(host,port,password)


    r = redisUtils(host,port,password)
    # r.set("test","1")
    # print(r.get("test"))
    # # print(r)
    #
    key = 'register:sms:verify:code:13417335080'
    #
    re = r.get_value(key)
    print(type(re))

    a = str(re,encoding="utf-8")
    print(a)
    print(type(a))