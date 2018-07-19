#coding:utf-8
import pymysql
import json
class OperationMysql:
	def __init__(self):
		self.conn = pymysql.connect(
			host='60.205.227.59',
			port=3306,
			user='root',
			passwd='lW4uNoe,d*',
			db='aware',
			charset='utf8',
			cursorclass=pymysql.cursors.DictCursor
			)
		self.cur = self.conn.cursor()

	#查询一条数据
	def search_one(self,sql):
		self.cur.execute(sql)
		result = self.cur.fetchone()
		# result = json.dumps(result)
		return result
		self.conn.close()
if __name__ == '__main__':
	op_mysql = OperationMysql()
	res = op_mysql.search_one("SELECT * FROM accounts WHERE pid=33")
	print res
