#!/usr/bin/python3
'''
Defines a class City which inherits from from BaseModel
'''

from models.base_model import BaseModel


class City(BaseModel):
    '''
    Creates an instance of class City
    '''

    state_id = ""
    name = ""

'''
    def __init__(self, *args, **kwargs):
        
        initializes the instance City
        
        super().__init__(*args, **kwargs)
'''
