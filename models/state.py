#!/usr/bin/python3
"""
This module contains class state
which inherits from class BaseModel
"""


from models.base_model import BaseModel


class State(BaseModel):
    """
    State class for state instances
    """

    name = ""
