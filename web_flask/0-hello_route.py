#!/usr/bin/python3
"""
Simple module that starts a Flask web application
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """
    displays hello HBNB
    """
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run()
