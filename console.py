#!/usr/bin/python3
"""
contains the entry point of the command interpreter
"""

import cmd
from shlex import split
import re

import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage


CLASSES = [
        "BaseModel",
        "User",
        "State",
        "City",
        "Amenity",
        "Place",
        "Review",
        ]


def parse(arg):
    curly_braces = re.search(r"\{(.*?)\}", arg)
    brackets = re.search(r"\[(.*?)\]", arg)
    if curly_braces is None:
        if brackets is None:
            return [i.strip(",") for i in split(arg)]
        else:
            lexer = split(arg[:brackets.span()[0]])
            retl = [i.strip(",") for i in lexer]
            retl.append(brackets.group())
            return retl
    else:
        lexer = split(arg[:curly_braces.span()[0]])
        retl = [i.strip(",") for i in lexer]
        retl.append(curly_braces.group())
        return retl


def check_args(args):
    '''
    checks args
    '''
    arg_list = parse(args)

    if len(arg_list) == 0:
        print("** class name missing **")
    elif arg_list[0] not in CLASSES:
        print("** class doesn't exist **")
    else:
        return arg_list


def all(self):
    '''
    Returns dict objs
    '''
    return self.__objects


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    storage = models.storage

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
        args = check_args(line)
        if args:
            print(eval(args[0])().id)
            self.storage.save()
        '''args = line.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in CLASSES:
            print("** class doesn't exist **")
            return
        new_obj = CLASSES
        self.storage.save()
        print(new_obj.id)'''

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
        arg_list = line.split()
        objects = self.storage.all().values()
        if not arg_list:
            print([str(obj) for obj in objects])
        else:
            if arg_list[0] not in CLASSES:
                print("** class doesn't exist **")
            else:
                print([str(obj) for obj in objects
                       if arg_list[0] in str(obj)])

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
