// #include <iostream>
// #include <string>

// int main() {
//     // Read the calibration document line by line
//     std::string line;
//     int totalSum = 0;

//     while (std::getline(std::cin, line)) {
//         // Extract the first and last digits
//         char firstDigit = line.front();
//         char lastDigit = line.back();

//         // Convert characters to integers
//         int firstValue = firstDigit - '0';
//         int lastValue = lastDigit - '0';

//         // Combine the digits to form a two-digit number
//         int calibrationValue = firstValue * 10 + lastValue;

//         // Add the calibration value to the total sum
//         totalSum += calibrationValue;
//     }

//     // Print the sum of all calibration values
//     std::cout << "Sum of calibration values: " << totalSum << std::endl;

//     return 0;
// }

#include <iostream>
#include <string>

int main() {
    // Read the calibration document line by line
    std::string line;
    int totalSum = 0;

    while (std::getline(std::cin, line)) {
        // Extract the first and last digits
        char firstDigit = line.front();
        char lastDigit = line.back();

        // Convert characters to integers
        int firstValue = firstDigit - '0';
        int lastValue = lastDigit - '0';

        // Combine the digits to form a two-digit number
        int calibrationValue = firstValue * 10 + lastValue;

        // Add the calibration value to the total sum
        totalSum += calibrationValue;
    }

    // Print the sum of all calibration values
    std::cout << "Sum of calibration values: " << totalSum << std::endl;

    return 0;
}
