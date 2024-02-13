#!/usr/bin/python3

"""defines the State Model
inherits from the BaseModel
"""

from models.base_model import BaseModel


class State(BaseModel):
    """State Model"""

    # Attributes
    name: str = ""
