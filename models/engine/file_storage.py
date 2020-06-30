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
        """new: method that sets in __objects the obj with the key
        obj_class_name.id
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
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        dictionary = None
        try:
            with open(self.__file_path, mode="r", encoding="utf-8") as r_file:
                dictionary = json.load(r_file)
        except:
            pass
        if dictionary is not None:
            for key, value in dictionary.items():
                obj = None
                if "BaseModel" in key:
                    obj = BaseModel(**value)
                elif "User" in key:
                    obj = User(**value)
                elif "Place" in key:
                    obj = Place(**value)
                elif "State" in key:
                    obj = State(**value)
                elif "Amenity" in key:
                    obj = Amenity(**value)
                elif "Review" in key:
                    obj = Review(**value)
                elif "City" in key:
                    obj = City(**value)
                self.__objects[key] = obj
