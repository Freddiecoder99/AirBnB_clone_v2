#!/usr/bin/python3
<<<<<<< HEAD
"""
start Flask application
"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """returns Hello HBNB!"""
    return 'Hello HBNB!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
=======
""" creating an html with flask
1. the server listens on 0.0.0.0 on port 5000
"""

from flask import Flask

app = Flask("__name__")


@app.route("/", strict_slashes=False)
def display():
    """ the root of the wed page"""

    return 'Hello HBNB!'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000', debug=None)
>>>>>>> 365ffa39d2e9e7463dcfc2bc2a6d116df35790d3
