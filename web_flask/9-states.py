#!/usr/bin/python3
"""
start Flask application
"""

from flask import Flask, render_template
from models import *
from models import storage

app = Flask(__name__)


@app.route("/states", strict_slashes=False)
@app.route("/states/<state_id>", strict_slashes=False)
def states(state_id=None):
    """
    Display a list of states and cities in alphabetical order.

    Args:
        state_id (str, optional): The ID of a specific state.

    Returns:
        str: The rendered HTML template with the states and state_id as variables.
    """
    states = storage.all("State")
    if state_id is not None:
        state_id = "State." + state_id
    return render_template("9-states.html", states=states, state_id=state_id)


@app.teardown_appcontext
def teardown_db(exception):
    """
    Closes the storage connection when the application context is torn down.

    :param exception: The exception that occurred during the teardown process (if any).
    :type exception: Exception

    :return: None
    """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
