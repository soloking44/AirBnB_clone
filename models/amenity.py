#!/usr/bin/python3
""" this choes the amenity class """

import uuid
from datetime import datetime
from models import storage
from models.base_model import BaseModel


class Amenity(BaseModel):
    """ this is the amenity """
    name = ""
