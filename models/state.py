#!/usr/bin/python3
'''
Class State that inherits from Super class BaseModel
'''

from models.base_model import BaseModel


class State(BaseModel):
    '''
    creates an object stae that inherits from BaseModel
    '''

    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
