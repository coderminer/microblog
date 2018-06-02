# coding:utf-8
from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username':'Kevin'}
    posts = [
        {
            'author' : {'username':'Harry'},
            'body' :'Beatuiful day'
        },
        {
            'author': {'username':'John'},
            'body':'The Aventers movie was so cool!'
        }
    ]
    return render_template('index.html',title = 'Home', user=user,posts = posts)
