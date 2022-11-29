#!/usr/bin/python3
"""
Simple module that starts a Flask web application
Starting to display formatted text and conditional message
Addind basic template
"""
from flask import Flask, render_template
from models import storage
from models import *

app = Flask(__name__)


@app.teardown_appcontext
def handle_appcontext(self):
    """
    Method for handling app context
    """
    storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
def filters():
    """
    Displays html page accordingly
    """
    states = storage.all(State).values()
    amenities = storage.all(Amenity).values()
    return render_template('10-hbnb_filters.html', states=states, amen=amenities)


if __name__ == "__main__":
    """ app listening on host 0.0.0.0 and port 5000 """
    app.run(host='0.0.0.0', port='5000')
