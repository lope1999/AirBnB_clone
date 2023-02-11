#!/usr/bin/python3
''' console module '''
import cmd
import sys
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
import json


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
        return True

    def emptyline(self):
        ''' do nothing with empty line '''
        pass

    def do_create(self, classname):
        ''' create a new instance of '''
        if len(classname) == 0:
            print('** class name missing **')
        else:
            try:
                new = eval("{}()".format(classname))
                new.save()
                print(new.id)
            except:
                print('** class doesn\'t exist **')

    def help_create(self):
        ''' help create '''
        print("Create command to create a class\n")

    def do_show(self, line):
        '''represents an instance'''
        args = line.split()
        if len(args) == 0:
            print('** class name missing **')
        else:
            try:
                eval("{}()".format(args[0]))
            except:
                print('** class doesn\'t exist **')
                return False
        if len(args) < 2:
            print('** instance id missing **')
            return False

        all_objs = storage.all()
        for i in all_objs.keys():
            if i == "{}.{}".format(args[0], args[1]):
                print(all_objs[i])
                return
        print('** no instance found **')

    def help_show(self):
        ''' help show '''
        print("Show command to display the classes\n")

    def do_destroy(self, line):
        ''' deletes an instance based on the class id'''
        args = line.split()
        if len(line) == 0:
            print('** class name missing **')
            return False
        else:
            try:
                eval("{}()".format(args[0]))
            except:
                print('** class doesn\'t exist ** ')
        if len(args) < 2:
            print('** instance id missing **')
            return False

        all_objs = storage.all()
        for i in all_objs:
            if i == "{}.{}".format(args[0], args[1]):
                all_objs.pop(i)
                storage.save()
                return
        print('** no instance found **')

    def help_destroy(self):
        ''' help destroy '''
        print("Destroy command to destroy a class\n")

    def do_all(self, line):
        ''' prints all string representations of instances'''
        args = line.split()
        all_objs = storage.all()
        final = []

        if len(args) == 0:
            for i in all_objs:
                strarg = str(all_objs[i])
                final.append(strarg)
            if final != []:
                print(final)

        elif len(args) > 0:
            for i in all_objs:
                if i.startswith(args[0]):
                    strarg = str(all_objs[i])
                    final.append(strarg)
            if final == []:
                print('** class doesn\'t exist **')
                return False
            else:
                print(final)

    def help_all(self):
        ''' help all'''
        print("All command to show all instances\n")

    def do_update(self, line):
        ''' updates an instance based on class name and id'''
        args = line.split()
        flag = 0

        if len(line) == 0:
            print('** class name missing **')
            return False

        try:
            clsname = line.split()[0]
            eval("{}()".format(clsname))
        except:
            print('** class doesn\'t exist **')
            return False

        try:
            instanceid = line.split()[1]
        except:
            print('** instance id missing **')
            return False

        all_objs = storage.all()
        try:
            clschange = all_objs["{}.{}".format(clsname, instanceid)]
        except:
            print('** no instance found **')
            return False

        try:
            attributename = line.split()[2]
        except:
            print('** attribute name missing **')
            return False

        try:
            updatevalue = line.split()[3]
        except:
            print('** value missing **')
            return False

            if updatevalue.isdecimal() is True:
                setattr(clschange, attributename, int(updatevalue))
                storage.save()
            else:
                try:
                    setattr(clschange, attributename, float(updatevalue))
                    storage.save()
                except:
                    setattr(clschange, attributename, updatevalue)
                    storage.save()

    def help_update(self):
        '''help update'''
        print("update command to update attributes")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
