#!/usr/bin/python3
"""
<<<<<<< HEAD
start Flask application
"""

from flask import Flask, render_template
from models import *
from models import storage
app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/<state_id>', strict_slashes=False)
def states(state_id=None):
    """display the states and cities listed in alphabetical order"""
    states = storage.all("State")
    if state_id is not None:
        state_id = 'State.' + state_id
    return render_template('9-states.html', states=states, state_id=state_id)


@app.teardown_appcontext
def teardown_db(exception):
    """closes the storage on teardown"""
    storage.close()

if __name__ == '__main__':
=======
rendering states and cities by flask
"""
from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)
storage.all()


@app.teardown_appcontext
def teardown_data(self):
    """
        refrech data
    """
    storage.close()


@app.route('/states', strict_slashes=False)
def state():
    """Displays a html page with states"""
    states = storage.all(State)
    return render_template('9-states.html', states=states)


@app.route('/states/<id>', strict_slashes=False)
def state_id(id):
    """ render states by its id """

    for state in storage.all(State).values():
        if state.id == id:
            return render_template("9-states.html", states=state, search_id=id)
    return render_template("9-states.html", states=state, search_id=None)


if __name__ == "__main__":
>>>>>>> 365ffa39d2e9e7463dcfc2bc2a6d116df35790d3
    app.run(host='0.0.0.0', port='5000')
