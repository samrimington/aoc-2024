from typing import Dict, List, Tuple

import numpy as np

Coords = Tuple[int, int]

def convert_to_grid(wordsearch: str) -> np.array:
    return np.array(list(map(list, wordsearch.splitlines())))

def find_letter(grid: np.array, letter: str) -> List[Coords]:
    assert(len(letter) == 1)
    x, y = np.where(grid == letter)
    return list(zip(x.tolist(), y.tolist()))

def get_adjacent(grid: np.array, x0: int, y0: int) -> Dict[Coords, str]:
    adjacent = {}
    for x in range(max(0, x0 - 1), min(len(grid), x0 + 2)):
        for y in range(max(0, y0 - 1), min(len(grid), y0 + 2)):
            if not (x == x0 and y == y0):
                adjacent[(x, y)] = str(grid[x, y])
    return adjacent

def find_word(grid: np.array, word: str) -> List[Tuple[Coords, Coords]]:
    def line_contains_rest_of_word(x: int, y: int, d_x: int, d_y: int) -> bool:
        assert(d_x != 0 or d_y != 0)
        for letter in word[2:]:
            x, y = x + d_x, y + d_y
            if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[x]) or grid[x, y] != letter:
                return False
        return True
    assert(len(word) > 1)
    results = []
    for x0, y0 in find_letter(grid, word[0]):
        for (x, y), letter in get_adjacent(grid, x0, y0).items():
            if letter != word[1]:
                continue
            d_x, d_y = x - x0, y - y0
            if line_contains_rest_of_word(x, y, d_x, d_y):
                results.append(((x0, y0), (d_x, d_y)))
    return results

def get_diagonals(grid: np.array, x: int, y: int) -> Tuple[str, str, str, str]:
    x0, x1 = x - 1, x + 1
    y0, y1 = y - 1, y + 1
    return (
        grid[x0, y0] if x0 >= 0        and y0 >= 0            else '.',
        grid[x0, y1] if x0 >= 0        and y1 < len(grid[x0]) else '.',
        grid[x1, y0] if x1 < len(grid) and y0 >= 0            else '.',
        grid[x1, y1] if x1 < len(grid) and y1 < len(grid[x1]) else '.'
    )
