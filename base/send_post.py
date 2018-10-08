#coding:utf-8
import requests
import json
#json是服务端返回回来的数据，发送数据要使用x-www-form-urlencoded
# url='http://api.test.initialvc.com/v1/account/signin'
# url='http://baijiahao.baidu.com/s?id=1575504957240029&wfr=spider&for=pc'
url = 'http://api.test.initialvc.com/v1/projects/22/articles'
header={
    'Accept': '*/*',
    'authorization':'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwOlwvXC9hcGkudGVzdC5pbml0aWFsdmMuY29tXC92MVwvYWNjb3VudFwvc2lnbmluIiwiaWF0IjoxNTMzNjI3NDI4LCJleHAiOjE1NjUxNjM0MjgsIm5iZiI6MTUzMzYyNzQyOCwianRpIjoiam02a1FBZ0g3QzU1OUt5diIsInN1YiI6MzMsInBydiI6ImM4ZWUxZmM4OWU3NzVlYzRjNzM4NjY3ZTViZTE3YTU5MGI2ZDQwZmMifQ.kANEjT7ADi_1lQ2T2mtzjdt4QD0tXTAEdx2Sx1MJNP0',
    'Content-Type': 'application/x-www-form-urlencoded',
}

def post_main(url,data,header):
    res=requests.post(url=url,data=data,headers=header).content
    return res

for i in range(10):
    data = {
        'title': '42个行业 上篇{} '.format(i),
        'link': 'https://www.jinse.com/bitcoin/223741{}.html'.format(i),
        'type': '1'
    }
    res = post_main(url, data, header)
    # print data['link']
# with open('baidu.html','w')as f:
#     f.write(res)
    print '第%d次' % i,res

