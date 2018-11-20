from util.operation_excel import OperationExcel
from data import data_config
from util.operation_json import OperetionJson
class GetData:
	def __init__(self):
		self.opera_excel = OperationExcel()
	#去获取excel行数,就是我们的case个数
	def get_case_lines(self):
		return self.opera_excel.get_lines()

	#获取是否执行
	def get_is_run(self,row):
		flag = None
		col = int(data_config.get_run())
		run_model = self.opera_excel.get_cell_value(row,col)
		if run_model == 'yes':
			flag = True
		else:
			flag = False
		return flag

	def get_header_value(self):
		#api.at.top
		header = {
			'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczpcL1wvYXBpLmF0LnRvcFwvdjFcL2FjY291bnRcL3NpZ25pbiIsImlhdCI6MTU0MjAxMDM2OCwiZXhwIjoxNTczNTQ2MzY4LCJuYmYiOjE1NDIwMTAzNjgsImp0aSI6Im1zcERIMWVaTDM5SG9mazkiLCJzdWIiOiIzMyIsInBydiI6ImM4ZWUxZmM4OWU3NzVlYzRjNzM4NjY3ZTViZTE3YTU5MGI2ZDQwZmMifQ.0s8qGjniMd3INLbE9rg0NBiKXyp_b1K76M8ZyPrd_ZA'
		}
		return header
	#获取模块的名称
	def get_request_name(self,row):
		col=int(data_config.get_request_name())
		request_name=self.opera_excel.get_cell_value(row,col)
		return request_name
	#是否携带header
	def is_header(self,row):
		col = int(data_config.get_header())
		header = self.opera_excel.get_cell_value(row,col)
		if header =='yes':
			header= {
				'Host': 'api.at.top',
				'Connection': 'Keep-Alive',
				'Accept-Encoding': 'gzip',
				'User-Agent': 'okhttp/3.8.1',
				'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczpcL1wvYXBpLmF0LnRvcFwvdjFcL2FjY291bnRcL3NpZ25pbiIsImlhdCI6MTU0MjY5NjkzMiwiZXhwIjoxNTc0MjMyOTMyLCJuYmYiOjE1NDI2OTY5MzIsImp0aSI6IlNxN01BajR3QUZIU0pUcHMiLCJzdWIiOiIzMyIsInBydiI6ImM4ZWUxZmM4OWU3NzVlYzRjNzM4NjY3ZTViZTE3YTU5MGI2ZDQwZmMifQ.KDlYlvi7z50fKGSsIywDOhRhqZdgxtrkhWwqbtzz2iw',
				'deviceid': 'ac:c1:ee:c0:33:34-ac:c1:ee:c0:33:34',
				'getuiclientid': '5b9a0d6f110d2b136f9ca135d93fad06',
				'platform': 'android',
				'userid': '33',
				'version': '2.1.0'
			}
		else:
			return None
		return header
	#获取请求方式
	def get_request_method(self,row):
		col = int(data_config.get_run_way())
		request_method = self.opera_excel.get_cell_value(row,col)
		return request_method

	#获取url
	def get_request_url(self,row):
		col = int(data_config.get_url())
		url = self.opera_excel.get_cell_value(row,col)
		return url

	#获取请求数据
	def get_request_data(self,row):
		col = int(data_config.get_data())
		data = self.opera_excel.get_cell_value(row,col)
		if not data:
			return None
		return data
	#通过获取关键字拿到data数据
	def get_data_for_json(self,row):
		if not row:
			return None
		opera_json = OperetionJson()
		request_data = opera_json.get_data(self.get_request_data(row))
		# if not request_data:
		# 	return None
		# else:
		return request_data
	#获取预期结果
	def get_expcet_data(self,row):
		col = int(data_config.get_expect())
		expect = self.opera_excel.get_cell_value(row,col)
		# expect = expect.encode('utf-8')
		# print type(expect)
		if expect == '':
			return None
		return expect
	#写入数据
	def write_result(self,row,value):
		col = int(data_config.get_result())
		self.opera_excel.write_value(row,col,value)
	#获取caseid
	def get_number_id(self,row):
		col=int(data_config.get_id())
		ID=self.opera_excel.get_cell_value(row,col)
		return ID
if __name__ == '__main__':
	get_data=GetData()
	print(get_data.write_result(1,"'code': 0"))