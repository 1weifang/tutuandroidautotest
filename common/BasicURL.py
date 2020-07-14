#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/10/8 15:47
# @Author  : Durat
# @Email   : durant.zeng@sunvalley.com.cn
# @File    : getBasicURL.py
# @Software: PyCharm

import sys,os
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from common.Logger import Logger



class BasicURL:

    def __init__(self):
        self.logger = Logger(logger="BasicRUL").getlog()

    def basicURL(self,env):

        param = {
            "mi":"https://mi-api.nailtutu.com",
            "usami":"https://usa-mi-api.nailtutu.com",
            "env":"https://env-proxy.nailtutu.com/api"
        }

        if env == "prod":
            return param
        elif env == "uat":
            param["mi"]="https://mi-api-uat.nailtutu.com"
            param["usami"] = "https://usa-mi-api-uat.nailtutu.com"
            param["env"] = "https://env-proxy-uat.nailtutu.com/api"
            return param
        elif env == "dev":
            param["mi"]="https://mi-api-dev.nailtutu.com"
            param["usami"] = "https://usa-mi-api-dev.nailtutu.com"
            param["env"] = "https://env-proxy-dev.nailtutu.com/api"
            return param
        else:
            self.logger.error("您传入的参数有误,请检查！")

if __name__ == "__main__":
    base = BasicURL()
    env = "dev"
    data = base.basicURL(env)
    print(data)
    print(data["mi"])
    print(data["usami"])
    print(data["env"])




