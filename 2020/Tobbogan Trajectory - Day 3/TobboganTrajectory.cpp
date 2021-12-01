#include <iostream>
#include <cstring>
#include <fstream>
using namespace std;

int main() {
  ifstream inputFile;
  string line;

  // tree count
  int trees = 0;

  // column iterator
  int col = 0;

  inputFile.open("input.txt");

  while (inputFile >> line) {
    // check column for tree - loops around at end of line
    if (line.at(col % line.length()) == '#') {
      trees++;
    }
    //turn right 3 indicated by the slope value of 3
    col += 3;
  }

  //output to C STDOUT
  cout << trees << endl;

  inputFile.close();
  return 0;
}