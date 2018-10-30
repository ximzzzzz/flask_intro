# flask intro


* 파이썬 환경설정
* flask
  * pip install flask
* app.py

```python
#라우터설정 == 주소설정이라고 보면됨, url구조도 디렉토리와 똑같다
from flask import Flask
app = Flask(__name__)

@app.route("/") #최상단으로 요청하면 아래 hello 함수작동
def hello():
    return "Hello World!"

@app.route("/welcome") 
def welcome():
    return "my pleasure"git remote add origin 

git remote add origin https://github.com/ximzzzzz/flask_intro.git
    
```