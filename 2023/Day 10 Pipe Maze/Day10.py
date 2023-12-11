# --- Day 10: Pipe Maze ---
# You use the hang glider to ride the hot air from Desert Island all the way up to the floating metal island. This island is surprisingly cold and there definitely aren't any thermals to glide on, so you leave your hang glider behind.

# You wander around for a while, but you don't find any people or animals. However, you do occasionally find signposts labeled "Hot Springs" pointing in a seemingly consistent direction; maybe you can find someone at the hot springs and ask them where the desert-machine parts are made.

# The landscape here is alien; even the flowers and trees are made of metal. As you stop to admire some metal grass, you notice something metallic scurry away in your peripheral vision and jump into a big pipe! It didn't look like any animal you've ever seen; if you want a better look, you'll need to get ahead of it.

# Scanning the area, you discover that the entire field you're standing on is densely packed with pipes; it was hard to tell at first because they're the same metallic silver color as the "ground". You make a quick sketch of all of the surface pipes you can see (your puzzle input).

# The pipes are arranged in a two-dimensional grid of tiles:

# | is a vertical pipe connecting north and south.
# - is a horizontal pipe connecting east and west.
# L is a 90-degree bend connecting north and east.
# J is a 90-degree bend connecting north and west.
# 7 is a 90-degree bend connecting south and west.
# F is a 90-degree bend connecting south and east.
# . is ground; there is no pipe in this tile.
# S is the starting position of the animal; there is a pipe on this tile, but your sketch doesn't show what shape the pipe has.
# Based on the acoustics of the animal's scurrying, you're confident the pipe that contains the animal is one large, continuous loop.

# For example, here is a square loop of pipe:

# .....
# .F-7.
# .|.|.
# .L-J.
# .....
# If the animal had entered this loop in the northwest corner, the sketch would instead look like this:

# .....
# .S-7.
# .|.|.
# .L-J.
# .....
# In the above diagram, the S tile is still a 90-degree F bend: you can tell because of how the adjacent pipes connect to it.

# Unfortunately, there are also many pipes that aren't connected to the loop! This sketch shows the same loop as above:

# -L|F7
# 7S-7|
# L|7||
# -L-J|
# L|-JF
# In the above diagram, you can still figure out which pipes form the main loop: they're the ones connected to S, pipes those pipes connect to, pipes those pipes connect to, and so on. Every pipe in the main loop connects to its two neighbors (including S, which will have exactly two pipes connecting to it, and which is assumed to connect back to those two pipes).

# Here is a sketch that contains a slightly more complex main loop:

# ..F7.
# .FJ|.
# SJ.L7
# |F--J
# LJ...
# Here's the same example sketch with the extra, non-main-loop pipe tiles also shown:

# 7-F7-
# .FJ|7
# SJLL7
# |F--J
# LJ.LJ
# If you want to get out ahead of the animal, you should find the tile in the loop that is farthest from the starting position. Because the animal is in the pipe, it doesn't make sense to measure this by direct distance. Instead, you need to find the tile that would take the longest number of steps along the loop to reach from the starting point - regardless of which way around the loop the animal went.

# In the first example with the square loop:

# .....
# .S-7.
# .|.|.
# .L-J.
# .....
# You can count the distance each tile in the loop is from the starting point like this:

# .....
# .012.
# .1.3.
# .234.
# .....
# In this example, the farthest point from the start is 4 steps away.

# Here's the more complex loop again:

# ..F7.
# .FJ|.
# SJ.L7
# |F--J
# LJ...
# Here are the distances for each tile on that loop:

# ..45.
# .236.
# 01.78
# 14567
# 23...
# Find the single giant loop starting at S. How many steps along the loop does it take to get from the starting position to the point farthest from the starting position?
# def read_input(filename="input.txt"):
#     with open(filename, "r") as file:
#         return [list(line.strip()) for line in file.readlines()]

# def find_start_position(grid):
#     for i in range(len(grid)):
#         for j in range(len(grid[i])):
#             if grid[i][j] == 'S':
#                 return i, j

# def is_valid_move(x, y, grid):
#     return 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] != '.'

# def find_loop(grid, start_x, start_y):
#     directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up
#     loop = []
#     visited = set()

#     def dfs(x, y):
#         if (x, y) in visited:
#             return
#         visited.add((x, y))
#         loop.append((x, y))

#         for dx, dy in directions:
#             nx, ny = x + dx, y + dy
#             if is_valid_move(nx, ny, grid) and (nx, ny) not in visited:
#                 dfs(nx, ny)

#     dfs(start_x, start_y)
#     return loop

# def find_loop(grid, start_x, start_y):
#     directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up
#     loop = []
#     visited = set()
#     stack = [(start_x, start_y)]

#     while stack:
#         x, y = stack.pop()
#         if (x, y) in visited:
#             continue
#         visited.add((x, y))
#         loop.append((x, y))

#         for dx, dy in directions:
#             nx, ny = x + dx, y + dy
#             if is_valid_move(nx, ny, grid) and (nx, ny) not in visited:
#                 stack.append((nx, ny))

#     return loop

# def find_max_distance(grid, loop):
#     max_distance = 0

#     for i in range(len(loop)):
#         for j in range(i + 1, len(loop)):
#             distance = abs(loop[i][0] - loop[j][0]) + abs(loop[i][1] - loop[j][1])
#             max_distance = max(max_distance, distance)

#     return max_distance


# def main():
#     grid = read_input()
#     start_x, start_y = find_start_position(grid) # type: ignore
#     loop = find_loop(grid, start_x, start_y)
#     max_distance = find_max_distance(grid, loop)

#     print("Maximum distance along the loop:", max_distance)

# if __name__ == "__main__":
#     main()

# from collections import deque

# def find_max_distance(grid, loop):
#     max_distance = 0
#     directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

#     for x, y in loop:
#         visited = set()
#         queue = deque([(x, y, 0)])

#         while queue:
#             cx, cy, distance = queue.popleft()

#             if (cx, cy) in visited:
#                 continue

#             visited.add((cx, cy))

#             for dx, dy in directions:
#                 nx, ny = cx + dx, cy + dy

#                 if (nx, ny) in loop and (nx, ny) not in visited:
#                     queue.append((nx, ny, distance + 1))

#         max_distance = max(max_distance, distance)

#     return max_distance

# # Update the main function to use the corrected function
# def main():
#     grid = read_input()
#     start_x, start_y = find_start_position(grid) # type: ignore
#     loop = find_loop(grid, start_x, start_y)
#     max_distance = find_max_distance(grid, loop)

#     print("Maximum distance along the loop:", max_distance)

# if __name__ == "__main__":
#     main()


# def read_input(filename="input.txt"):
#     with open(filename, "r") as file:
#         return [list(line.strip()) for line in file.readlines()]

import numpy as np

with open('input.txt') as f:
    maze = [[char for char in lines.strip()] for lines in f]
    maze = np.array(maze)

# Just for the visualization    
symbol_map = {'J': '┘', 'L': '└', 'F': '┌', '7': '┐'}
for key, value in symbol_map.items():
    maze[maze == key] = value
            
def show_map(line):           
    for sublist in line:
        print(''.join(sublist))     

vizualize_maze = np.copy(maze)
direction_maze = np.zeros(maze.shape)
        
# Define movable symbols and their possible directions
movable_symbols = {
    '┘': [(0, -1), (-1, 0)],  # Left or Up
    '└': [(0, 1), (-1, 0)], # Right or Up
    '┌': [(0, 1), (1, 0)],# Right or Down
    '┐': [(0, -1), (1, 0)], # Left or Down
    '|': [(-1, 0), (1, 0)], # Up or Down
    '-': [(0, -1), (0, 1)], # Left or Right
}

highlight = {'┘': '╝', '└': '╚', '┌': '╔', '┐':'╗', '|': '║', '-': '═', 'S': '█'}

pos = np.where(maze == 'S')
current_pos = (pos[0][0], pos[1][0])  

# Starting from S, searching for the start that have to meet the condition
searching = [(-1, 0), (1, 0), (0, -1), (0, 1)] # Up, Down, Left and Right

for way in searching:
    next_pos = (current_pos[0] + way[0], current_pos[1] + way[1])
    diff = np.array(current_pos) - np.array(next_pos)
    if maze[next_pos] in movable_symbols and tuple(diff) in movable_symbols[maze[next_pos]]:
        vizualize_maze[next_pos] = highlight[maze[next_pos]]
        if way[0]!= 0:
            direction_maze[current_pos] = way[0]
        else:
            direction_maze[current_pos] = - diff[0]
        break

found_end = False
n = 0
while found_end == False:
    if tuple(diff) in movable_symbols[maze[next_pos]]:
        next_directions = [d for d in movable_symbols[maze[next_pos]] if tuple(diff) != d]
        if next_directions:
            dx, dy = next_directions[0]
            current_pos = next_pos
            if dx != 0:
                direction_maze[next_pos] = dx  
            else:
                direction_maze[next_pos] = - diff[0]
            next_pos = (next_pos[0] + dx, next_pos[1] + dy)

    diff = np.array(current_pos) - np.array(next_pos)    
    if maze[next_pos] == 'S':
        found_end = True

    vizualize_maze[next_pos] = highlight[maze[next_pos]]
    n = n + 1        

print(n/2) # Do the Rounding yourself
print(round(n/2))    # Using the round function here will not work.
show_map(vizualize_maze)   

#### Part 2

# --- Part Two ---
# You quickly reach the farthest point of the loop, but the animal never emerges. Maybe its nest is within the area enclosed by the loop?

# To determine whether it's even worth taking the time to search for such a nest, you should calculate how many tiles are contained within the loop. For example:

# ...........
# .S-------7.
# .|F-----7|.
# .||.....||.
# .||.....||.
# .|L-7.F-J|.
# .|..|.|..|.
# .L--J.L--J.
# ...........
# The above loop encloses merely four tiles - the two pairs of . in the southwest and southeast (marked I below). The middle . tiles (marked O below) are not in the loop. Here is the same loop again with those regions marked:

# ...........
# .S-------7.
# .|F-----7|.
# .||OOOOO||.
# .||OOOOO||.
# .|L-7OF-J|.
# .|II|O|II|.
# .L--JOL--J.
# .....O.....
# In fact, there doesn't even need to be a full tile path to the outside for tiles to count as outside the loop - squeezing between pipes is also allowed! Here, I is still within the loop and O is still outside the loop:

# ..........
# .S------7.
# .|F----7|.
# .||OOOO||.
# .||OOOO||.
# .|L-7F-J|.
# .|II||II|.
# .L--JL--J.
# ..........
# In both of the above examples, 4 tiles are enclosed by the loop.

# Here's a larger example:

# .F----7F7F7F7F-7....
# .|F--7||||||||FJ....
# .||.FJ||||||||L7....
# FJL7L7LJLJ||LJ.L-7..
# L--J.L7...LJS7F-7L7.
# ....F-J..F7FJ|L7L7L7
# ....L7.F7||L7|.L7L7|
# .....|FJLJ|FJ|F7|.LJ
# ....FJL-7.||.||||...
# ....L---J.LJ.LJLJ...
# The above sketch has many random bits of ground, some of which are in the loop (I) and some of which are outside it (O):

# OF----7F7F7F7F-7OOOO
# O|F--7||||||||FJOOOO
# O||OFJ||||||||L7OOOO
# FJL7L7LJLJ||LJIL-7OO
# L--JOL7IIILJS7F-7L7O
# OOOOF-JIIF7FJ|L7L7L7
# OOOOL7IF7||L7|IL7L7|
# OOOOO|FJLJ|FJ|F7|OLJ
# OOOOFJL-7O||O||||OOO
# OOOOL---JOLJOLJLJOOO
# In this larger example, 8 tiles are enclosed by the loop.

# Any tile that isn't part of the main loop can count as being enclosed by the loop. Here's another example with many bits of junk pipe lying around that aren't connected to the main loop at all:

# FF7FSF7F7F7F7F7F---7
# L|LJ||||||||||||F--J
# FL-7LJLJ||||||LJL-77
# F--JF--7||LJLJ7F7FJ-
# L---JF-JLJ.||-FJLJJ7
# |F|F-JF---7F7-L7L|7|
# |FFJF7L7F-JF7|JL---7
# 7-L-JL7||F7|L7F-7F7|
# L.L7LFJ|||||FJL7||LJ
# L7JLJL-JLJLJL--JLJ.L
# Here are just the tiles that are enclosed by the loop marked with I:

# FF7FSF7F7F7F7F7F---7
# L|LJ||||||||||||F--J
# FL-7LJLJ||||||LJL-77
# F--JF--7||LJLJIF7FJ-
# L---JF-JLJIIIIFJLJJ7
# |F|F-JF---7IIIL7L|7|
# |FFJF7L7F-JF7IIL---7
# 7-L-JL7||F7|L7F-7F7|
# L.L7LFJ|||||FJL7||LJ
# L7JLJL-JLJLJL--JLJ.L
# In this last example, 10 tiles are enclosed by the loop.

# Figure out whether you have time to search for the nest by calculating the area within the loop. How many tiles are enclosed by the loop?

walls = ['╝', '╚', '╔', '╗', '║', '═', '█']

main_array = np.zeros(direction_maze.shape)

highlight = False

for i, row in enumerate(main_array):
    for j, item in enumerate(row):
        if direction_maze[i][j] != 0:
            rotating_direction = int(direction_maze[i][j])
            
for i, row in enumerate(main_array):
    for j, item in enumerate(row):
        if highlight:
            main_array[i][j] = 1

        if direction_maze[i][j] == - rotating_direction:
            highlight = True 
        if direction_maze[i][j] == rotating_direction:
            highlight = False

for i, row in enumerate(main_array):
    for j, item in enumerate(row):
        if vizualize_maze[i][j] in walls:
            main_array[i][j] = 0

print(round(np.sum(main_array)))