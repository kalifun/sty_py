# 在Flask中的Hello world
``` bash
mkdir microblog
cd microblog
mkdir -p app/static
mkdir -p app/templates
mkdir tmp
```
## 我们的应用程序放置app文件中，static放静态文件，templates用于放html文件。
## 在app/__init__.py创建一个初始化脚本。
``` python
from flask import Flask   //导入模块
 
app = Flask(__name__)     //创建一个名叫app的程序
from app import views     //导入app下的views脚本
```
## 在app/views.py 创建视图模块
```python
from app import app   //导入app这个程序

@app.route('/')    //路由到首页时作处理 
@app.route('/index')  //路由到/index时处理

def index():
    return "Hello World"     //根据上面路由返回的结果
```
## 创建启动文件
```python
from app import app

app.run(debug=True)
```
``` bash
➜  ~ curl -i http://127.0.0.1:5000
HTTP/1.0 200 OK
Content-Type: text/html; charset=utf-8
Content-Length: 11
Server: Werkzeug/0.14.1 Python/2.7.15
Date: Wed, 26 Dec 2018 15:11:35 GMT

Hello World
```