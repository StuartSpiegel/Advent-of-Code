// --- Part Two ---
// The galaxies are much older (and thus much farther apart) than the researcher initially estimated.
// Now, instead of the expansion you did before, make each empty row or column one million times larger. That is, each empty row should be replaced with 1000000 empty rows, and each empty column should be replaced with 1000000 empty columns.
// (In the example above, if each empty row or column were merely 10 times larger, the sum of the shortest paths between every pair of galaxies would be 1030. If each empty row or column were merely 100 times larger, the sum of the shortest paths between every pair of galaxies would be 8410. However, your universe will need to expand far beyond these values.)
// Starting with the same initial image, expand the universe according to these new rules, then find the length of the shortest path between every pair of galaxies. What is the sum of these lengths?

const input = require("fs").readFileSync("input.txt", "utf-8").split(/\r?\n/g);

let expandedMap = input;
for (let i = 0; i < expandedMap.length; i++) { if (expandedMap[i].indexOf("#") == -1) expandedMap.splice(++i, 0, new Array(expandedMap[i].length).fill("$").join("")); }
for (let i = 0; i < expandedMap[0].length; i++) {
    if (!expandedMap.reduce((acc, cur) => acc || cur[i] == "#", false)) {
        for (let j = 0; j < expandedMap.length; j++) expandedMap[j] = expandedMap[j].slice(0, i + 1) + "$" + expandedMap[j].slice(i + 1);
        i++;
    }
}

let positions = [];
for (let i = 0; i < expandedMap.length; i++) { for (let j = 0; j < expandedMap[i].length; j++) { if (expandedMap[i][j] == "#") positions.push([i, j]); } }
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

console.log(pairs.map(pair => {
    let [ y1, x1 ] = pair[0], [ y2, x2 ] = pair[1];
    let dY = 0, dX = 0, delta = 999999;

    while (y1 < y2) {
        if (expandedMap[y1][x1] == "$") dY += delta;
        else dY++;
        y1++;
    }
    while (y1 > y2) {
        if (expandedMap[y1][x1] == "$") dY += delta;
        else dY++;
        y1--;
    }

    while (x1 < x2) {
        if (expandedMap[y1][x1] == "$") dX += delta;
        else dX++;
        x1++;
    }
    while (x1 > x2) {
        if (expandedMap[y1][x1] == "$") dX += delta;
        else dX++;
        x1--;
    }

    return dX + dY;
}).reduce((acc, x) => acc + x));