# --- Day 11: Seating System --- Your plane lands with plenty of time to spare. The final leg of your journey is a
# ferry that goes directly to the tropical island where you can finally start your vacation. As you reach the waiting
# area to board the ferry, you realize you're so early, nobody else has even arrived yet!
#
# By modeling the process people use to choose (or abandon) their seat in the waiting area, you're pretty sure you
# can predict the best place to sit. You make a quick map of the seat layout (your puzzle input).
#
# The seat layout fits neatly on a grid. Each position is either floor (.), an empty seat (L), or an occupied seat (
# #). For example, the initial seat layout might look like this:
#
# L.LL.LL.LL LLLLLLL.LL L.L.L..L.. LLLL.LL.LL L.LL.LL.LL L.LLLLL.LL ..L.L..... LLLLLLLLLL L.LLLLLL.L L.LLLLL.LL Now,
# you just need to model the people who will be arriving shortly. Fortunately, people are entirely predictable and
# always follow a simple set of rules. All decisions are based on the number of occupied seats adjacent to a given
# seat (one of the eight positions immediately up, down, left, right, or diagonal from the seat). The following rules
# are applied to every seat simultaneously:
#
# If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
# If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
# Otherwise, the seat's state does not change.
# Floor (.) never changes; seats don't move, and nobody sits on the floor.
#
# After one round of these rules, every seat in the example layout becomes occupied:
#
# #.##.##.##
# #######.##
# #.#.#..#..
# ####.##.##
# #.##.##.##
# #.#####.##
# ..#.#.....
# ##########
# #.######.#
# #.#####.##
# After a second round, the seats with four or more occupied adjacent seats become empty again:
#
# #.LL.L#.##
# #LLLLLL.L#
# L.L.L..L..
# #LLL.LL.L#
# #.LL.LL.LL
# #.LLLL#.##
# ..L.L.....
# #LLLLLLLL#
# #.LLLLLL.L
# #.#LLLL.##
# This process continues for three more rounds:
#
# #.##.L#.## #L###LL.L# L.#.#..#.. #L##.##.L# #.##.LL.LL #.###L#.## ..#.#..... #L######L# #.LL###L.L #.#L###.##
# #.#L.L#.## #LLL#LL.L# L.L.L..#.. #LLL.##.L# #.LL.LL.LL #.LL#L#.## ..L.L..... #L#LLLL#L# #.LLLLLL.L #.#L#L#.##
# #.#L.L#.## #LLL#LL.L# L.#.L..#.. #L##.##.L# #.#L.LL.LL #.#L#L#.## ..L.L..... #L#L##L#L# #.LLLLLL.L #.#L#L#.## At
# this point, something interesting happens: the chaos stabilizes and further applications of these rules cause no
# seats to change state! Once people stop moving around, you count 37 occupied seats.
#
# Simulate your seating area by applying the seating rules repeatedly until no seats change state. How many seats end
# up occupied?
#

from itertools import product
from time import time

starttime = time()
f = list(
    filter(lambda x: x != '', list(open('input.txt').read().split("\n"))))

mods = list(product([0, 1, -1], repeat=2))
mods.pop(0)
coords = {}


def applyrules(limit=4):
    coordscop = coords.copy()
    coordscompare = {}
    while True:
        for i in coordscop:
            if limit == 4:
                adjseats = list(
                    tuple(map(sum, zip(i, mod))) for mod in mods)
                occupiedseats = len([
                    coordscop[value] for value in adjseats
                    if value in coordscop if coordscop[value] == "#"
                ])
            else:
                occupiedseats = part2(coordscop, i)
            if coordscop[i] == ".":
                coordscompare[i] = "."
            elif coordscop[i] == "L" and occupiedseats == 0:
                coordscompare[i] = "#"
            elif coordscop[i] == "#" and occupiedseats >= limit:
                coordscompare[i] = "L"
        if coordscompare == coordscop:
            totaloccupiedseats = sum(x == "#" for x in coordscop.values())
            print(f'There are {totaloccupiedseats} total occupied seats')
            break
        else:
            coordscop = coordscompare.copy()


def part2(coordscop, i):
    adjseats = list(tuple(map(sum, zip(i, mod))) for mod in mods)
    occupiedseats = []
    for i in adjseats:
        index = adjseats.index(i)
        factor = 1
        found = False
        while found == False:
            x, y = i
            if i not in coordscop:
                found = True
            elif coordscop[i] == ".":
                x += mods[index][0]
                y += mods[index][1]
                i = x, y
            elif coordscop[i] == "L":
                found = True
            elif coordscop[i] == "#":
                occupiedseats.append("#")
                found = True
    return len(occupiedseats)


# Build grid
y = 0
for i in f[-1::-1]:
    x = 0
    for e in i:
        coord = x, y
        coords[coord] = e
        x += 1
    y += 1

# Solve puzzle
applyrules(4)
applyrules(5)

timer = "{:.2f}".format(time() - starttime)
print(f'{timer}s')

