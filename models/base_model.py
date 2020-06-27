#!/usr/bin/python3
"""
Module for BaseModel Class
"""
import datetime
import uuid


class BaseModel:
    """
    BaseModel Class
    """
    def __init__(self, *args, **kwargs):
        """__init__: method that initialize an object"""
        import models
        dates = ['created_at', 'updated_at']
        date_format = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs:
            for key, value in kwargs.items():
                if key in dates:
                    date = datetime.datetime.strptime(value, date_format)
                    setattr(self, key, date)
                elif '__class__' not in key:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            models.storage.new(self)

    def __str__(self):
        """__str__: method that converts the object in a string
        Return:
            The return value: The object object in string
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                     self.__dict__)

    def save(self):
        """
        method that modifies the update_at attribute
        """
        import models
        self.updated_at = datetime.datetime.now()
        models.storage.save()

    def to_dict(self):
        """to_dictionary: method that returns the dictionary representation of
            a basemodel object
        Return:
            The return value: The basemodel object's dictionary
        """
        new_dict = dict(self.__dict__)
        new_dict['created_at'] = new_dict.get('created_at').isoformat()
        new_dict['updated_at'] = new_dict.get('updated_at').isoformat()
        new_dict['__class__'] = self.__class__.__name__
        return new_dict
