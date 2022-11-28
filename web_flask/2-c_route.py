#!/usr/bin/python3
"""
Simple module that starts a Flask web application
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """
    displays Hello HBNB
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """
    displays HBNB
    """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_is_mylove(text):
    """
    displays 'C' followed by the value of text variable
    """
    return "C " + text.replace('_', ' ')


if __name__ == "__main__":
    """ app listening on host 0.0.0.0 and port 5000 """
    app.run(host='0.0.0.0', port='5000')
