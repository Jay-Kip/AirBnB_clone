#!/usr/bin/python3
'''
Base model that defines all common attributes/methods for other classes
'''

from uuid import uuid4
from datetime import datetime
# from models.engine import file_storage
# from models import storage


class BaseModel:
    '''Defining the base model'''

    def __init__(self, *args, **kwargs):
        '''Initializes a new instance'''

        if kwargs:
            storage.new(self)

            for key, value in kwargs.items():
                if key != "__class__":

                    if key in ("created_at", "updated_at"):
                        '''convert datetime string to detetime object
                        '''
                        setattr(self, key, datetime.fromisoformat(value))

                    else:
                        setattr(self, key, value)

        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at

    def __str__(self):
        '''
        Returns string representation of an instance
        '''
        return "[{} ({}) {}".format(
                self.__class__.__name__,
                self.id,
                self.__dict__
                )

    def save(self):
        '''
        Saves the instance
        '''
        from models import storage
        self.update_at = datetime.now()
        storage.save()

    def to_dict(self):
        '''
        Saves to a dictionary
        '''
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
