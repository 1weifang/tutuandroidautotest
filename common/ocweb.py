#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/9/5 13:45
# @Author  : Durat
# @Email   : durant.zeng@sunvalley.com.cn
# @File    : ocweb.py
# @Software: PyCharm

import sys,os
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
import json
import requests
from common.Logger import Logger
from common.baseUtil import baseUtils
base = baseUtils()

class ocweb:

    def __init__(self):
        self.logger = Logger(logger="ocweb").getlog()

    def get_ocweb_url(self,env):
        '''
        :param env:
        :return:
        '''
        if env == "prod":
            url = "https://oc-api.nailtutu.com/oauth/login"
            self.logger.info("oc_web登录的url为：%s" %url)
        elif env == "uat":
            url = "https://oc-api-uat.nailtutu.com/oauth/login"
            self.logger.info("oc_web登录的url为：%s" % url)
        elif env == "dev":
            url = "https://oc-api-dev.nailtutu.com/oauth/login"
            self.logger.info("oc_web登录的url为：%s" % url)
        else:
            self.logger.error("配置有误，请检查！")
        return url

    def get_ocweb_logged_in(self, email, password):
        '''
        :param email:
        :param password:
        :return:
        '''
        ocweb_logged_in = {
            "client_id": "d6165bbf3d804c6196c0c6d7201de970",
            "client_secret": "25f9e794323b453885f5181f1b624d0b",
            "scope": "all",
            "grant_type": "password",
            "email": email,
            "password": base.MD5(password),
            "auth_type": "email_password"
        }
        self.logger.info("账号【%s】开始登录oc_web......" %email)
        return ocweb_logged_in


    def send_request_ocweb_login(self,url,data):
        '''
        :param url:
        :param data:
        :return:
        '''
        headers = {"Content-Type": "application/json"}
        self.logger.info("请求的参数为:%s" %data)
        r = requests.post(url, data=json.dumps(data), headers=headers)
        self.logger.info("返回的参数为:%s" % json.loads(r.text))
        return json.loads(r.text)

if __name__ == "__main__":
    oc = ocweb()
    env = "uat"
    email = "durant.zeng@sunvalley.com.cn"
    password = "123456"
    url = oc.get_ocweb_url(env)
    data = oc.get_ocweb_logged_in(email,password)
    oc.send_request_ocweb_login(url,data)

    # print(result["data"])
    # print(type(result["data"]))






