#!/usr/bin/env python
# coding:utf-8
# Author:eycode

from flask import Flask, jsonify
from flask.ext.httpauth import HTTPBasicAuth
from flask import abort, make_response

# 使用异步处理
from tasks import SVNUPDATE


auth = HTTPBasicAuth()
@auth.get_password
def get_password(username):
	if username == "eycode":
		return 'python'
	return None

@auth.error_handler
def unauthorized():
	return make_response(jsonify({'error':'Unauthorized access'}), 403)

app = Flask(__name__)

@app.route('/api/v1.0/version=<version>', methods=['GET'])
@auth.login_required
def get_tasks(version):
	SVNUPDATE.delay(version)
	return "Eycode"
    #return jsonify({'tasks': task})

if __name__ == "__main__":
	app.run(debug=True)
