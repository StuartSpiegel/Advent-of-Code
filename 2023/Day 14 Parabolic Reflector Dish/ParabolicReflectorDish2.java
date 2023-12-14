// --- Part Two ---
// The parabolic reflector dish deforms, but not in a way that focuses the beam. To do that, you'll need to move the rocks to the edges of the platform. Fortunately, a button on the side of the control panel labeled "spin cycle" attempts to do just that!
// Each cycle tilts the platform four times so that the rounded rocks roll north, then west, then south, then east. After each tilt, the rounded rocks roll as far as they can before the platform tilts in the next direction. After one cycle, the platform will have finished rolling the rounded rocks in those four directions in that order.
// Here's what happens in the example above after each of the first few cycles:
// After 1 cycle:
// .....#....
// ....#...O#
// ...OO##...
// .OO#......
// .....OOO#.
// .O#...O#.#
// ....O#....
// ......OOOO
// #...O###..
// #..OO#....

// After 2 cycles:
// .....#....
// ....#...O#
// .....##...
// ..O#......
// .....OOO#.
// .O#...O#.#
// ....O#...O
// .......OOO
// #..OO###..
// #.OOO#...O

// After 3 cycles:
// .....#....
// ....#...O#
// .....##...
// ..O#......
// .....OOO#.
// .O#...O#.#
// ....O#...O
// .......OOO
// #...O###.O
// #.OOO#...O
// This process should work if you leave it running long enough, but you're still worried about the north support beams. To make sure they'll survive for a while, you need to calculate the total load on the north support beams after 1000000000 cycles.

// In the above example, after 1000000000 cycles, the total load on the north support beams is 64.

// Run the spin cycle for 1000000000 cycles. Afterward, what is the total load on the north support beams?
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class ParabolicReflectorDish2 {

    public static void main(String[] args) {
        try {
            List<String> lines = Files.readAllLines(Paths.get("input.txt"));
            char[][] grid = new char[lines.size()][lines.get(0).length()];

            // Filling the grid with the input
            for (int i = 0; i < lines.size(); i++) {
                grid[i] = lines.get(i).toCharArray();
            }

            Map<String, Integer> seenStates = new HashMap<>();
            int cycle = 0;
            int totalCycles = 1000000000;

            while (cycle < totalCycles) {
                runSpinCycle(grid);
                cycle++;

                String currentState = gridToString(grid);
                if (seenStates.containsKey(currentState)) {
                    int previousCycle = seenStates.get(currentState);
                    int cycleLength = cycle - previousCycle;

                    // Skip the remaining cycles by calculating the equivalent cycle number
                    while (cycle + cycleLength < totalCycles) {
                        cycle += cycleLength;
                    }
                } else {
                    seenStates.put(currentState, cycle);
                }
            }

            // Calculating the load
            int load = calculateLoad(grid);
            System.out.println("Total load on the north support beams after " + totalCycles + " cycles: " + load);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    private static void runSpinCycle(char[][] grid) {
        tiltPlatform(grid, Direction.NORTH);
        tiltPlatform(grid, Direction.WEST);
        tiltPlatform(grid, Direction.SOUTH);
        tiltPlatform(grid, Direction.EAST);
    }

    private static void tiltPlatform(char[][] grid, Direction direction) {
        switch (direction) {
            case NORTH:
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
                break;
            case WEST:
                for (int row = 0; row < grid.length; row++) {
                    for (int col = 0; col < grid[row].length; col++) {
                        if (grid[row][col] == 'O') {
                            int targetCol = col;
                            while (targetCol > 0 && grid[row][targetCol - 1] == '.') {
                                targetCol--;
                            }
                            if (targetCol != col) {
                                grid[row][targetCol] = 'O';
                                grid[row][col] = '.';
                            }
                        }
                    }
                }
                break;
            case SOUTH:
                for (int col = 0; col < grid[0].length; col++) {
                    for (int row = grid.length - 1; row >= 0; row--) {
                        if (grid[row][col] == 'O') {
                            int targetRow = row;
                            while (targetRow < grid.length - 1 && grid[targetRow + 1][col] == '.') {
                                targetRow++;
                            }
                            if (targetRow != row) {
                                grid[targetRow][col] = 'O';
                                grid[row][col] = '.';
                            }
                        }
                    }
                }
                break;
            case EAST:
                for (int row = 0; row < grid.length; row++) {
                    for (int col = grid[row].length - 1; col >= 0; col--) {
                        if (grid[row][col] == 'O') {
                            int targetCol = col;
                            while (targetCol < grid[row].length - 1 && grid[row][targetCol + 1] == '.') {
                                targetCol++;
                            }
                            if (targetCol != col) {
                                grid[row][targetCol] = 'O';
                                grid[row][col] = '.';
                            }
                        }
                    }
                }
                break;
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

    private static String gridToString(char[][] grid) {
        StringBuilder sb = new StringBuilder();
        for (char[] row : grid) {
            sb.append(new String(row));
            sb.append("\n");
        }
        return sb.toString();
    }

    enum Direction {
        NORTH, WEST, SOUTH, EAST
    }
}
