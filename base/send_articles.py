#coding:utf-8
import requests
import json
from data.data_config_sign import *
from data.get_data_sign import GetData
class Run:
    def __init__(self):
        self.data = GetData()


    def post_main(self,url,data,header):
        res=self.requests.post(url=url,data=data,headers=header)
        return res
    def is_contain(self,str_one,str_two):
            flag=None
            if str_one in str_two:
                flag=True
            else:
                flag=False
            return flag
    def go_run(self):
        rows_count = self.data.get_case_lines()
        for i in range(1,rows_count):
            self.url=self.data.get_request_url(i)
            self.title=self.data.get_title(i)
        data={
            'title': self.title,
            'link': self.url,
            'type': '1'
        }
        print data['title']
        print link['link']
        header = {
            'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczpcL1wvYXBpLmF0LnRvcFwvdjFcL2FjY291bnRcL3NpZ25pbiIsImlhdCI6MTUzMDY4MjM5NSwiZXhwIjoxNTYyMjE4Mzk1LCJuYmYiOjE1MzA2ODIzOTUsImp0aSI6IkZSWEZ3aFRSQ242UVpNZzAiLCJzdWIiOjMzLCJwcnYiOiJjOGVlMWZjODllNzc1ZWM0YzczODY2N2U1YmUxN2E1OTBiNmQ0MGZjIn0.dEwtzuJJSHmoHNP7xqAJ5GWcBJF9yhgP6twnwbEdpuw'
        }
if __name__ == '__main__':
    run=Run()
    run.go_run(self)
