#!/usr/bin/python3

"""defines the UserModel class
inherits from the BaseModel
"""

from models.base_model import BaseModel


class User(BaseModel):
    """User Model"""

    # Attributes
    email: str = ""
    password: str = ""
    first_name: str = ""
    last_name: str = ""
