# --- Day 4: Giant Squid --- You're already almost 1.5km (almost a mile) below the surface of the ocean, already so
# deep that you can't see any sunlight. What you can see, however, is a giant squid that has attached itself to the
# outside of your submarine.
#
# Maybe it wants to play bingo?
#
# Bingo is played on a set of boards each consisting of a 5x5 grid of numbers. Numbers are chosen at random,
# and the chosen number is marked on all boards on which it appears. (Numbers may not appear on all boards.) If all
# numbers in any row or any column of a board are marked, that board wins. (Diagonals don't count.)
#
# The submarine has a bingo subsystem to help passengers (currently, you and the giant squid) pass the time. It
# automatically generates a random order in which to draw numbers and a random set of boards (your puzzle input). For
# example:
#
# 7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1
#
# 22 13 17 11  0
#  8  2 23  4 24
# 21  9 14 16  7
#  6 10  3 18  5
#  1 12 20 15 19
#
#  3 15  0  2 22
#  9 18 13 17  5
# 19  8  7 25 23
# 20 11 10 24  4
# 14 21 16 12  6
#
# 14 21 17 24  4 10 16 15  9 19 18  8 23 26 20 22 11 13  6  5 2  0 12  3  7 After the first five numbers are drawn (
# 7, 4, 9, 5, and 11), there are no winners, but the boards are marked as follows (shown here adjacent to each other
# to save space):
#
# 22 13 17 11  0         3 15  0  2 22        14 21 17 24  4
#  8  2 23  4 24         9 18 13 17  5        10 16 15  9 19
# 21  9 14 16  7        19  8  7 25 23        18  8 23 26 20
#  6 10  3 18  5        20 11 10 24  4        22 11 13  6  5
#  1 12 20 15 19        14 21 16 12  6         2  0 12  3  7
# After the next six numbers are drawn (17, 23, 2, 0, 14, and 21), there are still no winners:
#
# 22 13 17 11  0         3 15  0  2 22        14 21 17 24  4
#  8  2 23  4 24         9 18 13 17  5        10 16 15  9 19
# 21  9 14 16  7        19  8  7 25 23        18  8 23 26 20
#  6 10  3 18  5        20 11 10 24  4        22 11 13  6  5
#  1 12 20 15 19        14 21 16 12  6         2  0 12  3  7
# Finally, 24 is drawn:
#
# 22 13 17 11  0         3 15  0  2 22        14 21 17 24  4 8  2 23  4 24         9 18 13 17  5        10 16 15  9
# 19 21  9 14 16  7        19  8  7 25 23        18  8 23 26 20 6 10  3 18  5        20 11 10 24  4        22 11 13
# 6  5 1 12 20 15 19        14 21 16 12  6         2  0 12  3  7 At this point, the third board wins because it has
# at least one complete row or column of marked numbers (in this case, the entire top row is marked: 14 21 17 24 4).
#
# The score of the winning board can now be calculated. Start by finding the sum of all unmarked numbers on that
# board; in this case, the sum is 188. Then, multiply that sum by the number that was just called when the board won,
# 24, to get the final score, 188 * 24 = 4512.
#
# To guarantee victory against the giant squid, figure out which board will win first. What will your final score be
# if you choose that board?

# Parse the input
lines = [i.replace("\n", "") for i in open("input.txt", "r")]
nums = lines.pop(0).split(",")  # get the numbers lines.pop(0) from the parsed lines

# Create the boards from the parsed number data, check for bounds given in problem
boards = []
sboard = []
for i in range(len(lines)):
    sboard.append([[0, int(lines[i][j:j + 2])] for j in range(0, len(lines[i]), 3)]) if len(lines[i]) != 0 else None
    if i == len(lines) - 1 or len(lines[i]) == 0:
        boards.append(sboard)
        sboard = []


# Iterative algo to check if a board has won, if so save the board
# Only checks row and cols, Diagonal wins dont count
def searchBingo():
    winners = []
    won = []
    for num in nums:
        for i in range(len(boards)):  # all boards
            for j in boards[i]:  # all rows
                if i in won:
                    continue
                isWon = [False, 0]

                for k in j:  # all cols
                    if k[1] == int(num):
                        k[0] = 1

                if sum([a[0] for a in j]) == len(j):  # check row
                    isWon = [True, num]
                else:  # check col
                    for a in range(5):
                        col = []
                        for k in boards[i]:
                            col.append(k[a])

                        if sum([a[0] for a in col]) == len(j):
                            isWon = [True, num]

                if isWon[0]:
                    winners.append([boards[i], int(isWon[1])])
                    won.append(i)

    return winners


# Do the Brute force search to get a list of WON boards returned
wintables = searchBingo()

firstwon = wintables[0]  # of those winners mark the first board to win and the last board to win
lastwon = wintables[-1]
# Results
print(firstwon[1] * sum(sum(a[1] if a[0] == 0 else 0 for a in i) for i in firstwon[0]))
print(lastwon[1] * sum(sum(a[1] if a[0] == 0 else 0 for a in i) for i in lastwon[0]))

