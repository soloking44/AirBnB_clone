#!/usr/bin/python3

"""defines the Amenity Model
inherits from the BaseModel
"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity Model"""

    # Attributes
    name: str = ""
