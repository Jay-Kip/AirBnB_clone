#!/usr/bin/python3
"""
contains the entry point of the command interpreter
"""

import cmd


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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
