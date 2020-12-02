# --- Day 2: Password Philosophy --- Your flight departs in a few days from the coastal airport; the easiest way down
# to the coast from here is via toboggan.

# The shopkeeper at the North Pole Toboggan Rental Shop is having a bad day. "Something's wrong with our computers;
# we can't log in!" You ask if you can take a look.

# Their password database seems to be a little corrupted: some of the passwords wouldn't have been allowed by the
# Official Toboggan Corporate Policy that was in effect when they were chosen.

# To try to debug the problem, they have created a list (your puzzle input) of passwords (according to the corrupted
# database) and the corporate policy when that password was set.

# For example, suppose you have the following list:

# 1-3 a: abcde 1-3 b: cdefg 2-9 c: ccccccccc Each line gives the password policy and then the password. The password
# policy indicates the lowest and highest number of times a given letter must appear for the password to be valid.
# For example, 1-3 a means that the password must contain a at least 1 time and at most 3 times.

# In the above example, 2 passwords are valid. The middle password, cdefg, is not; it contains no instances of b,
# but needs at least 1. The first and third passwords are valid: they contain one a or nine c, both within the limits
# of their respective policies.

# How many passwords are valid according to their policies?

# Stuart - The easist way to complete this question is to compare the array elements with a parse policy that is
# defined as a regular expression.
import re
import sys
from collections import namedtuple

contents = sys.stdin.read()


# This is probably the quickest way to accomplish the task but also the most complex - using a REG policy check
def parse_policy(line):
    match = re.search("(\d+)-(\d+) ([a-zA-Z]): (.*)", line)
    return match.group(1), match.group(2), match.group(3), match.group(4)


def is_valid_part_one(line):
    minimum, maximum, char, password = parse_policy(line)
    return int(minimum) <= password.count(char) <= int(maximum)


def is_valid_part_two(line):
    pos_1, pos_2, char, password = parse_policy(line)
    return (password[int(pos_1) - 1] == char) != (password[int(pos_2) - 1] == char)


def main():
    print(sum(is_valid_part_one(r.strip())) for r in contents)
    print(sum(is_valid_part_two(r.strip())) for r in contents)


def solve():
    Entry = namedtuple("Entry", "low high c pw")

    data = []
    for line in sys.stdin.readlines():
        allowed, c, pw = line.split()
        low, high = map(int, allowed.split('-'))
        data.append(Entry(low, high, c[0], pw))

    # Sub functions that do the regular expression policy check but this time using a named tuple
    def valid_1(e): return e.low <= e.pw.count(e.c) <= e.high

    def valid_2(e): return (e.pw[e.low - 1] == e.c) ^ (e.pw[e.high - 1] == e.c)

    # Run our input data through the policy checker using map then sum the valid entries
    print("Part 1:", sum(map(valid_1, data)), "valid passwords.")
    print("Part 2:", sum(map(valid_2, data)), "valid passwords.")
