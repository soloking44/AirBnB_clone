#!/usr/bin/python3

"""defines the Review Model
inherits from the BaseModel
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Review Model"""

    # Attributes
    place_id: str = ""
    user_id: str = ""
    text: str = ""
