from flask import Flask, request
from flask import redirect
from flask import url_for

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1> %sdasd</h1>' % (app.name + ' jidanyu')

@app.route('/home')
def home():
    return redirect(url_for('index'))

@app.route('/hello')
def hello():
    name = request.args.get('name')
    return '<h1>hello %s</h1>' % name

@app.route('/home/<address>')
def homepage(address):

    return '<h1>HOME %s</h1>' % address