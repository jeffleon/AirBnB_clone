#!/usr/bin/python3
"""Unittest for Place"""
import unittest
import pep8


class TestPlace(unittest.TestCase):
    """Class for testing with unit test the Place class"""

    def test_pep8(self):
        """ Test for PEP8 """
        pep8_val = pep8.StyleGuide(quiet=True)
        place_path = 'models/place.py'
        result_place = pep8_val.check_files([place_path])
        self.assertEqual(result_place.total_errors, 0)
        test_place_path = 'tests/test_models/test_place.py'
        result_test_place = pep8_val.check_files([test_place_path])
        self.assertEqual(result_test_place.total_errors, 0)

if __name__ == '__main__':
    unittest.main()
