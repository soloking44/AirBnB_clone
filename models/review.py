#!/usr/bin/python3
"""this is class review
"""

import uuid
from datetime import datetime
from models import storage
from models.base_model import BaseModel


class Review(BaseModel):
    """ this the Review class  """
    place_id = ""
    user_id = ""
    text = ""
