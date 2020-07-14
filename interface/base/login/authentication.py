#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/5/21 20:50
# @Author  : Durat
# @Email   : durant.zeng@sunvalley.com.cn
# @File    : test.py
# @Software: PyCharm

import sys,os
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
import requests
import json
from common.baseUtil import baseUtils
from common.Logger import Logger

base = baseUtils()

class Authentication:

	def __init__(self):
		self.logger = Logger(logger="Authentication").getlog()



	def get_Android_CN_Not_logged_in(self):
		'''
		:return:ok
		'''
		Android_CN_Not_logged_in = {
									"client_id": "72e4664b6055411284eb3f9dc14fb280",
									"client_secret": "27cb32fd6113b86ab989d6f08618c202",
									"device_name": "ANDROID",
									"scope": "all",
									"grant_type": "client_credentials",
									"imei": "5155515454444"
									}
		self.logger.info("Android_CN鉴权的参数为%s"%Android_CN_Not_logged_in)
		return Android_CN_Not_logged_in



	def get_test_IOS_client_Not_logged_in(self):
		'''
		:return:ok
		'''
		IOS_CN_Not_logged_in = {
									"client_id": "a62d47e603b64b059755fa84c500753d",
									"client_secret": "add30a6f69614900a73a5d6814950954",
									"device_name": "ios",
									"scope": "all",
									"grant_type": "client_credentials",
									"imei": "5155515454444"
									}
		self.logger.info("鉴权的参数为%s"%IOS_CN_Not_logged_in)
		return IOS_CN_Not_logged_in



	def get_Android_CN_logged_in(self,mobile,password,countryCode=None):
		'''
		:param mobile:ok
		:return:
		'''

		Android_CN_logged_in = {
								"auth_type": "mobile_password",
								"client_id": "72e4664b6055411284eb3f9dc14fb280",
								"client_secret": "27cb32fd6113b86ab989d6f08618c202",
								"device_name": "ANDROID",
								"grant_type": "password",
								"imei": "560689945444355",
								"mobile": mobile,
								"password": base.MD5(password),
								"scope": "all"
								}
		if countryCode:
			self.logger("美甲涂涂移动Android端的鉴权参数为%s" %Android_CN_logged_in)
			Android_CN_logged_in["countryCode"] = countryCode
			self.logger.info("账号:%s开始登录......" % mobile)
			return Android_CN_logged_in
		else:
			self.logger.info("账号:%s开始登录......" % mobile)
			return Android_CN_logged_in


	def get_Android_CN_sms_logged_in(self,mobile,verify_code):
		'''
		:param mobile:ok
		:return:
		'''
		Android_CN_logged_in = {
								"auth_type": "mobile_verify_code",
								"client_id": "72e4664b6055411284eb3f9dc14fb280",
								"client_secret": "27cb32fd6113b86ab989d6f08618c202",
								"device_name": "anjou_android_app",
								"grant_type": "password",
								"imei": "a000006d937c5f",
								"mobile": mobile,
								"scope": "all",
								"verify_code": verify_code
								}

		self.logger.info("账号:%s开始登录......" % mobile)
		return Android_CN_logged_in



	def get_Android_EN_Not_logged_in(self):
		'''
		:return:
		'''
		Android_EN_Not_logged_in = {
									"client_id": "1ee50af9e9194d999583bf64224074bc",
									"client_secret": "7c172a92fd38428a57902f77c05e2bf3",
									"scope": "all",
									"grant_type": "client_credentials"
									}

		self.logger.info("Android_EN_Not_logged_in参数的值为:%s" % Android_EN_Not_logged_in)
		return Android_EN_Not_logged_in



	def get_Android_EN_logged_in(self,email,password):
		'''
		:param email:
		:param password:
		:return:
		'''
		Android_EN_logged_in = {
								"auth_type": "email_password",
								"client_id": "1ee50af9e9194d999583bf64224074bc",
								"client_secret": "7c172a92fd38428a57902f77c05e2bf3",
								"device_name": "ANDROID",
								"email": email,
								"grant_type": "password",
								"imei": "864588030495393",
								"password": base.MD5(password),
								"scope": "all"
								}
		self.logger("anjou移动Android端的鉴权参数为%s" % Android_EN_logged_in)
		self.logger.info("账号:%s开始登录......" % email)
		return Android_EN_logged_in



	def get_Applets_Merchant_logged_in(self,phone,password):
		'''
		:param phone:
		:param password:
		:return:
		'''
		SmallProgram_ZH_logged_in = {
								"client_id": "e230de4a1a64452c89919b1341f7229a",
								"client_secret": "c3d72eb29df7fd295b734c24f1e8aa43",
								"grant_type":"password",
								"mobile": phone,
								"password": base.MD5(password),
								"auth_type": "mobile_password",
								"scope": "all",
								"product_line_id": "46981435671117824",
								"imei": "IMEI_1568613543758",
								"device_name": "EVA-AL10"
								}
		self.logger.info("美甲涂涂小程序商户端鉴权的参数为%s" % SmallProgram_ZH_logged_in)
		return SmallProgram_ZH_logged_in


	def get_Applets_ordinary_logged_in(self,phone,password):
		'''
		:param phone:
		:param password:
		:return:
		'''
		SmallProgram_ZH_logged_in = {
								"client_id": "f9c8218ff78a4e8daa6f014b20c61be2",
								"client_secret": "c3d72eb29df7fd295b734c24f1e8aa43",
								"grant_type":"password",
								"mobile": phone,
								"password": base.MD5(password),
								"auth_type": "mobile_password",
								"scope": "all",
								"product_line_id": "46981435671117824",
								"imei": "IMEI_1568613543758",
								"device_name": "EVA-AL10"
								}
		self.logger.info("美甲涂涂小程序普通端鉴权的参数为%s" % SmallProgram_ZH_logged_in)
		return SmallProgram_ZH_logged_in


	def get_IOS_CN_Not_logged_in(self):
		'''
		:return:ok
		'''
		IOS_CN_Not_logged_in = {
									"client_id": "e79661c27154473eaf5f3136b7587518",
									"client_secret": "78163c4521ed8490a967db3bd4dae48a",
									"scope": "all",
									"grant_type": "client_credentials"
									}
		self.logger.info("IOS_CN_Not_logged_in参数的值为:%s" % IOS_CN_Not_logged_in)
		return IOS_CN_Not_logged_in


	def get_IOS_CN_logged_in(self,mobile,password):
		'''
		:param mobile:
		:return:ok
		'''

		IOS_CN_logged_in = {
							"mobile": mobile,
							"password": base.MD5(password),
							"device_name": "anjou_ios_app",
							"imei": "2A0E951B-CABD-42D8-AC72-B00D1B0C46EA",
							"scope": "all",
							"grant_type": "password",
							"client_secret": "78163c4521ed8490a967db3bd4dae48a",
							"client_id": "e79661c27154473eaf5f3136b7587518",
							"auth_type": "mobile_password"
							}

		self.logger.info("美甲涂涂移动IOS端鉴权的参数为%s" % IOS_CN_logged_in)
		self.logger.info("账号:%s开始登录......" % mobile)
		return IOS_CN_logged_in


	def get_IOS_EN_Not_logged_in(self):
		'''
		:return:
		'''
		IOS_EN_Not_logged_in = {
									"client_id": "4b61e3634c364384ab26e25ac856058d",
									"client_secret": "dfc7098421aed0c1348d063ddf134a83",
									"scope": "all",
									"grant_type": "client_credentials"
									}
		self.logger.info("IOS_EN_Not_logged_in参数的值为:%s" % IOS_EN_Not_logged_in)
		return IOS_EN_Not_logged_in


	def get_IOS_EN_logged_in(self,email,password):
		'''
		:param mobile:
		:return:
		'''
		IOS_EN_logged_in = {
								"auth_type": "email_password",
								 "client_id": "4b61e3634c364384ab26e25ac856058d",
								 "client_secret": "dfc7098421aed0c1348d063ddf134a83",
								 "device_name": "anjou_IOS_app",
								 "grant_type": "password",
								 "imei": "317813771187541",
								 "email": email,
								 "password": base.MD5(password),
								 "scope": "all"
								}
		self.logger.info("anjou移动IOS端鉴权的参数为%s" % IOS_EN_logged_in)
		self.logger.info("账号:%s开始登录......" % email)
		return IOS_EN_logged_in


	def get_PAD_Not_logged_in(self):
		'''
		:return:
		'''
		PAD__Not_logged_in = {
									"client_id": "d4909d4e5c40467ebdef591e7e161a0a",
									"client_secret": "cdec037307bb368dd4da842e8829b2e1",
									"device_channel_id": "ClientId_Pad_App_CN_e4937a14f91c05a3",
									"device_name": "PAD",
									"grant_type": "client_credentials",
									"imei": "e4937a14f91c05a3",
									"scope": "all"
									}
		self.logger.info("PAD_Not_logged_in参数的值为:%s" % PAD__Not_logged_in)
		return PAD__Not_logged_in


	def get_PAD_Not_logged_in_25_30(self):
		'''
		:return:
		'''
		PAD_Not_logged_in = {
									"client_id": "d4909d4e5c40467ebdef591e7e161a0a",
									"client_secret": "cdec037307bb368dd4da842e8829b2e1",
									"device_name": "Anjou_Pad",
									"grant_type": "client_credentials",
									"imei": "521912129226407",
									"scope": "all"
									}
		self.logger.info("PAD_Not_logged_in参数的值为:%s" % PAD_Not_logged_in)
		return PAD_Not_logged_in




	def get_PAD_CN_logged_in(self,mobile,password,countryCode=None,version=None):
		'''
		:param mobile:
		:return:
		'''
		PAD_CN_logged_in = {
							"auth_type": "mobile_password",
							"client_id": "d4909d4e5c40467ebdef591e7e161a0a",
							"client_secret": "cdec037307bb368dd4da842e8829b2e1",
							"device_name": "pad",
							"grant_type": "password",
							"imei": "e4937a14f91c05a3",
							"mobile": mobile,
							"password": base.MD5(password),
							"scope": "all"
							}
		# if countryCode:
		# 	PAD_CN_logged_in["countryCode"] = countryCode
		# 	logger.info("请求的参数为：%s" % PAD_CN_logged_in)
		# 	logger.info("账号:%s开始登录......" % mobile)
		# 	return PAD_CN_logged_in
		if version == "01.00.25":
			PAD_CN_logged_in["imei"] = "986151127149663"
			self.logger.info("请求的参数为：%s" % PAD_CN_logged_in)
			self.logger.info("账号:%s开始登录......" % mobile)
			return PAD_CN_logged_in
		elif version == "01.00.18":
			PAD_CN_logged_in["imei"] = "808678559873015"
			self.logger.info("请求的参数为：%s" % PAD_CN_logged_in)
			self.logger.info("账号:%s开始登录......" % mobile)
			return PAD_CN_logged_in
		else:
			self.logger.info("请求的参数为：%s" %PAD_CN_logged_in)
			self.logger.info("账号:%s开始登录......" % mobile)
			return PAD_CN_logged_in

	def get_PAD_CN_logged_in_countryCode(self,mobile,password,countryCode=None):
		'''
		:param mobile:
		:return:
		'''
		PAD_CN_logged_in = {
							"auth_type": "mobile_password",
							"client_id": "d4909d4e5c40467ebdef591e7e161a0a",
							"client_secret": "cdec037307bb368dd4da842e8829b2e1",
							"device_name": "pad",
							"grant_type": "password",
							"imei": "e4937a14f91c05a3",
							"mobile": mobile,
							"password": base.MD5(password),
							"scope": "all"
							}
		if countryCode:
			PAD_CN_logged_in["countryCode"] = countryCode
			self.logger.info("请求的参数为：%s" % PAD_CN_logged_in)
			self.logger.info("账号:%s开始登录......" % mobile)
			return PAD_CN_logged_in
		else:
			self.logger.info("请求的参数为：%s" %PAD_CN_logged_in)
			self.logger.info("账号:%s开始登录......" % mobile)
			return PAD_CN_logged_in


	def get_PAD_CN_logged_in_email(self,email,password):
		'''
		:param email:
		:return:
		'''
		PAD_CN_logged_in = {
							"auth_type": "email_password",
							"client_id": "d4909d4e5c40467ebdef591e7e161a0a",
							"client_secret": "cdec037307bb368dd4da842e8829b2e1",
							"device_name": "PAD",
							"grant_type": "password",
							"email": email,
							"imei": "e4937a14f91c05a3",
							"password": base.MD5(password),
							"scope": "all"
							}

		self.logger.info("请求的参数为：%s" % PAD_CN_logged_in)
		self.logger.info("账号:%s开始登录......" % email)



	def get_PAD_CN_scan_code_logged_in(self,qr_code):
		'''
		:param qr_code:
		:return:
		'''
		PAD_CN_logged_in = {
							"auth_type": "scan_code",
							"client_id": "d4909d4e5c40467ebdef591e7e161a0a",
							"client_secret": "cdec037307bb368dd4da842e8829b2e1",
							"device_name": "PAD",
							"grant_type": "password",
							"imei": "e4937a14f91c05a3",
							"qr_code": qr_code,
							"scope": "all"
							}

		self.logger.info("pad端扫码登录请求的参数为%s" % PAD_CN_logged_in)
		return PAD_CN_logged_in


	def get_PAD_EN_Not_logged_in(self):
		'''
		:return:
		'''
		PAD_EN_Not_logged_in = {
									"client_id": "dfd558847f184e8e844971764e510661",
									"client_secret": "902457d20226393bda22a95124ea6620",
									"scope": "all",
									"grant_type": "client_credentials"
									}
		self.logger.info("PAD_EN_Not_logged_in参数的值为:%s" % PAD_EN_Not_logged_in )
		return PAD_EN_Not_logged_in



	def get_PAD_EN_logged_in(self,email,password,version = None):
		'''
		:param email:
		:param password:
		:return:
		'''
		PAD_EN_logged_in = {
								"auth_type": "email_password",
								"client_id": "dfd558847f184e8e844971764e510661",
								"client_secret": "902457d20226393bda22a95124ea6620",
								"device_name": "pad",
								"email": email,
								"grant_type": "password",
								"imei": "e4937a14f91c05a3",
								"password": base.MD5(password),
								"scope": "all"
								}
		if version == "01.00.34":
			PAD_EN_logged_in["device_name"] = "PAD"
			self.logger.info("PAD_EN_logged_in参数的值为:%s" % PAD_EN_logged_in)
			return PAD_EN_logged_in
		else:
			self.logger.info("PAD_EN_logged_in参数的值为:%s" % PAD_EN_logged_in)
			return PAD_EN_logged_in



	def get_firmware(self,sn):
		'''
		:return:
		'''
		firmware = {
					"auth_type": "sn_password",
					"client_id": "d00a9260baff4ad386939a7baf22b799",
					"client_secret": "8236dc7b20ed484c830aabc5643717e9",
					"grant_type": "password",
					"scope": "all",
					"sn": sn
					}
		self.logger.info("sn:%s鉴权成功" % sn)
		return firmware

	def get_oc_web(self,userName,password):

		password = base.MD5(password)

		oc_web = {
				"client_id": "d6165bbf3d804c6196c0c6d7201de970",
				"client_secret": "25f9e794323b453885f5181f1b624d0b",
				"scope": "all",
				"grant_type": "password",
				"email": userName,
				"password": password,
				"auth_type": "email_password"
				}
		self.logger.info("用户名:%s开始登录！"%userName)
		return oc_web


	def get_AuthenticationURL_OC(self, baseURL,loginURL, lang, timeStamp,clientVersionInfo):
		'''
		:param url:
		:param lang:
		:param timeStamp:
		:param clientVersionInfo:
		:return:
		'''
		AuthenticationURL = baseURL + loginURL + "?lang=%s&timeStamp=%s&clientVersionInfo=%s" % (lang, timeStamp,clientVersionInfo)
		self.logger.info("AuthenticationURL_OC的值为:%s" % AuthenticationURL)
		return AuthenticationURL



	def get_AuthenticationURL(self,baseURL,loginURL,lang,timeStamp,clientVersionInfo):
		'''
		:param url:
		:param lang:
		:param timeStamp:
		:param clientVersionInfo:
		:return:
		'''
		AuthenticationURL = baseURL + loginURL + "?lang=%s&timeStamp=%s&clientVersionInfo=%s" %(lang, timeStamp,clientVersionInfo)
		self.logger.info("AuthenticationURL的值为:%s" % AuthenticationURL)
		return AuthenticationURL


	def get_AuthenticationURL_SmallProgram(self,baseURL,loginURL,lang,timeStamp):
		'''
		:param url:
		:param lang:
		:param timeStamp:
		:param clientVersionInfo:
		:return:
		'''
		AuthenticationURL = baseURL + loginURL + "?lang=%s&timeStamp=%s" %(lang, timeStamp)
		self.logger.info("AuthenticationURL的值为:%s" % AuthenticationURL)
		return AuthenticationURL



	def get_response(self,url,dictPara):
		'''
		:param url:
		:param dictPara:
		:return: 获取accesstoken
		'''
		headers = {"Content-Type": "application/json"}
		try:
			r = requests.post(url, data=json.dumps(dictPara), headers=headers)
			result = json.loads(r.text)
		except:
			self.logger.info("返回的参数为：%s" % result)
			self.logger.error("登录失败，请检查您的配置！")
		else:
			self.logger.info("返回的参数为：%s" % result)
			self.logger.info("登录成功")
			return result



	def get_Access_token(self,url,dictPara):
		'''
		:param url:
		:param dictPara:
		:return: 获取accesstoken
		'''
		headers = {"Content-Type": "application/json"}
		result = ""
		try:
			r = requests.post(url, data=json.dumps(dictPara), headers=headers,timeout=30)
			result = json.loads(r.text)
		except:
			self.logger.info("返回的参数为：%s" % result)
			self.logger.error("登录失败，请检查您的配置！")
		else:
			self.logger.info("返回的参数为：%s" % result)
			access_token = json.loads(r.text)["data"]["access_token"]
			self.logger.info("登录成功")
			return access_token


	def get_Access_token_not_login(self,url,dictPara):
		'''
		:param url:
		:param dictPara:
		:return: 获取accesstoken
		'''
		headers = {"Content-Type": "application/json"}
		result = ""
		try:
			r = requests.post(url, data=json.dumps(dictPara), headers=headers,timeout=30)
			result = json.loads(r.text)
		except:
			self.logger.info("返回的参数为：%s" % result)
			self.logger.error("鉴权失败，请检查您的配置！")
		else:
			self.logger.info("返回的参数为：%s" % result)
			access_token = json.loads(r.text)["data"]["access_token"]
			self.logger.info("鉴权成功")
			return access_token


	def get_logout_url(self, env):

		url = ""
		if env == "prod":
			url = "http://mi-api.nailtutu.com/oauth/logout"
		elif env == "uat":
			url = "http://mi-api-uat.nailtutu.com/oauth/logout"
		elif env == "dev":
			url = "http://mi-api-dev.nailtutu.com/oauth/logout"
		else:
			self.logger.error("配置有误，请检查！")
		return url


	def get_ocweb_really_logout_url(self, url, access_token):
		ReallyURL = url + "?timeStamp=%s&access_token=%s&lang=zh" % (base.getTimeStamp(), access_token)
		self.logger.info("退出登录的URL为:%s" % ReallyURL)
		return ReallyURL


	def send_request_logout(self, url):
		headers = {"Content-Type": "application/json",
				   "User-Agent": "User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"}
		parameters = {
		}
		self.logger.info("请求的参数为:%s" % parameters)
		r = requests.post(url, data=json.dumps(parameters), headers=headers, timeout=30)
		self.logger.info("返回的参数为:%s" % json.loads(r.text))
		return json.loads(r.text)


	def logout(self, env, access_token):
		url = self.get_ocweb_really_logout_url(self.get_logout_url(env), access_token)
		self.send_request_logout(url)




if __name__ == "__main__":
	ac = Authentication()
	# print(ac)
	# userName = "admin@sunvalley.com.cn"
	# password = "danya@123"
	# data = ac.get_oc_web(userName,password)
	# baseURL = "https://oc-api-uat.nailtutu.com"
	# loginURL = "/oauth/login"
	# lang = "zh"
	# timeStamp = base.getTimeStamp()


	# phone = "13723746965"
	# password = "123456"
	# countryCode = "861"
	#
	#
	#
	# data = ac.get_PAD_CN_logged_in(phone,password)
	# print(data)




	# email = "durant.zeng@sunvalley.com.cn"
	# password = "123456"
	#



	# data = ac.get_PAD_EN_logged_in(email,password)
	#
	#
	# print(data)
	#
	# baseURL = "https://mi-api.nailtutu.com"
	# loginURL = "/oauth/login"
	# lang = "zh"
	# timeStamp = base.getTimeStamp()
	# clientVersionInfo = "android_1.0.34"
	# #
	# AuthenticationURL = ac.get_AuthenticationURL(baseURL, loginURL, lang, timeStamp,clientVersionInfo)
	# print(AuthenticationURL)
	# #
	# #
	# #
	# accessToken = ac.get_response(AuthenticationURL,data)
	# print(accessToken)


	URL = "https://mi-api-dev.nailtutu.com/oauth/login?lang=ch&timeStamp=20190823140131&clientVersionInfo=android_1.0.40"

	# phone = "13417335080"
	# password = "123456"
	# countryCode = "86"
	data = ac.get_test_IOS_client_Not_logged_in()
	print(data)
	# email = "124854364@qq.com"
	# password = "123456"
	# version = "01.00.34"
	# data = ac.get_PAD_EN_logged_in(email,password,version)
	# print(data)

	ac.get_response(URL,data)




	data = ac.get_test_Android_client_Not_logged_in()
	print(data)
	ac.get_response(URL,data)











