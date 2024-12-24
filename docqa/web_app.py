''' A simple web app that returns a simple HTML message '''
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    ''' Returns a simple HTML message '''
    return "<p>Hello, World!</p>"
