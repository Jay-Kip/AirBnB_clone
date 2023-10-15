#!/usr/bin/python3
"""
Class user that inherits from super class 'BaseModel'
"""


from models.base_model import BaseModel


class User(BaseModel):
    '''
    THis class inherits from BaseModel
    '''

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        '''initialize user instance'''
        super().__init__(*args, **kwargs)
