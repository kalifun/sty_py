# -*-coding:utf-8 -*-
from flask import render_template
from app import app
@app.route('/')
@app.route('/index')
@app.route('/fun')
def index():
    user = {'nickname':'Miguel'}
    posts = [
        {
            'author':{'nickname':'FUN'},
            'body':'Beautiful day in portland!'
        },
        {
            'author':{'nickname':'fun'},
            'body':'IT is so cool!'
        }
    ]
    return render_template('index.html',user = user,posts = posts)