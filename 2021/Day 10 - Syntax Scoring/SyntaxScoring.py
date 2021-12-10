# --- Day 10: Syntax Scoring ---
# You ask the submarine to determine the best route out of the deep-sea cave, but it only replies:

# Syntax error in navigation subsystem on line: all of them
# All of them?! The damage is worse than you thought. You bring up a copy of the navigation subsystem (your puzzle input).

# The navigation subsystem syntax is made of several lines containing chunks. There are one or more chunks on each line, and chunks contain zero or more other chunks. Adjacent chunks are not separated by any delimiter; if one chunk stops, the next chunk (if any) can immediately start. Every chunk must open and close with one of four legal pairs of matching characters:

# If a chunk opens with (, it must close with ).
# If a chunk opens with [, it must close with ].
# If a chunk opens with {, it must close with }.
# If a chunk opens with <, it must close with >.
# So, () is a legal chunk that contains no other chunks, as is []. More complex but valid chunks include ([]), {()()()}, <([{}])>, [<>({}){}[([])<>]], and even (((((((((()))))))))).

# Some lines are incomplete, but others are corrupted. Find and discard the corrupted lines first.

# A corrupted line is one where a chunk closes with the wrong character - that is, where the characters it opens and closes with do not form one of the four legal pairs listed above.

# Examples of corrupted chunks include (], {()()()>, (((()))}, and <([]){()}[{}]). Such a chunk can appear anywhere within a line, and its presence causes the whole line to be considered corrupted.

# For example, consider the following navigation subsystem:

# [({(<(())[]>[[{[]{<()<>>
# [(()[<>])]({[<{<<[]>>(
# {([(<{}[<>[]}>{[]{[(<()>
# (((({<>}<{<{<>}{[]{[]{}
# [[<[([]))<([[{}[[()]]]
# [{[{({}]{}}([{[{{{}}([]
# {<[[]]>}<{[{[{[]{()[[[]
# [<(<(<(<{}))><([]([]()
# <{([([[(<>()){}]>(<<{{
# <{([{{}}[<[[[<>{}]]]>[]]
# Some of the lines aren't corrupted, just incomplete; you can ignore these lines for now. The remaining five lines are corrupted:

# {([(<{}[<>[]}>{[]{[(<()> - Expected ], but found } instead.
# [[<[([]))<([[{}[[()]]] - Expected ], but found ) instead.
# [{[{({}]{}}([{[{{{}}([] - Expected ), but found ] instead.
# [<(<(<(<{}))><([]([]() - Expected >, but found ) instead.
# <{([([[(<>()){}]>(<<{{ - Expected ], but found > instead.
# Stop at the first incorrect closing character on each corrupted line.

# Did you know that syntax checkers actually have contests to see who can get the high score for syntax errors in a file? It's true! To calculate the syntax error score for a line, take the first illegal character on the line and look it up in the following table:

# ): 3 points.
# ]: 57 points.
# }: 1197 points.
# >: 25137 points.
# In the above example, an illegal ) was found twice (2*3 = 6 points), an illegal ] was found once (57 points), an illegal } was found once (1197 points), and an illegal > was found once (25137 points). So, the total syntax error score for this file is 6+57+1197+25137 = 26397 points!

# Find the first illegal character in each corrupted line of the navigation subsystem. What is the total syntax error score for those errors?

with open('input.txt', 'r') as file:
    lines = file.read().split('\n')

def getScore(lines):
    # Hold the char and its respective closing match
    pairs = {')': '(', ']': '[', '}': '{', '>': '<'}

    # Hold the integer values (scores) of each syntax error
    scores = {')': 3, ']': 57, '}': 1197, '>': 25137}
    scores_2 = {'(': 1, '[': 2, '{': 3, '<': 4}

    # current score counter / variable
    syntax_error_score = 0
    results = []

    for line in lines:
        corrupt = False
        the_Stack = []

        for char in line:
            if char in {'(', '{', '<'}:
                the_Stack.append(char)
            elif the_Stack[-1] != pairs[char]:
                syntax_error_score += scores[char]
                corrupt = True
                break
            else:
                the_Stack.pop()
        if not corrupt:
            results = 0
            while the_Stack:
                char_value = scores_2[the_Stack.pop()]
                results_score = results_score * 5 + char_value
            results.append(results_score)
    return syntax_error_score, results

syntax_error_score, results = getScore(lines)

def solvePart1():
    return syntax_error_score


# Autocomplete tools are an odd bunch: the winner is found by sorting all of the scores and then taking the middle score. (There will always be an odd number of scores to consider.)
# In this example, the middle score is 288957 because there are the same number of scores smaller and larger than it.
# Find the completion string for each incomplete line, score the completion strings, and sort the scores. What is the middle score?
def solvePart2():
    mid = len(results)//2
    return results[mid]

print(solvePart1())
print(solvePart2())


