#--- Day 3: Toboggan Trajectory ---
#With the toboggan login problems resolved, you set off toward the airport. While travel by toboggan might be easy, it's certainly not safe: there's very minimal #steering and the area is covered in trees. You'll need to see which angles will take you near the fewest trees.
#
#Due to the local geology, trees in this area only grow on exact integer coordinates in a grid. You make a map (your puzzle input) of the open squares (.) and trees (#) #you can see. For example:
#
#
#//..##.......
#//#...#...#..
#//.#....#..#.
#//..#.#...#.#
#//.#...##..#.
#//..#.##.....
#//.#.#.#....#
#//.#........#
#//#.##...#...
#//#...##....#
#//.#..#...#.#
#
# Prompt : Starting at the top-left corner of your map and following a slope of right 3 and down 1, how many trees would you encounter?
#
import sys
import operator
from functools import reduce
from pathlib import Path
from typing import List, Tuple

# My Python Solution to Part 1
def partOne:
	lines = [line for line in sys.stdin.read().strip().split("\n")]
	numHits = 0
	slope = 0
	for line in lines:
    	if line[slope] == "#":
        	numHits += 1
    	slope += 3
    	slope %= len(line)
	print(numHits)

#########################################################################################
# Interesting alternative Solution I found online post solve. 
def alt_partOne(smap: List[str], right: int, down: int) -> int:
	repeatlen = len(smap[0].rstrip())
    maplen = len(smap)
    rpos = 0
    dpos = 0
    trees = 0
    while dpos < maplen - down:
        rpos += right
        dpos += down
        if smap[dpos][rpos % repeatlen] == '#':
            trees += 1
    return trees


def partTwo:
	trees = [part1(smap, s[0], s[1]) for s in slopes]
    return reduce(operator.mul, trees)


if __name__ == '__main__':
    sledmap = sys.stdin.readlines()
    print(f'Trees: {part1(sledmap, 3, 1)}')
    print(f'Trees: {part2(sledmap, ((1,1),(3,1),(5,1),(7,1),(1,2)))}')
##########################################################################################

