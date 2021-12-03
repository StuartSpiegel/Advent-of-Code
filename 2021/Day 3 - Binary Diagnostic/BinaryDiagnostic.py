# --- Day 3: Binary Diagnostic ---
# The submarine has been making some odd creaking noises, so you ask it to produce a diagnostic report just in case.
#
# The diagnostic report (your puzzle input) consists of a list of binary numbers which, when decoded properly,
# can tell you many useful things about the conditions of the submarine. The first parameter to check is the power
# consumption.
#
# You need to use the binary numbers in the diagnostic report to generate two new binary numbers (called the gamma
# rate and the epsilon rate). The power consumption can then be found by multiplying the gamma rate by the epsilon
# rate.
#
# Each bit in the gamma rate can be determined by finding the most common bit in the corresponding position of all
# numbers in the diagnostic report. For example, given the following diagnostic report:
#
# 00100 11110 10110 10111 10101 01111 00111 11100 10000 11001 00010 01010 Considering only the first bit of each
# number, there are five 0 bits and seven 1 bits. Since the most common bit is 1, the first bit of the gamma rate is 1.
#
# The most common second bit of the numbers in the diagnostic report is 0, so the second bit of the gamma rate is 0.
#
# The most common value of the third, fourth, and fifth bits are 1, 1, and 0, respectively, and so the final three
# bits of the gamma rate are 110.
#
# So, the gamma rate is the binary number 10110, or 22 in decimal.
#
# The epsilon rate is calculated in a similar way; rather than use the most common bit, the least common bit from
# each position is used. So, the epsilon rate is 01001, or 9 in decimal. Multiplying the gamma rate (22) by the
# epsilon rate (9) produces the power consumption, 198.
#
# Use the binary numbers in your diagnostic report to calculate the gamma rate and epsilon rate, then multiply them
# together. What is the power consumption of the submarine? (Be sure to represent your answer in decimal, not binary.)

import time
from collections import defaultdict


# Wrapper method that returns program performance times per function
def profiler(method):
    def wrapper_method(*arg, **kw):
        t = time.time()
        ret = method(*arg, **kw)
        print('Method ' + method.__name__ + ' took : ' +
              "{:2.5f}".format(time.time() - t) + ' sec')
        return ret

    return wrapper_method


@profiler
def part1():
    input = [l.strip() for l in open("input.txt")]

    gamma = list(input[0])

    for bit in range(len(input[0])):
        bits = [l[bit] for l in input]

        gamma[bit] = str(int(bits.count('1') > bits.count('0') * 1))

    epsilon = int(''.join(gamma).replace(
        '0', 'x').replace('1', '0').replace('x', '1'), 2)
    gamma = int(''.join(gamma), 2)

    print("part 1 : ", gamma * epsilon)


@profiler
# Multiply Oxygen generator rating Decimal number with CO2 Scrubber Decimal reading number 
def part2():
    oxygen = [l.strip() for l in open("input.txt")]
    CO2 = oxygen.copy()

    for bit in range(len(oxygen[0])):

        bits_oxy = [l[bit] for l in oxygen]

        if bits_oxy.count('1') >= bits_oxy.count('0'):
            oxygen = [l for l in oxygen if l[bit] == '1']
        else:
            oxygen = [l for l in oxygen if l[bit] == '0']

        if len(oxygen) == 1:
            break

    for bit in range(len(CO2[0])):

        bits_car = [l[bit] for l in CO2]

        if bits_car.count('1') >= bits_car.count('0'):
            CO2 = [l for l in CO2 if l[bit] == '0']
        else:
            CO2 = [l for l in CO2 if l[bit] == '1']

        if len(CO2) == 1:
            break

    print("part 2 : ", int(oxygen[0], 2) * int(CO2[0], 2))


if __name__ == "__main__":
    part1()
    part2()

