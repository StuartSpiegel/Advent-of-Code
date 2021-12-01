

#include <iostream>
#include <fstream>
#include <vector>
#include <sstream>

typedef unsigned long u_long;

u_long solve_equation_1(std::string equation);
u_long solve_equation_2(std::string equation);

void reduce_parentheses(std::string &equation, int part) {
    bool contains_parentheses{true};
    while (contains_parentheses) { //Solve each outer parentheses first
        contains_parentheses = false;
        int left, right;
        int p_level{0};
        int i{0};
        for (char c : equation) {
            if (c == '(') {
                if (p_level == 0) {
                    left = i;
                }
                contains_parentheses = true;
                p_level++;
            } else if (c == ')') {
                p_level--;
                if (p_level == 0) {
                    right = i;
                }
            }
            i++;
        }
        if (contains_parentheses) {
            std::string left_of = equation.substr(0,left); //Left of parantheses, including spaces
            std::string right_of = equation.substr(right+1); //Right of parentheses, including spaces
            std::string inside = equation.substr(left+1, right-left-1); //Inside of parentheses, parentheses not included
            if (part == 1) {
                equation = left_of + std::to_string(solve_equation_1(inside)) + right_of; //Reduce the parentheses by recursive call of solver
            } else {
                equation = left_of + std::to_string(solve_equation_2(inside)) + right_of; //Reduce the parentheses by recursive call of solver
            }

        }
    }
}

u_long solve_equation_1(std::string equation) {
    reduce_parentheses(equation, 1);

    std::stringstream parser; parser << equation;
    u_long current_value{0};
    parser >> current_value; //Extract the first value from the equation
    while (parser) { //Sine the parenthese were removed, the remaining string is an operation followed by a number
        char new_op;
        u_long new_num;
        parser >> new_op;
        parser >> new_num;
        if (parser.fail()) break;

        switch (new_op) {
            case '+':
                current_value += new_num;
                break;
            case '*':
                current_value *= new_num;
                break;
        }
    }
    return current_value;
}
u_long solve_equation_2(std::string equation) {
    reduce_parentheses(equation, 2);

    std::stringstream parser; parser << equation;
    u_long current_value{0};
    std::vector<u_long> sums{};
    parser >> current_value; //Extract the first value from the equation
    while (parser) { //Sine the parenthese were removed, the remaining string is an operation followed by a number
        char new_op;
        u_long new_num;
        parser >> new_op;
        parser >> new_num;
        if (parser.fail()) break;

        switch (new_op) {
            case '+':
                current_value += new_num;
                break;
            case '*':
                sums.push_back(current_value);
                current_value = new_num;
                break;
        }
    }
    for (u_long n : sums) {
        current_value *= n;
    }

    return current_value;
}


int main() {

    //Open file
    std::ifstream input{"input.txt"};
    if (!input) {
        std::cout << "Could not open input file 'input.txt'!";
        return 1;
    }


    u_long answer_1{0};
    u_long answer_2{0};

    std::string line;

    while (input) {
        std::getline(input, line);
        if (input.fail()) break;

        answer_1 += solve_equation_1(line);
        answer_2 += solve_equation_2(line);

    }


    std::cout << "Answer 1: " << answer_1 << "\n";
    std::cout << "Answer 2: " << answer_2 << "\n";

    return 0;
}