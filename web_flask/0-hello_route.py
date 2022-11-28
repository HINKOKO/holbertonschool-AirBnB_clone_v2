#!/usr/bin/python3
from flask import Flask
"""
Simple module that starts a Flask web application
"""

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """
    displays hello HBNB
    """
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run()
