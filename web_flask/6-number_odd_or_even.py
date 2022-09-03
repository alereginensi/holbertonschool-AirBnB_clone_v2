#!/usr/bin/python3
'''A minimal application exaple using flask'''

from flask import Flask
from markupsafe import escape
from flask import render_template

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
    return 'C {}'.format(parce_text)


@app.route("/python", defaults={'text': "is cool"}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def text_2(text):
    '''display “Python ”, followed by the value of the text variable'''
    parce_text = escape(text.replace('_', ' '))
    return 'Python {}'.format(parce_text)


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    '''display “n is a number” only if n is an integer'''
    return '{} is a number'.format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_html(n):
    '''display a HTML page only if n is an integer'''
    return render_template('5-number.html', n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def odd_or_even(n):
    '''Number: n is even|odd” inside the tag BODY'''
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
