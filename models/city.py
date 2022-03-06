#!/usr/bin/python3
"""Defines City class
"""
from models.base_model import BaseModel


class City(BaseModel):
    """ City class!
    Attributes:
        name (str): name of City
        state_id (str): ID of state the city
    """
    name = ""
    state_id = ""
