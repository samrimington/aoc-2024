import unittest

from . import construct_pair_of_lists,\
              calc_distance_between_lists,\
              calc_similarity_scores

TEST_INPUT = """\
3   4
4   3
2   5
1   3
3   9
3   3
"""

class TestPairOfLists(unittest.TestCase):
    def test_construction(self):
        left_list, right_list = construct_pair_of_lists(TEST_INPUT)
        self.assertListEqual(left_list, [3, 4, 2, 1, 3, 3])
        self.assertListEqual(right_list, [4, 3, 5, 3, 9, 3])

    def test_calc_distance(self):
        left_list = [1, 2, 3, 3, 3, 4]
        right_list = [3, 3, 3, 4, 5, 9]
        distances = calc_distance_between_lists(left_list, right_list)
        self.assertListEqual(distances, [2, 1, 0, 1, 2, 5])

    def test_calc_similarity(self):
        num_list = [3, 4, 2, 1, 3, 3]
        num_frequency = {3: 3, 4: 1}
        scores = calc_similarity_scores(num_list, num_frequency)
        self.assertListEqual(scores, [9, 4, 0, 0, 9, 9])
