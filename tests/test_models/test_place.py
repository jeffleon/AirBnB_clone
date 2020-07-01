#!/usr/bin/python3
"""Unittest for Place"""
import unittest
import pep8
import json
from models import place
from models.place import Place


class TestPlace(unittest.TestCase):
    """Class for testing with unit test the Place class"""

    def test_docstrings(self):
        """Tests for dosctrings"""
        self.assertGreater(len(place.__doc__), 1)
        self.assertGreater(len(Place.__doc__), 1)

    def test_pep8(self):
        """ Test for PEP8 """
        pep8_val = pep8.StyleGuide(quiet=True)
        place_path = 'models/place.py'
        result_place = pep8_val.check_files([place_path])
        self.assertEqual(result_place.total_errors, 0)
        test_place_path = 'tests/test_models/test_place.py'
        result_test_place = pep8_val.check_files([test_place_path])
        self.assertEqual(result_test_place.total_errors, 0)

    def test_new_object(self):
        """Tests when an instance is created"""
        place_obj = Place()
        self.assertIsInstance(place_obj, Place)
        self.assertEqual(type(place_obj.id), str)
        self.assertEqual(type(place_obj.created_at), datetime.datetime)
        self.assertEqual(type(place_obj.updated_at), datetime.datetime)
        pattern = '[0-9]*, [0-9]*, [0-9]*, [0-9]*, [0-9]*, [0-9]*, [0-9]*'
        pattern_t = '[0-9]*-[0-9]*-[0-9]*T[0-9]*:[0-9]*:[0-9]*.[0-9]*'
        datetime_patt = 'datetime.datetime(' + pattern_t + ')'
        self.assertIsNotNone(re.match(pattern, place_obj.id))
        self.assertIsNotNone(re.match(datetime_patt, place_obj.created_at))
        self.assertIsNotNone(re.match(datetime_patt, place_obj.updated_at))

if __name__ == '__main__':
    unittest.main()
