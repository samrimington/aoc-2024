"""
--- Day 4: Ceres Search ---

"Looks like the Chief's not here. Next!" One of The Historians pulls out a device and pushes the only button on it. After a brief flash, you recognize the interior of the Ceres monitoring station!

As the search for the Chief continues, a small Elf who lives on the station tugs on your shirt; she'd like to know if you could help her with her word search (your puzzle input). She only has to find one word: XMAS.

This word search allows words to be horizontal, vertical, diagonal, written backwards, or even overlapping other words. It's a little unusual, though, as you don't merely need to find one instance of XMAS - you need to find all of them. Here are a few ways XMAS might appear, where irrelevant characters have been replaced with .:

..X...
.SAMX.
.A..A.
XMAS.S
.X....

The actual word search will be full of letters instead. For example:

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

In this word search, XMAS occurs a total of 18 times; here's the same word search again, but where letters not involved in any XMAS have been replaced with .:

....XXMAS.
.SAMXMS...
...S..A...
..A.A.MS.X
XMASAMX.MM
X.....XA.A
S.S.S.S.SS
.A.A.A.A.A
..M.M.M.MM
.X.X.XMASX

Take a look at the little Elf's word search. How many times does XMAS appear?

--- Part Two ---

The Elf looks quizzically at you. Did you misunderstand the assignment?

Looking for the instructions, you flip over the word search to find that this isn't actually an XMAS puzzle; it's an X-MAS puzzle in which you're supposed to find two MAS in the shape of an X. One way to achieve that is like this:

M.S
.A.
M.S

Irrelevant characters have again been replaced with . in the above diagram. Within the X, each MAS can be written forwards or backwards.

Here's the same example from before, but this time all of the X-MASes have been kept instead:

.M.S......
..A..MSMS.
.M.S.MAA..
..A.ASMSM.
.M.S.M....
..........
S.S.S.S.S.
.A.A.A.A..
M.M.M.M.M.
..........

In this example, an X-MAS appears 9 times.

Flip the word search from the instructions back over to the word search side and try again. How many times does an X-MAS appear?
"""

import os

from . import convert_to_grid,\
              find_letter,\
              find_word,\
              get_diagonals

script_dir = os.path.dirname(__file__)
input_path = os.path.join(script_dir, "input.txt")
with open(input_path, 'r') as f:
    input_str = f.read()

# Part 1
grid = convert_to_grid(input_str)
results = find_word(grid, "XMAS")
print(f"XMAS appears {len(results)} times")

# Part 2
inner_grid = grid[1:-1, 1:-1]
a_occurences = find_letter(inner_grid, 'A')
x_mas_total = 0
for x, y in a_occurences:
    diags = get_diagonals(grid, x + 1, y + 1)
    if diags == ('M', 'S', 'M', 'S') or\
       diags == ('S', 'M', 'S', 'M') or\
       diags == ('S', 'S', 'M', 'M') or\
       diags == ('M', 'M', 'S', 'S'):
        x_mas_total += 1
print(f"X-MAS appears {x_mas_total} times")
