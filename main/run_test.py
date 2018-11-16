#coding:utf-8
# import sys
# sys.path.append("E:/www/ImoocInterface")
from base.runmethod import RunMethod
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
		# self.send_mai = SendEmail()

	#程序执行的
	def go_on_run(self):
		res = None
		rows_count = self.data.get_case_lines()
		for i in range(1,rows_count):
			is_run = self.data.get_is_run(i)
			if is_run:
				url = self.data.get_request_url(i)
				method = self.data.get_request_method(i)
				request_data = self.data.get_data_for_json(i)
				# print request_data
				# expect = self.data.get_expcet_data_for_mysql(i)
				header = self.data.is_header(i)
				id=self.data.get_number_id(i)
				expect=self.data.get_expcet_data(i)
				# print type(expect)
				# depend_case = self.data.is_depend(i)
				if header == 'no':
					res = self.run_method.run_main(method,url,request_data)
					print ('第%d次' %i,id,res)
					if res['code']==0:
						self.data.write_result(i, 'pass')
					elif res.status_code==200:
						self.data.write_result(i, 'pass')
					else:
						self.data.write_result(i, res)
				else:
					header=self.data.get_header_value()
					# print header
					res=self.run_method.run_main(method,url,header,request_data)
					# if res['code']==0:
					# 	self.data.write_result(i, 'pass')
					# else:
					# 	self.data.write_result(i, res)
					print ('第%d次' % i,id,res)
					# self.run_method.run_main(method,url,header,request_data)
				# if self.com_util.is_equal_dict(expect,res) == 0:
				# 	self.data.write_result(i,'pass')
				# else:
				# 	self.data.write_result(i,res)
if __name__ == '__main__':
	run = RunTest()
	print (run.go_on_run())

