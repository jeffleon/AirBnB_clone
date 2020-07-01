#!/usr/bin/python3
"""Unittest for Review"""
import unittest
import pep8
import json
from models import review
from models.review import Review


class TestReview(unittest.TestCase):
    """Class for testing with unit test the Review class"""

    def test_docstrings(self):
        """Tests for dosctrings"""
        self.assertGreater(len(review.__doc__), 1)
        self.assertGreater(len(Review.__doc__), 1)

    def test_pep8(self):
        """ Test for PEP8 """
        pep8_val = pep8.StyleGuide(quiet=True)
        review_path = 'models/review.py'
        result_review = pep8_val.check_files([review_path])
        self.assertEqual(result_review.total_errors, 0)
        test_review_path = 'tests/test_models/test_review.py'
        result_test_review = pep8_val.check_files([test_review_path])
        self.assertEqual(result_test_review.total_errors, 0)

    def test_new_object(self):
        """Tests when an instance is created"""
        review_obj = Review()
        self.assertIsInstance(review_obj, Review)
        self.assertEqual(type(review_obj.id), str)
        self.assertEqual(type(review_obj.created_at), datetime.datetime)
        self.assertEqual(type(review_obj.updated_at), datetime.datetime)
        pattern = '[0-9]*, [0-9]*, [0-9]*, [0-9]*, [0-9]*, [0-9]*, [0-9]*'
        pattern_t = '[0-9]*-[0-9]*-[0-9]*T[0-9]*:[0-9]*:[0-9]*.[0-9]*'
        datetime_patt = 'datetime.datetime(' + pattern_t + ')'
        self.assertIsNotNone(re.match(pattern, review_obj.id))
        self.assertIsNotNone(re.match(datetime_patt, review_obj.created_at))
        self.assertIsNotNone(re.match(datetime_patt, review_obj.updated_at))

if __name__ == '__main__':
    unittest.main()
