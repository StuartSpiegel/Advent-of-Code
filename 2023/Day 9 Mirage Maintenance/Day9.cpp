// #include <iostream>
// #include <fstream>
// #include <vector>

// std::vector<int> extrapolate(const std::vector<std::vector<int>>& matrix) {
//     std::vector<int> extrapolated_values(matrix[0].size(), 0);

//     for (size_t i = 0; i < matrix.size(); ++i) {
//         for (size_t j = 0; j < matrix[i].size(); ++j) {
//             extrapolated_values[j] += matrix[i][j];
//         }
//     }

//     return extrapolated_values;
// }

// int main() {
//     // Read the matrix from the file
//     std::ifstream infile("input.txt");
//     if (!infile.is_open()) {
//         std::cerr << "Error opening input file." << std::endl;
//         return 1;
//     }

//     std::vector<std::vector<int>> data;
//     int value;
//     while (infile >> value) {
//         data.emplace_back(1, value);
//     }

//     // Perform extrapolation
//     std::vector<int> extrapolated_values = extrapolate(data);

//     // Calculate and print the sum of extrapolated values
//     int result = 0;
//     for (int val : extrapolated_values) {
//         result += val;
//     }

//     std::cout << "Sum of extrapolated values: " << result << std::endl;

//     return 0;
// }

#include <iostream>
#include <fstream>
#include <vector>
#include <cmath>

int main() {
    std::ifstream inputFile("input.txt");

    if (!inputFile.is_open()) {
        std::cerr << "Error opening input file." << std::endl;
        return 1;
    }

    int rows, cols;

    inputFile >> rows >> cols;

    std::vector<std::vector<int>> matrix(rows, std::vector<int>(cols));

    for (int i = 0; i < rows; ++i) {
        for (int j = 0; j < cols; ++j) {
            inputFile >> matrix[i][j];
        }
    }

    inputFile.close();

    long long sum = 0;  // Use long long to handle large sums

    for (int i = 0; i < rows; ++i) {
        for (int j = 0; j < cols; ++j) {
            long long extrapolatedValue = static_cast<long long>(matrix[i][j]) * static_cast<long long>(std::pow(2, i + j));
            sum += extrapolatedValue;
        }
    }

    std::cout << "Sum of extrapolated values: " << sum << std::endl;

    return 0;
}
