// --- Day 11: Cosmic Expansion ---
// You continue following signs for "Hot Springs" and eventually come across an observatory. The Elf within turns out to be a researcher studying cosmic expansion using the giant telescope here.

// He doesn't know anything about the missing machine parts; he's only visiting for this research project. However, he confirms that the hot springs are the next-closest area likely to have people; he'll even take you straight there once he's done with today's observation analysis.

// Maybe you can help him with the analysis to speed things up?

// The researcher has collected a bunch of data and compiled the data into a single giant image (your puzzle input). The image includes empty space (.) and galaxies (#). For example:

// ...#......
// .......#..
// #.........
// ..........
// ......#...
// .#........
// .........#
// ..........
// .......#..
// #...#.....
// The researcher is trying to figure out the sum of the lengths of the shortest path between every pair of galaxies. However, there's a catch: the universe expanded in the time it took the light from those galaxies to reach the observatory.

// Due to something involving gravitational effects, only some space expands. In fact, the result is that any rows or columns that contain no galaxies should all actually be twice as big.

// In the above example, three columns and two rows contain no galaxies:

//    v  v  v
//  ...#......
//  .......#..
//  #.........
// >..........<
//  ......#...
//  .#........
//  .........#
// >..........<
//  .......#..
//  #...#.....
//    ^  ^  ^
// These rows and columns need to be twice as big; the result of cosmic expansion therefore looks like this:

// ....#........
// .........#...
// #............
// .............
// .............
// ........#....
// .#...........
// ............#
// .............
// .............
// .........#...
// #....#.......
// Equipped with this expanded universe, the shortest path between every pair of galaxies can be found. It can help to assign every galaxy a unique number:

// ....1........
// .........2...
// 3............
// .............
// .............
// ........4....
// .5...........
// ............6
// .............
// .............
// .........7...
// 8....9.......
// In these 9 galaxies, there are 36 pairs. Only count each pair once; order within the pair doesn't matter. For each pair, find any shortest path between the two galaxies using only steps that move up, down, left, or right exactly one . or # at a time. (The shortest path between two galaxies is allowed to pass through another galaxy.)

// For example, here is one of the shortest paths between galaxies 5 and 9:

// ....1........
// .........2...
// 3............
// .............
// .............
// ........4....
// .5...........
// .##.........6
// ..##.........
// ...##........
// ....##...7...
// 8....9.......
// This path has length 9 because it takes a minimum of nine steps to get from galaxy 5 to galaxy 9 (the eight locations marked # plus the step onto galaxy 9 itself). Here are some other example shortest path lengths:

// Between galaxy 1 and galaxy 7: 15
// Between galaxy 3 and galaxy 6: 17
// Between galaxy 8 and galaxy 9: 5
// In this example, after expanding the universe, the sum of the shortest path between all 36 pairs of galaxies is 374.

// Expand the universe, then find the length of the shortest path between every pair of galaxies. What is the sum of these lengths?

// import { readFileSync } from 'fs';
// let answer = 0;

// try {
//     const input = readFileSync('input.txt', 'utf8');
//     const lines = input.split("\r\n");
//     let expanded_set = []
//     lines.forEach((line) => {
//         const points = line.split("");
//         if(points.includes("#") == false) {
//             expanded_set.push(points);
//         }
//         expanded_set.push(points);
//     });

//     let flipped = expanded_set[0].map((col,c) => expanded_set.map((row, r) => expanded_set[r][c]));

//     expanded_set = []
//     flipped.forEach((points) => {
//         if(points.includes("#") == false) {
//             expanded_set.push(points);
//         }
//         expanded_set.push(points);
//     });

//     flipped = expanded_set[0].map((col,c) => expanded_set.map((row, r) => expanded_set[r][c]));

//     let galaxies = []
//     let debug = '';
//     for(let r = 0; r < flipped.length; r++) {
//         debug += flipped[r].join('') + "\n";
//         for(let c = 0; c < flipped[0].length; c++) {
//             if(flipped[r][c] == '#') {
//                 galaxies.push([r,c]);
//             }
//         }
//     }
//     //console.log(debug);
//     //console.log(galaxies);

//     for(a = 0; a < galaxies.length - 1; a++) {
//         for(b = a+1; b < galaxies.length; b++) {
//             let dist = Math.abs(galaxies[a][0] - galaxies[b][0]) + Math.abs(galaxies[a][1] - galaxies[b][1]);
//             console.log(a,b,dist);
//             answer+= dist;
//         }
//     }
// }
// catch(e) {
//     console.error(e);
// }

// console.log("The answer is:", answer);

const input = require("fs").readFileSync("input.txt", "utf-8").split(/\r?\n/g);

let adjustedMap = input;
for (let i = 0; i < adjustedMap.length; i++) { if (adjustedMap[i].indexOf("#") == -1) adjustedMap.splice(i, 0, adjustedMap[i++]); }
for (let i = 0; i < adjustedMap[0].length; i++) {
    if (!adjustedMap.reduce((acc, cur) => acc || cur[i] == "#", false)) {
        for (let j = 0; j < adjustedMap.length; j++) adjustedMap[j] = adjustedMap[j].slice(0, i) + "." + adjustedMap[j].slice(i);
        i++;
    }
}

let positions = [];
for (let i = 0; i < adjustedMap.length; i++) { for (let j = 0; j < adjustedMap[i].length; j++) { if (adjustedMap[i][j] == "#") positions.push([i, j]); } }
let pairs = [];
let progress = 0;
for (let i = 0; i < positions.length; i++) {
    console.log(((progress / Math.pow(positions.length, 2)) * 100).toFixed(2) + "% done (" + progress, "/", Math.pow(positions.length, 2) + ")");
    for (let j = 0; j < positions.length; j++) {
        progress++;
        if (i != j && !pairs.filter(pair => pair.indexOf(positions[i]) != -1 && pair.indexOf(positions[j]) != -1).length)
            pairs.push([ positions[i], positions[j] ]);
    }
}

console.log(pairs.map(pair => Math.abs(pair[0][0] - pair[1][0]) + Math.abs(pair[0][1] - pair[1][1])).reduce((acc, x) => acc + x));