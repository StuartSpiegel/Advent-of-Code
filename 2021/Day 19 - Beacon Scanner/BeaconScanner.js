const fs = require('fs');
const { Scanner } = require('./Scanner');

// Strip the input list and build a map of the scanners 
const input = ('\n' + fs.readFileSync('input.txt', 'utf8')).split('\n--- scanner ').slice(1).map(a => a.split(' ---\n'));

let toScan = [];
//create scanner and read in list of beacons
input.forEach(info => {
	const curr = new Scanner();
	curr.id = Number(info[0]);
	curr.detected = info[1].split('\n').map(a=>a.split(',').map(Number)).filter(a=> a.length === 3);
	toScan.push(curr);
});

const initialScanner = toScan.shift();
const beacons = initialScanner.detected.map(a => [a[0] - initialScanner.detected[0][0],a[1] - initialScanner.detected[0][1],a[2] - initialScanner.detected[0][2] ]);
// while loop builds the actual map - > while there are values to read off of the array --> append to newBeacons
while (toScan.length > 0){
	const newFounds = [];
	for(let i=0; i<toScan.length; i++){
		const newBeacons = toScan[i].getBeaconsIfCommonWith(beacons);
		if(newBeacons.length >= 12){
			newFounds.push(toScan[i]);
			newBeacons.forEach(newBeacon => {
				if(beacons.filter(b => b[0] === newBeacon[0] && b[1] === newBeacon[1] && b[2] === newBeacon[2]).length === 0){
					beacons.push(newBeacon);
				}
			});
		}
	}
	if(newFounds.length > 0){
		newFounds.forEach(newFound => {
			toScan = toScan.filter(s => s.id !==  newFound.id);
		});
	}

}

console.log(beacons.length); //part 1 -- Part 1 of this question really is just counting while checking a condition to enforce

// --- Part Two ---
// Sometimes, it's a good idea to appreciate just how big the ocean is. Using the Manhattan distance, how far apart do the scanners get?
// In the above example, scanners 2 (1105,-1205,1229) and 3 (-92,-2380,-20) are the largest Manhattan distance apart. In total, they are 1197 + 1175 + 1249 = 3621 units apart.
// What is the largest Manhattan distance between any two scanners?
const manhattan = (pos1, pos2) => {
	return Math.abs(pos1[0] - pos2[0]) + Math.abs(pos1[1] - pos2[1]) + Math.abs(pos1[2] - pos2[2]);
};

const ansss = positions.map(a => [a[0] + initialScanner.detected[0][0],a[1] + initialScanner.detected[0][1],a[2] + initialScanner.detected[0][2] ]);
ansss[0] = [0,0,0];

let maxDist = 0;
for(let i=0; i<ansss.length; i++){
	for(let j=0; j<ansss.length; j++){
		if(i !== j)
			maxDist = Math.max(maxDist, manhattan(ansss[i], ansss[j]));
	}
}
console.log(maxDist);