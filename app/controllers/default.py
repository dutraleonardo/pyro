from app import app
from flask import request

@app.route("/")
@app.route("/index")
def index():
    return "<h1>Hello World</h1>"


@app.route("/login")
def login():
    if request.method == 'POST':
        return login()
    else:
        return ";*"