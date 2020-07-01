#!/usr/bin/python3
"""Unittest for City"""
import unittest
import pep8


class TestCity(unittest.TestCase):
    """Class for testing with unit test the City class"""

    def test_pep8(self):
        """ Test for PEP8 """
        pep8_val = pep8.StyleGuide(quiet=True)
        city_path = 'models/city.py'
        result_city = pep8_val.check_files([city_path])
        self.assertEqual(result_city.total_errors, 0)
        test_city_path = 'tests/test_models/test_city.py'
        result_test_city = pep8_val.check_files([test_city_path])
        self.assertEqual(result_test_city.total_errors, 0)

if __name__ == '__main__':
    unittest.main()
