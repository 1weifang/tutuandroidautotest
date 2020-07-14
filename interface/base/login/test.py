#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/6/4 14:08
# @Author  : Durat
# @Email   : durant.zeng@sunvalley.com.cn
# @File    : pictureUpload.py
# @Software: PyCharm

import sys,os
projectPath = os.path.dirname(os.path.abspath('.'))
# systemSep = os.sep
# conf = projectPath+systemSep+"config"+systemSep+"config.ini"
print(projectPath)

a = projectPath.split("anjouAutoTest")
print(a)


c = ['D:\\interface\\', '\\interface\\base']

bList = c[0].split(os.sep)
print(bList)

for i in bList[0:-1]:
    i = i+os.sep
    print(i)


really = os.sep.join(bList[0:-1])
print(really)


# aList = projectPath.split(os.sep)
# print(aList)
# reallyProject = aList[0]+systemSep+aList[1]
# print(reallyProject)
# a = os.path.abspath('.')
# print(a)

