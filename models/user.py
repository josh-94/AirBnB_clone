#!/usr/bin/python3
"""
Defines User Class that inherits from BaseModel
"""
from models.base_model import BaseModel


class User(BaseModel):
    """create User objects
    Attributes:
        email (str): user email
        password (str): user password
        first_name (str): first name of the user
        last_name (str): last name of the user
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
