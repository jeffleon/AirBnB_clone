#!/usr/bin/python3
"""Unittest for City"""
import unittest
import pep8
import json
from models import city
from models.city import City
import datetime
import re


class TestCity(unittest.TestCase):
    """Class for testing with unit test the City class"""

    def test_docstrings(self):
        """Tests for dosctrings"""
        self.assertGreater(len(city.__doc__), 1)
        self.assertGreater(len(City.__doc__), 1)

    def test_pep8(self):
        """ Test for PEP8 """
        pep8_val = pep8.StyleGuide(quiet=True)
        city_path = 'models/city.py'
        result_city = pep8_val.check_files([city_path])
        self.assertEqual(result_city.total_errors, 0)
        test_city_path = 'tests/test_models/test_city.py'
        result_test_city = pep8_val.check_files([test_city_path])
        self.assertEqual(result_test_city.total_errors, 0)

    def test_new_object(self):
        """Tests when an instance is created"""
        city_obj = City()
        self.assertIsInstance(city_obj, City)
        self.assertEqual(type(city_obj.id), str)
        self.assertEqual(type(city_obj.created_at), datetime.datetime)
        self.assertEqual(type(city_obj.updated_at), datetime.datetime)
        pattern = '[a-z0-9]*-[a-z0-9]*-[a-z0-9]*-[a-z0-9]*-[a-z0-9]*'
        datetime_patt = '[0-9]*-[0-9]*-[0-9]* [0-9]*:[0-9]*:[0-9]*.[0-9]*'
        self.assertIsNotNone(re.match(pattern, city_obj.id))
        self.assertIsNotNone(re.match(datetime_patt, str(city_obj.created_at)))
        self.assertIsNotNone(re.match(datetime_patt, str(city_obj.updated_at)))


if __name__ == '__main__':
    unittest.main()
