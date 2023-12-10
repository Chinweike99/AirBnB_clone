#!/usr/bin/python3
"""
This module contains class City
which  inherits from BaseModel
"""


from models.base_model import BaseModel


class City(BaseModel):
    """
    City class for city instances
    """

    state_id = ""
    name = ""
