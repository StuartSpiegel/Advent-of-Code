# ----- PART 1 -----
import math

file_input = 'input.txt'
boarding_passes = []

with open(file_input, 'r', encoding='utf-8') as file:
    inputs = [row.strip() for row in file]


# This problem is basically an inverted binary search - very sneaky haha
def binary_search(b_pass, low, high, lower, upper):
    for i in b_pass:
        mid = (low + high) / 2
        if i == lower:
            high = math.floor(mid)
            low = low
        if i == upper:
            high = high
            low = math.ceil(mid)
    return high


for i in inputs:
    row_code = i[:7]
    col_code = i[-3:]
    row = binary_search(b_pass=row_code, low=0, high=127,
                        lower='F', upper='B')

    col = binary_search(b_pass=col_code, low=0, high=7,
                        lower='L', upper='R')

    seat_id = row * 8 + col
    boarding_passes.append(seat_id)

print(max(boarding_passes))  # <---- RESULT

# ----- PART 2 -----
missing_seats = []

for i in range(0, 771):
    if i not in boarding_passes:
        if i - 1 in boarding_passes and i + 1 in boarding_passes:
            missing_seats.append(i)

print(missing_seats)  # <---- RESULT
