## 基于Flask架构的API小案例

### 描述：

1.  浏览器提交页面地址，访问后台资源
2.  通过HTTP安全认证，控制用户访问资源（前期测试简单认证，后期会修改成Mysql + Toke）
3.  在处理后端资源时，使用到Celery异步


> 完成效果：

1.  通过url，更新SVN资源，并将资源储存在数据库中储存，为前端使用
2.  Celery异步充当成中间人使用，解决flask单进程问题


#### 使用到的模块：

1.  Flask
2.  Celery && Celery-with-redis
3.  MySQL
4.  svn


#### 环境：

1.  Linux
2.  Python2.7

#### service.py文件描述：

1.  访问入口文件，默认端口5000


> 启动服务：

	python service.py

> 访问资源：

	curl -u eycode:python -i http://localhost:5000/api/v1.0/0421-1.8.0


#### tasks.py文件描述：

1.  异步事务处理文件，配置Celery服务和相关函数

> 启动Celery服务

	/usr/local/python2.7/bin/celery -A tasks.celery worker --loglevel=info


#### SVNupdate.py文件描述：

1.  SVN更新文件，文件中部分代码需要重写（暂时测试使用，待更新）

#### DBinset.py文件描述：

1.  数据库更新文件，属于底层服务


#### 参考文件：

1. Celery官方：[http://docs.jinkan.org/docs/celery/getting-started/first-steps-with-celery.html#id22](http://docs.jinkan.org/docs/celery/getting-started/first-steps-with-celery.html#id22)
