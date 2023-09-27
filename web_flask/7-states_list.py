#!/usr/bin/python3
"""
start Flask application
"""

from flask import Flask, render_template
from models import *
from models import storage

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states_list():
    """
    Display a HTML page with a list of states in alphabetical order.

    Returns:
        str: Rendered HTML template with the states variable.
    """
    states = sorted(list(storage.all("State").values()), key=lambda x: x.name)
    return render_template("7-states_list.html", states=states)


@app.teardown_appcontext
def teardown_db(exception):
    """
    Closes the storage connection after each request.

    :param exception: An optional parameter that represents any exception that occurred during the request.
    :type exception: Exception

    :return: None
    """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
