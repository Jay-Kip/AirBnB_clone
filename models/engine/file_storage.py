#!/usr/bin/python3
"""
Defines class filestorage that serializes
and deserializes JSON file to instances
"""

import json
from models.base_model import BaseModel


class FileStorage:

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        returns __objects
        """
        return self.__objects

    def new(self, obj):
        '''
        sets in __object with key <obj class name>.id
        '''
        self.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        '''
        serializes the __objects to the specified HSIN file
        '''
        with open(self.__file_path, mode="w") as f:
            dict_storage = {}
            for key, value in self.__objects.items():
                dict_storage[key] = value.to_dict()
            json.dump(dict_storage, f)

    def reload(self):
        """
        deserializes the JSON file to __objects
        if the json file (__file_path) exists
        if not it does nothing. if the file
        does not exist o exception is raised
        """
        try:
            with open(FileStorage.__file_path, 'r') as file:
                obj_dict = json.load(file)
                for key, value in obj_dict.items():
                    class_name, obj_id = key.split('.')
                    class_ = eval(class_name)
                    obj = class_(**value)
                    self.__object[key] = obj
        except FileNotFoundError:
            return
