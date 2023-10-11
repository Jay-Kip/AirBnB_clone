import unittest
from models import base_model
'''
Unit test for the base model class
'''


class TestBaseModel(unittest.TestCase):
    '''Tests the initialization of the base model class'''

    def test_initialization(self):
        '''Creates an instance of the base model'''
        model = base_model.BaseModel()

        '''Checks that the instance is of the correct type'''
        self.assertIsInstance(model, base_model.BaseModel)
