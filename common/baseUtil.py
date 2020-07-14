#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/5/21 20:50
# @Author  : Durat
# @Email   : durant.zeng@sunvalley.com.cn
# @File    : test.py
# @Software: PyCharm

import hashlib
import time
import datetime
import random
import string
import sys, os
from faker import Faker

class baseUtils:
    def __init__(self):
        pass

    @classmethod
    def MD5(self,str):
        '''
        :param str:
        :return: MD5 encryption
        '''
        m = hashlib.md5()
        b = str.encode(encoding='utf-8')
        m.update(b)
        str_md5 = m.hexdigest()
        return str_md5

    @classmethod
    def getTimeStamp(self):
        '''
        :return: str
        '''
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        tempList = now.split(" ")
        return ("".join(tempList[0].split("-")) + "".join(tempList[1].split(":")))


    def timestamp_to_str(self,timeStamp=None, format='%Y-%m-%d %H:%M:%S'):
        if timeStamp:
            time_tuple = time.localtime(timeStamp)  # 把时间戳转换成时间元祖
            result = time.strftime(format, time_tuple)  # 把时间元祖转换成格式化好的时间
            return result
        else:
            return time.strptime(format)


    def str_to_timestamp(self,str_time=None, format='%Y-%m-%d %H:%M:%S'):
        if str_time:
            time_tuple = time.strptime(str_time, format)  # 把格式化好的时间转换成元祖
            result = time.mktime(time_tuple)  # 把时间元祖转换成时间戳
            return int(result)
        return int(time.time())



    def get_random_string(self,number):
        '''只能产生最多50'''
        ran_str = ''.join(random.sample(string.ascii_letters + string.digits, number))
        return  ran_str


    def get_millisecond(self):
        millis = int(round(time.time() * 1000))
        return millis

    def get_miniRectWidth(self):
        number = random.randint(100,130)
        return number


    def str2int(self,str):
        return int(str)


    def getToDay(self):
        return datetime.date.today()


    def chooseTwoAgentId(self,dict):
        if dict["supplierCompanyName"] == "深圳市丹芽科技":
            return dict["twoAgentId"]
        else:
            return None

    def choosePlan(self,dict):
        if dict["title"] == "美甲机租赁":
            return dict["id"]
        else:
            return None

    def get_random_content(self):
        Myfake = Faker(locale='zh_CN')
        content = Myfake.sentence(nb_words=6, variable_nb_words=True, ext_word_list=None)
        return content


    def getProjectPath(self):
        #projectName = "D:\AutoTest\tutuAndroidAutoTest"
        projectName = "tutuandroidautotest"

        projectPath = os.path.dirname(os.path.abspath('.'))
        aList = projectPath.split(projectName)
        bList = aList[0].split(os.sep)
        reallyProject = os.sep.join(bList[0:-1])+os.sep+projectName
        return reallyProject


    def get_deviceID(self,dict):
        result = []
        try:
            data = dict.get('data')
            for lst in data:
                res = lst.get('sn')
                if res != None:
                    result.append(lst.get('id'))
        except:
            raise Exception('error')
        finally:
            return result

    def get_nailSuitStatus_for_1(self,dict):
        result = []
        try:
            data = dict.get('data')
            for lst in data:
                res = lst.get('nailSuitStatus')
                if res == 1:
                    result.append(lst.get('albumsId'))
        except:
            raise Exception('error')
        finally:
            return result


#     def get_end_time(self,start_time,duration_time)：
#          pass
#
#
#
if __name__ == "__main__":
    BU = baseUtils()
    print(BU.getTimeStamp())
    re = BU.getProjectPath()
    print(re)

#     str = "123456"
#
#     print('MD5加密前为 ：' + str)
#     print('MD5加密后为 ：' + BU.MD5(str))
#
#     re = BU.get_random_string(50)
#     print(re*10)
#
#
#     print(BU.get_millisecond())
#
#     test = BU.get_miniRectWidth()
#     print(test)
#
#     print(BU.getProjectPath())

    # print(BU.getToDay())
    # print(type(BU.getToDay()))




#     mm = {
# 	'stateCode': 200,
# 	'stateMsg': 'OK',
# 	'currentPage': 1,
# 	'pageSize': 15,
# 	'totalNum': 187,
# 	'totalPage': 13,
# 	'data': [{
# 		'albumsId': 'd426909943f249a0b613b516a5ed12f1',
# 		'waterfallFlowUrl': '/tutu/system/20191021112224809_261668.jpg',
# 		'waterfallFlowThumbnailUrl': '/tutu/system/20191021112224809_261668.jpg_360x360.jpg',
# 		'galleryUrl': '/tutu/system/20191021112230120_887818.jpg',
# 		'galleryThumbnailUrl': '/tutu/system/20191021112230120_887818.jpg_500x500.jpg',
# 		'albumsTitle': '骷髅狂欢',
# 		'authorNickname': 'Cony',
# 		'authorHeadPortrait': '/tutu/system/20191021102639725_569239.jpg',
# 		'authorHeadPortraitThumbnail': '/tutu/system/20191021102639725_569239.jpg_100x100.jpg',
# 		'praiseNum': 14,
# 		'booleanPraise': False,
# 		'galleryStandard': '501x501',
# 		'nailSuitStatus': 0
# 	}, {
# 		'albumsId': 'caf08b48224a479da1fd9e0f73e0bace',
# 		'waterfallFlowUrl': '/tutu/system/20191031160749697_082981.jpg',
# 		'waterfallFlowThumbnailUrl': '/tutu/system/20191031160749697_082981.jpg_360x360.jpg',
# 		'galleryUrl': '/tutu/system/20191031160818995_042194.jpg',
# 		'galleryThumbnailUrl': '/tutu/system/20191031160818995_042194.jpg_500x500.jpg',
# 		'albumsTitle': '黑白大咖',
# 		'authorNickname': 'Mona',
# 		'authorHeadPortrait': '/tutu/system/20191031160803074_536204.jpg',
# 		'authorHeadPortraitThumbnail': '/tutu/system/20191031160803074_536204.jpg_100x100.jpg',
# 		'praiseNum': 12,
# 		'booleanPraise': False,
# 		'galleryStandard': '501x501',
# 		'nailSuitStatus': 0
# 	}, {
# 		'albumsId': 'c0f915731cac45379f49e007a0b6f559',
# 		'waterfallFlowUrl': '/tutu/system/20190620144419322_857009.jpg',
# 		'waterfallFlowThumbnailUrl': '/tutu/system/20190620144419322_857009.jpg_240x361.jpg',
# 		'galleryUrl': '/tutu/system/20190620144425738_109728.jpg',
# 		'galleryThumbnailUrl': '/tutu/system/20190620144425738_109728.jpg_501x501.jpg',
# 		'albumsTitle': '自然之风',
# 		'authorNickname': 'Cony',
# 		'authorHeadPortrait': '/tutu/system/20191015151852271_500489.jpg',
# 		'authorHeadPortraitThumbnail': '/tutu/system/20191015151852271_500489.jpg_100x100.jpg',
# 		'praiseNum': 21,
# 		'booleanPraise': False,
# 		'galleryStandard': '501x666',
# 		'nailSuitStatus': 1
# 	}, {
# 		'albumsId': 'bdf8d10c5efb4f29a6b4f460dbf0fedf',
# 		'waterfallFlowUrl': '/tutu/system/20190716114412038_715672.jpg',
# 		'waterfallFlowThumbnailUrl': '/tutu/system/20190716114412038_715672.jpg_240x361.jpg',
# 		'galleryUrl': '/tutu/system/20190716114418634_548148.jpg',
# 		'galleryThumbnailUrl': '/tutu/system/20190716114418634_548148.jpg_501x501.jpg',
# 		'albumsTitle': '草莓樱桃',
# 		'authorNickname': 'Una',
# 		'authorHeadPortrait': '/tutu/system/20190627203208459_480989.jpg',
# 		'authorHeadPortraitThumbnail': '/tutu/system/20190627203208459_480989.jpg_240x361.jpg',
# 		'praiseNum': 46,
# 		'booleanPraise': False,
# 		'galleryStandard': '501x501',
# 		'nailSuitStatus': 1
# 	}, {
# 		'albumsId': 'd01048a172934569b16076be516fa9ec',
# 		'waterfallFlowUrl': '/tutu/system/20190620135942814_919815.jpg',
# 		'waterfallFlowThumbnailUrl': '/tutu/system/20190620135942814_919815.jpg_240x361.jpg',
# 		'galleryUrl': '/tutu/system/20190620135951064_440294.jpg',
# 		'galleryThumbnailUrl': '/tutu/system/20190620135951064_440294.jpg_501x501.jpg',
# 		'albumsTitle': '招财猫猫',
# 		'authorNickname': 'Cony',
# 		'authorHeadPortrait': '/tutu/system/20191015150818268_301613.jpg',
# 		'authorHeadPortraitThumbnail': '/tutu/system/20191015150818268_301613.jpg_100x100.jpg',
# 		'praiseNum': 23,
# 		'booleanPraise': False,
# 		'galleryStandard': '501x666',
# 		'nailSuitStatus': 1
# 	}, {
# 		'albumsId': '0a7307d726884a07b24515bfe4a8bfb4',
# 		'waterfallFlowUrl': '/tutu/system/20190626211750700_362209.jpg',
# 		'waterfallFlowThumbnailUrl': '/tutu/system/20190626211750700_362209.jpg_240x361.jpg',
# 		'galleryUrl': '/tutu/system/20190626211757234_183930.jpg',
# 		'galleryThumbnailUrl': '/tutu/system/20190626211757234_183930.jpg_501x501.jpg',
# 		'albumsTitle': '少女蜻蜓',
# 		'authorNickname': 'Cony',
# 		'authorHeadPortrait': '/tutu/system/20190625222600779_432342.jpg',
# 		'authorHeadPortraitThumbnail': '/tutu/system/20190625222600779_432342.jpg_240x361.jpg',
# 		'praiseNum': 24,
# 		'booleanPraise': False,
# 		'galleryStandard': '501x501',
# 		'nailSuitStatus': 1
# 	}, {
# 		'albumsId': '42655714fc5c4fa488ecef7c811019f2',
# 		'waterfallFlowUrl': '/tutu/system/20190628104630420_623685.jpg',
# 		'waterfallFlowThumbnailUrl': '/tutu/system/20190628104630420_623685.jpg_240x361.jpg',
# 		'galleryUrl': '/tutu/system/20190628104641134_822401.jpg',
# 		'galleryThumbnailUrl': '/tutu/system/20190628104641134_822401.jpg_501x501.jpg',
# 		'albumsTitle': '爱心五连击',
# 		'authorNickname': 'Cony',
# 		'authorHeadPortrait': '/tutu/system/20190625223941164_139129.jpg',
# 		'authorHeadPortraitThumbnail': '/tutu/system/20190625223941164_139129.jpg_240x361.jpg',
# 		'praiseNum': 40,
# 		'booleanPraise': False,
# 		'galleryStandard': '501x666',
# 		'nailSuitStatus': 1
# 	}, {
# 		'albumsId': 'd221536a5add45779b3d9d0c76b63b78',
# 		'waterfallFlowUrl': '/tutu/system/20190620143902731_084768.jpg',
# 		'waterfallFlowThumbnailUrl': '/tutu/system/20190620143902731_084768.jpg_240x361.jpg',
# 		'galleryUrl': '/tutu/system/20190620143908576_560580.jpg',
# 		'galleryThumbnailUrl': '/tutu/system/20190620143908576_560580.jpg_501x501.jpg',
# 		'albumsTitle': '甜美樱桃',
# 		'authorNickname': 'Cony',
# 		'authorHeadPortrait': '/tutu/system/20190426182021380_120204.jpg',
# 		'authorHeadPortraitThumbnail': '/tutu/system/20190426182021380_120204.jpg_240x361.jpg',
# 		'praiseNum': 33,
# 		'booleanPraise': True,
# 		'galleryStandard': '501x666',
# 		'nailSuitStatus': 1
# 	}, {
# 		'albumsId': '48d43bc7df9346ae90dd37036b56c719',
# 		'waterfallFlowUrl': '/tutu/system/20190711155141826_690850.jpg',
# 		'waterfallFlowThumbnailUrl': '/tutu/system/20190711155141826_690850.jpg_240x361.jpg',
# 		'galleryUrl': '/tutu/system/20190711155149702_532305.jpg',
# 		'galleryThumbnailUrl': '/tutu/system/20190711155149702_532305.jpg_501x501.jpg',
# 		'albumsTitle': '绝美玫瑰',
# 		'authorNickname': 'Olia',
# 		'authorHeadPortrait': '/tutu/system/20190626215407676_360132.jpg',
# 		'authorHeadPortraitThumbnail': '/tutu/system/20190626215407676_360132.jpg_240x361.jpg',
# 		'praiseNum': 32,
# 		'booleanPraise': True,
# 		'galleryStandard': '501x501',
# 		'nailSuitStatus': 1
# 	}, {
# 		'albumsId': '42043ce596a7450f9a3f8b88c583f906',
# 		'waterfallFlowUrl': '/tutu/system/20190626141104462_226098.jpg',
# 		'waterfallFlowThumbnailUrl': '/tutu/system/20190626141104462_226098.jpg_240x361.jpg',
# 		'galleryUrl': '/tutu/system/20190626141139617_097778.jpg',
# 		'galleryThumbnailUrl': '/tutu/system/20190626141139617_097778.jpg_501x501.jpg',
# 		'albumsTitle': '岩石里的花',
# 		'authorNickname': 'Cony',
# 		'authorHeadPortrait': '/tutu/system/20190626141117894_191933.jpg',
# 		'authorHeadPortraitThumbnail': '/tutu/system/20190626141117894_191933.jpg_240x361.jpg',
# 		'praiseNum': 17,
# 		'booleanPraise': False,
# 		'galleryStandard': '501x501',
# 		'nailSuitStatus': 1
# 	}, {
# 		'albumsId': 'f32ce881801d48c1902f9838f9645d93',
# 		'waterfallFlowUrl': '/tutu/system/20190711145147044_443676.jpg',
# 		'waterfallFlowThumbnailUrl': '/tutu/system/20190711145147044_443676.jpg_240x361.jpg',
# 		'galleryUrl': '/tutu/system/20190711145223134_451734.jpg',
# 		'galleryThumbnailUrl': '/tutu/system/20190711145223134_451734.jpg_501x501.jpg',
# 		'albumsTitle': '大眼猫咪',
# 		'authorNickname': 'Una',
# 		'authorHeadPortrait': '/tutu/system/20190711145205758_774956.jpg',
# 		'authorHeadPortraitThumbnail': '/tutu/system/20190711145205758_774956.jpg_240x361.jpg',
# 		'praiseNum': 12,
# 		'booleanPraise': False,
# 		'galleryStandard': '501x501',
# 		'nailSuitStatus': 1
# 	}, {
# 		'albumsId': '70fb2bb396974af9b60f2a4d99e0ae5d',
# 		'waterfallFlowUrl': '/tutu/system/20190711180936611_379494.jpg',
# 		'waterfallFlowThumbnailUrl': '/tutu/system/20190711180936611_379494.jpg_240x361.jpg',
# 		'galleryUrl': '/tutu/system/20190711180942447_825015.jpg',
# 		'galleryThumbnailUrl': '/tutu/system/20190711180942447_825015.jpg_501x501.jpg',
# 		'albumsTitle': '樱桃波点',
# 		'authorNickname': 'Cony',
# 		'authorHeadPortrait': '/tutu/system/20190625224153823_938346.jpg',
# 		'authorHeadPortraitThumbnail': '/tutu/system/20190625224153823_938346.jpg_240x361.jpg',
# 		'praiseNum': 26,
# 		'booleanPraise': False,
# 		'galleryStandard': '501x501',
# 		'nailSuitStatus': 1
# 	}, {
# 		'albumsId': '539b227e32134e999187b24293f1579b',
# 		'waterfallFlowUrl': '/tutu/system/20190711143344804_219046.jpg',
# 		'waterfallFlowThumbnailUrl': '/tutu/system/20190711143344804_219046.jpg_240x361.jpg',
# 		'galleryUrl': '/tutu/system/20190711143351580_331525.jpg',
# 		'galleryThumbnailUrl': '/tutu/system/20190711143351580_331525.jpg_501x501.jpg',
# 		'albumsTitle': 'LookAtMe',
# 		'authorNickname': 'Mona',
# 		'authorHeadPortrait': '/tutu/system/20190604170837268_078205.jpg',
# 		'authorHeadPortraitThumbnail': '/tutu/system/20190604170837268_078205.jpg_240x361.jpg',
# 		'praiseNum': 23,
# 		'booleanPraise': False,
# 		'galleryStandard': '501x501',
# 		'nailSuitStatus': 1
# 	}, {
# 		'albumsId': 'a2ca70b1303b4aa4ad5837c2deaf11aa',
# 		'waterfallFlowUrl': '/tutu/system/20190711142411169_589025.jpg',
# 		'waterfallFlowThumbnailUrl': '/tutu/system/20190711142411169_589025.jpg_240x361.jpg',
# 		'galleryUrl': '/tutu/system/20190711142417175_493491.jpg',
# 		'galleryThumbnailUrl': '/tutu/system/20190711142417175_493491.jpg_501x501.jpg',
# 		'albumsTitle': '可爱猫咪',
# 		'authorNickname': 'Carsey',
# 		'authorHeadPortrait': '/tutu/system/20191015152236309_680922.jpg',
# 		'authorHeadPortraitThumbnail': '/tutu/system/20191015152236309_680922.jpg_100x100.jpg',
# 		'praiseNum': 25,
# 		'booleanPraise': False,
# 		'galleryStandard': '501x666',
# 		'nailSuitStatus': 1
# 	}, {
# 		'albumsId': '764f44e47962472a899231da58a432d1',
# 		'waterfallFlowUrl': '/tutu/system/20191024145350284_667988.jpg',
# 		'waterfallFlowThumbnailUrl': '/tutu/system/20191024145350284_667988.jpg_360x360.jpg',
# 		'galleryUrl': '/tutu/system/20191024145406148_551392.jpg',
# 		'galleryThumbnailUrl': '/tutu/system/20191024145406148_551392.jpg_500x500.jpg',
# 		'albumsTitle': 'mongmong万圣节',
# 		'authorNickname': 'Mona',
# 		'authorHeadPortrait': '/tutu/system/20191024145358070_035676.jpg',
# 		'authorHeadPortraitThumbnail': '/tutu/system/20191024145358070_035676.jpg_100x100.jpg',
# 		'praiseNum': 10,
# 		'booleanPraise': False,
# 		'galleryStandard': '501x666',
# 		'nailSuitStatus': 0
# 	}]
# }
#
#     deviceID = BU.get_nailSuitStatus_for_1(mm)
#     print(deviceID)



