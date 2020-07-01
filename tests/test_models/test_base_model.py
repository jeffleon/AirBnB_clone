#!/usr/bin/python3
"""Unittest for BaseModel"""
import unittest
import pep8


class TestBaseModel(unittest.TestCase):
    """Class for testing with unit test the BaseModel class"""

    def test_pep8(self):
        """ Test for PEP8 """
        pep8_val = pep8.StyleGuide(quiet=True)
        base_model_path = 'models/base_model.py'
        result_base_model = pep8_val.check_files([base_model_path])
        self.assertEqual(result_base_model.total_errors, 0)
        tbase_path = 'tests/test_models/test_base_model.py'
        result_test_base_model = pep8_val.check_files([tbase_path])
        self.assertEqual(result_test_base_model.total_errors, 0)


if __name__ == '__main__':
    unittest.main()
