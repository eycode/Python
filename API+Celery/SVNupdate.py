# coding:utf-8
# author:eycode
# SVN Update File

import svn.remote, svn.local
import os, re, datetime

from DBinset import INSERT

class _Svnupdate:
	def __init__(self, version):
		self.name = "eycode"
		self.passwd = "eycode"
		self.version = version
		self.svnurl = "http://192.168.0.220:54162/svn/eycode/版本发布/正式对外发布版/%s"%self.version
		self.localpath = "/AppPack/%s"%self.version


	def _checkout(self):
		"""更新SVN数据"""
		try:
			_svn = svn.remote.RemoteClient(self.svnurl, username = self.name, password = self.passwd)
			_svn.checkout(self.localpath)
		except UnicodeDecodeError:
			pass

	def _list(self):
		"""获取更新文件列表"""
		if self.localpath is not None:
			# 获取刚刚更新的数据列表

			now = datetime.datetime.now()

			pack_list = [ i for i in os.listdir(self.localpath) if re.findall(r'apk$', i)]

			for i in pack_list:
				_path = "%s/%s" %(self.localpath, i)
				sql = 'insert into versionmanage_ceremonial(name, path, name_status, path_status, add_time) values ("%s", "%s", 1, 0, "%s")'%(i, _path, now.strftime('%Y-%m-%d %H:%M:%S'))
				INSERT(sql)

		else:
			print "falis"