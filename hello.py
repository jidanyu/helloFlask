from flask import Flask, request
from flask import redirect
from flask import url_for

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1> %s</h1>' % (app.name + ' jidanyu')

@app.route('/home')
def home():
    return redirect(url_for('index'))

@app.route('/hello',methods=['GET','POST'])
def hello():
    name = request.args.get('name')
    return '<h1>hello %s</h1>' % name

@app.route('/goback/<int:year>')
def gobac(year):
    return '<h1>欢迎回到 %d</h1>' % (2019 - year)

# @app.before_request
# def do():
#     print('dasdas大大')

@app.after_request
def do(request):
    return request