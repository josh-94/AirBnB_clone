#!/usr/bin/python3
"""Defines Place class
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """ Place class!
    Attributes:
        city_id (str): ID of city that place belongs to
        user_id (str): ID of User who owns place
        name (str): name's place
        description (str): place description
        number_rooms (int): number of rooms
        number_bathrooms (int):
        max_guest (int): maximum number of guests allowed
        price_by_night (int): price by night
        latitude (float): latitude coordinate
        longitude (float): longitude coordinate
        amenity_ids (list of str): list of amenities provided
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude: float = 0.0
    longitude: float = 0.0
    amenity_ids = []
