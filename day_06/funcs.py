from functools import cached_property

import numpy as np

from day_04 import convert_to_grid, Coords

class GuardPatrol:
    def __init__(self, lab_map: str) -> None:
        self.grid = convert_to_grid(lab_map)

    @cached_property
    def guard_position(self) -> Coords | None:
        pos = None
        for guard in ['^', '>', 'V', '<']:
            if guard in self.grid:
                assert pos is None, "There is more than one guard in different orientations"
                x, y = np.where(self.grid == guard)
                assert len(x) == len(y) == 1, "There is more than one guard in the same orientation"
                pos = x[0], y[0]
        return pos
    
    @property
    def distinct_positions(self) -> int:
        return (self.grid == 'X').sum()

    def take_step(self) -> None:
        assert self.guard_position is not None, "There is no guard on the map"
        x, y = self.guard_position
        del self.guard_position
        otation = self.grid[x, y]
        self.grid[x, y] = 'X'
        new_otation = 'X'
        if otation == '^':
            x -= 1
            if x - 1 >= 0:
                new_otation = '>' if self.grid[x - 1, y] == '#' else '^'
        elif otation == '>':
            y += 1
            if y + 1 < len(self.grid[x]):
                new_otation = 'V' if self.grid[x, y + 1] == '#' else '>'
        elif otation == 'V':
            x += 1
            if x + 1 < len(self.grid):
                new_otation = '<' if self.grid[x + 1, y] == '#' else 'V'
        elif otation == '<':
            y -= 1
            if y - 1 >= 0:
                new_otation = '^' if self.grid[x, y - 1] == '#' else '<'
        self.grid[x, y] = new_otation

    def complete_patrol(self) -> None:
        while self.guard_position is not None:
            self.take_step()
