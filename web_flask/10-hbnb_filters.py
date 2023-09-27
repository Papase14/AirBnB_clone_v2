#!/usr/bin/python3
"""
starts a Flask web application
"""

from flask import Flask, render_template
from models import *
from models import storage

app = Flask(__name__)


@app.route("/hbnb_filters", strict_slashes=False)
def filters():
    """
    Route handler for the "/hbnb_filters" URL.
    
    Retrieves data from the database and renders an HTML template.
    
    Returns:
        str: Rendered HTML page from the "10-hbnb_filters.html" template.
        
    Example Usage:
        states = storage.all("State").values()
        amenities = storage.all("Amenity").values()
        return render_template("10-hbnb_filters.html", states=states, amenities=amenities)
    """
    states = storage.all("State").values()
    amenities = storage.all("Amenity").values()
    return render_template("10-hbnb_filters.html", states=states, amenities=amenities)


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
