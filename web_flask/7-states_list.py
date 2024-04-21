#!/usr/bin/python3
""" Flask to display our HBNB data """

from flask import Flask
from flask import render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def display_states():
    """ dispplay states in html page """

    states = storage().all("State").values()
    sorted_states = sorted(states, key=lambda state: state.name)
    return render_template('7-states_list.html', states=sorted_states)


@app.teardown_appcontext
def close_session(self):
    """ method to close session"""

    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
