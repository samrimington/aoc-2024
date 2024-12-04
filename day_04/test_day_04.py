import unittest

from . import convert_to_grid,\
              find_letter,\
              find_word,\
              get_adjacent,\
              get_diagonals

TEST_INPUT = """\
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
"""

class TestWordsearch(unittest.TestCase):
    def test_find_letter(self):
        grid = convert_to_grid(TEST_INPUT)
        locs = find_letter(grid, 'X')
        self.assertTrue(all(grid[x] == 'X' for x in locs))
    
    def test_get_adjacent(self):
        grid = convert_to_grid(TEST_INPUT)
        # Top right corner
        self.assertDictEqual(
            get_adjacent(grid, 0, 9),
            {(1, 9): 'A', (1, 8): 'S', (0, 8): 'S'}
        )
        # Top row
        self.assertDictEqual(
            get_adjacent(grid, 0, 4),
            {(0, 5): 'X', (1, 5): 'M', (1, 4): 'X', (1, 3): 'M', (0, 3): 'S'}
        )
        # Middle
        self.assertDictEqual(
            get_adjacent(grid, 5, 5),
            {(4, 5): 'M', (4, 6): 'X', (5, 6): 'X', (6, 6): 'S', (6, 5): 'A', (6, 4): 'S', (5, 4): 'M', (4, 4): 'A'}
        )
        # Bottom left corner
        self.assertDictEqual(
            get_adjacent(grid, 9, 0),
            {(8, 0): 'M', (8, 1): 'A', (9, 1): 'X'}
        )

    def test_find_word(self):
        grid = convert_to_grid(TEST_INPUT)
        results = find_word(grid, "XMAS")
        self.assertEqual(len(results), 18)

    def test_get_diagonals(self):
        grid = convert_to_grid(TEST_INPUT)
        self.assertEqual(get_diagonals(grid, 0, 0), ('.', '.', '.', 'S'))
        self.assertEqual(get_diagonals(grid, 1, 1), ('M', 'M', 'A', 'X'))
        self.assertEqual(get_diagonals(grid, 1, 2), ('M', 'S', 'M', 'S'))
