import unittest

from . import GuardPatrol

TEST_INPUT = """\
....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
"""

class TestGuardPatrol(unittest.TestCase):
    def test_guard_patrol(self):
        gp = GuardPatrol(TEST_INPUT)
        self.assertEqual(gp.guard_position, (6, 4))
        gp.complete_patrol()
        self.assertEqual(gp.distinct_positions, 41)