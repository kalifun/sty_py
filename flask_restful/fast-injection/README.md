# 1.第一个Flask-RESTful API
```python
# -*- coding:utf-8 -*-
from flask import Flask
from flask_restful import Resource,Api

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'Hello':'World'}

api.add_resource(HelloWorld,'/')

if __name__ == "__main__":
    app.run(debug=True)
```
``` bash
➜  ~ curl -i http://127.0.0.1:5000
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 25
Server: Werkzeug/0.14.1 Python/2.7.15
Date: Tue, 25 Dec 2018 15:07:38 GMT

{
    "Hello": "World"
}
```
## 1.1另一种写法
``` python
# -*- coding:utf-8 -*-
from flask import Flask,jsonify

app = Flask(__name__)

@app.route('/',methods=['GET'])
def index():
    return jsonify({"Hello":"World"})

if __name__ == "__main__":
    app.run(debug=True)
```
``` bash
➜  ~ curl -i http://127.0.0.1:5000
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 23
Server: Werkzeug/0.14.1 Python/2.7.15
Date: Tue, 25 Dec 2018 15:12:54 GMT

{
  "Hello": "World"
}
```
### 你会发现效果是一样的。