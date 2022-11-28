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


if __name__ == "__main__":
    """ app listening on host 0.0.0.0 and port 5000 """
    app.run(host='0.0.0.0', port='5000')
