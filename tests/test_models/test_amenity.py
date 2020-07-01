#!/usr/bin/python3
"""Unittest for Amenity"""
import unittest
import pep8
import json
from models import amenity
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Class for testing with unit test the Amenity class"""

    def test_docstrings(self):
        """Tests for dosctrings"""
        self.assertGreater(len(amenity.__doc__), 1)
        self.assertGreater(len(Amenity.__doc__), 1)

    def test_pep8(self):
        """ Test for PEP8 """
        pep8_val = pep8.StyleGuide(quiet=True)
        amenity_path = 'models/amenity.py'
        result_amenity = pep8_val.check_files([amenity_path])
        self.assertEqual(result_amenity.total_errors, 0)
        test_amenity_path = 'tests/test_models/test_amenity.py'
        result_test_amenity = pep8_val.check_files([test_amenity_path])
        self.assertEqual(result_test_amenity.total_errors, 0)

    def test_new_object(self):
        """Tests when an instance is created"""
        amenity_obj = Amenity()
        self.assertIsInstance(amenity_obj, Amenity)
        self.assertEqual(type(amenity_obj.id), str)
        self.assertEqual(type(amenity_obj.created_at), datetime.datetime)
        self.assertEqual(type(amenity_obj.updated_at), datetime.datetime)
        pattern = '[0-9]*, [0-9]*, [0-9]*, [0-9]*, [0-9]*, [0-9]*, [0-9]*'
        pattern_t = '[0-9]*-[0-9]*-[0-9]*T[0-9]*:[0-9]*:[0-9]*.[0-9]*'
        datetime_patt = 'datetime.datetime(' + pattern_t + ')'
        self.assertIsNotNone(re.match(pattern, amenity_obj.id))
        self.assertIsNotNone(re.match(datetime_patt, amenity_obj.created_at))
        self.assertIsNotNone(re.match(datetime_patt, amenity_obj.updated_at))

if __name__ == '__main__':
    unittest.main()
