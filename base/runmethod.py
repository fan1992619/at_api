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
	def post_main(self,url,data=None,header=None):
		res = None
		if header !=None:
			res = requests.post(url=url,data=data,headers=header,verify=False).json()
			if res['code']==-204:
				print ("文章重复，false")
			elif res['code']!=0:
				res=self.delete_main(url,data,header)
				res=requests.post(url=url,data=data,headers=header,verify=False).json()
		else:
			res = requests.post(url=url,data=data,verify=False).json()
		return res
    #定义一个get方法
	def get_main(self,url,data=None,header=None):
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
		return res
	#定义一个delete方法
	def delete_main(self,url,header=None,data=None):
		res=None
		res=requests.delete(url=url,data=data,headers=header,verify=False).json()
		if res['code']!=0:
			res=self.post_main(url,data,header)
			res=requests.delete(url=url,data=data,headers=header,verify=False).json()
		return res
	def run_main(self,method,url,data=None,header=None):
		res = None
		if method == 'post':
			res = self.post_main(url,data,header)
		elif method=='delete':
			res=self.delete_main(url,data,header)
		else:
			res = self.get_main(url,data,header)
		# return json.dumps(res,ensure_ascii=False)
		return res
if __name__ == '__main__':
	run=RunMethod()
	header={
		'Authorization':'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczpcL1wvYXBpLmF0LnRvcFwvdjFcL2FjY291bnRcL3NpZ25pbiIsImlhdCI6MTU0MjAxMDM2OCwiZXhwIjoxNTczNTQ2MzY4LCJuYmYiOjE1NDIwMTAzNjgsImp0aSI6Im1zcERIMWVaTDM5SG9mazkiLCJzdWIiOiIzMyIsInBydiI6ImM4ZWUxZmM4OWU3NzVlYzRjNzM4NjY3ZTViZTE3YTU5MGI2ZDQwZmMifQ.0s8qGjniMd3INLbE9rg0NBiKXyp_b1K76M8ZyPrd_ZA'
	}
	url='https://api.at.top/v1/user/profile?intro=%E4%BB%8A%E5%A4%A9%E6%98%9F%E6%9C%9F%E4%BA%94'
	data={'intro':'今天星期六'}
	print(run.run_main('post',url,data,header))

