#### 模板 - Templates
在上一节中中方法`index()`直接返回的是字符串，也可以返回html的字符串，现在改造一下`index()`方法  

`app/routes.py`
```
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username':'Kevin'}

    return '''
    <html>
        <head>
            <title>Page - Microblog</title>
        </head>
        <body>
            <h1>Hello,'''+ user['username'] +'''!</h1>
        </body>
    </html>
''' 

```
在开发的过程中肯定不能用这种方式来写前段页面，没有提示也没有语法高亮，这样写起来会累死的，在Flask中可以渲染html文本，就是使用Flask内部的模板引擎渲染   
创建一个templates文件夹，来存放我们的页面文件  

`mkdir app/templates`
在templates文件夹中创建一个`index.html`文件  

`app/templates/index.html`
```
<html>
    <head>
        <title>{{ title }}</title>
    </head>
    <body>
        <h1>{{ user.username }}</h1>
    </body>
</html>
```
`{{...}}` 有点像Vue的语法，这里是渲染服务器传递的内容,为了渲染html文件，需要引入`render_template`模块  

`app/routes.py`
```
from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username':'Kevin'}
    return render_template('index.html',title = 'Home', user=user)
```
`render_template`方法一个参数是渲染的文件，会在`templates`文件夹中查找对应的文件，后面的参数是传递给页面的  
Flask中使用的是 [Jinja2](http://jinja.pocoo.org/)模板引擎来渲染页面

#### 在模板中支持条件表达式  

改造一个 `index.html`文件  

```
<html>
    <head>
        {% if title %}
            <title>{{ title }} - Microblog</title>
        {% else %}
            <title>Welcome to</title>
        {% endif %}
    </head>
    <body>
        <h1>{{ user.username }}</h1>
    </body>
</html>
```
在 `{% ... %}`中可以写对应的条件表达式  

#### 循环  

在模板中也支持循环表达式，可以很容易渲染列表，将`routes.py`的`index()`方法改造一下，让她返回一个列表  

`app/routes.py`
```
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

```
注意对应的改动，为了显示列表，需要把`index.html`也改造一下，显示`posts`的内容  

重新运行一下就可以看到对应的效果  

#### 模板继承  
在写html时，有些内容是共同的，我们可不想在每一个html中都重复的去写，可以将一些相对不变且每个页面都有的内容放在一个单独的文件中，然后其他的页面都继承这个页面  

创建一个基类文件 `app/templates/base.html`
```
<html>
    <head>
        {% if title %}
            <title>{{ title }} - Microblog</title>
        {% else %}
            <title>Welcome to</title>
        {% endif %}
    </head>
    <body>
       {% block content %}{% endblock %}
    </body>
</html>
```

使用 `{% extends "base.html" %}`继承这个基类文件,变化的内容方在 `{% block content %}{% endblock %}`中  

改造一下 `index.html`  

```
{% extends "base.html" %}
{% block content %}
    <h1>Hi,{{user.username}}</h1>
    {% for post in posts %}
        <div><p>{{ post.author.username }} says: <b>{{post.body}}</b></p></div>
    {% endfor %}
{% endblock %}
```