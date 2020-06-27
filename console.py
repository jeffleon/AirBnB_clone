#!/usr/bin/python3
"""
Module for Console Class
"""
import cmd
from models.base_model import BaseModel
from models import storage
import json

class HBNBCommand(cmd.Cmd):
    """ Class HBNBCommand"""
    prompt = '(hbnb) '
    def do_EOF(self, arg):
        """method that exit if find EOF
        """
        exit()

    def do_quit(self, arg):
        """method that exit if type quit
        """
        exit()

    def do_create(self, arg):
        """method that create a new Object 
        """
        if arg:
            if arg == 'BaseModel':
                nuevo = BaseModel()
                nuevo.save()
                print(nuevo.id)
            else:
                print('** class doesn\'t exist **')
        else:
            print('** class name missing **')
    def do_destroy(self, args):
        """method that destroy an Object
        """
        new_list = args.split()
        if args and len(new_list) == 2:
            if new_list[0] == 'BaseModel':
                i = False
                objects = storage.all()
                for key in objects.keys():
                    if key == new_list[0] + '.' + new_list[1]:
                        del objects[key]
                        i = True
                        break
                if i == False:
                    print('** no instance found **')
                else:
                    with open('file.json', mode='w', encoding='utf-8') as s_file:
                        json.dump(objects, s_file)
            else:
                print('** class doesn\'t exist **')
        elif args and len(new_list) == 1:
            print('** instance id missing **')
        elif len(new_list) < 1:
            print('** class name missing **')

    def do_show(self, args):
        """method that show an Object
        """
        new_list = args.split()
        if args and len(new_list) == 2:
            if new_list[0] == 'BaseModel':
                i = False
                for key, value in storage.all().items():
                    if key == new_list[0] + '.' + new_list[1]:
                        i = True
                        print(BaseModel(**value))
                        break
                if i == False:
                    print('** no instance found **')
            else:
                print('** class doesn\'t exist **')
        elif args and len(new_list) == 1:
            print('** instance id missing **')
        elif len(new_list) < 1:
            print('** class name missing **')
        
    def do_all(self, args):
        """method that print all Objects
        """
        new_list = args.split()
        G_dic = list()
        if args and len(new_list) == 1:
            if new_list[0] == 'BaseModel':
                new_var = dict(storage.all())
                for value in new_var.values():
                    G_dic.append(str(BaseModel(**value)))
                print(G_dic)
            else:
                print('** class doesn\'t exist **')
    
    def do_update(self, args):
        atribute = ""
        new_list = args.split()
        if len(new_list) > 4:
            index = args.find("\"")
            if index != -1:
                if args.find("\"", index + 1) != -1:
                    atribute = ' '.join(new_list[3:])
                    new_list = new_list[:4]
                    new_list[3] = atribute.replace("\"", "")
        if args: 
            if new_list[0] == 'BaseModel':
                if len(new_list) >= 2:
                    i = False
                    modificar = None
                    for key, value in storage.all().items():
                        if key == new_list[0] + '.' + new_list[1]:
                            i = True
                            modificar = BaseModel(**value)
                            break
                    if i == False:
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
                                new_list[3]= float(new_list[3])
                            except:
                                pass
                        setattr(modificar, new_list[2], new_list[3])
                        storage.new(modificar.to_dict())
                        storage.save()
                elif args and len(new_list) == 1:
                    print('** instance id missing **')
            else:
                print('** class doesn\'t exist **')
        else:
            print('** class name missing **')
    def default(self, arg):
        """method that print all Objects
        """
        print('command not found')
if __name__ == '__main__':
    HBNBCommand().cmdloop()
