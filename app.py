from flask import Flask
app = Flask(__name__)

@app.route('/')
@app.route('/index')
@app.route('/home')
def hello():
    return "Welcome to My Watchlist!"

@app.route('/user/<name>')
def user_page(name):
    return 'Hello, %s' % name