#### Flask 教程： Hello World!

#### 安装Python

请到python的 [官方网站](https://www.python.org/) 下载最新的版本的python，推荐使用3.x版本,为了确保已经安装配置成功，打开终端输入 `python`,看到下面的内容，说明python已经安装成功

```
Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 17:00:18) [MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>>

```

#### 安装Flask

python3.x版本已经内置了`pip`的命令，如果你的python已经安装配置好了，使用下面的命令就可以安装Flask

```
pip install flask
```

确保Flask已经安装成功，打开终端，输入 `python` 之后，执行下面的操作，如果没有报错，就说明Flask已经安装成功   

```
>>> import flask
>>>
```

#### Hello,World Flask 应用

创建工程目录 `microblog`,然后在这个目录中创建一个 `app` 目录，在 `app`包中创建一个 `__init__.py`的文件，并输入下面的代码  

`app/__init__.py`
```
# coding:utf-8 

from flask import Flask

app = Flask(__name__)

from app import routes
```

创建路由文件  

`app/routes.py`
```
# coding:utf-8

from app import app

@app.route('/')
@app.route('/index')
def index():
    return "Hello,Flask!"
```

创建Flask实例

`microblog.py`
```
#coding utf-8

from app import app
```

现在的工程的目录结构是

```
microblog/
  app/
    __init__.py
    routes.py
  microblog.py
```

运行  

`flask run`

如果没有错误的话  

```
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

现在打开浏览器输入 `127.0.0.1:5000`

