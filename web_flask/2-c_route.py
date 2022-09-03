#!/usr/bin/python3
'''A minimal application exaple using flask'''

from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    '''starts a Flask web application'''
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def HBNB():
    '''/hbnb: display “HBNB”'''
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def text(text):
    '''/c/<text>: display “C ” followed by the value of the text variable'''
    parce_text = escape(text.replace('_', ' '))
    return f'C {parce_text}'


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
