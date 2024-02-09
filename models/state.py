#!/usr/bin/python3
""" this is state """

import uuid
from datetime import datetime
from models import storage
from models.base_model import BaseModel


class State(BaseModel):
    """ this shows State class """
    name = ""
