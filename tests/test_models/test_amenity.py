#!/usr/bin/python3
"""Unittest for Amenity"""
import unittest
import pep8


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


if __name__ == '__main__':
    unittest.main()
