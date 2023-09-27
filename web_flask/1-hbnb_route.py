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


@app.route("/hbnb")
def hbnb():
    """
    Returns the string "HBNB" when a request is made to the "/hbnb" URL path.

    :return: The string "HBNB"
    """
    return "HBNB"


if "__name__" == "__main__":
    app.run(host="0.0.0.0", port=5000)
