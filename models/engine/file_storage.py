#!/usr/bin/python3
"""
Defines class filestorage that serializes
and deserializes JSON file to instances
"""

import json
from models.base_model import BaseModel
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.user import User


class FileStorage:
    '''
    Serializes instances to a JSON file
    Deserializes a Json file to an instance
    __file_path - private class attribute - path to the file
    __objects - private class attribute - the dixtionary
    '''

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
        with open(self.__file_path, "w") as file:
            dict_storage = {}
            for key, value in self.__objects.items():
                dict_storage[key] = value.to_dict()
            json.dump(dict_storage, file)

    def reload(self):
        """
        deserializes the JSON file to __objects
        if the json file (__file_path) exists
        if not it does nothing. if the file
        does not exist o exception is raised
        """
        try:
            with open(FileStorage.__file_path) as file:
                obj_dict = json.load(file)
                for o in obj_dict.values():
                    class_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(class_name)(**o))
                #for i in obj_dict.values():
                #for key, value in obj_dict.items():
                    #class_name, obj_id = key.split('.')
                    #class_type = class_registry.get(class_name)
                    #new_obj = class_type(**value)
                    #self.__objects[key] = new_obj
                    #nme = i["__class__"]
                    #del i["__class__"]
                    #self.new(eval(nme)(**i))
        except FileNotFoundError:
            return
