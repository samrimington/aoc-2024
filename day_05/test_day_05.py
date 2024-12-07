import unittest

from . import get_number_ordering,\
              group_updates

TEST_INPUT = """\
47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47
"""

class TestPageUpdateChecking(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.ordering = {
            '47': {'61', '13', '53', '29'},
            '97': {'75', '13', '29', '47', '61', '53'},
            '75': {'13', '29', '47', '61', '53'},
            '61': {'13', '53', '29'},
            '29': {'13'},
            '53': {'13', '29'}
        }

    def test_number_ordering(self):
        actual_ordering = get_number_ordering(TEST_INPUT)
        self.assertDictEqual(actual_ordering, self.ordering)

    def test_update_validation(self):
        valid_updates, invalid_updates = group_updates(TEST_INPUT, self.ordering)
        self.assertListEqual(valid_updates, [
            ['75', '47', '61', '53', '29'],
            ['97', '61', '53', '29', '13'],
            ['75', '29', '13']
        ])
        self.assertListEqual(invalid_updates, [
            ['75', '97', '47', '61', '53'],
            ['61', '13', '29'],
            ['97', '13', '75', '29', '47']
        ])
