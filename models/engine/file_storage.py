#!/usr/bin/python3
"""
Module for FileStorage Class
"""
import json


class FileStorage:
    """
    FileStorage Class
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """all: method that returns the __ojbects attribute
        Return:
            The return value: The __ojbects attribute
        """
        return self.__objects

    def new(self, obj):
        """new: method that sets in __objects the obj with the key obj_class_name.id
        """
        new_dict = dict(obj.__dict__)
        new_dict['created_at'] = new_dict.get('created_at').isoformat()
        new_dict['updated_at'] = new_dict.get('updated_at').isoformat()
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = new_dict
#        key = obj['__class__'] + "." + obj['id']
#        self.__objects[key] = obj

    def save(self):
        """save: method that serialize __objects to the JSON file
        """
        try:
            with open(self.__file_path, mode="w", encoding="utf-8") as s_file:
                json.dump(self.__objects, s_file)
        except:
            pass

    def reload(self):
        """reload: method that deserialize the JSON file to __objects
        """
        try:
            with open(self.__file_path, mode="r", encoding="utf-8") as r_file:
                self.__objects = json.load(r_file)
        except:
            pass
