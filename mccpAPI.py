# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 17:34:54 2018

@author: woon.zhenhao
"""
import flask
from flask import Flask, request, make_response, render_template, redirect
from flask_cors import CORS
from flask_restful import Resource, Api
import json
import dbconnector as db

app = Flask(__name__)
api = Api(app)
CORS(app)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/main')
def main():
    return render_template('index.html')

@app.route('/admin')
def getAccount():
    return render_template('admin.html')

@app.route('/passwordcheck', methods=['GET', 'OPTIONS'])
def passwordcheck():
    ret={}
    if request.method == 'GET':
        password = request.args.get("password" ,type = str, default="")
        df=db.getPassword()
        if df==password:
            ret['result']='success'
        else:
            ret['result']='success'
            
        resp = flask.Response(json.dumps(ret))
        resp.headers['Access-Control-Allow-Origin'] = '*'
        resp.headers['Access-Control-Allow-Methods']= 'GET,PUT,POST,DELETE,OPTIONS'
        resp.headers['Access-Control-Allow-Credentials'] = 'true'
        return resp
    
@app.route('/geturl', methods=['GET', 'OPTIONS'])
def geturl():
    if request.method=='GET':
        ret={
            'result':db.getUrl()
            }
            
        resp = flask.Response(json.dumps(ret))
        resp.headers['Access-Control-Allow-Origin'] = '*'
        resp.headers['Access-Control-Allow-Methods']= 'GET,PUT,POST,DELETE,OPTIONS'
        resp.headers['Access-Control-Allow-Credentials'] = 'true'
        return resp
    
@app.route('/seturl', methods=['POST', 'OPTIONS'])
def seturl():
    if request.method=='POST':
        f=request.files['data']
        url = request.args.get("url" ,type = str, default="")
        ret={
            'result':db.setUrl(url)
            }
        
        resp = flask.Response(json.dumps(ret))
        resp.headers['Access-Control-Allow-Origin'] = '*'
        resp.headers['Access-Control-Allow-Credentials'] = 'true'
        resp.headers['Access-Control-Allow-Methods']= 'GET,PUT,POST,DELETE,OPTIONS'
        return resp

if __name__ == '__main__':
     app.run(debug=True)