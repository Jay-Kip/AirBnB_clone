#!/usr/bin/python3
"""
Defines class filestorage that serializes 
and deserializes JSON file to instances
"""

import json

class FileStorage:

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        returns __objects
        """
        return self.__objects

    def new(self, obj):
        self.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        with open(self.__file_path, mode="w") as f:
            dict_storage = {}
            for key, value in self.__objects.items():
                dic_storage[key] = value.to_dict()
            json.dump(dict_storage, f)

    def reload(self):
        """
        deserializes the JSON file to __objects
        if the json file (__file_path) exists
        if not it does nothing. if the file
        does not exist o exception is raised
        """
        try:
            with open(FileStorage.__file_path) as f:
                objdict = json.load(f)
                for o in objdict.values():
                    cls_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(cls_name)(**o))
        except FileNotFoundError:
            return
