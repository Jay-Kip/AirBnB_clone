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
        '''obj_dict = {}
        for key, obj in self.__objects.items():
            obj.__dict[key] = obj.to_dict()

        with open(self.__file_path, 'w') as file:
            json.dump(obj_dict, file)'''
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
        '''

            with open(FileStorage.__file_path) as f:
                objdict = json.load(f)
                for o in objdict.values():
                    cls_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(cls_name)(**o))
        except FileNotFoundError:
            return'''
