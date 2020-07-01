#!/usr/bin/python3
"""Unittest for Review"""
import unittest
import pep8


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


if __name__ == '__main__':
    unittest.main()
