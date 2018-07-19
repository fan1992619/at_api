#coding:utf-8
import requests
import json
import sys
sys.path.append("D:/PycharmProjects/AWARE_API/dataconfig")
from data.get_data_sign import GetData
from data.data_config_sign import global_var
url = 'http://api.test.initialvc.com/v1/account/signin'
header = {
    'Accept': '*/*',
    'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwOlwvXC9hcGkudGVzdC5pbml0aWFsdmMuY29tXC92MVwvYWNjb3VudFwvc2lnbmluIiwiaWF0IjoxNTMxMjc5NDU3LCJleHAiOjE1NjI4MTU0NTcsIm5iZiI6MTUzMTI3OTQ1NywianRpIjoicVJQN3d4OWh6dGljYWJwSiIsInN1YiI6MzMsInBydiI6ImM4ZWUxZmM4OWU3NzVlYzRjNzM4NjY3ZTViZTE3YTU5MGI2ZDQwZmMifQ.iWIs8FuwhNtb7tkcObCfxMsIArfPEE0A1yZp2b2Ayf8',
    'Content-Type': 'application/x-www-form-urlencoded'
}
class RunTest:
    def __init__(self):
        self.data = GetData()
    def post_main(self):
        rows = self.data.get_case_lines()
        print rows
        for i in range(1,rows):
            telephone = int(self.data.get_phone(i))
            number = int(self.data.get_number(i))
            # print phone,number
            # return telephone,number
            data = {
            'phone': telephone,
            'verifycode': number
            }
            print data
            res =requests.post(url=url, data=data, headers=header).json()
            print '第%d次' % i,res
            # return json.dumps(res,indent=2,sort_keys=True)
if __name__ == '__main__':
    run=RunTest()
    run.post_main()


