#!/usr/bin/python3
""" Place Module for HBNB project """
from os import getenv
import models
from models.review import Review
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Float, ForeignKey
from sqlalchemy import Integer, String, Table
from sqlalchemy.orm import relationship


class Place(BaseModel, Base):
    """A place to stay"""

    if getenv("HBNB_TYPE_STORAGE") == "db":
        __tablename__ = "places"
        city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
        user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024))
        number_rooms = Column(Integer, default=0, nullable=False)
        number_bathrooms = Column(Integer, default=0, nullable=False)
        max_guest = Column(Integer, default=0, nullable=False)
        price_by_night = Column(Integer, default=0, nullable=False)
        latitude = Column(Float)
        longitude = Column(Float)

        reviews = relationship("Review", backref="place", cascade="delete")
        amenities = relationship(
            "Amenity",
            secondary="place_amenity",
            backref="place_amenities",
            viewonly=False,
        )

        place_amenity = Table(
            "place_amenity",
            Base.metadata,
            Column(
                "place_id",
                String(60),
                ForeignKey("places.id"),
                primary_key=True,
                nullable=False,
            ),
            Column(
                "amenity_id",
                String(60),
                ForeignKey("amenities.id"),
                primary_key=True,
                nullable=False,
            ),
        )

    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

    def __init__(self, *args, **kwargs):
        """initializes Place"""
        super().__init__(*args, **kwargs)

    # For FileStorage
    def get_reviews(self):
        """
        Returns the list of Review instances with place_id equals to the current Place.id
        """
        return self.reviews.filter(Review.place_id == self.id)

    def amenities(self, amenity):
        """
        Add an Amenity instance to the list of amenities associated with the current Place instance.
        """
        self.amenity_ids.append(amenity.id)

    def amenities(self):
        """
        Retrieve a list of Amenity instances associated with the current Place instance.
        """
        amenity_objs = []
        for a_id in self.amenity_ids:
            amenity_objs.append(models.storage.get("Amenity", str(a_id)))
        return amenity_objs
