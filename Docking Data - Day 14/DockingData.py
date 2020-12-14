# --- Day 14: Docking Data --- As your ferry approaches the sea port, the captain asks for your help again. The
# computer system that runs this port isn't compatible with the docking program on the ferry, so the docking
# parameters aren't being correctly initialized in the docking program's memory.
#
# After a brief inspection, you discover that the sea port's computer system uses a strange bitmask system in its
# initialization program. Although you don't have the correct decoder chip handy, you can emulate it in software!
#
# The initialization program (your puzzle input) can either update the bitmask or write a value to memory. Values and
# memory addresses are both 36-bit unsigned integers. For example, ignoring bitmasks for a moment, a line like mem[8]
# = 11 would write the value 11 to memory address 8.
#
# The bitmask is always given as a string of 36 bits, written with the most significant bit (representing 2^35) on
# the left and the least significant bit (2^0, that is, the 1s bit) on the right. The current bitmask is applied to
# values immediately before they are written to memory: a 0 or 1 overwrites the corresponding bit in the value,
# while an X leaves the bit in the value unchanged.
#
# For example, consider the following program:
#
# mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X mem[8] = 11 mem[7] = 101 mem[8] = 0 This program starts by specifying a
# bitmask (mask = ....). The mask it specifies will overwrite two bits in every written value: the 2s bit is
# overwritten with 0, and the 64s bit is overwritten with 1.
#
# The program then attempts to write the value 11 to memory address 8. By expanding everything out to individual
# bits, the mask is applied as follows:
#
# value:  000000000000000000000000000000001011  (decimal 11) mask:   XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X result:
# 000000000000000000000000000001001001  (decimal 73) So, because of the mask, the value 73 is written to memory
# address 8 instead. Then, the program tries to write 101 to address 7:
#
# value:  000000000000000000000000000001100101  (decimal 101) mask:   XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X result:
# 000000000000000000000000000001100101  (decimal 101) This time, the mask has no effect, as the bits it overwrote
# were already the values the mask tried to set. Finally, the program tries to write 0 to address 8:
#
# value:  000000000000000000000000000000000000  (decimal 0)
# mask:   XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
# result: 000000000000000000000000000001000000  (decimal 64)
# 64 is written to address 8 instead, overwriting the value that was there previously.
#
# To initialize your ferry's docking program, you need the sum of all values left in memory after the initialization
# program completes. (The entire 36-bit address space begins initialized to the value 0 at every address.) In the
# above example, only two values in memory are not zero - 101 (at address 7) and 64 (at address 8) - producing a sum
# of 165.
#
# Execute the initialization program. What is the sum of all values left in memory after it completes?
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Part 1 - Attempt 1
# import re
#
# with open('input.txt', 'r') as f:
#     data = list(map(str.strip, f.readlines()))
#
# mem_regular = re.compile(r'mem\[(?P<mem>\d+)\] = (?P<val>\d+)')
# bit_mask = []
# mem = {}
#
# for line in data:
#     if line.startswith('bit_mask'):
#         bit_mask = [(x, y) for x, y in zip(line.split(' = ')[1], range(36)) if x.isdigit()]
#     elif match := mem_regular.match(line):
#         val = list(f'{int(match.group("val")):036b}')
#         for v, i in bit_mask:
#             val[i] = v
#         mem[match.group('mem')] = int(''.join(val), 2)
# print('Part 1:', sum(mem.values()))
#
# # Part 2
# bit_mask = []
# mem = {}
#
# for line in data:
#     if line.startswith('mask'):
#         bit_mask = [(x, y) for x, y in zip(line.split(' = ')[1], range(36)) if x == '1']
#         f_mask = [y for x, y in zip(line.split(' = ')[1], range(36)) if x == 'X']
#         template = f'{{0:0{len(f_mask)}b}}'
#         masks = [list(zip(template.format(x), f_mask)) for x in range(2 ** len(f_mask))]
#     elif match := mem_regular.match(line):
#         val = list(f'{int(match.group("mem")):036b}')
#         for v, i in bit_mask:
#             val[i] = v
#         for m in masks:
#             for v, i in m:
#                 val[i] = v
#             mem[int(''.join(val), 2)] = int(match.group('val'))
# print('Part 2:', sum(mem.values()))

# Part 1 Refactored
import re


def intToBin(n):
    res = [0] * 36
    i, sigBit = 0, 2 ** 35
    while n != 0:
        if (n - sigBit) >= 0:
            n = n - sigBit
            res[i] = 1
        i += 1
        sigBit = sigBit / 2
    return res


def maskedIntToBin(n, mask):
    unmasked = intToBin(n)
    for i in range(len(mask)):
        if mask[i] != "X":
            unmasked[i] = int(mask[i])
    return unmasked


def binToInt(bin):
    res = 0
    sigBit = 2 ** 35
    for i in range(len(bin)):
        if bin[i] == 1:
            res += sigBit
        sigBit = int(sigBit / 2)
    return res


def main():
    memory = {}
    reMem = re.compile("mem\[([0-9]+)\] = ([0-9]+)")
    reMask = re.compile("(X|0|1){36}")
    input = [e.rstrip() for e in open("input.txt")]
    mask = None
    for e in input:
        if "mask = " in e:
            mask = re.search(reMask, e).group(0)
        else:
            newmem = (int(re.match(reMem, e).group(1)), int(re.match(reMem, e).group(2)))
            memory[newmem[0]] = binToInt(maskedIntToBin(newmem[1], mask))
    res = 0
    for e in memory:
        res += memory[e]
    return res


print(main())


def maskedIntToBins(n, mask):
    unmasked = intToBin(n)
    for i in range(len(mask)):
        if mask[i] == "1":
            unmasked[i] = 1
        elif mask[i] == "X":
            unmasked[i] = "X"

    def recur(unmaskedN, ret):
        if "X" not in unmaskedN:
            ret.append(unmaskedN)
            return
        for i in range(len(unmaskedN)):
            if unmaskedN[i] == "X":
                res = [unmaskedN.copy(), unmaskedN.copy()]
                res[0][i] = 0
                res[1][i] = 1
                assert len(res[0]) == 36
                return [recur(res[0], ret), recur(res[1], ret)]

    ret = []
    recur(unmasked, ret)

    return ret


def main():
    memory = {}
    reMem = re.compile("mem\[([0-9]+)\] = ([0-9]+)")
    reMask = re.compile("(X|0|1){36}")
    input = [e.rstrip() for e in open("input.txt")]
    for e in input:
        if "mask = " in e:
            mask = re.search(reMask, e).group(0)
        else:
            newmem = (int(re.match(reMem, e).group(1)), int(re.match(reMem, e).group(2)))
            for e in maskedIntToBins(newmem[0], mask):
                memory[binToInt(e)] = newmem[1]

    res = 0
    for e in memory:
        res += memory[e]
    return res


print(main())
