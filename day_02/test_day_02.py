import unittest

from . import construct_reports,\
              is_safe,\
              is_safe_with_problem_dampener

TEST_INPUT = """\
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
"""

class TestReports(unittest.TestCase):
    def test_construction(self):
        reports = construct_reports(TEST_INPUT)
        self.assertEqual(len(reports), 6)
        self.assertListEqual(reports[0], [7, 6, 4, 2, 1])
        self.assertListEqual(reports[1], [1, 2, 7, 8, 9])
        self.assertListEqual(reports[2], [9, 7, 6, 2, 1])
        self.assertListEqual(reports[3], [1, 3, 2, 4, 5])
        self.assertListEqual(reports[4], [8, 6, 4, 4, 1])
        self.assertListEqual(reports[5], [1, 3, 6, 7, 9])

    def test_is_safe(self):
        self.assertTrue(is_safe([7, 6, 4, 2, 1]))
        self.assertFalse(is_safe([1, 2, 7, 8, 9]))
        self.assertFalse(is_safe([9, 7, 6, 2, 1]))
        self.assertFalse(is_safe([1, 3, 2, 4, 5]))
        self.assertFalse(is_safe([8, 6, 4, 4, 1]))
        self.assertTrue(is_safe([1, 3, 6, 7, 9]))

    def test_is_safe_with_problem_dampener(self):
        self.assertTrue(is_safe_with_problem_dampener([7, 6, 4, 2, 1]))
        self.assertFalse(is_safe_with_problem_dampener([1, 2, 7, 8, 9]))
        self.assertFalse(is_safe_with_problem_dampener([9, 7, 6, 2, 1]))
        self.assertTrue(is_safe_with_problem_dampener([1, 3, 2, 4, 5]))
        self.assertTrue(is_safe_with_problem_dampener([8, 6, 4, 4, 1]))
        self.assertTrue(is_safe_with_problem_dampener([1, 3, 6, 7, 9]))
