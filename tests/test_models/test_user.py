#!/usr/bin/python3
"""Unittest for User"""
import unittest
import pep8


class TestUser(unittest.TestCase):
    """Class for testing with unit test the User class"""

    def test_pep8(self):
        """ Test for PEP8 """
        pep8_val = pep8.StyleGuide(quiet=True)
        user_path = 'models/user.py'
        result_user = pep8_val.check_files([user_path])
        self.assertEqual(result_user.total_errors, 0)
        test_user_path = 'tests/test_models/test_user.py'
        result_test_user = pep8_val.check_files([test_user_path])
        self.assertEqual(result_test_user.total_errors, 0)


if __name__ == '__main__':
    unittest.main()
