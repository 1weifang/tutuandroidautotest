#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/2/26 10:09
# @Author  : Durat
# @Email   : durant.zeng@sunvalley.com.cn
# @File    : batch.py
# @Software: PyCharm


import sys,os
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
import json
import requests
from common.Logger import Logger
import warnings
from retrying import retry

def _result(result):
    return result is None




class batch:


    def __init__(self):
        self.logger = Logger(logger="batch").getlog()
        warnings.simplefilter("ignore", ResourceWarning)


    def get_batchURL(self,baseURL,URL,lang,timeStamp,clientVersionInfo,access_token):
        '''
        :param baseURL:
        :param lang:
        :param timeStamp:
        :param clientVersionInfo:
        :return:上传-批量-图片
        '''
        reallyURL = baseURL + URL + "?lang=%s&timeStamp=%s&clientVersionInfo=%s&access_token=%s" % (lang, timeStamp, clientVersionInfo,access_token)
        self.logger.info("url为:%s" %reallyURL)
        return reallyURL



    # def send_request_batch(self,url,file,directory):
    #     '''
    #     :param url:
    #     :param content:
    #     :return:
    #     '''
    #     headers = {"Content-Type": "multipart/form-data"}
    #     # parameters = {
    #     #     "file": file,
    #     #     "directory":directory
    #     #          }
    #     files = {"file": (file, open(directory, "rb"), "multipart/form-data", {})}
    #
    #     self.logger.info("请求的参数为:%s" %files)
    #     r = requests.post(url, files=files,timeout=30)
    #     self.logger.info("返回的参数为:%s" % json.loads(r.text))
    #     return json.loads(r.text)



    # def post_files(self,url, header, data, filename, filepath):
    #     """
    #         :param files: (optional) Dictionary of ``'name': file-like-objects`` (or ``{'name': file-tuple}``) for multipart encoding upload.
    #         ``file-tuple`` can be a 2-tuple ``('filename', fileobj)``, 3-tuple ``('filename', fileobj, 'content_type')``
    #         or a 4-tuple ``('filename', fileobj, 'content_type', custom_headers)``, where ``'content-type'`` is a string
    #         defining the content type of the given file and ``custom_headers`` a dict-like object containing additional headers
    #         to add for the file.
    #     """
    #     data['file'] = (filename, open(filepath, 'rb').read())
    #     encode_data = encode_multipart_formdata(data)
    #     data = encode_data[0]
    #     header['Content-Type'] = encode_data[1]
    #     r = requests.post(url, headers=header, data=data)
    #     print(r.content)



    @retry(stop_max_attempt_number=5, wait_random_min=1000, wait_random_max=2000, retry_on_result=_result)
    def send_request_batch(self,url,fileName,filepath,directory=None):
        '''

        :param url:
        :param filename:
        :param filepath:
        :return:
        '''

        custom_headers = {

        }
        files = {"files": (fileName, open(filepath, "rb"), "multipart/form-data", custom_headers)}

        upload_data = {"targetid":"48d1cd1ef8d846d98897cf68f12dba01",
                "sizeswidthHeights":"20000:240:360",
                "proportion":"0",
                "directory":directory}

        self.logger.info("请求参数为%s" %upload_data)
        r = requests.request("post",url,data = upload_data,files=files,timeout=30)
        re = r.text
        josnre = json.loads(re)
        self.logger.info("返回值为：%s" %josnre)
        return json.loads(re)



# if __name__ == "__main__":



