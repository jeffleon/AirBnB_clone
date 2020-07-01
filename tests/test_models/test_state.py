#!/usr/bin/python3
"""Unittest for State"""
import unittest
import pep8


class TestState(unittest.TestCase):
    """Class for testing with unit test the State class"""

    def test_pep8(self):
        """ Test for PEP8 """
        pep8_val = pep8.StyleGuide(quiet=True)
        state_path = 'models/state.py'
        result_state = pep8_val.check_files([state_path])
        self.assertEqual(result_state.total_errors, 0)
        test_state_path = 'tests/test_models/test_state.py'
        result_test_state = pep8_val.check_files([test_state_path])
        self.assertEqual(result_test_state.total_errors, 0)

if __name__ == '__main__':
    unittest.main()
