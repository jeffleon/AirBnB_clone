#!/usr/bin/python3
"""
Module for Console Class
"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models import storage
import json
import shlex
import re
import os


class HBNBCommand(cmd.Cmd):
    """ Class HBNBCommand"""
    prompt = '(hbnb) '
    dic_class = {'BaseModel': BaseModel, 'User': User, 'City': City,
                 'Place': Place, 'Amenity': Amenity, 'State': State,
                 'Review': Review}

    def do_EOF(self, arg):
        """method that exit if find EOF
        """
        print("")
        exit()

    def do_quit(self, arg):
        """method that exit if type quit
        """
        exit()

    def do_create(self, arg):
        """method that create a new Object
        """
        nuevo = None
        if arg:
            new_list = arg.split()
            if len(new_list) == 1:
                if arg in self.dic_class.keys():
                    nuevo = self.dic_class[arg]()
                    nuevo.save()
                    print(nuevo.id)
                else:
                    print('** class doesn\'t exist **')
        else:
            print('** class name missing **')

    def do_destroy(self, args):
        """method that deletes an Object
        """
        new_list = args.split()
        if args and len(new_list) == 2:
            if new_list[0] in self.dic_class.keys():
                i = False
                objects = storage.all()
                for key in objects.keys():
                    if key == new_list[0] + '.' + new_list[1]:
                        del objects[key]
                        i = True
                        break
                if i is not True:
                    print('** no instance found **')
                else:
                    storage.save()
            else:
                print('** class doesn\'t exist **')
        elif args and len(new_list) == 1:
            if new_list[0] in self.dic_class.keys():
                print('** instance id missing **')
            else:
                print('** class doesn\'t exist **')
        elif len(new_list) < 1:
            print('** class name missing **')

    def do_show(self, args):
        """method that prints the Object
        """
        new_list = args.split()
        if args and len(new_list) == 2:
            if new_list[0] in self.dic_class.keys():
                i = False
                for key, value in storage.all().items():
                    if key == new_list[0] + '.' + new_list[1]:
                        i = True
                        print(value)
                        break
                if i is not True:
                    print('** no instance found **')
            else:
                print('** class doesn\'t exist **')
        elif args and len(new_list) == 1:
            if new_list[0] in self.dic_class.keys():
                print('** instance id missing **')
            else:
                print('** class doesn\'t exist **')
        elif len(new_list) < 1:
            print('** class name missing **')

    def do_all(self, args):
        """method that print all Objects
        """
        if args:
            new_list = args.split()
            G_dic = list()
            if args and len(new_list) == 1:
                if new_list[0] in self.dic_class.keys():
                    new_var = dict(storage.all())
                    for value in new_var.values():
                        if new_list[0] == value.__class__.__name__:
                            G_dic.append(str(value))
                    print(G_dic)
                else:
                    print('** class doesn\'t exist **')
        else:
            G_dic = list()
            for value in storage.all().values():
                G_dic.append(str(value))
            print(G_dic)

    def do_update(self, args):
        """method that updates the specified object
        """
        atribute = ""
        new_list = args.split()
        if len(new_list) >= 4:
            index = args.find("\"")
            if index != -1:
                if args.find("\"", index + 1) != -1:
                    atribute = ' '.join(new_list[3:])
                    new_list = new_list[:4]
                    new_list[3] = atribute.replace("\"", "")
        if args:
            if new_list[0] in self.dic_class.keys():
                if len(new_list) >= 2:
                    i = False
                    modificar = None
                    for key, value in storage.all().items():
                        if key == new_list[0] + '.' + new_list[1]:
                            i = True
                            modificar = value
                            break
                    if i is not True:
                        print('** no instance found **')
                    elif len(new_list) == 2:
                        print('** attribute name missing **')
                    elif len(new_list) == 3:
                        print('** value missing **')
                    elif len(new_list) == 4:
                        if new_list[3].isnumeric():
                            new_list[3] = int(new_list[3])
                        elif '.' in new_list[3]:
                            try:
                                new_list[3] = float(new_list[3])
                            except:
                                pass
                        setattr(modificar, new_list[2], new_list[3])
                        modificar.save()
                elif args and len(new_list) == 1:
                    print('** instance id missing **')
            else:
                print('** class doesn\'t exist **')
        else:
            print('** class name missing **')

    def all(self, args):
        """method that print all Objects
        """
        G_dic = list()
        new_var = dict(storage.all())
        for value in new_var.values():
            if args == value.__class__.__name__:
                G_dic.append(str(value))
        print(str(G_dic).replace('\"', ''))

    def count(self, args):
        """count instances
        """
        count = 0
        new_var = dict(storage.all())
        for value in new_var.values():
            if args == value.__class__.__name__:
                count += 1
        print(count)

    def show(self, arg, id_):
        """
        """
        i = False
        for key, value in storage.all().items():
            if key == arg + '.' + id_:
                i = True
                print(value)
                break
        if i is not True:
            print('** no instance found **')

    def default(self, arg):
        """method that prints a message in case a wrong command is entered
        """
        dic_methods = {"all": self.all, "destroy": self.do_destroy,
                       "show": self.do_show, "count": self.count,
                       "update": self.do_update}
        list_patterns = ['(.+)\.all\(\)$', '(.+)\.count\(\)$',
                         '(.+)\.show\(\"(.+)\"\)$',
                         '(.+)\.destroy\(\"(.+)\"\)$',
                         '(.+)\.update\(\"(.+)\", \"(.+)\", \"(.+)\"\)$']
        state = False
        sspc = arg.split()
        if len(sspc) == 1 or (arg.find('update') != -1 and len(sspc) == 3):
            new_list = arg.split('.', 1)
            if arg.find('(') != -1 and arg.find(')') != -1:
                try:
                    metodo = new_list[1].split('(')[0]
                    id_ = new_list[1].split('(')[1].replace(')',
                                                            '').replace('"',
                                                                        '')
                    attrs = id_.split(', ')
                except:
                    pass
            for pa_match in list_patterns:
                if re.match(pa_match, arg) is not None:
                    if new_list[0] in self.dic_class.keys():
                        if metodo in dic_methods.keys():
                            if id_ == "":
                                dic_methods[metodo]('{}'.format(new_list[0]))
                            elif len(attrs) == 1:
                                dic_methods[metodo](new_list[0] + ' ' + id_)
                            else:
                                attrs[2] = '"' + attrs[2] + '"'
                                send = new_list[0] + " " + " ".join(attrs)
                                dic_methods[metodo](send)
                            state = True
                    break
        if state is False:
            print('command not found')

    def emptyline(self):
        """redefine method that does nothing when empty line is entered
        """
        pass

#    def precmd(self, line):
#        os.isatty()
#
#    def postcmd(self, stop, line):
#        pass
#
if __name__ == '__main__':
    HBNBCommand().cmdloop()
