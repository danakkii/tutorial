from flask import Flask, Blueprint

app = Flask(__name__) 
# 플라스크 애플리케이션을 생성하는 코드, __name__이라는 변수에는 모듈명이 담김
# 이 파일을 실행하면 pybo.py라는 모듈이 실행되는 것이므로 __name__ 변수에는 "pybo"라는 문자열이 담긴다

@app.route('/')
# url과 플라스크 코드를 매핑하는 플라스크의 데코레이터다. 데코레잍는 기존 함수를 변경하지 않고 추가 기능을 덧붙일 수 있도록 해주는 함수
# '/' url이 요청되면 플라스크는 hello_pybo 함수를 실행시킨다.
def hello_pybo():
    return 'Hello, Pybo'

# app.run()

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/')
def hello_pybo():
    return 'Hello, pybo!'

bp.run()