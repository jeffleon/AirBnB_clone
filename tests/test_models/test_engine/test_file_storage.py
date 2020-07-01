#!/usr/bin/python3
"""Unittest for FileStorage"""
import unittest
import pep8


class TestFileStorage(unittest.TestCase):
    """Class for testing with unit test the FileStorage class"""

    def test_pep8(self):
        """ Test for PEP8 """
        pep8_val = pep8.StyleGuide(quiet=True)
        file_storage_path = 'models/engine/file_storage.py'
        result_file_storage = pep8_val.check_files([file_storage_path])
        self.assertEqual(result_file_storage.total_errors, 0)
        t_file_st_path = 'tests/test_models/test_engine/test_file_storage.py'
        result_test_file_storage = pep8_val.check_files([t_file_st_path])
        self.assertEqual(result_test_file_storage.total_errors, 0)

if __name__ == '__main__':
    unittest.main()
