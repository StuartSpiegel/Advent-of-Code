#include <iostream>
#include <vector>
#include <string>

int main(int argc, char** argv) { //2D array of char
  std::string line;
  std::vector<std::string> lines;
  while (std::cin >> line) { //read the lines from the file
    lines.push_back(std::move(line)); //increment the line
  }
  int product = 1; //initialize the product variable
  std::vector<std::pair<int, int>> slopes =  {{1, 1}, {3, 1}, {5, 1}, {7, 1}, {1, 2}}; //save slopes as Vectors
  for (auto [right, down] : slopes) { //save the vector movement patterns (A Vector has direction, i.e. in this case right and down: {right, down}
    int count = 0; //initialize the counters
    for (int i = 1; i * down < lines.size(); ++i) { //iterate the rows moving <V> -<down>
      if (lines[i * down][i * right % lines[i].size()] == '#') { //check for trees on the current line
        count++; //if tree found increment the counter
      }
    }
    product *= count; //in each row get the product of the total number of trees encountered in each slope iteration 
  }
  std::cout << "Num trees: " << product;
  return 0;
}

