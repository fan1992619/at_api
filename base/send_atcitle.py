#18210542401 bearer     Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczpcL1wvYXBpLmF0LnRvcFwvdjFcL2FjY291bnRcL3NpZ25pbiIsImlhdCI6MTUzMzg4NTIyNCwiZXhwIjoxNTY1NDIxMjI0LCJuYmYiOjE1MzM4ODUyMjQsImp0aSI6Im80ZmFKVnhlMUxXSmlmdksiLCJzdWIiOjMxLCJwcnYiOiJjOGVlMWZjODllNzc1ZWM0YzczODY2N2U1YmUxN2E1OTBiNmQ0MGZjIn0.UCbB_ilaw1xu92aB4oQ5k_dJXT6tj-xHVGtO5-NiHTM
#18782610762 bearer     Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczpcL1wvYXBpLmF0LnRvcFwvdjFcL2FjY291bnRcL3NpZ25pbiIsImlhdCI6MTUzMzg4NDY0NywiZXhwIjoxNTY1NDIwNjQ3LCJuYmYiOjE1MzM4ODQ2NDcsImp0aSI6ImlGTlJkTTRSVk90S3ZhWTgiLCJzdWIiOjMzLCJwcnYiOiJjOGVlMWZjODllNzc1ZWM0YzczODY2N2U1YmUxN2E1OTBiNmQ0MGZjIn0.uMkAI8VR6lZOCr27znRYLfkZRazvpvxDHjc8wBi1xPw
from lxml import html
# import xlsxwriter
# import urllib.request
from openpyxl import load_workbook,Workbook
import requests
import urllib.request
import random
import xlrd
from openpyxl.drawing.image import Image
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
from data import data_config_article
import json
import time
str_182='Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczpcL1wvYXBpLmF0LnRvcFwvdjFcL2FjY291bnRcL3NpZ25pbiIsImlhdCI6MTUzMzg4NTIyNCwiZXhwIjoxNTY1NDIxMjI0LCJuYmYiOjE1MzM4ODUyMjQsImp0aSI6Im80ZmFKVnhlMUxXSmlmdksiLCJzdWIiOjMxLCJwcnYiOiJjOGVlMWZjODllNzc1ZWM0YzczODY2N2U1YmUxN2E1OTBiNmQ0MGZjIn0.UCbB_ilaw1xu92aB4oQ5k_dJXT6tj-xHVGtO5-NiHTM'
str_187='Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczpcL1wvYXBpLmF0LnRvcFwvdjFcL2FjY291bnRcL3NpZ25pbiIsImlhdCI6MTUzMzg4NDY0NywiZXhwIjoxNTY1NDIwNjQ3LCJuYmYiOjE1MzM4ODQ2NDcsImp0aSI6ImlGTlJkTTRSVk90S3ZhWTgiLCJzdWIiOjMzLCJwcnYiOiJjOGVlMWZjODllNzc1ZWM0YzczODY2N2U1YmUxN2E1OTBiNmQ0MGZjIn0.uMkAI8VR6lZOCr27znRYLfkZRazvpvxDHjc8wBi1xPw'
class SendArticles():
    def spider_article(self):
        wb = load_workbook('../dataconfig/title.xlsx')
        ws = wb.active
        ws.title = "抓取标题"
        ws.sheet_properties.tabColor = 'ff0000'
        url = 'https://www.jinse.com/news/bitcoin'
        res = requests.get(url=url, verify=False)
        res.encoding = 'utf-8'
        html_doc = res.text
        # 获取xpath对象
        selector = html.fromstring(html_doc)
        # 找到列表集合
        ui_list = selector.xpath(
            '//div[@class="wrap margin-b clearfix"]/div[@class="wrap-left left"]/div/div[@class="content"]/div[@class="list clearfix"]')
        for i, li in enumerate(ui_list):
            title = li.xpath('//div[@class="post right"]/div/a/@title')
            link = li.xpath('//div[@class="post right"]/div/a/@href')
            content=li.xpath('//div[@class="post right"]/div[@class="message"]/text()')
            img_url=li.xpath('//div[@class="image left"]/a/img/@src')
            # print(content[i])
            # print('第%d次' % i,title[i],link[i],content[i],img_url[i])
            ws['A{0}'.format(i + 2)] = title[i]
            ws['B{0}'.format(i + 2)] = link[i]
            ws['C{0}'.format(i + 2)]=content[i]
            ws['D{0}'.format(i + 2)]=img_url[i]
            i += 1
        wb.save('../dataconfig/title.xlsx')
    #获取url
    def open_url(self,row):
        self.spider_article()
        data = xlrd.open_workbook('../dataconfig/title.xlsx')
        tables = data.sheets()[0]
        col = int(data_config_article.get_url())
        url =tables.cell_value(row, col)
        # print(url)
        return url
    #获取title
    def open_title(self,row):
        self.spider_article()
        data = xlrd.open_workbook('../dataconfig/title.xlsx')
        tables = data.sheets()[0]
        col = int(data_config_article.get_title())
        title =tables.cell_value(row, col)
        # print(title)
        return title
    #获取文章内容
    def open_content(self,row):
        self.spider_article()
        data = xlrd.open_workbook('../dataconfig/title.xlsx')
        tables = data.sheets()[0]
        col = int(data_config_article.get_content())
        content =tables.cell_value(row, col)
        # print(title)
        return content
    #获取文章图片的url
    def open_img_url(self,row):
        self.spider_article()
        data = xlrd.open_workbook('../dataconfig/title.xlsx')
        tables = data.sheets()[0]
        col = int(data_config_article.get_img_url())
        img_url =tables.cell_value(row, col)
        # print(title)
        return img_url
    #获取这张图片内容
    def open_img_content(self,row):
        self.spider_article()
        data = xlrd.open_workbook('../dataconfig/title.xlsx')
        tables = data.sheets()[0]
        col = int(data_config_article.get_img_content())
        img_content =tables.cell_value(row, col)
        # print(title)
        return img_content
    #遍历url
    def articles_url(self):
        self.spider_article()
        data = xlrd.open_workbook('../dataconfig/title.xlsx')
        tables_num = data.sheets()[0].nrows
        for i in range(tables_num):
            if i<1:
                continue
            return self.open_url(i)
    #测试插入图片
    def img_test(self):
        listurl = ['https://contestimg.wish.com/api/webimage/59647c7e7baa287c180fa0e0-3-original.jpg',
                   'https://contestimg.wish.com/api/webimage/59647c7e7baa287c180fa0e0-original.jpg', ]

        # 根据图片链接列表，把图片保存到本地
        i = 0
        for url in listurl:
            f = open(str(i) + '.jpg', "wb")  # 打开文件
            req = urllib.request.urlopen(url)
            buf = req.read()  # 读出文件
            f.write(buf)  # 写入文件
            i = i + 1
        # 将图片一次导入到表格的1，2...行
        data = load_workbook('../appium_android/pict.xlsx')
        ws = data.active
        img = Image('../appium_android/0.jpg')
        ws.add_image(img, 'E2')
        data.save('../dataconfig/title.xlsx')
    #发送文章
    def send_atricl(self):
        #随机获取项目id
        articles=[22,23,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,1503]
        random_articles_num=random.choice(articles)
        #随机获取主题id
        subjects = [1, 2, 3, 4, 5, 6]
        random_subject=random.choice(subjects)
        self.spider_article()
        data = xlrd.open_workbook('../dataconfig/title.xlsx')
        tables = data.sheets()[0].nrows
        print(tables)
        for i in range(tables):
            if i<1:
                continue
            link=self.open_url(i)
            title=self.open_title(i)
            url='https://api.at.top/v1/projects/22/articles'
            #发布文章到项目
            url_test_project='http://api.test.initialvc.com/v1/projects/{0}/articles'.format(random_articles_num)
            #发布文章到主题
            url_test_subject='http://api.test.initialvc.com/v1/subjects/{0}/articles'.format(random_subject)
            data={
                'type': '1',
                'link': '{0}'.format(link),
                'title':'{0}'.format(title)
                # 'timestamp': '1537583500',
                # 'signature': '43fa84601a94e0b5920b5ce7a73c680f'
            }
            header_at={
                'Content-Type': 'application/x-www-form-urlencoded',
                'Content-Length': '764',
                'Host': 'api.at.top',
                'Connection': 'Keep-Alive',
                'Accept-Encoding': 'gzip',
                'User-Agent': 'okhttp/3.8.1',
                'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwOlwvXC9hcGkudGVzdC5pbml0aWFsdmMuY29tXC92MVwvYWNjb3VudFwvc2lnbmluIiwiaWF0IjoxNTM3NTMxMDk3LCJleHAiOjE1NjkwNjcwOTcsIm5iZiI6MTUzNzUzMTA5NywianRpIjoiSk9VaUN2QVZBMVNGa05iZyIsInN1YiI6IjMzIiwicHJ2IjoiYzhlZTFmYzg5ZTc3NWVjNGM3Mzg2NjdlNWJlMTdhNTkwYjZkNDBmYyJ9.FExRUmpERoEDDUtFa666lxHjQhbBeD4TQKtH_sa6Jrw',
                'deviceid': 'ac:c1:ee:c0:33:34-ac:c1:ee:c0:33:34',
                'getuiclientid': '330ccf5988efd42e629f88e533488d4e',
                'platform': 'android',
                'userid': '33',
                'version': '2.2.0'
            }
            header_test={
                'Content-Type': 'application/x-www-form-urlencoded',
                'Content-Length': '325',
                'Host': 'api.test.initialvc.com',
                'Accept-Encoding': 'gzip',
                'User-Agent': 'okhttp/3.8.1',
                'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwOlwvXC9hcGkudGVzdC5pbml0aWFsdmMuY29tXC92MVwvYWNjb3VudFwvc2lnbmluIiwiaWF0IjoxNTQwNzk2OTk5LCJleHAiOjE1NzIzMzI5OTksIm5iZiI6MTU0MDc5Njk5OSwianRpIjoibGI4b241TTBCTno4V0JCNiIsInN1YiI6IjMzIiwicHJ2IjoiYzhlZTFmYzg5ZTc3NWVjNGM3Mzg2NjdlNWJlMTdhNTkwYjZkNDBmYyJ9.BHLtxjFJm-FlZePx9nZo6KMzQmURkwJfsFByBOsqDSY',
                'deviceid': 'ac:c1:ee:c0:33:34-ac:c1:ee:c0:33:34',
                'getuiclientid': '0419d93bf4806aa84c2187927d8f66bc',
                'platform': 'android',
                'userid': '33',
                'version': '1.2.0',
                'Connection': 'keep-alive'
            }
            #发布文章到主题
            res=requests.post(url=url_test_subject,data=data,headers=header_test,verify=False).json()
            #发布文章到项目
            # res = requests.post(url=url_test_project, data=data, headers=header_test, verify=False).json()
            print ('第%d次' % i,res)
    #发布提问
    def send_question(self):
        self.spider_article()
        data = xlrd.open_workbook('../dataconfig/title.xlsx')
        tables = data.sheets()[0].nrows
        #随机获取项目id
        project_id=[22,23,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,1503]
        random_project_num=random.choice(project_id)
        #随机获取主题id
        subjects = [1, 2, 3, 4, 5, 6]
        random_subject=random.choice(subjects)
        print(tables)
        for i in range(tables):
            if i < 1:
                continue
            content = self.open_content(i)
            title = self.open_title(i)+"?"
            url_question_project = 'http://api.test.initialvc.com/v1/question'
            url_question_subject = 'http://api.test.initialvc.com/v1/question/subject'
            data_subject = {
                'subject_id':random_subject,
                'is_anonymous':1,
                'description': '{0}'.format(content),
                'title': '{0}'.format(title)
            }
            data_project={
                'project_id': random_project_num,
                'is_anonymous': 1,
                'description': '{0}'.format(content),
                'title': '{0}'.format(title)
            }
            header_at = {
                'Content-Type': 'application/x-www-form-urlencoded',
                'Content-Length': '764',
                'Host': 'api.at.top',
                'Connection': 'Keep-Alive',
                'Accept-Encoding': 'gzip',
                'User-Agent': 'okhttp/3.8.1',
                'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwOlwvXC9hcGkudGVzdC5pbml0aWFsdmMuY29tXC92MVwvYWNjb3VudFwvc2lnbmluIiwiaWF0IjoxNTM3NTMxMDk3LCJleHAiOjE1NjkwNjcwOTcsIm5iZiI6MTUzNzUzMTA5NywianRpIjoiSk9VaUN2QVZBMVNGa05iZyIsInN1YiI6IjMzIiwicHJ2IjoiYzhlZTFmYzg5ZTc3NWVjNGM3Mzg2NjdlNWJlMTdhNTkwYjZkNDBmYyJ9.FExRUmpERoEDDUtFa666lxHjQhbBeD4TQKtH_sa6Jrw',
                'deviceid': 'ac:c1:ee:c0:33:34-ac:c1:ee:c0:33:34',
                'getuiclientid': '330ccf5988efd42e629f88e533488d4e',
                'platform': 'android',
                'userid': '33',
                'version': '2.2.0'
            }
            header_test={
                'Content-Type': 'application/x-www-form-urlencoded',
                'Content-Length': '325',
                'Host': 'api.test.initialvc.com',
                'Accept-Encoding': 'gzip',
                'User-Agent': 'okhttp/3.8.1',
                'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwOlwvXC9hcGkudGVzdC5pbml0aWFsdmMuY29tXC92MVwvYWNjb3VudFwvc2lnbmluIiwiaWF0IjoxNTQwNzk2OTk5LCJleHAiOjE1NzIzMzI5OTksIm5iZiI6MTU0MDc5Njk5OSwianRpIjoibGI4b241TTBCTno4V0JCNiIsInN1YiI6IjMzIiwicHJ2IjoiYzhlZTFmYzg5ZTc3NWVjNGM3Mzg2NjdlNWJlMTdhNTkwYjZkNDBmYyJ9.BHLtxjFJm-FlZePx9nZo6KMzQmURkwJfsFByBOsqDSY',
                'deviceid': 'ac:c1:ee:c0:33:34-ac:c1:ee:c0:33:34',
                'getuiclientid': '0419d93bf4806aa84c2187927d8f66bc',
                'platform': 'android',
                'userid': '33',
                'version': '1.2.0',
                'Connection': 'keep-alive'
            }
            # #提问到主题
            res = requests.post(url=url_question_subject, data=data_subject, headers=header_test, verify=False).json()
            #提问到项目
            # res = requests.post(url=url_question_project, data=data_project, headers=header_test, verify=False).json()
            print('第%d次' % i, res)
    #api发布评论
    def api_commit_deep(self):
        for i in range(6):
            num = random.randint(1, 15)
            comment_content=self.open_content(num)
            header_at = {
                'Host': 'api.at.top',
                'Connection': 'Keep-Alive',
                'Accept-Encoding': 'gzip',
                'User-Agent': 'okhttp/3.8.1',
                'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczpcL1wvYXBpLmF0LnRvcFwvdjFcL2FjY291bnRcL3NpZ25pbiIsImlhdCI6MTU0MjAxMDM2OCwiZXhwIjoxNTczNTQ2MzY4LCJuYmYiOjE1NDIwMTAzNjgsImp0aSI6Im1zcERIMWVaTDM5SG9mazkiLCJzdWIiOiIzMyIsInBydiI6ImM4ZWUxZmM4OWU3NzVlYzRjNzM4NjY3ZTViZTE3YTU5MGI2ZDQwZmMifQ.0s8qGjniMd3INLbE9rg0NBiKXyp_b1K76M8ZyPrd_ZA',
                'deviceid': 'ac:c1:ee:c0:33:34-ac:c1:ee:c0:33:34',
                'getuiclientid': '5b9a0d6f110d2b136f9ca135d93fad06',
                'platform': 'android',
                'userid': '33',
                'version': '1.2.0'
            }
            #获取评论的内容
            comment_data={
                'content':comment_content
            }
            # deep_id=[45717909825137196,42810485585750572]
            # deep_id_num=random.choice(deep_id)
            time.sleep(5)
            url_comment='https://api.at.top/v1/comment/answer/45717909825137196'
            res=requests.post(url=url_comment, headers=header_at, data=comment_data).json()
            # print(res)
            # send_comment=requests.post(url=url_comment,headers=header_at,data=comment_data).json()
            if res['code']==-204 or res['code']==-2:
                url_comment = 'https://api.at.top/v1/comment/answer/42810485585750572'
                res=requests.post(url=url_comment, headers=header_at, data=comment_data).json()
                # print("res",res)
            else:
                print("res", res)
if __name__ == '__main__':
    send = SendArticles()
    print(send.open_url(3))
    # send.open_title(3)
    # send.spider_article()
    # send.spider_images()
    # print(send.articles_url())
    # print(send.open_img_url(3))
    # print(send.open_content(3))
    # send.spider_img()
    # send.send_atricl()
    # send.send_question()
    # send.api_commit_deep()
    # send.send_get()