# -*- coding:utf-8 -*-
import traceback
from flask import Flask, request
#from flask.ext.babel import Babel, gettext
from rrd import config

# ----creat app----
app = Flask(__name__)
@app.errorhandler(Exception)
def all_exception_handler(error):
    tb = traceback.format_exc()
    err_tip = gettext('Temporary error, please contact your administrator.')
    err_msg = err_tip + '\n\nError: %s\n\nTraceback:\n%s' % (error, tb)
    return '<pre>' + err_msg + '</pre>', 500


