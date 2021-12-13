# --- Day 13: Transparent Origami ---
# You reach another volcanically active part of the cave. It would be nice if you could do some kind of thermal imaging so you could tell ahead of time which caves are too hot to safely enter.

# Fortunately, the submarine seems to be equipped with a thermal camera! When you activate it, you are greeted with:

# Congratulations on your purchase! To activate this infrared thermal imaging
# camera system, please enter the code found on page 1 of the manual.
# Apparently, the Elves have never used this feature. To your surprise, you manage to find the manual; as you go to open it, page 1 falls out. It's a large sheet of transparent paper! The transparent paper is marked with random dots and includes instructions on how to fold it up (your puzzle input). For example:

# 6,10
# 0,14
# 9,10
# 0,3
# 10,4
# 4,11
# 6,0
# 6,12
# 4,1
# 0,13
# 10,12
# 3,4
# 3,0
# 8,4
# 1,10
# 2,14
# 8,10
# 9,0

# fold along y=7
# fold along x=5
# The first section is a list of dots on the transparent paper. 0,0 represents the top-left coordinate. The first value, x, increases to the right. The second value, y, increases downward. So, the coordinate 3,0 is to the right of 0,0, and the coordinate 0,7 is below 0,0. The coordinates in this example form the following pattern, where # is a dot on the paper and . is an empty, unmarked position:

# ...#..#..#.
# ....#......
# ...........
# #..........
# ...#....#.#
# ...........
# ...........
# ...........
# ...........
# ...........
# .#....#.##.
# ....#......
# ......#...#
# #..........
# #.#........
# Then, there is a list of fold instructions. Each instruction indicates a line on the transparent paper and wants you to fold the paper up (for horizontal y=... lines) or left (for vertical x=... lines). In this example, the first fold instruction is fold along y=7, which designates the line formed by all of the positions where y is 7 (marked here with -):

# ...#..#..#.
# ....#......
# ...........
# #..........
# ...#....#.#
# ...........
# ...........
# -----------
# ...........
# ...........
# .#....#.##.
# ....#......
# ......#...#
# #..........
# #.#........
# Because this is a horizontal line, fold the bottom half up. Some of the dots might end up overlapping after the fold is complete, but dots will never appear exactly on a fold line. The result of doing this fold looks like this:

# #.##..#..#.
# #...#......
# ......#...#
# #...#......
# .#.#..#.###
# ...........
# ...........
# Now, only 17 dots are visible.

# Notice, for example, the two dots in the bottom left corner before the transparent paper is folded; after the fold is complete, those dots appear in the top left corner (at 0,0 and 0,1). Because the paper is transparent, the dot just below them in the result (at 0,3) remains visible, as it can be seen through the transparent paper.

# Also notice that some dots can end up overlapping; in this case, the dots merge together and become a single dot.

# The second fold instruction is fold along x=5, which indicates this line:

# #.##.|#..#.
# #...#|.....
# .....|#...#
# #...#|.....
# .#.#.|#.###
# .....|.....
# .....|.....
# Because this is a vertical line, fold left:

# #####
# #...#
# #...#
# #...#
# #####
# .....
# .....
# The instructions made a square!

# The transparent paper is pretty big, so for now, focus on just completing the first fold. After the first fold in the example above, 17 dots are visible - dots that end up overlapping after the fold is completed count as a single dot.

# How many dots are visible after completing just the first fold instruction on your transparent paper?
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# import numpy as np
# def performFold(dots, distance):
#     for axis, distance in instructions:
#         folded = []
#         for x,y in dots:
#             if axis == 'x' and x > distance:
#                 x = 2*distance - x
#             if axis == 'y' and y > distance:
#                 y = 2*distance - y
#             if (x,y) not in folded:
#                 folded.append((x,y))
#         dots = folded
#     return dots

# def printDotsMatrix(dots):
#     dots = sorted(dots)
#     X_MAX = dots[-1][0]
#     dots.sort(key=lambda dots: dots[1])
#     Y_MAX = dots[-1][1]

#     for y in range(Y_MAX + 1):
#         for x in range (X_MAX + 1):
#             if dots and dots[0] == (x, y):
#                 print ('#', end ='')
#                 dots.pop(0)
#             else:
#                 print(' ', end= '')
#         print()

# if __name__ == "__main__":
#     dots = [] # lists of tuples, Points in a Cartesian plane
#     instructions = [] # Holds the list of instructions to execute

#     # Read in input
#     with open('input.txt') as file:
#         line = file.readline()
#         while line != '':
#             single = line.strip().split(',')
#             if len(single) == 2:
#                 dots.append(list(map(int, single)))
#             else:
#                 j = line.strip().split()
#                 if len(j) == 3:
#                     p = j[2].split('=')
#                     instructions.append( (p[0], int(p[1]))) # append the object as a numerical point -- need the int casting
#             line = file.readline()

#     # Part 1
#     axis, distance = instructions.pop(0)
#     dots = performFold(dots, instructions[:1]) #Perform only 1 fold for Part 1 
#     print(f"Part 1: {len(dots)}")

#     # Part 2 - perform all the folds in the instructions until completion
#     # printDotsMatrix(performFold(dots, instructions[1:]))

dots, folds = open("input.txt").read().split("\n\n")
dots = [(int(dot.split(",")[0]), int(dot.split(",")[1])) for dot in dots.splitlines()]
folds = [(axis[-1], int(val)) for fold in folds.splitlines() for axis, val in [fold.split("=")]]

axis, fold_line = folds[0]

for i, (x, y) in enumerate(dots):
    if axis == "x" and x > fold_line:
        dots[i] = (2 * fold_line - x, y)
    if axis == "y" and y > fold_line:
        dots[i] = (x, 2 * fold_line - y)

print(len(set(dots)))

# Part 2
dots, folds = open("input.txt").read().split("\n\n")
dots = [(int(dot.split(",")[0]), int(dot.split(",")[1])) for dot in dots.splitlines()]
folds = [(axis[-1], int(val)) for fold in folds.splitlines() for axis, val in [fold.split("=")]]

for axis, fold_line in folds:
    for i, (x, y) in enumerate(dots):
        if axis == "x" and x > fold_line:
            dots[i] = (2 * fold_line - x, y)
        if axis == "y" and y > fold_line:
            dots[i] = (x, 2 * fold_line - y)

print("\n".join("".join("█" if (x, y) in dots else " " for x in range(40)) for y in range(6)))

