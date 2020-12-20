# --- Day 20: Jurassic Jigsaw --- The high-speed train leaves the forest and quickly carries you south. You can even
# see a desert in the distance! Since you have some spare time, you might as well see if there was anything
# interesting in the image the Mythical Information Bureau satellite captured.
#
# After decoding the satellite messages, you discover that the data actually contains many small images created by
# the satellite's camera array. The camera array consists of many cameras; rather than produce a single square image,
# they produce many smaller square image tiles that need to be reassembled back into a single image.
#
# Each camera in the camera array returns a single monochrome image tile with a random unique ID number. The tiles (
# your puzzle input) arrived in a random order.
#
# Worse yet, the camera array appears to be malfunctioning: each image tile has been rotated and flipped to a random
# orientation. Your first task is to reassemble the original image by orienting the tiles so they fit together.
#
# To show how the tiles should be reassembled, each tile's image data includes a border that should line up exactly
# with its adjacent tiles. All tiles have this border, and the border lines up exactly when the tiles are both
# oriented correctly. Tiles at the edge of the image also have this border, but the outermost edges won't line up
# with any other tiles.
#
# For example, suppose you have the following nine tiles:
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Tile 2311:
# ..##.#..#.
# ##..#.....
# #...##..#.
# ####.#...#
# ##.##.###.
# ##...#.###
# .#.#.#..##
# ..#....#..
# ###...#.#.
# ..###..###
#
# Tile 1951:
# #.##...##.
# #.####...#
# .....#..##
# #...######
# .##.#....#
# .###.#####
# ###.##.##.
# .###....#.
# ..#.#..#.#
# #...##.#..
#
# Tile 1171:
# ####...##.
# #..##.#..#
# ##.#..#.#.
# .###.####.
# ..###.####
# .##....##.
# .#...####.
# #.##.####.
# ####..#...
# .....##...
#
# Tile 1427:
# ###.##.#..
# .#..#.##..
# .#.##.#..#
# #.#.#.##.#
# ....#...##
# ...##..##.
# ...#.#####
# .#.####.#.
# ..#..###.#
# ..##.#..#.
#
# Tile 1489:
# ##.#.#....
# ..##...#..
# .##..##...
# ..#...#...
# #####...#.
# #..#.#.#.#
# ...#.#.#..
# ##.#...##.
# ..##.##.##
# ###.##.#..
#
# Tile 2473:
# #....####.
# #..#.##...
# #.##..#...
# ######.#.#
# .#...#.#.#
# .#########
# .###.#..#.
# ########.#
# ##...##.#.
# ..###.#.#.
#
# Tile 2971:
# ..#.#....#
# #...###...
# #.#.###...
# ##.##..#..
# .#####..##
# .#..####.#
# #..#.#..#.
# ..####.###
# ..#.#.###.
# ...#.#.#.#
#
# Tile 2729:
# ...#.#.#.#
# ####.#....
# ..#.#.....
# ....#..#.#
# .##..##.#.
# .#.####...
# ####.#.#..
# ##.####...
# ##..#.##..
# #.##...##.
#
# Tile 3079: #.#.#####. .#..###### ..#....... ######.... ####.#..#. .#...#.##. #.#####.## ..#.###... ..#.......
# ..#.###... By rotating, flipping, and rearranging them, you can find a square arrangement that causes all adjacent
# borders to line up:
#
# #...##.#.. ..###..### #.#.#####.
# ..#.#..#.# ###...#.#. .#..######
# .###....#. ..#....#.. ..#.......
# ###.##.##. .#.#.#..## ######....
# .###.##### ##...#.### ####.#..#.
# .##.#....# ##.##.###. .#...#.##.
# #...###### ####.#...# #.#####.##
# .....#..## #...##..#. ..#.###...
# #.####...# ##..#..... ..#.......
# #.##...##. ..##.#..#. ..#.###...
#
# #.##...##. ..##.#..#. ..#.###...
# ##..#.##.. ..#..###.# ##.##....#
# ##.####... .#.####.#. ..#.###..#
# ####.#.#.. ...#.##### ###.#..###
# .#.####... ...##..##. .######.##
# .##..##.#. ....#...## #.#.#.#...
# ....#..#.# #.#.#.##.# #.###.###.
# ..#.#..... .#.##.#..# #.###.##..
# ####.#.... .#..#.##.. .######...
# ...#.#.#.# ###.##.#.. .##...####
#
# ...#.#.#.# ###.##.#.. .##...####
# ..#.#.###. ..##.##.## #..#.##..#
# ..####.### ##.#...##. .#.#..#.##
# #..#.#..#. ...#.#.#.. .####.###.
# .#..####.# #..#.#.#.# ####.###..
# .#####..## #####...#. .##....##.
# ##.##..#.. ..#...#... .####...#.
# #.#.###... .##..##... .####.##.#
# #...###... ..##...#.. ...#..####
# ..#.#....# ##.#.#.... ...##.....
# For reference, the IDs of the above tiles are:
#
# 1951    2311    3079 2729    1427    2473 2971    1489    1171 To check that you've assembled the image correctly,
# multiply the IDs of the four corner tiles together. If you do this with the assembled tiles from the example above,
# you get 1951 * 3079 * 2971 * 1171 = 20899048083289.
#
# Assemble the tiles into an image. What do you get if you multiply together the IDs of the four corner tiles?

import time
import os
import re
import math
from collections import defaultdict


def wrapper(method):
    def wrapper_method(*arg, **kw):
        t = time.time()
        toReturn = method(*arg, **kw)
        print('Method ' + method.__name__ + ' took : ' + "{:2.5f}".format(time.time() - t) + ' sec')
        return toReturn

    return wrapper_method()


def tile_matches(t1, t2):
    t1_right = ''.join([t[-1] for t in t1])
    t2_right = ''.join([t[-1] for t in t2])
    t1_left = ''.join([t[0] for t in t1])
    t2_left = ''.join([t[0] for t in t2])

    t1_edges = [t1[0], t1[-1], t1_right, t1_left]
    t2_edges = [t2[0], t2[-1], t2[0][::-1], t2[-1][::-1], t2_left, t2_left[::-1], t2_right, t2_right[::-1]]

    for a in t1_edges:
        for b in t2_edges:
            if a == b:
                return True
    return False


def flip_tile(tile):
    return [l[::-1] for l in tile]


def rotate_tile(tile):
    return [*map("".join, zip(*reversed(tile)))]


def set_corner(cor, right, down):
    rr = ''.join([t[-1] for t in right])
    dr = ''.join([t[-1] for t in down])
    rl = ''.join([t[0] for t in right])
    dl = ''.join([t[0] for t in down])

    r_edges = [right[0], right[-1], right[0][::-1], right[-1][::-1], rr, rr[::-1], rl, rl[::-1]]
    d_edges = [down[0], down[-1], down[0][::-1], down[-1][::-1], dr, dr[::-1], dl, dl[::-1]]

    for _ in range(2):
        cor = flip_tile(cor)
        for _ in range(4):
            cor = rotate_tile(cor)
            if cor[-1] in d_edges and ''.join([t[-1] for t in cor]) in r_edges:
                return cor

    return None


def remove_border(t):
    return [x[1:-1] for x in t[1:-1]]


def set_left_edge(t1, t2):
    ref = ''.join([t[-1] for t in t1])

    for _ in range(2):
        t2 = flip_tile(t2)
        for _ in range(4):
            t2 = rotate_tile(t2)
            if ''.join([t[0] for t in t2]) == ref:
                return t2
    return None


def set_upper_edge(t1, t2):
    ref = t1[-1]
    for _ in range(2):
        t2 = flip_tile(t2)
        for _ in range(4):  # debug
            t2 = rotate_tile(t2)
            if t2[0] == ref:
                return t2
    return None


def assemble_image(img, tiles):
    compiled_image = []

    for k in img:
        slice = [''] * len(tiles[k[0]])
        for j in k:
            for i, s in enumerate(tiles[j]):
                slice[i] += s
            for s in slice:
                compiled_image.append(s)
    return compiled_image


@wrapper
def solve_part1():
    tiles = defaultdict(list)
    for l in open('input.txt'):
        if 'Tile' in l:
            tile = int(re.findall(r'\d+', l)[0])  # search for tiles in regex
        elif '.' in l or '#' in l:
            tiles[tile].append(l.strip())
    connected_tiles = defaultdict(set)

    for i in tiles:
        for t in tiles:
            if i == t: continue  # we dont want to match on indentical tiles
            if tile_matches(tiles[i], tiles[t]):
                connected_tiles[i].add(t)
                connected_tiles[t].add(i)

    product = 1

    for i in connected_tiles:
        if len(connected_tiles[i]) == 2:
            product *= i
    print(product)  # output the answer to part 1


# --- Part Two ---
# Now, you're ready to check the image for sea monsters.
#
# The borders of each tile are not part of the actual image; start by removing them.
#
# In the example above, the tiles become:
# Now, you're ready to search for sea monsters! Because your image is monochrome, a sea monster will look like this:
#
# # #    ##    ##    ### #  #  #  #  #  # When looking for this pattern in the image, the spaces can be anything;
# only the # need to match. Also, you might need to rotate or flip your image before it's oriented correctly to find
# sea monsters. In the above image, after flipping and rotating it to the appropriate orientation, there are two sea
# monsters (marked with O):
#
# .####...#####..#...###.. #####..#..#.#.####..#.#. .#.#...#.###...#.##.O#.. #.O.##.OO#.#.OO.##.OOO##
# ..#O.#O#.O##O..O.#O##.## ...#.#..##.##...#..#..## #.##.#..#.#..#..##.#.#.. .###.##.....#...###.#...
# #.####.#.#....##.#..#.#. ##...#..#....#..#...#### ..#.##...###..#.#####..# ....#.##.#.#####....#...
# ..##.##.###.....#.##..#. #...#...###..####....##. .#.##...#.##.#.#.###...# #.###.#..####...##..#...
# #.###...#.##...#.##O###. .O##.#OO.###OO##..OOO##. ..O#.O..O..O.#O##O##.### #.#..##.########..#..##.
# #.#####..#.#...##..#.... #....##..#.#########..## #...#.....#..##...###.## #..###....##.#...##.##.# Determine how
# rough the waters are in the sea monsters' habitat by counting the number of # that are not part of a sea monster.
# In the above example, the habitat's water roughness is 273.
#
# How many # are not part of a sea monster?
@wrapper
def solve_part2():
    tiles = defaultdict(list)

    for k in open('input.txt'):
        if 'Tile' in k:
            tile = int(re.findall(r'\d+', k)[0])
        elif '.' in k or '#' in k:
            tiles[tile].append(k.strip())

    connected_tiles = defaultdict(set)

    for i in tiles:
        for t in tiles:
            if i == t: continue
            if tile_matches(tiles[i], tiles[t]):
                connected_tiles[i].add(t)
                connected_tiles[t].add(i)

    sm = int(math.sqrt(len(connected_tiles)))
    image = [[0 for _ in range(sm)] for _ in range(sm)]
    for i in connected_tiles:
        if len(connected_tiles[i]) == 2:
            corner = i  # we found the correct corner
            break
    image[0][0] = corner  # set the image coordinates to the newly found corner
    added = {corner}

    for x in range(1, sm):
        pos_1 = connected_tiles[image[0][x - 1]]
        for candidate in pos_1:
            if candidate not in added and len(connected_tiles[candidate]) < 4:
                image[0][x] = candidate
                added.add(candidate)
                break

    for y in range(1, sm):
        for z in range(sm):
            pos_2 = connected_tiles[image[y - 1][z]]
            for candidate in pos_2:
                if candidate not in added:
                    image[y][z] = candidate
                    added.add(candidate)
                    break

    tiles[image[0][0]] = set_corner(tiles[image[0][0]], tiles[image[0][1]], tiles[image[1][0]])

    for y, l in enumerate(image):
        if y != 0:
            set_1 = image[y - 1][0]
            tiles[l[0]] = set_upper_edge(tiles[set_1], tiles[l[0]])

        for x, tile in enumerate(l):
            if x != 0:
                set_2 = image[y][x - 1]
                tiles[tile] = set_left_edge(tiles[set_2], tiles[tile])

    for t in tiles:
        tiles[t] = remove_border(tiles[t])

    image = assemble_image(image, tiles)

    key = 0
    monster = set()
    for line in open('input.txt').read().split('\n'):
        key_x = len(line)
        for i, ch in enumerate(line):
            if ch == '#':
                monster.add((i, key))
        key += 1

    for _ in range(2):
        image = flip_tile(image)
        for _ in range(4):
            image = rotate_tile(image)

            for x in range(0, len(image) - key_x):
                for y in range(0, len(image) - key):
                    parts = []
                    for i, p in enumerate(monster):
                        dx = x + p[0]
                        dy = y + p[1]
                        parts.append(image[dy][dx] == '#')
                    if all(parts):
                        for p in monster:
                            dx = x + p[0]
                            dy = y + p[1]
                            image[dy] = image[dy][: dx]
    with open('output.txt', 'w+') as f:
        for l in rotate_tile(image):
            f.write(l + '\n')
    print(sum(l.count('#') for l in image))

    if __name__ == "__main__":
        solve_part1()
        solve_part2()
