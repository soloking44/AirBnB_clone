#!/usr/bin/python3

"""defines the City Model
inherits from the BaseModel
"""

from models.base_model import BaseModel


class City(BaseModel):
    """City Model"""

    # Attributes
    name: str = ""
    state_id: str = ""
