// --- Day 13: Point of Incidence ---
// With your help, the hot springs team locates an appropriate spring which launches you neatly and precisely up to the edge of Lava Island.

// There's just one problem: you don't see any lava.

// You do see a lot of ash and igneous rock; there are even what look like gray mountains scattered around. After a while, you make your way to a nearby cluster of mountains only to discover that the valley between them is completely full of large mirrors. Most of the mirrors seem to be aligned in a consistent way; perhaps you should head in that direction?

// As you move through the valley of mirrors, you find that several of them have fallen from the large metal frames keeping them in place. The mirrors are extremely flat and shiny, and many of the fallen mirrors have lodged into the ash at strange angles. Because the terrain is all one color, it's hard to tell where it's safe to walk or where you're about to run into a mirror.

// You note down the patterns of ash (.) and rocks (#) that you see as you walk (your puzzle input); perhaps by carefully analyzing these patterns, you can figure out where the mirrors are!

// For example:

// #.##..##.
// ..#.##.#.
// ##......#
// ##......#
// ..#.##.#.
// ..##..##.
// #.#.##.#.

// #...##..#
// #....#..#
// ..##..###
// #####.##.
// #####.##.
// ..##..###
// #....#..#
// To find the reflection in each pattern, you need to find a perfect reflection across either a horizontal line between two rows or across a vertical line between two columns.

// In the first pattern, the reflection is across a vertical line between two columns; arrows on each of the two columns point at the line between the columns:

// 123456789
//     ><   
// #.##..##.
// ..#.##.#.
// ##......#
// ##......#
// ..#.##.#.
// ..##..##.
// #.#.##.#.
//     ><   
// 123456789
// In this pattern, the line of reflection is the vertical line between columns 5 and 6. Because the vertical line is not perfectly in the middle of the pattern, part of the pattern (column 1) has nowhere to reflect onto and can be ignored; every other column has a reflected column within the pattern and must match exactly: column 2 matches column 9, column 3 matches 8, 4 matches 7, and 5 matches 6.

// The second pattern reflects across a horizontal line instead:

// 1 #...##..# 1
// 2 #....#..# 2
// 3 ..##..### 3
// 4v#####.##.v4
// 5^#####.##.^5
// 6 ..##..### 6
// 7 #....#..# 7
// This pattern reflects across the horizontal line between rows 4 and 5. Row 1 would reflect with a hypothetical row 8, but since that's not in the pattern, row 1 doesn't need to match anything. The remaining rows match: row 2 matches row 7, row 3 matches row 6, and row 4 matches row 5.

// To summarize your pattern notes, add up the number of columns to the left of each vertical line of reflection; to that, also add 100 multiplied by the number of rows above each horizontal line of reflection. In the above example, the first pattern's vertical line has 5 columns to its left and the second pattern's horizontal line has 4 rows above it, a total of 405.

// Find the line of reflection in each of the patterns in your notes. What number do you get after summarizing all of your notes?

#include <chrono>
#include <iostream>
#include <string>
#include <vector>

int main()
{
    auto const begin{std::chrono::high_resolution_clock::now()};

    std::string line;
    std::vector<uint32_t> rows;
    std::vector<uint32_t> cols;
    uint32_t p1{};
    uint32_t p2{};
    while (!std::cin.eof()) {
        std::getline(std::cin, line);
        if (line == "") {
            auto const process = [&](auto const& cols_or_rows, auto const factor) {
                for (auto m{0}; m < cols_or_rows.size() - 1; ++m) {
                    uint32_t diffs{};
                    for (auto c0 = m, c1 = m + 1; c0 >= 0 && c1 < cols_or_rows.size(); --c0, ++c1) {
                        diffs += __builtin_popcount(cols_or_rows[c0] ^ cols_or_rows[c1]);
                    }
                    p1 += (diffs == 0) * (m + 1) * factor;
                    p2 += (diffs == 1) * (m + 1) * factor;
                }
            };
            process(rows, 100);
            process(cols, 1);
            rows.clear();
            cols.clear();
        } else {
            if (cols.size() == 0) {
                cols.resize(line.length());
            }
            uint32_t row{};
            auto const j{rows.size()};
            for (auto i{0U}; i < line.length(); ++i) {
                uint32_t const cond = line[i] == '#';
                row |= cond << i;
                cols[i] |= cond << j;
            }
            rows.push_back(row);
        }
    }
    std::cout << p1 << std::endl;
    std::cout << p2 << std::endl;

    auto const end{std::chrono::high_resolution_clock::now()};
    std::cout << (end - begin).count() << " ns\n";
}