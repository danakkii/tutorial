from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'hi'

@app.route('/hello')
def hello():
    return "hello, world"

@app.route('/log')
def log():
    return "login page"

app.debug = True
app.run()
