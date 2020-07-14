#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/6/17 20:38
# @Author  : Durat
# @Email   : durant.zeng@sunvalley.com.cn
# @File    : testList.py
# @Software: PyCharm



# a = "AD87B9A75DCB55A083AF4B5039122220"
#
# print(str.lower(a))


# 多国语言lang对应国家与编码:
# 中国  zh_CN
# 中国台湾 zh_TW
# 英文  en
# 德文    de
# 法文    fr
# 意大利文  it
# 日文      ja
# 西班牙文 es

from faker import Faker

fake = Faker("en")


while True:
    test = fake.email()
    print(test)
