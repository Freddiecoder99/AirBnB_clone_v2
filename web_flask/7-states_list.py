#!/usr/bin/python3
<<<<<<< HEAD
"""
start Flask application
"""

from flask import Flask, render_template
from models import *
from models import storage
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """display a HTML page with the states listed in alphabetical order"""
    states = sorted(list(storage.all("State").values()), key=lambda x: x.name)
=======
"""Flask to run the web app"""
from flask import Flask
from flask import render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def display_states():
    """Render state_list html page to display States created"""
    states = storage.all()
>>>>>>> 365ffa39d2e9e7463dcfc2bc2a6d116df35790d3
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
<<<<<<< HEAD
def teardown_db(exception):
    """closes the storage on teardown"""
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
=======
def teardown(self):
    """Method to remove current SQLAlchemy Session"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
>>>>>>> 365ffa39d2e9e7463dcfc2bc2a6d116df35790d3
