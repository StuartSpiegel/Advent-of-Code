#include <iostream>
#include <string>
#include <cctype>

int main() {
    // Read the calibration document line by line
    std::string line;
    int totalSum = 0;

    while (std::getline(std::cin, line)) {
        // Extract the first and last digits (considering spelled-out digits)
        char firstDigit = '\0', lastDigit = '\0';
        bool foundFirstDigit = false;

        for (char character : line) {
            if (std::isalpha(character)) {
                if (!foundFirstDigit) {
                    firstDigit = character;
                    foundFirstDigit = true;
                }
                lastDigit = character;
            } else if (std::isdigit(character)) {
                if (!foundFirstDigit) {
                    firstDigit = character;
                    foundFirstDigit = true;
                }
                lastDigit = character;
            }
        }

        // Convert characters to integers
        int firstValue = 0, lastValue = 0;

        if (std::isdigit(firstDigit)) {
            firstValue = firstDigit - '0';
        } else if (std::isalpha(firstDigit)) {
            firstValue = std::tolower(firstDigit) - 'a' + 1;
        }

        if (std::isdigit(lastDigit)) {
            lastValue = lastDigit - '0';
        } else if (std::isalpha(lastDigit)) {
            lastValue = std::tolower(lastDigit) - 'a' + 1;
        }

        // Combine the digits to form a two-digit number
        int calibrationValue = firstValue * 10 + lastValue;

        // Add the calibration value to the total sum
        totalSum += calibrationValue;
    }

    // Print the sum of all calibration values
    std::cout << "Sum of calibration values: " << totalSum << std::endl;

    return 0;
}
