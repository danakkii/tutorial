"""
api 정의
api endpoint의 요청 request로
"""
from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello World!'