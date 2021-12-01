# --- Part Two --- Now that you've identified which tickets contain invalid values, discard those tickets entirely.
# Use the remaining valid tickets to determine which field is which.
#
# Using the valid ranges for each field, determine what order the fields appear on the tickets. The order is
# consistent between all tickets: if seat is the third field, it is the third field on every ticket, including your
# ticket.
#
# For example, suppose you have the following notes:
#
# class: 0-1 or 4-19
# row: 0-5 or 8-19
# seat: 0-13 or 16-19
#
# your ticket:
# 11,12,13
#
# nearby tickets: 3,9,18 15,1,5 5,14,9 Based on the nearby tickets in the above example, the first position must be
# row, the second position must be class, and the third position must be seat; you can conclude that in your ticket,
# class is 12, row is 11, and seat is 13.
#
# Once you work out which field is which, look for the six fields on your ticket that start with the word departure.
# What do you get if you multiply those six values together?
#


class Ticket:
    def __init__(self, init_line):
        self.values = []
        for val in init_line.split(","):
            self.values.append(int(val))


class Field:
    def __init__(self, departure, lower, higher):
        self.departure = departure
        self.lower = lower
        self.higher = higher
        self.valid_positions = []
        self.pos = -1


def part_2():
    file = open('input.txt', 'r')
    fields = []  # stores field values per ticket
    tickets = []  # stores our tickets

    for line in file:
        line = line.strip('\n')
        if line == "":
            break  # if the line is blank - stop
        theValues = line.split(":")[1].split(" or ")  # otherwise split the fields into a list
        curr_field = Field("departure" in line.split(":")[0],
                           [int(theValues[0].split("-")[0]), int(theValues[0].split("-")[1])],
                           [int(theValues[1].split("-")[0]), int(theValues[1].split("-")[1])])
        fields.append(curr_field)  # append the fields that start "departure" to curr_fields

    file.readline()
    my_ticket = Ticket(file.readline())
    tickets.append(my_ticket)
    file.readline()
    file.readline()

    invalid_sum = 0

    for line in file:
        line = line.strip('\n')
        bad_ticket = False
        current_ticket = Ticket(line)
        for val_string in line.split(","):
            val = int(val_string)
            bad_val = True
            for field in fields:
                if field.lower[0] <= val <= field.lower[1] or field.higher[0] <= val <= field.higher[1]:  # enforce
                    # fields range policy per ticket
                    bad_val = False
                    break
            if bad_val:  # If we have a bad ticket add its field value to be summed (val_string)
                invalid_sum += val
                bad_ticket = True
                break
        if bad_ticket is False:
            tickets.append(current_ticket)  # if the ticket is good add it to the list of tickets

    num_of_positions = len(fields)  # the number of field positions on a ticket per ticket

    for field in fields:
        for pos in range(num_of_positions):  # Iterate over all fields in a ticket
            valid_position_for_current_range = True
            for ticket in tickets:
                if not ((field.lower[0] <= ticket.values[pos] <= field.lower[1]) or (  # Determine the order of the
                        # fields in your ticket list
                        field.higher[0] <= ticket.values[pos] <= field.higher[1])):
                    valid_position_for_current_range = False
                    break
            if valid_position_for_current_range:
                field.valid_positions.append(pos)  # If that field position is valid add it to our valid fields list

    change = True

    while change:
        change = False
        for field in fields:
            if len(field.valid_positions) == 1:
                change = True
                pos_to_remove = field.valid_positions[0]
                field.pos = pos_to_remove
                for neighbor in fields:
                    if pos_to_remove in neighbor.valid_positions:
                        neighbor.valid_positions.remove(pos_to_remove)

    answer = 1
    for field in fields:
        if field.departure:  # look for the fields on your ticket that start with the word departure
            answer *= my_ticket.values[field.pos]  # multiply those 6 values together and return

    return answer


print(part_2())
