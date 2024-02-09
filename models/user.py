#!/usr/bin/python3
""" this is the user """

import uuid
from models.base_model import BaseModel


class User(BaseModel):
    """ this is User class """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

