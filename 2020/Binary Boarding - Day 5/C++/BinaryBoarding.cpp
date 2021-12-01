#include <iostream>
#include <fstream>
#include <string>
#include <set>

void BinSearch(const char& c, int& min, int& max) {
    int mid = min + max;
    if (c == 'F' || c == 'L') {
        if (mid%2 == 0) {
        max = mid/2 - 1;
    }
    else {
        max = mid/2;
    }
    }
    else if (c == 'B' || c == 'R') {
    if (mid%2 == 0) {
            min = mid/2;
    }
    else {
        min = mid/2 + 1;
    }
    }
}

//To calculate a seat ID we multiple the row by 8 and add the column number, the row and columns are found with a binary search
int GetSeatID(const std::string& line) {
    int minR = 0, maxR = 127; //set the row boundaries
    int minC = 0, maxC = 7; //set the col boundaries
    for (int i=0; i<7; ++i) {
        BinSearch(line[i], minR, maxR);
    }
    for (int i=7; i<line.size(); ++i) {
        BinSearch(line[i], minC, maxC);
    }
    return minR * 8 + minC;
}

int main() {
    std::ifstream file("input.txt"); //read from the input file with a fileStream
    std::string line;
    std::set<int> seats; //int vector for the seats 
    int high = 0;
    if (file.is_open()) {
        while(std::getline(file, line)) {
            int id = GetSeatID(line);
        if (id > high) { //check current ID iteration for current value of highest int
            high = id; //find the max id, per the request in part 1 of the question
        }
        seats.insert(id);
    }
    }
    std::cout<<"Problem 1: "<<high<<std::endl; // output the highest seat ID to COUT
    int mySeat = 0; //initialize variable to hold your seat
    for (auto it = ++seats.begin(); it != --seats.end(); ++it) {
    if (!(*(std::prev(it)) + 1 == *it && *(std::next(it)) - 1 == *it)) { //the question indicates that the Seats with IDs +1 and -1 will exist on the plane, your seat number will be the only missing boarding pass
        mySeat = mySeat == 0 ? *it : (*it + mySeat)/2;
        }
    }
    std::cout<<"Problem 2: "<<mySeat<<std::endl; //output seatNumber to COUT
    return 0;
}