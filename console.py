#!/usr/bin/python3
"""
contains the entry point of the command interpreter
"""

import cmd

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb)"

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

if __name__ == '__main__':
    HBNBCommand().cmdloop()
