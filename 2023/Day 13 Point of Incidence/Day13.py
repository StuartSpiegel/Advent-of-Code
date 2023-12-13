# --- Day 13: Point of Incidence ---
# With your help, the hot springs team locates an appropriate spring which launches you neatly and precisely up to the edge of Lava Island.
# There's just one problem: you don't see any lava.
# You do see a lot of ash and igneous rock; there are even what look like gray mountains scattered around. After a while, you make your way to a nearby cluster of mountains only to discover that the valley between them is completely full of large mirrors. Most of the mirrors seem to be aligned in a consistent way; perhaps you should head in that direction?
# As you move through the valley of mirrors, you find that several of them have fallen from the large metal frames keeping them in place. The mirrors are extremely flat and shiny, and many of the fallen mirrors have lodged into the ash at strange angles. Because the terrain is all one color, it's hard to tell where it's safe to walk or where you're about to run into a mirror.
# You note down the patterns of ash (.) and rocks (#) that you see as you walk (your puzzle input); perhaps by carefully analyzing these patterns, you can figure out where the mirrors are!
# For example:

# #.##..##.
# ..#.##.#.
# ##......#
# ##......#
# ..#.##.#.
# ..##..##.
# #.#.##.#.

# #...##..#
# #....#..#
# ..##..###
# #####.##.
# #####.##.
# ..##..###
# #....#..#
# To find the reflection in each pattern, you need to find a perfect reflection across either a horizontal line between two rows or across a vertical line between two columns.
# In the first pattern, the reflection is across a vertical line between two columns; arrows on each of the two columns point at the line between the columns:
# 123456789
#     ><   
# #.##..##.
# ..#.##.#.
# ##......#
# ##......#
# ..#.##.#.
# ..##..##.
# #.#.##.#.
#     ><   
# 123456789
# In this pattern, the line of reflection is the vertical line between columns 5 and 6. Because the vertical line is not perfectly in the middle of the pattern, part of the pattern (column 1) has nowhere to reflect onto and can be ignored; every other column has a reflected column within the pattern and must match exactly: column 2 matches column 9, column 3 matches 8, 4 matches 7, and 5 matches 6.
# The second pattern reflects across a horizontal line instead:
# 1 #...##..# 1
# 2 #....#..# 2
# 3 ..##..### 3
# 4v#####.##.v4
# 5^#####.##.^5
# 6 ..##..### 6
# 7 #....#..# 7
# This pattern reflects across the horizontal line between rows 4 and 5. Row 1 would reflect with a hypothetical row 8, but since that's not in the pattern, row 1 doesn't need to match anything. The remaining rows match: row 2 matches row 7, row 3 matches row 6, and row 4 matches row 5.
# To summarize your pattern notes, add up the number of columns to the left of each vertical line of reflection; to that, also add 100 multiplied by the number of rows above each horizontal line of reflection. In the above example, the first pattern's vertical line has 5 columns to its left and the second pattern's horizontal line has 4 rows above it, a total of 405.
# Find the line of reflection in each of the patterns in your notes. What number do you get after summarizing all of your notes?

# Debugging the approach to correctly identify the line of reflection and accurately summarize the notes.

# def is_vertical_reflection(pattern, col):
#     """
#     Check if the given column 'col' is a line of vertical reflection for the pattern.
#     """
#     n_rows = len(pattern)
#     n_cols = len(pattern[0])

#     for row in range(n_rows):
#         # Compare the column with its mirrored column
#         if pattern[row][col] != pattern[row][n_cols - col - 1]:
#             return False
#     return True

# def is_horizontal_reflection(pattern, row):
#     """
#     Check if the given row 'row' is a line of horizontal reflection for the pattern.
#     """
#     n_rows = len(pattern)
#     n_cols = len(pattern[0])

#     for col in range(n_cols):
#         # Compare the row with its mirrored row
#         if pattern[row][col] != pattern[n_rows - row - 1][col]:
#             return False
#     return True

# def find_reflection_line(pattern):
#     """
#     Find the line of reflection in the given pattern.
#     Returns a tuple (is_vertical, index), where is_vertical is a boolean indicating whether the line is vertical or horizontal,
#     and index is the 0-based index of the column or row where the line of reflection is located.
#     """
#     n_rows = len(pattern)
#     n_cols = len(pattern[0])

#     # Check for vertical reflection
#     for col in range(n_cols // 2):
#         if is_vertical_reflection(pattern, col):
#             return (True, col)

#     # Check for horizontal reflection
#     for row in range(n_rows // 2):
#         if is_horizontal_reflection(pattern, row):
#             return (False, row)

#     return (None, None)

# def summarize_notes(file_path):
#     """
#     Summarize the notes by reading the patterns from the file and finding the reflection lines.
#     """
#     with open(file_path, 'r') as file:
#         patterns = file.read().strip().split("\n\n")  # Split the input into separate patterns
#         patterns = [p.split("\n") for p in patterns]  # Split each pattern into rows

#     summary = 0
#     for pattern in patterns:
#         is_vertical, index = find_reflection_line(pattern)
#         if is_vertical is not None:
#             if is_vertical:
#                 # Add the number of columns to the left of the vertical line
#                 summary += index   # type: ignore
#             else:
#                 # Add 100 times the number of rows above the horizontal line
#                 summary += 100 * index   # type: ignore

#     return summary

# # Re-run the program with the revised approach
# summarize_notes("input.txt")


# --- Part Two ---
# You resume walking through the valley of mirrors and - SMACK! - run directly into one. Hopefully nobody was watching, because that must have been pretty embarrassing.

# Upon closer inspection, you discover that every mirror has exactly one smudge: exactly one . or # should be the opposite type.

# In each pattern, you'll need to locate and fix the smudge that causes a different reflection line to be valid. (The old reflection line won't necessarily continue being valid after the smudge is fixed.)

# Here's the above example again:

# #.##..##.
# ..#.##.#.
# ##......#
# ##......#
# ..#.##.#.
# ..##..##.
# #.#.##.#.

# #...##..#
# #....#..#
# ..##..###
# #####.##.
# #####.##.
# ..##..###
# #....#..#
# The first pattern's smudge is in the top-left corner. If the top-left # were instead ., it would have a different, horizontal line of reflection:

# 1 ..##..##. 1
# 2 ..#.##.#. 2
# 3v##......#v3
# 4^##......#^4
# 5 ..#.##.#. 5
# 6 ..##..##. 6
# 7 #.#.##.#. 7
# With the smudge in the top-left corner repaired, a new horizontal line of reflection between rows 3 and 4 now exists. Row 7 has no corresponding reflected row and can be ignored, but every other row matches exactly: row 1 matches row 6, row 2 matches row 5, and row 3 matches row 4.

# In the second pattern, the smudge can be fixed by changing the fifth symbol on row 2 from . to #:

# 1v#...##..#v1
# 2^#...##..#^2
# 3 ..##..### 3
# 4 #####.##. 4
# 5 #####.##. 5
# 6 ..##..### 6
# 7 #....#..# 7
# Now, the pattern has a different horizontal line of reflection between rows 1 and 2.

# Summarize your notes as before, but instead use the new different reflection lines. In this example, the first pattern's new horizontal line has 3 rows above it and the second pattern's new horizontal line has 1 row above it, summarizing to the value 400.

# In each pattern, fix the smudge and find the different line of reflection. What number do you get after summarizing the new reflection line in each pattern in your notes?
content = open('input.txt', 'r').read()

def str_to_num(s: str) -> int:
    res = 0
    for c in s:
        res |= (1 if c == '#' else 0)
        res <<= 1
    return res >> 1

def get_grids() -> list[str]:
    return [grid for grid in content.split('\n\n')]

def parse_grid(grid: str) -> tuple[list[int], list[int]]:
    rows = [row for row in grid.split('\n')]
    cols = [col for col in list(zip(*grid.split('\n')))]

    return ([str_to_num(row) for row in rows], [str_to_num(col) for col in cols])

# Part 1
def find_reflection(ls: list[int]) -> int:
    for i in range(len(ls) - 1):
        n1, n2 = ls[i], ls[i + 1]
        if n1 == n2 :
            min_len = min(i + 1, len(ls) - (i + 1))
            sub_1 = ls[i+1 - min_len :i+1]
            sub_2 = ls[i + 1: i+1 + min_len]
            sub_2.reverse()
            if sub_1 == sub_2:
                return i + 1
    return 0

def part_1():
    grids = get_grids()
    res = 0
    for grid in grids:
        rows, cols = parse_grid(grid)
        res += find_reflection(rows) * 100 + find_reflection(cols)
    print(res)

# Part 2
def hamming_distance(a: int, b: int) -> int:
    x = a ^ b
    set_bits = 0

    while (x > 0) :
        set_bits += x & 1
        x >>= 1

    return set_bits

def find_reflection_2(ls: list[int]) -> int:
    for i in range(len(ls) - 1):
        min_len = min(i + 1, len(ls) - (i + 1))
        sub_1 = ls[i+1 - min_len :i+1]
        sub_2 = ls[i + 1: i+1 + min_len]
        sub_2.reverse()
        if sum(list(map(hamming_distance, sub_1, sub_2))) == 1:
            return i + 1

    return 0

def part_2():
    grids = get_grids()
    res = 0
    for grid in grids:
        rows, cols = parse_grid(grid)
        res += find_reflection_2(rows) * 100 + find_reflection_2(cols)
    print(res)

if __name__ == '__main__':
    part_1()
    part_2()