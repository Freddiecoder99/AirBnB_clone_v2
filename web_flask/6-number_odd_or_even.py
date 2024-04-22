#!/usr/bin/python3
<<<<<<< HEAD
"""
start Flask application
"""

from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """returns Hello HBNB!"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """returns HBNB"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def cisfun(text):
    """display “C ” followed by the value of the text variable"""
    return 'C ' + text.replace('_', ' ')


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def pythoniscool(text='is cool'):
    """display “Python ”, followed by the value of the text variable"""
    return 'Python ' + text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def imanumber(n):
    """display “n is a number” only if n is an integer"""
    return "{:d} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def numbersandtemplates(n):
    """display a HTML page only if n is an integer"""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def numbersandevenness(n):
    """display a HTML page only if n is an integer"""
    if n % 2 == 0:
        evenness = 'even'
    else:
        evenness = 'odd'
    return render_template('6-number_odd_or_even.html', n=n,
                           evenness=evenness)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
=======
""" creating an html with flask
1. the server listens on 0.0.0.0 on port 5000
2. routs / - display 'Hello HBNB!
3. route /hbnb - dispay 'hbnb '
4. create a /c/<text> route - display the text on the page
5. create a /python/<text> route - default text is "is cool"
6. create a /number/<n> route
"""

from flask import Flask, render_template

app = Flask(__name__)

# task 0


@app.route("/", strict_slashes=False)
def display():
    """ the root of the wed page"""

    return 'Hello HBNB!'

# task 1


@app.route("/hbnb", strict_slashes=False)
def hbnd():
    """the /hbnb page of the server"""

    return 'HBNB'

# task 2


@app.route("/c/<text>",  strict_slashes=False)
def c_text(text):
    """ (replace underscore _ symbols with a space)"""

    formated_text = text.replace('_', ' ')
    return "C {}".format(formated_text)


# task 3


@app.route("/python/", defaults={"text": 'is cool'}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_text(text):
    """display “Python ”, followed by the value of the text variable
    (replace underscore _ symbols with a space)
    """

    display_text = text.replace('_', ' ')
    return "Python {}".format(display_text)


# task 4


@app.route("/number/<int:n>", strict_slashes=False)
def is_a_number(n):
    """ display “n is a number” only if n is an integer
    """

    return "{} is a number".format(n)


# task 5


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n=None):
    """display a HTML page only if n is an integer"""
    if isinstance(n, int):
        return render_template("5-number.html", n=n)


# task 6

@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """ Number: n is even|odd” inside the tag BODY """

    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == "__main__":
    app.run()
>>>>>>> 365ffa39d2e9e7463dcfc2bc2a6d116df35790d3
