#!/usr/bin/python3
"""
contains the entry point of the command interpreter
"""

import cmd
from shlex import split
import re

import models
from models.base_model import BaseModel


CLASSES = [
        "BaseModel"
        ]


def all(self):
    '''
    Returns dict objs
    '''
    return self.__objects

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """
        to quit the command interpreter
        """
        return True

    def do_EOF(self, arg):
        """
        to exit ctrl+D EOF
        """
        print()
        return True

    def emptyline(self):
        """
        do nothing on an empty line
        """
        pass

    def help_quit(self):
        """
        Display help message for the quit command
        """
        print("Quit command to exit the program")
        print()

    def help_EOF(self):
        """
        Display help message for the quit command
        """
        print("Quit the program")

    def default(self, line):
        """
        Default behavior for unknown commands
        """
        print(f"Unknown command: {line}")

    def do_create(self, line):
        '''
        Create a new instance of basemodel
        '''
        args = line.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in CLASSES:
            print("** class doesn't exist **")
            return
        new_obj = CLASSES
        new_obj.save()
        print(new_obj.id)

    def do_show(self, line):
        '''
        prints the string representation of an instance
        '''
        args = line.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in CLASSES:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        obj_id = args[1]
        key = class_name + "." + obj_id
        if key not in models.storage.all():
            print("** no instance found **")
            return
        print(models.storage.all()[key])

    def do_destroy(self, line):
        '''
        Deletes an instance bases on the class name and id
        '''
        args = line.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in CLASSES:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        obj_id = args[1]
        key = class_name + "." + obj_id
        if key not in models.storage.all():
            print("** no instance found **")
            return
        models.storage.all().pop(key)
        models.storage.save()

        def do_all(self, line):
            '''
            print all string representation of instances
            '''
            args = line.split()
            if args and args[0] not in CLASSES:
                print("** class doesn't exist **")
                return
            objects = []
            if not args:
                objects = models.storage.all().values()
            else:
                objects = [obj for obj in models.storage.all().values()
                           if type(obj).__name__ == args[0]]
            print([str(obj) for obj in objects])

        def do_update(self, line):
            '''
            Updates an instance based on the class name and id
            '''
            args = line.split()
            if not args:
                print("** class name missing **")
                return
            class_name = args[0]
            if class_name not in CLASSES:
                print("** class doesn't exist **")
                return
            if len(args) < 2:
                print("** instance id missing **")
                return
            obj_id = args[1]
            key = class_name + "." + obj_id
            if key not in models.storage.all():
                print("** no instance found **")
                return
            if len(args) < 3:
                print("** attribute name missing **")
                return
            if len(args) < 4:
                print("** value missing **")
                return
            attribute_name = args[2]
            attribute_value = args[3]
            obj = models.storage.all()[key]
            setattr(obj, attribute_name, attribute_value)
            obj.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
