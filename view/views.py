# /usr/bin/env python
# -*- coding:utf-8 -*-

from flask import Flask, g, request, abort, render_template, redirect, session, make_response, jsonify
from . import app
import requests, json
import time

headers = {'content-type': 'application/json'}


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username == 'admin' and password == 'admin123':
            user = username
            session['username'] = username
            session['password'] = password
            resp = make_response(render_template('index.html', name=username))
            resp.set_cookie('username', username)
            print('aaaa')
            return json.dumps({'status': '0', 'errmsg': '登陆成功！'})
        else:
            return json.dumps({'status': '1', 'errmsg': '登陆失败!!'})
    print('ccc')
    return render_template('login.html')


@app.route("/")
def index():
    if 'username' in session:
        cpu_io = [1, 2, 3, 4, 2, 0.8]
        cpu_user = [0.2, 0.3, 0.4, 0.5]
        cpu_system = [0.3, 0.4, 0.5, 0.6]
        mem_use = [0.4, 0.5, 0.6, 0.7, 0.8]

        cpu_time = ['20180802195412', '20180802195512', '20180802195612', '20180802195712']
        new_cpu_time = []
        for cputime in cpu_time:
            local = time.mktime(time.strptime(cputime, "%Y%m%d%H%M%S"))
            new_cpu_time.append(time.strftime("%Y%m%d-%H:%M:%S", time.localtime(local)))

        mem_use = [0.7, 0.6, 0.55, 0.8]
        mem_time = ['20180802195412', '20180802195512', '20180802195612', '20180802195712']
        new_mem_time = []
        for memtime in mem_time:
            local1 = time.mktime(time.strptime(memtime, "%Y%m%d%H%M%S"))
            new_mem_time.append(time.strftime("%Y%m%d-%H:%M:%S", time.localtime(local1)))

        #print("bbb")
        return render_template('index.html', cpu_io=cpu_io, cpu_user=cpu_user, cpu_system=cpu_system, mem_use=mem_use,
                               new_cpu_time=new_cpu_time,
                               new_mem_time=new_mem_time)
    else:
        #print('ddd')
        return render_template('login.html')


@app.route("/test", methods=["GET", "POST"])
def test():
    return render_template('test.html', contents='This is test page!!')


@app.errorhandler(404)
def not_found(e):
    return render_template("404.html")


@app.errorhandler(500)
def internal_server_error(e):
    return render_template("500.html")


@app.route("/cmdb/<hostname>", methods=["GET", "POST"])
def cmdb(hostname):
    if 'username' in session:
        if request.method=='POST':
            data = request.form.get("data")
            print(json.loads(data)['hostname'])
        print('xx')
        return render_template(hostname+'.html',info=session, user=session['username'])
    else:
        return render_template('login.html')

    
