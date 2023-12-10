#!/usr/bin/python3
"""
This module contains class user
which inherits from class BaseModel
"""


from models.base_model import BaseModel


class User(BaseModel):
    """
    User class for user instances
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
