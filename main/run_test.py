#coding:utf-8
# import sys
# sys.path.append("E:/www/ImoocInterface")
from base.runmethod import RunMethod
from base.send_atcitle import SendArticles
from data.get_data import GetData
from util.common_util import CommontUtil
# from data.dependent_data import DependdentData
# from util.send_email import SendEmail
# from util.operation_header import OperationHeader
from util.operation_json import OperetionJson
import json
class RunTest:
	def __init__(self):
		self.run_method = RunMethod()
		self.data = GetData()
		self.com_util = CommontUtil()
		self.article=SendArticles()
		# self.send_mai = SendEmail()

	#程序执行的
	def go_on_run(self):
		res = None
		rows_count = self.data.get_case_lines()
		for i in range(1,rows_count):
			if i<38:
				continue
			is_run = self.data.get_is_run(i)
			if is_run:
				url = self.data.get_request_url(i)
				request_name=self.data.get_request_name(i)

				method = self.data.get_request_method(i)
				request_data = self.data.get_data_for_json(i)
				header = self.data.is_header(i)
				id=self.data.get_number_id(i)
				expect=self.data.get_expcet_data(i)
				#判断except的值是否为字符串
				if type(expect) != str :
					expect=int(expect)
					expect=str(expect)
				else:
					pass
				if i==39 or i==40:
					#判断该链接是否为发布文章主题之列的
					if self.com_util.is_contain("发布项目文章",request_name):
						res=self.article.send_article_project()
						if self.com_util.is_contain(expect,res):
							self.data.write_result(i,'pass')
						else:
							self.data.write_result(i, res)
					elif self.com_util.is_contain("发布主题文章",request_name):
						res=self.article.send_article_subject()
						if self.com_util.is_contain(expect,res):
							self.data.write_result(i,'pass')
						else:
							self.data.write_result(i, res)
				else:
					# print(type(expect))
					# print(expect)
					# print(url,method,request_name,"request_data是：{}".format(request_data),header,id,expect)
					if header == 'no':
						res = self.run_method.run_main(method,url,header,request_data)
						# print(type(res))
						print ('第%d次' %i,id)
						if self.com_util.is_contain(expect,res):
							self.data.write_result(i,'pass')
						else:
							# print('第%d次' % i, id)
							self.data.write_result(i, res)
					else:
						print('第%d次' % i, id)
						res=self.run_method.run_main(method,url,header,request_data)
						if self.com_util.is_contain(expect,res):
							self.data.write_result(i,'pass')
						else:
							self.data.write_result(i, res)
					continue
			else:
				continue
if __name__ == '__main__':
	run = RunTest()
	print(run.go_on_run())

