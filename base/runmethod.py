# coding:utf-8
import requests
import json
import time
#解决ssl证书报错导入以下包
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
# verify=False  忽略https产生的ssl报错
import random
class RunMethod:
    # 定义一个post方法
	def post_main(self,url,header=None,data=None):
		res = None
		if header !=None:
			try:
				res = requests.post(url=url,data=data,headers=header,verify=False).json()
				if res['code']==-204:
					#发布文章已达到上线或者重复提交
					print ("重复提交，false")
					res=self.delete_main(url,header,data)
				elif res['code']==-201:
					#已经点赞过该文章
					time.sleep(3)
					res=self.delete_main(url,header,data)
					res=requests.post(url=url,data=data,headers=header,verify=False).json()
				elif res['code']==-2:
					#你无权修改他人信息，标记信息已读或者数据格式错误
					pass
			except:
				res = requests.post(url=url, data=data, headers=header, verify=False)
				res=res.status_code
		else:
			res = requests.post(url=url,data=data,verify=False).json()
			time.sleep(2)
		return json.dumps(res)
    #定义一个get方法
	def get_main(self,url,header=None,data=None):
		res = None
		if header !=None:
			try:
				res = requests.get(url=url, data=data, headers=header, verify=False).json()
			except:
				res=requests.get(url=url, data=data, headers=header, verify=False)
				res=res.status_code
		else:
			try:
				res = requests.get(url=url, data=data, verify=False).json()
				# if res['accessid']:
				# 	#处理oss签名接口
				# 	time.sleep(3)
				# 	res=requests.get(url=url, data=data, verify=False)
				# 	res=res.status_code
				# elif res['code']:
				# 	pass
			except:
				res = requests.get(url=url, data=data, verify=False)
				res = res.status_code
		return json.dumps(res)
	#定义一个delete方法
	def delete_main(self,url,header=None,data=None):
		res=None
		res=requests.delete(url=url,data=data,headers=header,verify=False).json()
		if res['code']!=0:
			res=self.post_main(url,data,header)
			res=requests.delete(url=url,data=data,headers=header,verify=False).json()
		return json.dumps(res)
	def run_main(self,method,url,header=None,data=None):
		res = None
		if method == 'post':
			res = self.post_main(url,header,data)
		elif method=='delete':
			res=self.delete_main(url,header,data)
		else:
			res = self.get_main(url,header,data)
		# return json.dumps(res,ensure_ascii=False)
		return res
if __name__ == '__main__':
	run=RunMethod()
	header={
		'Host': 'api.at.top',
		'Connection': 'Keep-Alive',
		'Accept-Encoding': 'gzip',
		'User-Agent': 'okhttp/3.8.1',
		'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczpcL1wvYXBpLmF0LnRvcFwvdjFcL2FjY291bnRcL3NpZ25pbiIsImlhdCI6MTU0MjcxMDM2MywiZXhwIjoxNTc0MjQ2MzYzLCJuYmYiOjE1NDI3MTAzNjMsImp0aSI6Ijk4ZUtCb2gzaEV1SUE1ckgiLCJzdWIiOiIzMSIsInBydiI6ImM4ZWUxZmM4OWU3NzVlYzRjNzM4NjY3ZTViZTE3YTU5MGI2ZDQwZmMifQ.Ey2Ot4nRgH_fV8Q7D42aKoXH2NzzPYja6bedpBqaXI4',
		'deviceid': 'ac:c1:ee:c0:33:34-ac:c1:ee:c0:33:34',
		'getuiclientid': '5b9a0d6f110d2b136f9ca135d93fad06',
		'platform': 'android',
		'userid': '33',
		'version': '2.1.0'
	}
	data={}
	url='https://api.at.top/v1/public/parameters'
	print(run.run_main('get',url))

