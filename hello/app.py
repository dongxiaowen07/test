#!/usr/bin/python
#coding=utf-8

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello Flask!</h1>'