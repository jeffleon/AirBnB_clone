#!/usr/bin/python3
"""Unittest for BaseModel"""
import unittest
import pep8
import json
import re
from models import base_model
from models.base_model import BaseModel
import datetime


class TestBaseModel(unittest.TestCase):
    """Class for testing with unit test the BaseModel class"""

    def test_docstrings(self):
        """Tests for dosctrings"""
        self.assertGreater(len(base_model.__doc__), 1)
        self.assertGreater(len(BaseModel.__doc__), 1)
        self.assertGreater(len(BaseModel.__init__.__doc__), 1)
        self.assertGreater(len(BaseModel.__str__.__doc__), 1)
        self.assertGreater(len(BaseModel.save.__doc__), 1)
        self.assertGreater(len(BaseModel.to_dict.__doc__), 1)

    def test_pep8(self):
        """ Test for PEP8 """
        pep8_val = pep8.StyleGuide(quiet=True)
        base_model_path = 'models/base_model.py'
        result_base_model = pep8_val.check_files([base_model_path])
        self.assertEqual(result_base_model.total_errors, 0)
        test_base_model_path = 'tests/test_models/test_base_model.py'
        result_test_base_model = pep8_val.check_files([test_base_model_path])
        self.assertEqual(result_test_base_model.total_errors, 0)

    def test_new_object(self):
        """Tests when an instance is created"""
        base_obj = BaseModel()
        self.assertIsInstance(base_obj, BaseModel)
        self.assertEqual(type(base_obj.id), str)
        self.assertEqual(type(base_obj.created_at), datetime.datetime)
        self.assertEqual(type(base_obj.updated_at), datetime.datetime)
        pattern = '[a-z0-9]*-[a-z0-9]*-[a-z0-9]*-[a-z0-9]*-[a-z0-9]*'
        datetime_patt = '[0-9]*-[0-9]*-[0-9]* [0-9]*:[0-9]*:[0-9]*.[0-9]*'
        self.assertIsNotNone(re.match(pattern, base_obj.id))
        self.assertIsNotNone(re.match(datetime_patt, str(base_obj.created_at)))
        self.assertIsNotNone(re.match(datetime_patt, str(base_obj.updated_at)))

if __name__ == '__main__':
    unittest.main()
