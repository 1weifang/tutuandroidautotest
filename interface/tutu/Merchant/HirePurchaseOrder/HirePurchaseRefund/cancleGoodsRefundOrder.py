#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/10/15 15:13
# @Author  : Durat
# @Email   : durant.zeng@sunvalley.com.cn
# @File    : cancleGoodsRefundOrder.py
# @Software: PyCharm


import sys,os
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
import json
import requests
from common.Logger import Logger



class cancleGoodsRefundOrder:

    def __init__(self):
        self.logger = Logger(logger="cancleGoodsRefundOrder").getlog()

    def get_cancleGoodsRefundOrderURL(self,baseURL,URL,lang,timeStamp,access_token):
        '''
        :param baseURL:
        :param lang:
        :param timeStamp:
        :param clientVersionInfo:
        :return:出租退货退款-撤销退货退款
        '''
        reallyURL = baseURL + URL + "?lang=%s&timeStamp=%s&access_token=%s" % (lang, timeStamp, access_token)
        self.logger.info("url为:%s" %reallyURL)
        return reallyURL


    def send_request_cancleGoodsRefundOrder(self,url,refundNo):
        '''
        :param url:
        :param content:
        :return:
        '''
        headers = {"Content-Type": "application/json"}
        parameters = {
                        "refundNo": refundNo
                            }
        self.logger.info("请求的参数为:%s" %parameters)
        r = requests.post(url, data=json.dumps(parameters), headers=headers,timeout=30)
        self.logger.info("返回的参数为:%s" % json.loads(r.text))
        return json.loads(r.text)


if __name__ == '__main__':
    cancel = cancleGoodsRefundOrder()
    url = "https://mi-api.nailtutu.com/imi/orderGoodsRefund/cancleGoodsRefundOrder?lang=zh&timeStamp=1573540323674&access_token=4f79cc97-0e50-4434-9ba2-5eeaaf212563"
    refundNo = "12643852590009810944"
    cancel.send_request_cancleGoodsRefundOrder(url,refundNo)

