#!/usr/bin/python3
"""Defines review class
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """ Review class!
    Attributes:
        place_id (str): ID of place with review
        user_id (str): ID of user leaving review
        text (str): text of review
    """
    place_id = ""
    user_id = ""
    text = ""
