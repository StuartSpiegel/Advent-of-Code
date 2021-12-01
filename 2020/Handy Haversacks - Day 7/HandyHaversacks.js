
// Get input data from page
const rows = $('pre').innerText.split('\n').filter(row => row.length)
const obj = {}
// Create object of every possible container bag color: containee bag color
rows.forEach(row => {
    const rule = row.split("bags contain")
    obj[rule[0].trim()] = rule[1]
        .split(",")
        .map(bag => bag
                .replace(/bags? ?|contains? ?|[0-9] ?|\./g, '')
                .trim()
        )
})

// Create `containers` object to hold all containers at each level.
// Returns number of uniquely colored found container (bag) colors
const countContainers = color => {
    let i = 1
    let containers = {
        0: [color],
        1: [],
    }
    let result = []
    while (true) {
        for (rule in obj) {
            containers[i-1].forEach(c => {
                if (obj[rule].includes(c)) {
                    containers[i].push(rule)
                }
            })
        }
        if (containers[i].length == 0) {
            break
        }
        result.push(containers[i])
        i += 1
        containers[i] = []
    }
    return new Set(result.flat().sort())
}

// returns # of container bags, not including input color, PART 1
countContainers("shiny gold")


//Part 2 -------------------------------------------------------------------------------------------
const fs = require("fs");
let input = fs.readFileSync("input.txt", "utf8").split("\r\n"); //read in from the file

const ints = "1234567890"; //number of bags per level can only be (0-9)

let graph = {}; //our data structure

for (line of input) { //build the graph - line by line
let parent = line.split(" bags contain ")[0]; //parent nodes contain a bag inside them
let childUnprocessed = line.split(" bags contain ")[1].split(" ");

let children = [];

for (let i = 0; i < childUnprocessed.length; i++) { //iterate over all bags (objects) that do not have a child node in the graph (processing)
    const num = childUnprocessed[i]; //we can just add these to our list because they are leaf nodes in the graph (have no children)
    if (ints.includes(num)) {
    let nextChild = childUnprocessed[i + 1] + " " + childUnprocessed[i + 2]; //check for children nodes at the curr level
    children.push([nextChild, num]);
    }
}
graph[parent] = children; //reset so that the current parent is the last nodes child
}

let numBags = -1;
let queue = [["shiny gold", 1]]; //we start with a shiny gold bag

while (queue.length > 0) { //while the input still exists - DO
let currNode = queue.shift(); //advance the queue , select a new parent node
let [currBag, num] = currNode;

numBags += num; //append the number of bags at the current level to the bag list

let subBags = graph[currBag]; //the subbags (subgraph) are the current nodes children
subBags.forEach((currentSub) => {
    let [subBag, subNum] = currentSub; //recursion
    subNum *= num; //how many sub bags were there at the current level 
    queue.push([subBag, subNum]); //advance the queue, move to the next node in the graph
});
}

console.log('total bags', numBags); //return the final sum of bags required 
//158,493