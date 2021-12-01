# --- Day 18: Operation Order --- As you look out the window and notice a heavily-forested continent slowly appear
# over the horizon, you are interrupted by the child sitting next to you. They're curious if you could help them with
# their math homework.
#
# Unfortunately, it seems like this "math" follows different rules than you remember.
#
# The homework (your puzzle input) consists of a series of expressions that consist of addition (+), multiplication (
# *), and parentheses ((...)). Just like normal math, parentheses indicate that the expression inside must be
# evaluated before it can be used by the surrounding expression. Addition still finds the sum of the numbers on both
# sides of the operator, and multiplication still finds the product.
#
# However, the rules of operator precedence have changed. Rather than evaluating multiplication before addition,
# the operators have the same precedence, and are evaluated left-to-right regardless of the order in which they appear.
#
# For example, the steps to evaluate the expression 1 + 2 * 3 + 4 * 5 + 6 are as follows:
#
# 1 + 2 * 3 + 4 * 5 + 6 3   * 3 + 4 * 5 + 6 9   + 4 * 5 + 6 13   * 5 + 6 65   + 6 71 Parentheses can override this
# order; for example, here is what happens if parentheses are added to form 1 + (2 * 3) + (4 * (5 + 6)):
#
# 1 + (2 * 3) + (4 * (5 + 6))
# 1 +    6    + (4 * (5 + 6))
#      7      + (4 * (5 + 6))
#      7      + (4 *   11   )
#      7      +     44
#             51
# Here are a few more examples:
#
# 2 * 3 + (4 * 5) becomes 26. 5 + (8 * 3 + 9 + 3 * 4 * 3) becomes 437. 5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))
# becomes 12240. ((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2 becomes 13632. Before you can help with the
# homework, you need to understand it yourself. Evaluate the expression on each line of the homework; what is the sum
# of the resulting values?

exp = []  # list to hold expressions to be evaluated


def between_parentheses(expression):
    bracket = 1
    expression = expression[1: len(expression)]
    for i, ch in enumerate(expression):
        if ch == '(':
            bracket += 1
        elif ch == ')':
            bracket -= 1
        if bracket == 0:
            return i


def calculate(expression):
    res = expression[0]
    if len(expression) == 1:
        res = int(res)
        return res
    elif res.isdigit():
        res = int(res)
        if expression[1] == '+':
            res += calculate(expression[2: len(expression)])
        elif expression[1] == '*':
            res *= calculate(expression[2: len(expression)])
    elif res == '(':
        '''two cases:
              1)single or nested parentheses couples
              2)(...)...(...)
        '''
        close_bracket = between_parentheses(expression)
        res = calculate(expression[1: close_bracket + 1])
        if len(expression) > close_bracket + 2:
            if expression[close_bracket + 2] == '+':
                res += calculate(expression[close_bracket + 3: len(expression)])
            elif expression[close_bracket + 2] == '*':
                res *= calculate(expression[close_bracket + 3: len(expression)])
    return res


def OperationOrder(filename):
    with open(filename, 'r') as fd:
        res = 0
        for line in fd:
            if line[-1] == '\n':
                line = line[0: -1]
            # remove all spaces
            line = line.replace(' ', '')

            # operation is from right to left instead of left to right so invert the line before passing to the function
            line = line[::-1]
            line_list = []
            for ch in line:
                line_list.append(ch)
            for i, ch in enumerate(line_list):
                if ch == ')':
                    line_list[i] = '('
                elif ch == '(':
                    line_list[i] = ')'
            inverted_line = ''
            for ch in line_list:
                inverted_line += ch
            res += calculate(inverted_line)
    print(res)


filename = "input.txt"
OperationOrder(filename)

# Part 2 Code
for x in filename:
    expr = []
    for l in x:
        if l != ' ':
            expr += [l]
    exp += [expr]


def calc2(f):
    if f[0] != '(':
        r = int(f[0])
    else:
        r = 0
    i = 0
    while i < len(f) - 1:
        if f[i] == '(':
            a, b = between_parentheses(f)
            r = a
            i += b
        elif f[i] == '+':
            if f[i + 1] != '(':
                r += int(f[i + 1])
                i += 1
            else:
                a, b = between_parentheses(f[i + 1:])
                r += a
                i += b + 1
        elif f[i] == '*':
            a, b = calc2(f[i + 1:])
            r *= a
            i += b + 1
        elif f[i] == ')':
            i += 1
            return r, i
        else:
            i += 1
    return r, i


sum2 = 0
for e in exp:
    sum2 += calc2(e)[0]
print('part2', sum2)
