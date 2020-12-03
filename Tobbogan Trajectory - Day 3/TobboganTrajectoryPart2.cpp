#include <iostream>
#include <cstring>
#include <fstream>
using namespace std;

int main() {
  ifstream inputFile;
  string line;

  // current line number
  int lineNum = 0;

  // tree counts
  int trees[5] = { 0 };

  // column iterators
  int cols[5] = { 0 };

  // changes in columns
  int slopesRight[5] = { 1, 3, 5, 7, 1 };

  // changes in rows
  int slopesDown[5] = { 1, 1, 1, 1, 2 };

  inputFile.open("input.txt");

  while (inputFile >> line) {
    // check slopes
    for (int i = 0; i < 5; ++i) {
      // check only even rows when slope down is 2
      if (lineNum % slopesDown[i] == 0) {
        // check if tree in path
        if (line.at(cols[i] % line.length()) == '#') {
          trees[i]++;
        }
        // increment column iterators
        cols[i] += slopesRight[i];
      }
    }
    // increment line count
    lineNum++;
  }

  long int product = 1;

  for (int i = 0; i < 5; ++i) {
    product *= trees[i];
  }

  cout << product << endl;

  inputFile.close();
  return 0;
}