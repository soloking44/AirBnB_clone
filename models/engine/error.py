#!/usr/bin/python3

"""
this explains the customer errors applied in the File Storage
"""


class ModelNotFoundError(Exception):
    """boosted as unidentified module occurred"""
    def __init__(self, arg="BaseModel"):
        super().__init__(f"Model with name {arg} is not registered!")


class InstanceNotFoundError(Exception):
    """boosted as unidentified id occurred"""

    def __init__(self, obj_id="", mod="BaseModel"):
        super().__init__(
                f"Instance of {mod} with id {obj_id} does not exist!")
