// const util = require("util");
// const fs = require("fs");
// const internal = require("stream");

// function maxLevel(array, level = 0) {
//   return Math.max(
//     ...array.map((item) => {
//       if (Array.isArray(item)) return maxLevel(item, level + 1);
//       return level;
//     })
//   );
// }

// function maxNumber(array) {
//   return Math.max(...array.flat(10));
// }

// class Node {
//   constructor(val, parent) {
//     this.val = val;
//     this.parent = parent;
//   }
// }

// function primitiveToNode(array) {
//   const parent = array.map((item) => {
//     if (Array.isArray(item)) return primitiveToNode(item);
//     return new Node(item);
//   });
//   for (let child of parent) {
//     child.parent = parent;
//   }
//   return parent;
// }

// function nodeToPrimitive(array) {
//   return array.map((item) => {
//     if (Array.isArray(item)) return nodeToPrimitive(item);
//     return item.val;
//   });
// }

// To explode a pair, the pair's left value is added to the first regular number to the left of the exploding pair (if any), and the pair's right value is added to the first regular number to the right of the exploding pair (if any). 
// Exploding pairs will always consist of two regular numbers. Then, the entire exploding pair is replaced with the regular number 0.
// *******************************************************************************************
// function explode(array) {
//   function explodeNode(nodes, level, root, parent = null) {
//     if (level === 4) {
//       const [left, right] = nodes;
//       const flatten = root.flat(10);
//       const leftIndex = flatten.indexOf(left);
//       const rightIndex = flatten.indexOf(right);
//       if (leftIndex > 0) {
//         flatten[leftIndex - 1].val = flatten[leftIndex - 1].val + left.val;
//       }
//       if (rightIndex < flatten.length - 1) {
//         flatten[rightIndex + 1].val = flatten[rightIndex + 1].val + right.val;
//       }
//       parent[parent.indexOf(nodes)] = new Node(0);
//       return root;
//     }

//     for (let value of nodes) {
//       if (Array.isArray(value)) {
//         explodeNode(value, level + 1, root, nodes);
//       }
//     }
//     return root;
//   }

//   const nodes = primitiveToNode(array);
//   nodes.flat(10);
//   root = nodes;

//   return nodeToPrimitive(explodeNode(nodes, 0, root));
// }
// To reduce a snailfish number, you must repeatedly do the first action in this list that applies to the snailfish number:
// If any pair is nested inside four pairs, the leftmost such pair explodes.
// If any regular number is 10 or greater, the leftmost such regular number splits.
// Once no action in the above list applies, the snailfish number is reduced.
// *****************************************************************************************************************
// function split(array) {
//   const tree = primitiveToNode(array);
//   const flatten = tree.flat(10);
//   const over = flatten.find((item) => item.val > 9);
//   if (!over) return nodeToPrimitive(tree);
//   const pair = [
//     new Node(Math.floor(over.val / 2)),
//     new Node(Math.ceil(over.val / 2)),
//   ];
//   const index = over.parent.indexOf(over);
//   over.parent[index] = pair;
//   return nodeToPrimitive(tree);
// }

// function add(n1, n2) {
//   let result = [n1, n2];
//   while (maxLevel(result) === 4 || maxNumber(result) > 9) {
//     result = explode(result);
//     result = split(result);
//   }

//   return result;
// }

// To check whether it's the right answer, the snailfish teacher only checks the magnitude of the final sum.
// The magnitude of a pair is 3 times the magnitude of its left element plus 2 times the magnitude of its right element.
// The magnitude of a regular number is just that number.
// function magnitude(array) {
//   const [left, right] = array;
//   const leftValue = Array.isArray(left) ? magnitude(left) : left;
//   const rightValue = Array.isArray(right) ? magnitude(right) : right;
//   return 3 * leftValue + 2 * rightValue;
// }

// const getInput = (fileName) => {
//   return fs
//     .readFileSync(fileName)
//     .toString("utf-8")
//     .trim()
//     .split("\n")
//     .map((line) => parser.parse(line));
// };

// const part1 = (input) => {
//   return magnitude(input.reduce((a, b) => add(a, b)));
// };

// console.log("Part1");
// console.log(part1(getInput("input.txt")));

// const part2 = (input) => {
//   const combinations = [];
//   for (let i = 0; i < input.length; i++) {
//     for (let j = i + 1; j < input.length; j++) {
//       combinations.push([input[i], input[j]]);
//     }
//   }
//   let largestMagnitude = Number.MIN_SAFE_INTEGER;
//   for (let combination of combinations) {
//     const v1 = magnitude(add(combination[0], combination[1]));
//     const v2 = magnitude(add(combination[1], combination[0]));
//     largestMagnitude = Math.max(v1, v2, largestMagnitude);
//   }
//   return largestMagnitude;
// };

// console.log("Part2");
// console.log(part2(getInput("input.txt")));
//**********************************************************************************************************************
// let input = fs.readFile('input.txt', 'utf8').toString();
// let data = input.split('\n').map(s => s.split(',').join("").trim());
 
// data = data.map(s => {
//     return s.split('').map(s =>isNaN(s)?s:Number(s));
// });
 
// function add(a,b){
//     let c =  ["[",...a,...b,"]"];
//     while(explode(c) || split(c));
//     return c;
// }
 
// function explode(a){
//     let open = 0;
//     for (let i = 0; i < a.length; i++) {
//         const e = a[i];
//         if(e == "[")open++;
//         if(e == "]")open--;
//         if(open == 5){
//             let buf = a.splice(i, 4);
//             let up=i-1;
//             let down=i;
//             while(down--){
//                 if(!isNaN(a[down])){
//                     a[down]+= buf[1];
//                     break;
//                 }
//             }
//             while(up++<a.length){
//                 if(!isNaN(a[up])){
//                     a[up]+= buf[2];
//                     break;
//                 }
//             }
//             a.splice(i, 0,0);
//             explode(a);
//             return true;
//         }
//     }
//     return false;
// }
 
// function split(a){
//     for (let i = 0; i < a.length; i++) {
//         const e = a[i];
//         if(!isNaN(e) && e>9){
//             let l = Math.floor(e/2);
//             let h = Math.ceil(e/2);
//             let s = ['[',l,h,']'];
//             a.splice(i,1,...s);
//             return true;
//         }
//     }
//     return false;
// }
 
// function magnitude (a){
//     for (let i = 0; i < a.length; i++) {
//         const e = a[i];
//         if(e == "]"){
//             let buf = a.splice(i-3, 4);
//             let sum = buf[1]*3 + buf[2]*2;
//             a.splice(i-3,0,sum);
//             i-=3;
//         }
//     }
//     return a;
// }
 
// let sum =  data[0];
// for (let i = 0; i < data.length-1; i++) {
//     sum = add(sum,data[i+1]);
// }
// let mag = magnitude(sum);
// console.log(1,mag[0]);
 
// let max = 0;
// for (let i = 0; i < data.length-1; i++) { 
//     for (let j = 0; j < data.length; j++) {
//         if(i != j){
//             max = Math.max( max, magnitude( add(data[i],data[j])));
//             max = Math.max( max, magnitude( add(data[j],data[i])))
//         }
//     }
// }
// console.log(2,max);
// *********************************************************************************
var fs = require('fs');
const readFileLines = () =>
fs
	.readFileSync('input.txt')
	.toString('UTF8')
	.split('\n');

var input = readFileLines();

function magnitude(pair) {
	pair = eval(pair)
	    const [a, b] = pair.map((n) => (Array.isArray(n) ? magnitude(n) : n));
	        return 3 * a + 2 * b;
  }
function getDepth(line, index) {
	let depth = 0;
	for (let i = 0; i < index; i++) {
	  if (line[i] === '[') depth++;
	    else if (line[i] === ']') depth--;
	}
	return depth;
}
function sum(a1, a2) {
    var num = `[${a1},${a2}]`
        return reduce(num)
}
function split(line, index, length) {
	var num = line.substr(index, length);
	var l = line.substr(0, index);
	var r = line.substr(index + length);
	return `${l}[${Math.floor(num/2)},${Math.ceil(num/2)}]${r}`;
}
function explode(num, index){
    let end=index+num.slice(index).indexOf(']');

    let [left,right]=num.slice(index+1,end).split(",");
    let [strL,strR]=[num.slice(0,index),num.slice(end+1)];
    //left start
    let t=[...strL.matchAll(/\d+/g)],digit="",idx=-1;

    if(t.length>0){
        digit=t[t.length-1][0]

        idx=strL.lastIndexOf(digit)
        strL=strL.slice(0,idx)+((+digit)+(+left))+strL.slice(idx+digit.length)
    }

    t=strR.match(/\d+/),digit="",idx=-1;
    if(t){
        digit=t[0]

        idx=strR.indexOf(digit)
        strR=strR.slice(0,idx)+((+digit)+(+right))+strR.slice(idx+digit.length)
    }
    //right end
    return strL+0+strR
}
function getExplodeIndex(num){

	//loop through each element find the one that is nested into 4
    let n=0;
    for(let i=0;i<num.length;i++){
		if(getDepth(num,i) == 5) return i-1;
    }
	//if not found return -1
	return -1
}
function getSplitIndex(sNum){
	//match 2 numbers together basically a 2digit number
    let t=sNum.match(/\d{2,}/),splNum="",index=-1;
    if(t){
        splNum=t[0]
        index=sNum.indexOf(splNum)
    }
    return {splNum,index}
}
function reduce(num) {
	//keep reducing until nothing happens anymore
	let {splNum,index}=getSplitIndex(num)
    let explosionIndex=getExplodeIndex(num)
    while(index>-1||explosionIndex>-1){
        while(explosionIndex>-1){
			//keep exploding until its done
            num=explode(num,explosionIndex)
            explosionIndex=getExplodeIndex(num)
        }
		
        ({splNum,index}=getSplitIndex(num))
        if(index>-1){
            num=split(num,index,splNum.length)
        }
        explosionIndex=getExplodeIndex(num)
    }
    return num
}

var summed = undefined;
input.forEach((e) => {
	if(!summed) summed = e;
	else summed = sum(summed, e);
})
console.log(magnitude(summed));

// --- Part Two ---
// You notice a second question on the back of the homework assignment:

// What is the largest magnitude you can get from adding only two of the snailfish numbers?

// Note that snailfish addition is not commutative - that is, x + y and y + x can produce different results.

// Again considering the last example homework assignment above:

// [[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]
// [[[5,[2,8]],4],[5,[[9,9],0]]]
// [6,[[[6,2],[5,6]],[[7,6],[4,7]]]]
// [[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]
// [[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]
// [[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]
// [[[[5,4],[7,7]],8],[[8,3],8]]
// [[9,3],[[9,9],[6,[4,9]]]]
// [[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]
// [[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]
// The largest magnitude of the sum of any two snailfish numbers in this list is 3993. This is the magnitude of [[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]] + [[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]], which reduces to [[[[7,8],[6,6]],[[6,0],[7,7]]],[[[7,8],[8,8]],[[7,9],[0,6]]]].

// What is the largest magnitude of any sum of two different snailfish numbers from the homework assignment?
var sums = []; //part 2

var getPermutations = function(list, maxLen) {
    // Copy initial values as arrays
    var perm = list.map(function(val) {
        return [val];
    });
    // Our permutation generator
    var generate = function(perm, maxLen, currLen) {
        // Reached desired length
        if (currLen === maxLen) {
            return perm;
        }
        // For each existing permutation
        for (var i = 0, len = perm.length; i < len; i++) {
            var currPerm = perm.shift();
            // Create new permutation
            for (var k = 0; k < list.length; k++) {
                perm.push(currPerm.concat(list[k]));
            }
        }
        // Recurse
        return generate(perm, maxLen, currLen + 1);
    };
    // Start with size 1 because of initial values
    return generate(perm, maxLen, 1);
};

getPermutations(input, 2).forEach((pair) => {
    if(pair[0] === pair[1]) return;
sums.push(magnitude(sum(pair[0], pair[1])));
});
console.log(sums.sort((a,b)=>b-a)[0]);
