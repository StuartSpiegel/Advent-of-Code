# --- Day 17: Conway Cubes --- As your flight slowly drifts through the sky, the Elves at the Mythical Information
# Bureau at the North Pole contact you. They'd like some help debugging a malfunctioning experimental energy source
# aboard one of their super-secret imaging satellites.
#
# The experimental energy source is based on cutting-edge technology: a set of Conway Cubes contained in a pocket
# dimension! When you hear it's having problems, you can't help but agree to take a look.
#
# The pocket dimension contains an infinite 3-dimensional grid. At every integer 3-dimensional coordinate (x,y,z),
# there exists a single cube which is either active or inactive.
#
# In the initial state of the pocket dimension, almost all cubes start inactive. The only exception to this is a
# small flat region of cubes (your puzzle input); the cubes in this region start in the specified active (#) or
# inactive (.) state.
#
# The energy source then proceeds to boot up by executing six cycles.
#
# Each cube only ever considers its neighbors: any of the 26 other cubes where any of their coordinates differ by at
# most 1. For example, given the cube at x=1,y=2,z=3, its neighbors include the cube at x=2,y=2,z=2, the cube at x=0,
# y=2,z=3, and so on.
#
# During a cycle, all cubes simultaneously change their state according to the following rules:
#
# If a cube is active and exactly 2 or 3 of its neighbors are also active, the cube remains active. Otherwise,
# the cube becomes inactive. If a cube is inactive but exactly 3 of its neighbors are active, the cube becomes
# active. Otherwise, the cube remains inactive. The engineers responsible for this experimental energy source would
# like you to simulate the pocket dimension and determine what the configuration of cubes should be at the end of the
# six-cycle boot process.
#
# For example, consider the following initial state:
#
# .#. ..# ### Even though the pocket dimension is 3-dimensional, this initial state represents a small 2-dimensional
# slice of it. (In particular, this initial state defines a 3x3x1 region of the 3-dimensional space.)
#
# Simulating a few cycles from this initial state produces the following configurations, where the result of each
# cycle is shown layer-by-layer at each given z coordinate (and the frame of view follows the active cells in each
# cycle):

# After the full six-cycle boot process completes, 112 cubes are left in the active state.
#
# Starting with your given initial configuration, simulate six cycles. How many cubes are left in the active state
# after the sixth cycle?

# !/usr/bin/env python3
#
# import sys
# import numpy as np
#
#
# def rule(old, count): return count == 3 or old and count == 2
#
#
# def step(grid):
#     grow = np.zeros(tuple(i + 2 for i in grid.shape), dtype=np.int8)
#     new = np.zeros(tuple(i + 2 for i in grid.shape), dtype=np.int8)
#     grow[tuple(slice(1, -1) for _ in grow.shape)] = grid
#     for idx, x in np.ndenumerate(grow):
#         n = grow[tuple(slice(max(0, i - 1), (i + 2)) for i in idx)]
#         count = np.count_nonzero(n) - grow[idx]
#         new[idx] = rule(grow[idx], count)
#     return new
#
#
# def solve(start, dim, every=slice(None, None)):
#     pre, yx = tuple(1 for _ in range(dim - 2)), (len(start), len(start[0]))
#     grid = np.zeros(pre + yx, dtype=np.int8)
#     grid[tuple(0 for _ in pre) + (every, every)] = start
#     for x in range(6): grid = step(grid)
#     return np.count_nonzero(grid)
#
#
# if __name__ == '__main__':
#     start = [[c == '#' for c in l[:-1]] for l in open(sys.argv[1])]
#     print(solve(start, 3))
#     print(solve(start, 4))
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
import re
import networkx as nx
from parse import *
import copy
from collections import defaultdict
import itertools
import numpy as np
from math import cos, sin, pi
import contextlib
import functools
from unittest import TestCase


def read_input(filename="input.txt"):
    with open(filename) as f:
        lines = [line.strip() for line in f.readlines() if line.strip()]
    return lines


@functools.lru_cache(None)
def neighbours(p, dim):
    n = set()
    zero = (0,) * dim
    for dp in itertools.product((-1, 0, 1), repeat=dim):
        if dp != zero:
            n.add(tuple(map(sum, zip(p, dp))))
    return n


def part_1_and_2(lines, dim, num_cycles=6):
    x_ini = len(lines[0])
    y_ini = len(lines)
    g = set()
    for x, line in enumerate(lines):
        for y, val in enumerate(line):
            if val == "#":
                g.add((x, y) + (0,) * (dim - 2))

    def run_sim(g, dim):
        g_new = set()
        grids_to_check = set()
        for p in g:
            grids_to_check = grids_to_check.union((neighbours(p, dim)))
        for p in grids_to_check:
            active_n = len(g.intersection(neighbours(p, dim)))
            if p in g and active_n in (2, 3):
                g_new.add(p)
            elif p not in g and active_n == 3:
                g_new.add(p)
        return g_new

    for i in range(num_cycles):
        g = run_sim(g, dim)
        print(".", end="")
    print("")
    p_1 = len(g)
    return p_1


def main(input_file):
    """Solve puzzle and connect part 1 with part 2 if needed."""
    # part 1
    inp = read_input(input_file)
    p1 = part_1_and_2(inp, 3)
    print(f"Solution to part 1: {p1}")

    # part 2
    inp = read_input(input_file)
    p2 = part_1_and_2(inp, 4)
    print(f"Solution to part 2: {p2}")
    return p1, p2


def test_samples(self):
    input_file = "input.txt"
    p1, p2 = main(input_file)
    self.assertEqual(267, p1)
    self.assertEqual(1812, p2)
    print("***Tests passed so far***")


if __name__ == "__main__":
    test_samples(TestCase())
    main("input.txt")

