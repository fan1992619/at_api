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
					print ("重复提交，false")
					res=requests.delete(url=url,data=data,headers=header).json()
				elif res['code']!=0:
					res=self.delete_main(url,data,header)
					res=requests.post(url=url,data=data,headers=header,verify=False).json()
				elif res['code']==-2:
					print(res)
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
			# return res
		else:
			try:
				res = requests.get(url=url, data=data, verify=False).json()
			except:
				res = requests.get(url=url, data=data, verify=False)
				res = res.status_code
				# print(res)
		# print('-' * 80)
			# print(res.content.decode())
			# time.sleep(2)
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
		'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczpcL1wvYXBpLmF0LnRvcFwvdjFcL2FjY291bnRcL3NpZ25pbiIsImlhdCI6MTU0MjY5NjkzMiwiZXhwIjoxNTc0MjMyOTMyLCJuYmYiOjE1NDI2OTY5MzIsImp0aSI6IlNxN01BajR3QUZIU0pUcHMiLCJzdWIiOiIzMyIsInBydiI6ImM4ZWUxZmM4OWU3NzVlYzRjNzM4NjY3ZTViZTE3YTU5MGI2ZDQwZmMifQ.KDlYlvi7z50fKGSsIywDOhRhqZdgxtrkhWwqbtzz2iw',
		'deviceid': 'ac:c1:ee:c0:33:34-ac:c1:ee:c0:33:34',
		'getuiclientid': '5b9a0d6f110d2b136f9ca135d93fad06',
		'platform': 'android',
		'userid': '33',
		'version': '2.1.0'
	}
	url='http://api.at.top/v1/6/articles'
	data={"phone":"18782610762", "verifycode":"158266"}
	print(run.run_main('post',url,header))

