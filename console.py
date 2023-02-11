#!/usr/bin/python3
''' console module '''
import cmd
import sys


class HBNBCommand(cmd.Cmd):
    ''' HBNB class contains entry point '''

    prompt = '(hbnb) '

    def do_EOF(self, line):
        ''' exit the program '''
        return True

    def help_quit(self):
        ''' help quit '''
        print ("Quit command to exit the program\n")

    def do_quit(self, arg):
        ''' quit interpreter '''
        sys.exit(1)

    def emptyline(self):
        ''' do nothing with empty line '''
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
