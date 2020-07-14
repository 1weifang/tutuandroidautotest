#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/5/21 20:50
# @Author  : Durat
# @Email   : durant.zeng@sunvalley.com.cn
# @File    : test.py
# @Software: PyCharm

# import sys
# from importlib import reload
# reload(sys)
# import os
# path = os.path.normpath(os.path.join(os.path.join(os.path.dirname(__file__), '../../../../')))
# # sys.setdefaultencoding('utf-8')
# sys.getdefaultencoding()
# sys.path.append(path)


import sys,os
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from configparser import ConfigParser
from common.Logger import Logger



class FileParser:

    def __init__(self, fileName):
        '''
        :param fileName:
        '''
        self.logger = Logger(logger="FileParser").getlog()
        try:
            self.config = ConfigParser()
            self.config.read(fileName, encoding='utf-8')
        except:
            self.logger.exception('文件名不存在,请检查配置!')




    def get(self, section, option):
        '''
        :param section:
        :param option:
        :return:value
        '''
        # 获取对应环境的配置信息，使用get('env',url)
        # if section == 'env':
        #     section = self.config.get(section, 'env')
        #     return self.config.get(section, option)
        return self.config.get(section, option)


if __name__ == "__main__":
    config = FileParser(r'D:\test\containerTest\tutuandroidautotest\config\config.ini')
    dev = config.get('imi_base_url_ch', 'base_url_dev_k8s')
    print(dev)


