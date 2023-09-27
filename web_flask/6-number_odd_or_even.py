#!/usr/bin/python3
"""
Write a script that starts a Flask web application
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """
    Returns a greeting message.

    Returns:
        str: A string containing the greeting message "Hello HBNB!".
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """
    Returns the string "HBNB" when a request is made to the "/hbnb" URL.

    :return: The string "HBNB"
    """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """
    Returns a string that starts with "C " followed by the value of `text` with underscores replaced by spaces.

    Args:
        text (str): The value of `text` is extracted from the URL.

    Returns:
        str: A string that starts with "C " followed by the value of `text` with underscores replaced by spaces.
    """
    return "C " + text.replace("_", " ")


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text="is cool"):
    """
    Concatenates the word "Python" with the value of the "text" parameter, replacing underscores
    with spaces if present.

    Args:
        text (str, optional): The text to be concatenated with "Python". Defaults to "is cool".

    Returns:
        str: The concatenated string.
    """
    return "Python " + text.replace("_", " ")


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """
    Returns a string that includes the value of `n` formatted as a number.

    :param n: (optional) An integer value that represents a number.
    :type n: int
    :return: A string that includes the value of `n` formatted as a number.
    :rtype: str
    """
    return "{:d} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """
    Renders a template called "5-number.html" and passes the value of the
    parameter to the template.

    Args:
        n (int): An integer representing the number to be passed to the template.

    Returns:
        str: The rendered template with the value of the parameter passed to it.
    """
    return render_template("/5-number.html", n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def odd_or_even(n):
    """
    Determines whether a given number is odd or even.

    Args:
        n (int): The number to be checked.

    Returns:
        str: A string indicating whether the number is odd or even.
    """
    if n % 2 == 0:
        oddoreven = "even"
    else:
        oddoreven = "odd"

    return render_template("/6-number_odd_or_even.html", n=n, oddoreven=oddoreven)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
