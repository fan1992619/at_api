#coding:utf-8
# import sys
# sys.path.append("E:/www/ImoocInterface")
from base.runmethod import RunMethod
from base.send_atcitle import SendArticles
from data.get_data import GetData
from util.common_util import CommontUtil
# from data.dependent_data import DependdentData
from util.send_email import SendEmail
# from util.operation_header import OperationHeader
from util.operation_json import OperetionJson
import json
class RunTest:
	global pass_count
	global fail_count
	global message_list
	pass_count=[]
	fail_count=[]
	message_list=[]
	def __init__(self):
		self.run_method = RunMethod()
		self.data = GetData()
		self.com_util = CommontUtil()
		self.article=SendArticles()
		self.send_mai = SendEmail()
	#num表示循环次数或者case数量，id_list：case id,expect,res:表示需要判断是否包含的两个预期结果
	def is_write(self,num,id_list,expect,res):
		if self.com_util.is_contain(expect, res):
			self.data.write_result(num, 'pass')
			print('第%d次' % num, id_list, 'pass')
			pass_count.append(num)
		else:
			self.data.write_result(num, res)
			print('第%d次' % num, id_list, res)
			fail_count.append(num)
			m=('第%d次' % num, id_list)
			message_list.append(m)
	#程序执行的
	def go_on_run(self):
		res = None
		rows_count = self.data.get_case_lines()
		for i in range(1,rows_count):
			# if i<1:
			# 	continue
			is_run = self.data.get_is_run(i)
			#判断程序是否执行
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
				if i==39 or i==40 or i==71 or i==72:
					#判断该链接是否为发布文章主题之列的
					if self.com_util.is_contain("发布项目文章",request_name):
						res=self.article.send_article_project()
						self.is_write(i,id,expect,res)
					elif self.com_util.is_contain("发布主题文章",request_name):
						res=self.article.send_article_subject()
						self.is_write(i,id,expect,res)
					elif self.com_util.is_contain("发布项目问题",request_name):
						res=self.article.send_question_project()
						self.is_write(i,id,expect,res)
					elif self.com_util.is_contain("发布主题问题",request_name):
						res=self.article.send_question_subject()
						self.is_write(i,id,expect,res)
				else:
					if header == 'no':
						res = self.run_method.run_main(method,url,header,request_data)
						# print(type(res))
						if self.com_util.is_contain(expect,res):
							self.data.write_result(i,'pass')
							print('第%d次' % i, id,'pass')
							pass_count.append(i)
						else:
							# print('第%d次' % i, id)
							self.data.write_result(i, res)
							print('第%d次' % i, id, res)
							fail_count.append(i)
							m = ('第%d次' % num, id)
							message_list.append(m)
					else:
						res=self.run_method.run_main(method,url,header,request_data)
						if self.com_util.is_contain(expect,res):
							self.data.write_result(i,'pass')
							print('第%d次' % i, id,'pass')
							pass_count.append(i)
						else:
							self.data.write_result(i, res)
							print('第%d次' % i, id,res)
							fail_count.append(i)
							m = ('第%d次' % num, id)
							message_list.append(m)
			else:
				continue
		self.send_mai.send_main(pass_count,fail_count,message_list)
if __name__ == '__main__':
	run = RunTest()
	print(run.go_on_run())

