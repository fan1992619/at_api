#coding:utf-8
import requests
import json
#解决ssl证书报错导入以下包
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
#verify=False  忽略https产生的ssl报错
import random
i=random.randint(1,10000)
class RunMethod:
    #定义一个post方法
	def post_main(self,url,data=None,header=None):
		res = None
		if header !=None:
			res = requests.post(url=url,data=data,headers=header,verify=False).json()
			if res['code']==-204:
				print "文章重复，false"
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
			res = requests.get(url=url,data=data,headers=header,verify=False).json()
		else:
			res = requests.get(url=url,data=data,verify=False).json()
		return res
	#定义一个delete方法
	def delete_main(self,url,data=None,header=None):
		res=None
		res=requests.delete(url=url,data=data,headers=header,verify=False).json()
		if res['code']!=0:
			res=self.post_main(url,data,header)
			res=requests.delete(url=url,data=data,headers=header,verify=False).json()
		return res
	def run_main(self,method,url,header=None,data=None):
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
    url='https://api.at.top/v1/projects/1540/articles'
    data = {
        # 'phone': '18782610762',
        # 'verifycode': '158266'
        # 'name':'fy'
		'title': '好比我先知',
		'link': 'www.a1t{}1a.top'.format(i),
		'type': '7'
     }
    header = {
        'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczpcL1wvYXBpLmF0LnRvcFwvdjFcL2FjY291bnRcL3NpZ25pbiIsImlhdCI6MTUzMDY4MjM5NSwiZXhwIjoxNTYyMjE4Mzk1LCJuYmYiOjE1MzA2ODIzOTUsImp0aSI6IkZSWEZ3aFRSQ242UVpNZzAiLCJzdWIiOjMzLCJwcnYiOiJjOGVlMWZjODllNzc1ZWM0YzczODY2N2U1YmUxN2E1OTBiNmQ0MGZjIn0.dEwtzuJJSHmoHNP7xqAJ5GWcBJF9yhgP6twnwbEdpuw'
    }
    print run.run_main('post',url,header,data)

