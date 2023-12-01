# --- Day 1: Trebuchet?! ---
# Something is wrong with global snow production, and you've been selected to take a look. The Elves have even given you a map; on it, they've used stars to mark the top fifty locations that are likely to be having problems.

# You've been doing this long enough to know that to restore snow operations, you need to check all fifty stars by December 25th.

# Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!

# You try to ask why they can't just use a weather machine ("not powerful enough") and where they're even sending you ("the sky") and why your map looks mostly blank ("you sure ask a lot of questions") and hang on did you just say the sky ("of course, where do you think snow comes from") when you realize that the Elves are already loading you into a trebuchet ("please hold still, we need to strap you in").

# As they're making the final adjustments, they discover that their calibration document (your puzzle input) has been amended by a very young Elf who was apparently just excited to show off her art skills. Consequently, the Elves are having trouble reading the values on the document.

# The newly-improved calibration document consists of lines of text; each line originally contained a specific calibration value that the Elves now need to recover. On each line, the calibration value can be found by combining the first digit and the last digit (in that order) to form a single two-digit number.

# For example:

# 1abc2
# pqr3stu8vwx
# a1b2c3d4e5f
# treb7uchet
# In this example, the calibration values of these four lines are 12, 38, 15, and 77. Adding these together produces 142.

# Consider your entire calibration document. What is the sum of all of the calibration values?

def extract_calibration_values(document):
    total_sum = 0 # counter to hold the total sum

    for line in document:
        first_digit = None
        last_digit = None

        # Find the first digit
        for char in line:
            if char.isdigit():
                first_digit = char
                break

        # Find the last digit
        for char in reversed(line):
            if char.isdigit():
                last_digit = char
                break

        # If both digits are found, add to the total sum
        if first_digit is not None and last_digit is not None:
            calibration_value = int(first_digit + last_digit)
            total_sum += calibration_value

    return total_sum

def main():
    # Get the file path from the user
    file_path = input("Enter the path to the calibration document text file: ")

    try:
        with open(file_path, 'r') as file:
            # Read the calibration document from the file
            calibration_document = file.readlines()

        # Calculate the sum of calibration values
        result = extract_calibration_values(calibration_document)

        # Print the result
        print("The sum of all calibration values is:", result)

    except FileNotFoundError:
        print("File not found. Please provide a valid file path.")

if __name__ == "__main__":
    main()
