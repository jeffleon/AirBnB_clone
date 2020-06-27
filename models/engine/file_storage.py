#!/usr/bin/python3
"""
Module for FileStorage Class
"""
import json
from models.base_model import BaseModel

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
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj
        
    def save(self):
        """save: method that serialize __objects to the JSON file
        """
        dictionary = dict()
        for key, value in self.__objects.items():
            dictionary[key] = value.to_dict()
        try:
            with open(self.__file_path, mode="w", encoding="utf-8") as s_file:
                json.dump(dictionary, s_file)
        except:
            pass

    def reload(self):
        """reload: method that deserialize the JSON file to __objects
        """
        dictionary = dict() 
        try:
            with open(self.__file_path, mode="r", encoding="utf-8") as r_file:
                dictionary = json.load(r_file)
        except:
            pass
        if dictionary != {}:
            for key, value in dictionary.items():
                self.__objects[key] = BaseModel(**value)
