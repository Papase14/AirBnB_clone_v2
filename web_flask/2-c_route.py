#!/usr/bin/python3
"""
Write a script that starts a Flask web application
"""

from flask import Flask

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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
