#!/usr/bin/python3
"""script that starts a Flask web application"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """
    script that starts a Flask web application, /: display “Hello HBNB!”
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """
    script that starts a Flask web application, /hbnb: display “HBNB”
    """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """
    script that starts a Flask web application, /c: display “C + text”
    """
    return "C {}".format(text.replace('_', ' '))


@app.route("/python/", defaults={'text': "is cool"})
@app.route("/python/<text>", strict_slashes=False)
def python(text):
    """
    starts a Flask web application, /python: display “Python + text”
    """
    return "Python {}".format(text.replace('_', ' '))


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """
    starts a Flask web application, /number/<int:n>: display “n is a number”
    """
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """
    starts a Flask web application, /number/<int:n>: display “n is a number”
    """
    return render_template("5-number.html", n=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
