#!/usr/bin/python3
"""Unittest for State"""
import unittest
import pep8
import json
from models import state
from models.state import State
import datetime
import re


class TestState(unittest.TestCase):
    """Class for testing with unit test the State class"""

    def test_docstrings(self):
        """Tests for dosctrings"""
        self.assertGreater(len(state.__doc__), 1)
        self.assertGreater(len(State.__doc__), 1)

    def test_pep8(self):
        """ Test for PEP8 """
        pep8_val = pep8.StyleGuide(quiet=True)
        state_path = 'models/state.py'
        result_state = pep8_val.check_files([state_path])
        self.assertEqual(result_state.total_errors, 0)
        test_state_path = 'tests/test_models/test_state.py'
        result_test_state = pep8_val.check_files([test_state_path])
        self.assertEqual(result_test_state.total_errors, 0)

    def test_new_object(self):
        """Tests when an instance is created"""
        state_obj = State()
        self.assertIsInstance(state_obj, State)
        self.assertEqual(type(state_obj.id), str)
        self.assertEqual(type(state_obj.created_at), datetime.datetime)
        self.assertEqual(type(state_obj.updated_at), datetime.datetime)
        pattern = '[a-z0-9]*-[a-z0-9]*-[a-z0-9]*-[a-z0-9]*-[a-z0-9]*'
        d_patt = '[0-9]*-[0-9]*-[0-9]* [0-9]*:[0-9]*:[0-9]*.[0-9]*'
        self.assertIsNotNone(re.match(pattern, state_obj.id))
        self.assertIsNotNone(re.match(d_patt, str(state_obj.created_at)))
        self.assertIsNotNone(re.match(d_patt, str(state_obj.updated_at)))

if __name__ == '__main__':
    unittest.main()
