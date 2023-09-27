#!/usr/bin/python3
"""
starts a Flask web applicationstart Flask application"""

from flask import Flask, render_template
from models import *
from models import storage

app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states():
    """
    Renders a template called "8-cities_by_states.html" and passes a 
    list of all the states from the database.

    Returns:
        The rendered template "8-cities_by_states.html".
    """
    states = storage.all("State").values()
    return render_template("8-cities_by_states.html", states=states)


@app.teardown_appcontext
def teardown_db(exception):
    """
    Closes the database connection after each request.

    :param exception: An optional parameter that represents any exception 
    that occurred during the request.
    
    :type exception: Exception

    :return: None
    """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
