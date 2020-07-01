#!/usr/bin/python3
"""Unittest for User"""
import unittest
import pep8
import datetime
import re
from models import user
from models.user import User


class TestUser(unittest.TestCase):
    """Class for testing with unit test the User class"""

    def test_docstrings(self):
        """Tests for dosctrings"""
        self.assertGreater(len(user.__doc__), 1)
        self.assertGreater(len(User.__doc__), 1)
        self.assertGreater(len(User.__init__.__doc__), 1)
        self.assertGreater(len(User.__str__.__doc__), 1)
        self.assertGreater(len(User.save.__doc__), 1)
        self.assertGreater(len(User.to_dict.__doc__), 1)

    def test_pep8(self):
        """ Test for PEP8 """
        pep8_val = pep8.StyleGuide(quiet=True)
        user_path = 'models/user.py'
        result_user = pep8_val.check_files([user_path])
        self.assertEqual(result_user.total_errors, 0)
        test_user_path = 'tests/test_models/test_user.py'
        result_test_user = pep8_val.check_files([test_user_path])
        self.assertEqual(result_test_user.total_errors, 0)

    def test_new_object(self):
        """Tests when an instance is created"""
        user_obj = User()
        self.assertIsInstance(user_obj, User)
        self.assertEqual(type(user_obj.id), str)
        self.assertEqual(type(user_obj.created_at), datetime.datetime)
        self.assertEqual(type(user_obj.updated_at), datetime.datetime)
        pattern = '[a-z0-9]*-[a-z0-9]*-[a-z0-9]*-[a-z0-9]*-[a-z0-9]*'
        d_patt = '[0-9]*-[0-9]*-[0-9]* [0-9]*:[0-9]*:[0-9]*.[0-9]*'
        self.assertIsNotNone(re.match(pattern, user_obj.id))
        self.assertIsNotNone(re.match(d_patt, str(user_obj.created_at)))
        self.assertIsNotNone(re.match(d_patt, str(user_obj.updated_at)))

if __name__ == '__main__':
    unittest.main()
