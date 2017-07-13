# coding:utf-8
# author:eycode
# MysqlDB

import MySQLdb, threading

class _DBConnect(threading.local):
	"""处理数据库"""
	def __init__(self):
		self.dbhost = "192.168.0.220"
		self.dbport = 51858
		self.dbuser = "root"
		self.dbpasswd = "root3306"
		self.dbname = "operation"
		self.dbcharset = "utf8"
		self.dbconnect = MySQLdb.connect(self.dbhost, self.dbuser, self.dbpasswd, self.dbname, self.dbport, charset=self.dbcharset)

	def _cursor(self):
		"""获取游标"""
		return self.dbconnect.cursor()

	def _execute(self, sql):
		"""执行语句"""
		try:
			cursor = self._cursor()
			cursor.execute(sql)
			self._commit()
		except MySQLdb.ProgrammingError:
			self._rollback()


	def _commit(self):
		"""提交数据"""
		self.dbconnect.commit()

	def _rollback(self):
		"""回滚事务"""
		self.dbconnect.rollback()

	def _close(self):
		"""关闭数据库"""
		self.dbconnect.close()


def with_connection(func):
	def wrapper(sql):
		_func = func(sql)
		obj = _DBConnect()
		info = obj._execute(_func)
		obj._close()
		return info
	return wrapper


@with_connection
def INSERT(sql):
	return sql


@with_connection
def SELECT(sql):
	info = None
	return sql