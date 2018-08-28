# /usr/bin/env python
# -*- coding:utf-8 -*-

from flask import Flask
import  sys, os
reload(sys)
sys.setdefaultencoding('utf-8')

app = Flask(__name__)
app.secret_key = os.urandom(24)

#@app.route('/index')
#def index():
#   return 'Hello World'

import views

