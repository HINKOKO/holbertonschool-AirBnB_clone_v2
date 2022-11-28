#!/usr/bin/python3
"""
Simple module that starts a Flask web application
Starting to display formatted text and conditional message
Addind basic template
"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models import *

app = Flask(__name__)


@app.teardown_appcontext
def handle_appcontext(self):
    """
    Method for handling
    After each request current SQLAlchemy is removed
    """
    storage.close()


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def list_states(id=None):
    """
    Displays 9-states.html page
    accordingly to conditions
    """
    states = storage.all(State)
    if id is not None:
        id = 'State.' + id
    return render_template('9-states.html', states=states, id=id)


if __name__ == "__main__":
    """ app listening on host 0.0.0.0 and port 5000 """
    app.run(host='0.0.0.0', port='5000')
