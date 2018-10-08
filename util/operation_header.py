# coding:utf-8
import requests
import json
from operation_json import OperetionJson
import random
class OperationHeader:
    def __init__(self, response):
        self.response = json.loads(response)
    # def get_response_url(self):
    #     '''
    #     获取登录返回的token的url
    #     '''
    #     url = self.response['data']['url'][0]
    #     return url
    def get_cookie(self):
        '''
        获取cookie的jar文件
        '''
        # url = self.get_response_url()
        cookie = requests.post(url=url,data=data).json()
        return  cookie['data']['access_token']
        print(cookie)
    def write_cookie(self):
        cookie = requests.utils.dict_from_cookiejar(self.get_cookie())
        op_json = OperetionJson()
        op_json.write_data(cookie)
    def post_data(self):
        i=random.randint(1,10000)
        data={
            'title': '好比我先知',
            'link': 'www.a1t{}1a.top'.format(i),
            'type': '7'
        }
        return data
if __name__ == '__main__':
    url = "http://api.test.initialvc.com/v1/account/signin"
    data = {
        'phone': '18782610762',
        'verifycode': '158266'
    }
    res = json.dumps(requests.post(url, data).json())
    op_header = OperationHeader(res)
    op_header.write_cookie()
