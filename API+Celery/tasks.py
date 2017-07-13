# coding:utf-8
# author:eycode

# Flask + Celery异步处理 = API接口

# 参考：
# http://www.pythondoc.com/flask-celery/first.html
# http://www.ziyoubaba.com/archives/590
# http://docs.jinkan.org/docs/celery/getting-started/first-steps-with-celery.html#id22

# 启用celery：
# /usr/local/python2.7/bin/celery -A tasks.celery worker --loglevel=info

# 安装模块：
# pip install celery celery-with-redis flask

from flask import Flask
from celery import Celery
from SVNupdate import _Svnupdate

# 让root用户具有运行权限
from celery import platforms
platforms.C_FORCE_ROOT = True

# 等待存储容器
app = Flask(__name__)
app.config['CELERY_BROKER_URL'] = 'redis://192.168.0.220:50885/1'
app.config['CELERY_RESULT_BACKEND'] = 'redis://192.168.0.220:50885/1'

# 提交入口
celery = Celery("tasks", broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)


@celery.task
def SVNUPDATE(version):
	if version is not None:
		version = str(version)
		obj = _Svnupdate(version)
		obj._checkout()
		obj._list()
		return {"status": "success"}
	else:
		return {"status": "faild"}
