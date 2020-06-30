#!/usr/bin/python3
"""Unittest for BaseModel"""
import unittest
import pep8
import json
import re
from models import base_model
from models.base_model import BaseModel
#from models.rectangle import Rectangle
#from models.square import Square


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
        pattern = '[0-9]*, [0-9]*, [0-9]*, [0-9]*, [0-9]*, [0-9]*, [0-9]*'
        pattern_t = '[0-9]*-[0-9]*-[0-9]*T[0-9]*:[0-9]*:[0-9]*.[0-9]*'
        datetime_patt = 'datetime.datetime(' + pattern_t + ')'
        self.assertIsNotNone(re.match(pattern, base_obj.id))
        self.assertIsNotNone(re.match(datetime_patt, base_obj.created_at))
        self.assertIsNotNone(re.match(datetime_patt, base_obj.updated_at))

        base_obj2 = Base(9)
        self.assertEqual(base_obj2.id, 9)
        base_obj3 = Base('a')
        self.assertEqual(base_obj3.id, 'a')
        base_obj4 = Base()
        self.assertEqual(base_obj4.id, 2)
        with self.assertRaises(TypeError):
            base_obj5 = Base(1, 3)

    def test_save_to_file(self):
        """Tests for save_to_file method"""
        rectangle_obj = Rectangle(9, 8, 1, 2, 23)
        square_obj = Square(4, 5, 6, 21)
        Base.save_to_file([rectangle_obj, square_obj])
        with open('Base.json', mode='r', encoding='utf-8') as n_file:
            f_cont = json.load(n_file)
            self.assertEqual(type(f_cont), list)
            self.assertEqual(len(f_cont), 2)
        with self.assertRaises(TypeError):
            Base.save_to_file()

    def test_load_from_file(self):
        """Tests for load_from_file method"""
        pass

    def test_to_json_string(self):
        """Tests for to_json_string method"""
        res = Base.to_json_string([])
        self.assertEqual(type(res), str)
        self.assertEqual(Base.to_json_string(None), '[]')
        self.assertEqual(Base.to_json_string(1), '1')
        self.assertEqual(Base.to_json_string([]), '[]')
        self.assertEqual(Base.to_json_string([{}]), '[{}]')
        self.assertEqual(Base.to_json_string([1]), '[1]')
        self.assertEqual(Base.to_json_string([[1, 2]]), '[[1, 2]]')
        self.assertEqual(Base.to_json_string([(True, 2)]), '[[true, 2]]')
        self.assertEqual(Base.to_json_string([{'id': 3}]), '[{"id": 3}]')
        with self.assertRaises(TypeError):
            Base.to_json_string()
        with self.assertRaises(TypeError):
            Base.to_json_string([], [])

    def test_from_json_string(self):
        """Tests for from_json_string method"""
        with self.assertRaises(TypeError):
            Base.from_json_string()
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string(''), [])
        self.assertEqual(Base.from_json_string('[]'), [])
        self.assertEqual(Base.from_json_string(1), None)
        self.assertEqual(Base.from_json_string((1, 2)), None)
        self.assertEqual(Base.from_json_string(True), None)
        self.assertEqual(Base.from_json_string('[{}]'), [{}])
        self.assertEqual(Base.from_json_string('[{"id": 3}]'), [{'id': 3}])

    def test_create(self):
        """Tests for create method"""
        pass

if __name__ == '__main__':
    unittest.main()
