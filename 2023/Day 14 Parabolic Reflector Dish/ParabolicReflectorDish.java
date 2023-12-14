// --- Day 14: Parabolic Reflector Dish ---
// You reach the place where all of the mirrors were pointing: a massive parabolic reflector dish attached to the side of another large mountain.

// The dish is made up of many small mirrors, but while the mirrors themselves are roughly in the shape of a parabolic reflector dish, each individual mirror seems to be pointing in slightly the wrong direction. If the dish is meant to focus light, all it's doing right now is sending it in a vague direction.

// This system must be what provides the energy for the lava! If you focus the reflector dish, maybe you can go where it's pointing and use the light to fix the lava production.

// Upon closer inspection, the individual mirrors each appear to be connected via an elaborate system of ropes and pulleys to a large metal platform below the dish. The platform is covered in large rocks of various shapes. Depending on their position, the weight of the rocks deforms the platform, and the shape of the platform controls which ropes move and ultimately the focus of the dish.

// In short: if you move the rocks, you can focus the dish. The platform even has a control panel on the side that lets you tilt it in one of four directions! The rounded rocks (O) will roll when the platform is tilted, while the cube-shaped rocks (#) will stay in place. You note the positions of all of the empty spaces (.) and rocks (your puzzle input). For example:

// O....#....
// O.OO#....#
// .....##...
// OO.#O....O
// .O.....O#.
// O.#..O.#.#
// ..O..#O..O
// .......O..
// #....###..
// #OO..#....
// Start by tilting the lever so all of the rocks will slide north as far as they will go:

// OOOO.#.O..
// OO..#....#
// OO..O##..O
// O..#.OO...
// ........#.
// ..#....#.#
// ..O..#.O.O
// ..O.......
// #....###..
// #....#....
// You notice that the support beams along the north side of the platform are damaged; to ensure the platform doesn't collapse, you should calculate the total load on the north support beams.

// The amount of load caused by a single rounded rock (O) is equal to the number of rows from the rock to the south edge of the platform, including the row the rock is on. (Cube-shaped rocks (#) don't contribute to load.) So, the amount of load caused by each rock in each row is as follows:

// OOOO.#.O.. 10
// OO..#....#  9
// OO..O##..O  8
// O..#.OO...  7
// ........#.  6
// ..#....#.#  5
// ..O..#.O.O  4
// ..O.......  3
// #....###..  2
// #....#....  1
// The total load is the sum of the load caused by all of the rounded rocks. In this example, the total load is 136.

// Tilt the platform so that the rounded rocks all roll north. Afterward, what is the total load on the north support beams?

// import java.nio.file.Files;
// import java.nio.file.Paths;
// import java.util.List;

// public class ParabolicReflectorDish {

//     public static void main(String[] args) {
//         try {
//             List<String> lines = Files.readAllLines(Paths.get("input.txt"));
//             char[][] grid = new char[lines.size()][lines.get(0).length()];

//             // Filling the grid with the input
//             for (int i = 0; i < lines.size(); i++) {
//                 grid[i] = lines.get(i).toCharArray();
//             }

//             // Tilting the platform north
//             tiltPlatformNorth(grid);

//             // Calculating the load
//             int load = calculateLoad(grid);
//             System.out.println("Total load on the north support beams: " + load);
//         } catch (Exception e) {
//             e.printStackTrace();
//         }
//     }

//     private static void tiltPlatformNorth(char[][] grid) {
//         for (int col = 0; col < grid[0].length; col++) {
//             int emptyRow = -1;
//             for (int row = 0; row < grid.length; row++) {
//                 if (grid[row][col] == 'O' && emptyRow != -1) {
//                     // Move the rounded rock up
//                     grid[emptyRow][col] = 'O';
//                     grid[row][col] = '.';
//                     emptyRow++;
//                 } else if (grid[row][col] == '.') {
//                     // Update the topmost empty row
//                     if (emptyRow == -1) {
//                         emptyRow = row;
//                     }
//                 }
//             }
//         }
//     }

//     private static int calculateLoad(char[][] grid) {
//         int totalLoad = 0;
//         for (int row = 0; row < grid.length; row++) {
//             for (int col = 0; col < grid[row].length; col++) {
//                 if (grid[row][col] == 'O') {
//                     totalLoad += grid.length - row;
//                 }
//             }
//         }
//         return totalLoad;
//     }
// }

import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.List;

public class ParabolicReflectorDish {

    public static void main(String[] args) {
        try {
            List<String> lines = Files.readAllLines(Paths.get("input.txt"));
            char[][] grid = new char[lines.size()][lines.get(0).length()];

            // Filling the grid with the input
            for (int i = 0; i < lines.size(); i++) {
                grid[i] = lines.get(i).toCharArray();
            }

            // Tilting the platform north
            tiltPlatformNorth(grid);

            // Calculating the load
            int load = calculateLoad(grid);
            System.out.println("Total load on the north support beams: " + load);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    private static void tiltPlatformNorth(char[][] grid) {
        for (int col = 0; col < grid[0].length; col++) {
            for (int row = 0; row < grid.length; row++) {
                if (grid[row][col] == 'O') {
                    int targetRow = row;
                    while (targetRow > 0 && grid[targetRow - 1][col] == '.') {
                        targetRow--;
                    }
                    if (targetRow != row) {
                        grid[targetRow][col] = 'O';
                        grid[row][col] = '.';
                    }
                }
            }
        }
    }

    private static int calculateLoad(char[][] grid) {
        int totalLoad = 0;
        for (int row = 0; row < grid.length; row++) {
            for (int col = 0; col < grid[row].length; col++) {
                if (grid[row][col] == 'O') {
                    totalLoad += grid.length - row;
                }
            }
        }
        return totalLoad;
    }
}

