#coding:utf-8
import requests
import json
#json是服务端返回回来的数据，发送数据要使用x-www-form-urlencoded
url = 'https://api.at.top/v1/projects/1540/articles'
data={
    'title':'好币我先知！',
    'link':'www.at2.top',
    'type':'7'
}
header={
    'authorization':'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczpcL1wvYXBpLmF0LnRvcFwvdjFcL2FjY291bnRcL3NpZ25pbiIsImlhdCI6MTUzMTg4MTc2MSwiZXhwIjoxNTYzNDE3NzYxLCJuYmYiOjE1MzE4ODE3NjEsImp0aSI6IlMwR2R1ZmFPclppdEVBcmEiLCJzdWIiOjMzLCJwcnYiOiJjOGVlMWZjODllNzc1ZWM0YzczODY2N2U1YmUxN2E1OTBiNmQ0MGZjIn0.ZflYjQaCR-B4dsKl9Ivgc9IAtg6WEynipMO695qceQ0'
}
def post_main(url,data,header):
    res=requests.post(url=url,data=data,headers=header).json()
    return res
print post_main(url,data,header)


