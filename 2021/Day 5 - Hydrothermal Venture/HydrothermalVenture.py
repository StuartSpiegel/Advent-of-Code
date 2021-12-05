# --- Day 5: Hydrothermal Venture --- You come across a field of hydrothermal vents on the ocean floor! These vents
# constantly produce large, opaque clouds, so it would be best to avoid them if possible.
#
# They tend to form in lines; the submarine helpfully produces a list of nearby lines of vents (your puzzle input)
# for you to review. For example:
#
# 0,9 -> 5,9 8,0 -> 0,8 9,4 -> 3,4 2,2 -> 2,1 7,0 -> 7,4 6,4 -> 2,0 0,9 -> 2,9 3,4 -> 1,4 0,0 -> 8,8 5,5 -> 8,
# 2 Each line of vents is given as a line segment in the format x1,y1 -> x2,y2 where x1,y1 are the coordinates of one
# end the line segment and x2,y2 are the coordinates of the other end. These line segments include the points at both
# ends. In other words:
#
# An entry like 1,1 -> 1,3 covers points 1,1, 1,2, and 1,3.
# An entry like 9,7 -> 7,7 covers points 9,7, 8,7, and 7,7.
# For now, only consider horizontal and vertical lines: lines where either x1 = x2 or y1 = y2.
#
# So, the horizontal and vertical lines from the above list would produce the following diagram:
#
# .......1.. ..1....1.. ..1....1.. .......1.. .112111211 .......... .......... .......... .......... 222111.... In
# this diagram, the top left corner is 0,0 and the bottom right corner is 9,9. Each position is shown as the number
# of lines which cover that point or . if no line covers that point. The top-left pair of 1s, for example,
# comes from 2,2 -> 2,1; the very bottom row is formed by the overlapping lines 0,9 -> 5,9 and 0,9 -> 2,9.
#
# To avoid the most dangerous areas, you need to determine the number of points where at least two lines overlap. In
# the above example, this is anywhere in the diagram with a 2 or larger - a total of 5 points.
#
# Consider only horizontal and vertical lines. At how many points do at least two lines overlap?

# Parse the line data
lines = [
    [int(num) for xy in line.split(" -> ") for num in xy.split(",")]
    for line in open("input.txt", "r").readlines()
]


def get_vent_locations_on_line(x1, y1, x2, y2):
    dx = bool(x2 > x1) - bool(x2 < x1)
    dy = bool(y2 > y1) - bool(y2 < y1)
    return [(x1 + n * dx, y1 + n * dy) for n in range(max(abs(x2 - x1), abs(y2 - y1)) + 1)]


# Each position is shown as the number of lines that cover that point
def intersection(vent_lines):
    vent_locations = set()
    overlaps = set()
    for line in vent_lines:
        for x, y in get_vent_locations_on_line(*line):
            if (x, y) in vent_locations:
                overlaps.add((x, y))
            else:
                vent_locations.add((x, y))
    return overlaps


# Part 2 requires that we consider diagonals and I figured this would be the ask so I made the is_diagonal method to
# filter out the diagonals from part 1
def is_diagonal(x1, y1, x2, y2):
    return x1 != x2 and y1 != y2


print("Part 1:", len(intersection([k for k in lines if not is_diagonal(*k)])))
print("Part 2:", len(intersection(lines)))
