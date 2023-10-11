#!/usr/bin/python3
'''
Base model that defines all common attributes/methods for other classes
'''

from uuid  import uuid4
from datetime import datetime


class BaseModel:
    '''Defining the base model'''

    def __init__(self):
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        return "[{} ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        self.update_at = datetime.now()

    def to_dict(self):
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
