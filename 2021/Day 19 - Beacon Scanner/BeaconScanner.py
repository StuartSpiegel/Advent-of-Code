
import itertools
from collections import Counter

lines = open("input.txt").read().splitlines()
scanners = []
current = None
for k in lines:
    if k == "":
        continue
    elif k[0:3] == "---":
        current = []
        scanners.append(cur)
    else:
        current.append(tuple(map(int, k.split(","))))
