#coding:utf-8
import requests
import json
#json是服务端返回回来的数据，发送数据要使用x-www-form-urlencoded
# url='http://api.test.initialvc.com/v1/account/signin'
# url='http://baijiahao.baidu.com/s?id=1575504957240029&wfr=spider&for=pc'
url = 'http://api.test.initialvc.com/v1/projects/22/articles'
header={
    'Accept': '*/*',
    'authorization':'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwOlwvXC9hcGkudGVzdC5pbml0aWFsdmMuY29tXC92MVwvYWNjb3VudFwvc2lnbmluIiwiaWF0IjoxNTMxMzc4ODA0LCJleHAiOjE1NjI5MTQ4MDQsIm5iZiI6MTUzMTM3ODgwNCwianRpIjoiN1FKNHVFVUl5ckFNRER3SyIsInN1YiI6NDIsInBydiI6ImM4ZWUxZmM4OWU3NzVlYzRjNzM4NjY3ZTViZTE3YTU5MGI2ZDQwZmMifQ.ukpUMBy66JYx069TPqwY7Gu2I6g6pkCof6WpWOMebAY',
    'Content-Type': 'application/x-www-form-urlencoded',
}

def post_main(url,data,header):
    res=requests.post(url=url,data=data,headers=header).content
    return res

for i in range(2,13):
    data = {
        'title': '了解行业前沿信息{},「活动家」提供2018年区块链'.format(i),
        'link': 'http://svip.gp241.com/baidu/al/13{}'.format(i),
        'type': '1'
    }
    res = post_main(url, data, header)
    # print data['link']
# with open('baidu.html','w')as f:
#     f.write(res)
    print '第%d次' % i,res

