#!/usr/bin/python3
'''
Defies class review that inherits from super class BaseModel
'''


from models.base_model import BaseModel


class Review(BaseModel):
    '''
    Defines class review
    '''

    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        '''
        initializes the class
        '''
        super().__init__(*args, **kwargs)
