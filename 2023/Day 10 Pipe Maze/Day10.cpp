// --- Day 10: Pipe Maze ---
// You use the hang glider to ride the hot air from Desert Island all the way up to the floating metal island. This island is surprisingly cold and there definitely aren't any thermals to glide on, so you leave your hang glider behind.

// You wander around for a while, but you don't find any people or animals. However, you do occasionally find signposts labeled "Hot Springs" pointing in a seemingly consistent direction; maybe you can find someone at the hot springs and ask them where the desert-machine parts are made.

// The landscape here is alien; even the flowers and trees are made of metal. As you stop to admire some metal grass, you notice something metallic scurry away in your peripheral vision and jump into a big pipe! It didn't look like any animal you've ever seen; if you want a better look, you'll need to get ahead of it.

// Scanning the area, you discover that the entire field you're standing on is densely packed with pipes; it was hard to tell at first because they're the same metallic silver color as the "ground". You make a quick sketch of all of the surface pipes you can see (your puzzle input).

// The pipes are arranged in a two-dimensional grid of tiles:

// | is a vertical pipe connecting north and south.
// - is a horizontal pipe connecting east and west.
// L is a 90-degree bend connecting north and east.
// J is a 90-degree bend connecting north and west.
// 7 is a 90-degree bend connecting south and west.
// F is a 90-degree bend connecting south and east.
// . is ground; there is no pipe in this tile.
// S is the starting position of the animal; there is a pipe on this tile, but your sketch doesn't show what shape the pipe has.
// Based on the acoustics of the animal's scurrying, you're confident the pipe that contains the animal is one large, continuous loop.

// For example, here is a square loop of pipe:

// .....
// .F-7.
// .|.|.
// .L-J.
// .....
// If the animal had entered this loop in the northwest corner, the sketch would instead look like this:

// .....
// .S-7.
// .|.|.
// .L-J.
// .....
// In the above diagram, the S tile is still a 90-degree F bend: you can tell because of how the adjacent pipes connect to it.

// Unfortunately, there are also many pipes that aren't connected to the loop! This sketch shows the same loop as above:

// -L|F7
// 7S-7|
// L|7||
// -L-J|
// L|-JF
// In the above diagram, you can still figure out which pipes form the main loop: they're the ones connected to S, pipes those pipes connect to, pipes those pipes connect to, and so on. Every pipe in the main loop connects to its two neighbors (including S, which will have exactly two pipes connecting to it, and which is assumed to connect back to those two pipes).

// Here is a sketch that contains a slightly more complex main loop:

// ..F7.
// .FJ|.
// SJ.L7
// |F--J
// LJ...
// Here's the same example sketch with the extra, non-main-loop pipe tiles also shown:

// 7-F7-
// .FJ|7
// SJLL7
// |F--J
// LJ.LJ
// If you want to get out ahead of the animal, you should find the tile in the loop that is farthest from the starting position. Because the animal is in the pipe, it doesn't make sense to measure this by direct distance. Instead, you need to find the tile that would take the longest number of steps along the loop to reach from the starting point - regardless of which way around the loop the animal went.

// In the first example with the square loop:

// .....
// .S-7.
// .|.|.
// .L-J.
// .....
// You can count the distance each tile in the loop is from the starting point like this:

// .....
// .012.
// .1.3.
// .234.
// .....
// In this example, the farthest point from the start is 4 steps away.

// Here's the more complex loop again:

// ..F7.
// .FJ|.
// SJ.L7
// |F--J
// LJ...
// Here are the distances for each tile on that loop:

// ..45.
// .236.
// 01.78
// 14567
// 23...
// Find the single giant loop starting at S. How many steps along the loop does it take to get from the starting position to the point farthest from the starting position?


#include <iostream>
#include <fstream>
#include <vector>
#include <queue>

using namespace std;

struct PipeTile {
    char type;
    int distance;
};

vector<vector<PipeTile>> readInput(const string& filename) {
    ifstream inputFile(filename);
    vector<vector<PipeTile>> maze;

    if (inputFile.is_open()) {
        string line;
        while (getline(inputFile, line)) {
            vector<PipeTile> row;
            for (char c : line) {
                row.push_back({c, -1});
            }
            maze.push_back(row);
        }
        inputFile.close();
    } else {
        cerr << "Unable to open file: " << filename << endl;
        exit(EXIT_FAILURE);
    }

    return maze;
}

void findMainLoop(vector<vector<PipeTile>>& maze, pair<int, int>& start) {
    queue<pair<int, int>> q;
    q.push(start);
    maze[start.first][start.second].distance = 0;

    int dx[] = {-1, 1, 0, 0};
    int dy[] = {0, 0, -1, 1};

    while (!q.empty()) {
        auto current = q.front();
        q.pop();

        for (int i = 0; i < 4; ++i) {
            int newX = current.first + dx[i];
            int newY = current.second + dy[i];

            if (newX >= 0 && newX < maze.size() && newY >= 0 && newY < maze[newX].size() &&
                maze[newX][newY].type != '.' && maze[newX][newY].distance == -1) {
                maze[newX][newY].distance = maze[current.first][current.second].distance + 1;
                q.push({newX, newY});
            }
        }
    }
}

int findFarthestPoint(const vector<vector<PipeTile>>& maze) {
    int farthestDistance = 0;

    for (const auto& row : maze) {
        for (const auto& tile : row) {
            if (tile.type != '.' && tile.distance > farthestDistance) {
                farthestDistance = tile.distance;
            }
        }
    }

    return farthestDistance;
}

int main() {
    vector<vector<PipeTile>> maze = readInput("input.txt");

    pair<int, int> start;
    for (int i = 0; i < maze.size(); ++i) {
        for (int j = 0; j < maze[i].size(); ++j) {
            if (maze[i][j].type == 'S') {
                start = {i, j};
                break;
            }
        }
    }

    findMainLoop(maze, start);

    // Reset distances for tiles in the loop
    for (auto& row : maze) {
        for (auto& tile : row) {
            if (tile.type != '.' && tile.distance != -1) {
                tile.distance %= 4; // Considering the loop
            }
        }
    }

    int farthestDistance = findFarthestPoint(maze);

    cout << "Steps along the loop to the farthest point: " << farthestDistance << endl;

    return 0;
}
