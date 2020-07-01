#!/usr/bin/python3
"""Unittest for FileStorage"""
import unittest
import pep8
import json
from models.engine import file_storage


class TestFileStorage(unittest.TestCase):
    """Class for testing with unit test the FileStorage class"""

    def test_docstrings(self):
        """Tests for dosctrings"""
        self.assertGreater(len(file_storage.__doc__), 1)
        self.assertGreater(len(FileStorage.__doc__), 1)
        self.assertGreater(len(FileStorage.all.__doc__), 1)
        self.assertGreater(len(FileStorage.new.__doc__), 1)
        self.assertGreater(len(FileStorage.save.__doc__), 1)
        self.assertGreater(len(FileStorage.reload.__doc__), 1)

    def test_pep8(self):
        """ Test for PEP8 """
        pep8_val = pep8.StyleGuide(quiet=True)
        file_storage_path = 'models/engine/file_storage.py'
        result_file_storage = pep8_val.check_files([file_storage_path])
        self.assertEqual(result_file_storage.total_errors, 0)
        t_file_st_path = 'tests/test_models/test_engine/test_file_storage.py'
        result_test_file_storage = pep8_val.check_files([t_file_st_path])
        self.assertEqual(result_test_file_storage.total_errors, 0)

    def test_new_object(self):
        """Tests when an instance is created"""
        file_s_obj = FileStorage()
        self.assertIsInstance(file_s_obj, FileStorage)
        self.assertEqual(type(file_s_obj.id), str)
        self.assertEqual(type(file_s_obj.created_at), datetime.datetime)
        self.assertEqual(type(file_s_obj.updated_at), datetime.datetime)
        pattern = '[0-9]*, [0-9]*, [0-9]*, [0-9]*, [0-9]*, [0-9]*, [0-9]*'
        pattern_t = '[0-9]*-[0-9]*-[0-9]*T[0-9]*:[0-9]*:[0-9]*.[0-9]*'
        datetime_patt = 'datetime.datetime(' + pattern_t + ')'
        self.assertIsNotNone(re.match(pattern, file_s_obj.id))
        self.assertIsNotNone(re.match(datetime_patt, file_s_obj.created_at))
        self.assertIsNotNone(re.match(datetime_patt, file_s_obj.updated_at))

if __name__ == '__main__':
    unittest.main()
