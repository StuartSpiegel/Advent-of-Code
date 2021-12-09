from itertools import combinations
# --- Day 8: Seven Segment Search --- You barely reach the safety of the cave when the whale smashes into the cave
# mouth, collapsing it. Sensors indicate another exit to this cave at a much greater depth, so you have no choice but
# to press on.
#
# As your submarine slowly makes its way through the cave system, you notice that the four-digit seven-segment
# displays in your submarine are malfunctioning; they must have been damaged during the escape. You'll be in a lot of
# trouble without them, so you'd better figure out what's wrong.
#
# Each digit of a seven-segment display is rendered by turning on or off any of seven segments named a through g:
#
#   0:      1:      2:      3:      4:
#  aaaa    ....    aaaa    aaaa    ....
# b    c  .    c  .    c  .    c  b    c
# b    c  .    c  .    c  .    c  b    c
#  ....    ....    dddd    dddd    dddd
# e    f  .    f  e    .  .    f  .    f
# e    f  .    f  e    .  .    f  .    f
#  gggg    ....    gggg    gggg    ....
#
# 5:      6:      7:      8:      9: aaaa    aaaa    aaaa    aaaa    aaaa b    .  b    .  .    c  b    c  b    c b
# .  b    .  .    c  b    c  b    c dddd    dddd    ....    dddd    dddd .    f  e    f  .    f  e    f  .    f .
# f  e    f  .    f  e    f  .    f gggg    gggg    ....    gggg    gggg So, to render a 1, only segments c and f
# would be turned on; the rest would be off. To render a 7, only segments a, c, and f would be turned on.
#
# The problem is that the signals which control the segments have been mixed up on each display. The submarine is
# still trying to display numbers by producing output on signal wires a through g, but those wires are connected to
# segments randomly. Worse, the wire/segment connections are mixed up separately for each four-digit display! (All of
# the digits within a display use the same connections, though.)
#
# So, you might know that only signal wires b and g are turned on, but that doesn't mean segments b and g are turned
# on: the only digit that uses two segments is 1, so it must mean segments c and f are meant to be on. With just that
# information, you still can't tell which wire (b/g) goes to which segment (c/f). For that, you'll need to collect
# more information.
#
# For each display, you watch the changing signals for a while, make a note of all ten unique signal patterns you
# see, and then write down a single four digit output value (your puzzle input). Using the signal patterns,
# you should be able to work out which pattern corresponds to which digit.
#
# For example, here is what you might see in a single entry in your notes:
#
# acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab |
# cdfeb fcadb cdfeb cdbaf
# (The entry is wrapped here to two lines so it fits; in your notes, it will all be on a single line.)
#
# Each entry consists of ten unique signal patterns, a | delimiter, and finally the four digit output value. Within
# an entry, the same wire/segment connections are used (but you don't know what the connections actually are). The
# unique signal patterns correspond to the ten different ways the submarine tries to render a digit using the current
# wire/segment connections. Because 7 is the only digit that uses three segments, dab in the above example means that
# to render a 7, signal lines d, a, and b are on. Because 4 is the only digit that uses four segments, eafb means
# that to render a 4, signal lines e, a, f, and b are on.
#
# Using this information, you should be able to work out which combination of signal wires corresponds to each of the
# ten digits. Then, you can decode the four digit output value. Unfortunately, in the above example, all of the
# digits in the output value (cdfeb fcadb cdfeb cdbaf) use five segments and are more difficult to deduce.
#
# For now, focus on the easy digits. Consider this larger example:
# ###################################################################################################################
# be cfbegad cbdgef
# fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe edbfga begcd cbg gc gcadebf fbgde acbgfd abcde
# gfcbed gfec | fcgedb cgb dgebacf gc fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
# fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb aecbfdg fbg gf bafeg dbefa fcge
# gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf |
# gebdcfa ecba ca fadegcb dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe bdfegc
# cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef egadfb cdbfeg cegd fecab cgb gbdefca cg
# fgcdab egfdb bfceg | gbdfcae bgc cg cgb gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg
# bagce #############################################################################################################
#
# Because the digits 1, 4, 7, and 8 each use a unique number of segments, you should be able to tell which
# combinations of signals correspond to those digits. Counting only digits in the output values (the part after | on
# each line), in the above example, there are 26 instances of digits that use a unique number of segments (
# highlighted above).
# In the output values, how many times do digits 1, 4, 7, or 8 appear?

# Part 1
print(len([j for z in [y.split('|')[1].strip().split(' ') for y in open('input.txt').read().split('\n')] for j in z if
           len(j) in [2, 3, 4, 7]]))

# Part 2 --- Part Two --- Through a little deduction, you should now be able to determine the remaining digits.
# Consider again the first example above:
#
# acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf After some careful analysis,
# the mapping between signal wires and segments only make sense in the following configuration:
#
#  dddd
# e    a
# e    a
#  ffff
# g    b
# g    b
#  cccc
# So, the unique signal patterns would correspond to the following digits:
#
# acedgfb: 8
# cdfbe: 5
# gcdfa: 2
# fbcad: 3
# dab: 7
# cefabd: 9
# cdfgeb: 6
# eafb: 4
# cagedb: 0
# ab: 1
# Then, the four digits of the output value can be decoded:
#
# cdfeb: 5
# fcadb: 3
# cdfeb: 5
# cdbaf: 3
# Therefore, the output value for this entry is 5353.
#
# Following this same process for each entry in the second, larger example above, the output value of each entry can
# be determined:
#
# fdgacbe cefdb cefbgd gcbe: 8394
# fcgedb cgb dgebacf gc: 9781
# cg cg fdcagb cbg: 1197
# efabcd cedba gadfec cb: 9361
# gecf egdcabf bgf bfgea: 4873
# gebdcfa ecba ca fadegcb: 8418
# cefg dcbef fcge gbcadfe: 4548
# ed bcgafe cdgba cbgef: 1625
# gbdfcae bgc cg cgb: 8717
# fgae cfgab fg bagce: 4315
# Adding all of the output values in this larger example produces 61229.
#####################################################################################################################
# For each entry, determine all of the wire/segment connections and decode the four-digit output values. What do you
# get if you add up all of the output value?
######################################################################################################################
# This method performs the letter substitution per string
# def remove(letter, strings):
#     return {key: [x.replace(letter, '') for x in value] for key, value in strings.items()}
#
#
display_lines = [x.split('|')[1].strip().split(' ') for x in open('input.txt').read().split('\n')]
all_lines = [z.split('|')[0].strip().split(' ') for z in open('input.txt').read().split('\n')]
#####################################################################################################################
# This is the dictionary that holds the decoded string representations as integers Make a
# dictionary with key=number of segments, value=list of strings with that length By process of elimination map each
# of t,u,v,w,x,y,z to exactly one of a,b,c,d,e,f,g Use this mapping to figure out what the display is showing and add
# it to our total.
# def dictionary_of_Definitions(iterable, sub):
#     strings = {i:[x for x in iterable if len(x) == i] for i in range(2, 8)}
#     translations = {}
#
#     translations['t'] = [x for x in strings[3][0] if x not in strings[2][0]]
#     strings = remove(translations['t'], strings)
#
#     translations['y'] = \
#         [list(z)[0] for z in [set(strings[2][0]).intersection(set(x)) for x in strings[6]] if len(z) == 1][
#             0]  # segment y the overlap of 1 and 6
#     strings = remove(translations['y'], strings)
#
#     translations['v'] = strings[2][0][0]  # v is the remaining segment in 1
#     strings = remove(translations['v'], strings)
#
#     translations['u'] = \
#         [list(z)[0] for z in [set(strings[4][0]).intersection(set(x)) for x in strings[6]] if len(z) == 1][0]  # segment
#     # u is the overlap of the remainder of 4 and 0
#     strings = remove(translations['u'], strings)
#
#     translations['w'] = strings[4][0][0]  # w is the only segment left in 4
#     strings = remove(translations['w'], strings)
#
#     translations['z'] = [x for x in strings[5] if len(x) == 1][0][0]  # z is the only singleton segment left in the
#     # set which started with 5 segments
#     strings = remove(translations['z'], strings)
#
#     translations['x'] = strings[7][0][0]  # x is the only segment left in 8
#     reverse_translation = {value: key for key, value in translations.items()}  # keys = letters , values are the new letters after
#     # the translation
#
#     # 0-9 in set form containing their translated segments
#     array = [{'t', 'u', 'v', 'x', 'y', 'z'}, {'v', 'y'}, {'t', 'v', 'w', 'x', 'z'}, {'t', 'v', 'w', 'y', 'z'},
#              {'u', 'w', 'v', 'y'}, {'t', 'u', 'w', 'y', 'z'}, {'t', 'u', 'w', 'x', 'y', 'z'}, {'t', 'v', 'y'},
#              {'t', 'u', 'v', 'w', 'x', 'y', 'z'}, {'z', 'y', 'u', 'v', 'w', 't'}]
#
#     return int(''.join([str(array.index(x)) for x in [set([reverse_translation[l] for l in k]) for k in sub]]))  #
#     # convert display representations into integers
#
#
# for index in range(len(display_lines)):
#     counter += dictionary_of_Definitions(all_lines[index], display_lines[index])
#
# print(counter)
#################################################################################################
# Part 2
with open("input.txt", "rt") as file:
    values = []
    for line in file:
        k, out = line.rstrip().split(" | ")
        values += [(k.split(), out.split())]

counter = 0

for (k, out) in values:
    mapping = {frozenset(signal): None for signal in k}
    temp_len5 = set()
    temp_len6 = set()

    for signal in k:
        size = len(signal)
        ID = frozenset(signal)
        if size == 2:
            mapping[ID] = 1
        elif size == 4:
            mapping[ID] = 4
        elif size == 3:
            mapping[ID] = 7
        elif size == 7:
            mapping[ID] = 8
        elif size == 5:
            temp_len5.add(ID)
        elif size == 6:
            temp_len6.add(ID)

    assert len(temp_len5) == 3
    assert len(temp_len6) == 3

    digits_2_or_5 = {}
    digits_0_or_9 = {}
    for pair in combinations(temp_len5, 2):
        s1, s2 = pair
        if len(s1 | s2) == 7:
            (s3,) = (temp_len5 - {s1, s2})
            mapping[s3] = 3
            digits_2_or_5 = {s1, s2}

    digits = {dig: ID for ID, dig in mapping.items() if dig}

    for pair in combinations(temp_len5, 2):
        s1, s2 = pair
        if len(s1 | s2) == 7:
            (s3,) = (temp_len5 - {s1, s2})
            mapping[s3] = 3
            digits_2_or_5 = {s1, s2}
            break

    s1, s2 = digits_2_or_5
    if len(s1 | digits[4]) == 7:
        mapping[s1] = 2
        mapping[s2] = 5
        digits[2] = s1
        digits[5] = s2
    else:
        mapping[s1] = 5
        mapping[s2] = 2
        digits[5] = s1
        digits[2] = s2

    for signal in temp_len6:
        if len(signal | digits[1]) == 7:
            mapping[signal] = 6
            digits[6] = signal
            digits_0_or_9 = temp_len6 - {signal}
            break

    s1, s2 = digits_0_or_9
    if len(s1 - digits[5]) == 1:
        mapping[s1] = 9
        mapping[s2] = 0
        digits[9] = s1
        digits[0] = s2
    else:
        mapping[s1] = 0
        mapping[s2] = 9
        digits[0] = s1
        digits[9] = s2

    assert len(mapping) == 10
    assert len(digits) == 10

    counter += sum(
        mapping[frozenset(signal)] * (10 ** n)
        for n, signal in zip(range(3, -1, -1), out)
    )

print(f"Part 2: {counter}")
