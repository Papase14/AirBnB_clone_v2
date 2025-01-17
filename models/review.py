#!/usr/bin/python3
""" Review module for the HBNB project """
from os import getenv
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey

class Review(BaseModel, Base):
    """ 
    Review class to store review information 
    Attributes:
        __tablename__ (str): The name of the table in the database.
        place_id (str): The foreign key referencing the id of the place associated with the review.
        user_id (str): The foreign key referencing the id of the user who wrote the review.
        text (str): The text content of the review.
    """

    if getenv("HBNB_TYPE_STORAGE") == 'db':
        __tablename__ = 'reviews'
        place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        text = Column(String(1024), nullable=False)
    else:
        place_id = ""
        user_id = ""
        text = ""

    def __init__(self, *args, **kwargs):
        """initializes Review"""
        super().__init__(*args, **kwargs)
