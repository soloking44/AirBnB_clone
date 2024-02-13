#!/usr/bin/python3

"""this data explains the UserModel class
It receives via the BaseModel
"""

from models.base_model import BaseModel


class User(BaseModel):
    """this is the User Model"""

    # Attributes
    email: str = ""
    password: str = ""
    first_name: str = ""
    last_name: str = ""

