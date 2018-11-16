#coding:utf-8
from util.operation_excel import OperationExcel
from util.operation_json import OperetionJson
from data import data_config_sign
class GetData:
	def __init__(self):
		self.opera_excel = OperationExcel()
	#去获取excel行数,就是我们的case个数
	def get_case_lines(self):
		return self.opera_excel.get_lines()


	def get_phone(self,row):
		col = int(data_config_sign.get_phone())
		phone = self.opera_excel.get_cell_value(row,col)
		return phone

	def get_number(self,row):
		col = int(data_config_sign.get_name())
		name = self.opera_excel.get_cell_value(row,col)
		return name

	def get_pid(self,row):
		col = int(data_config_sign.get_pid())
		pid = self.opera_excel.get_cell_value(row,col)
		return pid
if __name__ == '__main__':
	data=GetData()
	print(data.get_name(1))


