#!/usr/bin/python3
""" this is the city """

import uuid
from datetime import datetime
from models import storage
from models.base_model import BaseModel


class City(BaseModel):
    """ this shows the city class """
    state_id = ""
    name = ""
