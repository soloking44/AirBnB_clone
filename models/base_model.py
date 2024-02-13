#!/usr/bin/python3
"""
this data sets the BaseModel class that will
aid the base class to all the models."""

from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """this is base class of all the classes"""

    def __init__(self, *args, **kwargs):
        """initialize it to deserialize
        a serialized class or setup a new"""

        # initialize if nothing is passed
        if kwargs == {}:
            self.id = str(uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()
            models.storage.new(self)
            return

        # using key words (deserialize)
        for key, val in kwargs.items():
            if key == '__class__':
                continue
            self.__dict__[key] = val
        if 'created_at' in kwargs:
            self.created_at = datetime.strptime(
                    kwargs['created_at'],
                    '%Y-%m-%dT%H:%M:%S.%f')
        if 'updated_at' in kwargs:
            self.updated_at = datetime.strptime(
                    kwargs['updated_at'],
                    '%Y-%m-%dT%H:%M:%S.%f')

    def __str__(self):
        """replace str simulation of self"""
        fmt = "[{}] ({}) {}"
        return fmt.format(
                type(self).__name__,
                self.id,
                self.__dict__)

    def save(self):
        """modifies last updated valu"""
        self.updated_at = datetime.utcnow()
        models.storage.save()

    def to_dict(self):
        """offerss a dictionary simulation of self"""
        temp = {**self.__dict__}
        temp['__class__'] = type(self).__name__
        temp['created_at'] = self.created_at.strftime('%Y-%m-%dT%H:%M:%S.%f')
        temp['updated_at'] = self.updated_at.strftime('%Y-%m-%dT%H:%M:%S.%f')
        return temp

    @classmethod
    def all(cls):
        """Recovers all present instances of cls"""
        return models.storage.find_all(cls.__name__)

    @classmethod
    def count(cls):
        """fetch the number of all present instances of cls"""
        return len(models.storage.find_all(cls.__name__))

    @classmethod
    def creates(cls, *args, **kwargs):
        """generates an Instance"""
        new = cls(*args, **kwargs)
        return new.id

    @classmethod
    def show(cls, instance_id):
        """Recovers an instance"""
        return models.storage.find_by_id(
            cls.__name__,
            instance_id
        )

    @classmethod
    def destroy(cls, instance_id):
        """removes an instance"""
        return models.storage.delete_by_id(
            cls.__name__,
            instance_id
        )

    @classmethod
    def update(cls, instance_id, *args):
        """modifies an instance
        if args has one elem and its a dict:
        it updates by key value
        else:
        updates by first being key and second being value"""
        if not len(args):
            print("** attribute name missing **")
            return
        if len(args) == 1 and isinstance(args[0], dict):
            args = args[0].items()
        else:
            args = [args[:2]]
        for arg in args:
            models.storage.update_one(
                cls.__name__,
                instance_id,
                *arg
            )

