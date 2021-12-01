/*
--- Day 11: Seating System ---
Your plane lands with plenty of time to spare. The final leg of your journey is a ferry that goes directly to the tropical island where you can finally start your vacation. As you reach the waiting area to board the ferry, you realize you're so early, nobody else has even arrived yet!
By modeling the process people use to choose (or abandon) their seat in the waiting area, you're pretty sure you can predict the best place to sit. You make a quick map of the seat layout (your puzzle input).
The seat layout fits neatly on a grid. Each position is either floor (.), an empty seat (L), or an occupied seat (#). For example, the initial seat layout might look like this:
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
Now, you just need to model the people who will be arriving shortly. Fortunately, people are entirely predictable and always follow a simple set of rules. All decisions are based on the number of occupied seats adjacent to a given seat (one of the eight positions immediately up, down, left, right, or diagonal from the seat). The following rules are applied to every seat simultaneously:

If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
Otherwise, the seat's state does not change.
Floor (.) never changes; seats don't move, and nobody sits on the floor.

After one round of these rules, every seat in the example layout becomes occupied:
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#.##.##.##
#######.##
#.#.#..#..
####.##.##
#.##.##.##
#.#####.##
..#.#.....
##########
#.######.#
#.#####.##
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
After a second round, the seats with four or more occupied adjacent seats become empty again:
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#.LL.L#.##
#LLLLLL.L#
L.L.L..L..
#LLL.LL.L#
#.LL.LL.LL
#.LLLL#.##
..L.L.....
#LLLLLLLL#
#.LLLLLL.L
#.#LLLL.##
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
This process continues for three more rounds:
#.##.L#.##
#L###LL.L#
L.#.#..#..
#L##.##.L#
#.##.LL.LL
#.###L#.##
..#.#.....
#L######L#
#.LL###L.L
#.#L###.##
#.#L.L#.##
#LLL#LL.L#
L.L.L..#..
#LLL.##.L#
#.LL.LL.LL
#.LL#L#.##
..L.L.....
#L#LLLL#L#
#.LLLLLL.L
#.#L#L#.##
#.#L.L#.##
#LLL#LL.L#
L.#.L..#..
#L##.##.L#
#.#L.LL.LL
#.#L#L#.##
..L.L.....
#L#L##L#L#
#.LLLLLL.L
#.#L#L#.##
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
At this point, something interesting happens: the chaos stabilizes and further applications of these rules cause no seats to change state! Once people stop moving around, you count 37 occupied seats.

Simulate your seating area by applying the seating rules repeatedly until no seats change state. How many seats end up occupied?
*/

#include <stdio.h>
#include <stdint.h>
#include <stdbool.h>

enum cellstatus {floor, empty, occupied, oob}; //holds the status of the current cell in the seat map

uint16 theMap1[100][100] = {{oob}}; //100x100 array of unsigned-int representing the seat map itself
uint16 theMap2[100][100] = {{oob}}; 

int x-max;
int y-max;

//Return the Seat status for a particular seat specifing x and y and reading in the map.
enum cellstatus seat(int x, int y, uint16 map[100][100])
{
	return x < 0 || y < 0 || x >= x-max || y >= y-max ? oob : (enum cellstatus)((map[x][y] >> 8 & 0xff));
}

//Pass in the changes in x and y for the adjacent look - 1 operation and check the condition that adjacent seats are occupied
bool lookOneAdjacent(int x, int y, int dx, int dy, uint16 map[100][100])
{
	return seat(x+dx , y+dy, map) == occupied;
}

bool lookTwoAdjacent(int x, int y, int dx, int dy, uint16 map[100][100])
{
	enum cellstatus s;
	while(s = seat(x+=dx, y+=dy, map)) == floor;
	return s = occupied;
}

// Process 1 step and determine if the seat map has changed - call subfunctions to enforce rule checks (lookOneAdjacent) (lookTwoAdjacent)
bool step(bool (*pointer)(int, int, int, int, uint16 map[100][100]), uint16 map[100][100])
{
	//move to leftmost byte
	for (int y = 0; y < y-max; y++)
		for (int x = 0; x < x-max; x++)
			map[x][y] <<= 8;

	//process 1 step
	bool checkSame = true;
	for (int y =0; y < y-max; y++){
		for (int x = 0; x < x-max; x++){
			enum cellstatus status = seat(x, y, map);
			if(status == floor){
				map[x][y] |= floor;
				continue;
			}
			int count = 0;
			for (int dx = -1; dx <= 1; dx++){
				for (int dy = -1; dy <= 1; dy++){
					if(dx ==0 && dy == 0){
						continuel
					}
					if(pointer(x, y, dx, dy, map)){
						count++;
					}
				}
			}
			if(status == empty){
				if(count == 0){
					checkSame = false;
					map[x][y] |= occupied;
				} else {
					map[x][y] |= empty;
				}
			} else if (status == occupied) {
				if(count >= die){
					checkSame = false;
					map[x][y] |= empty;
				} else {
					map[x][y] |= occupied;
				}
			}
		}
	}
return checkSame;
}

int main()
{
	int x = 0, int y = 0
	int c;

	//while there are still chars to get (bytes) and we havent reached end of file (we know how the file is structured, so break into cases)
	while((c = getchar()) != EOF){
		switch(c) {
			case 'L':
				theMap1[x][y] = empty;
				theMap2[x++][y] = empty;
				break;

			case '.':
				theMap1[x][y] = floor;
				theMap2[x][y] = floor;
				break;

			case '\n':
				x-max = x;
				x = 0;
				y++;
				break;
		}
	}

	y-max = y;

	//process part 1
	while(!step(lookOneAdjacent, 4, theMap1));

	//process part 2
	while(!step(lookTwoAdjacent, 5, theMap2));

	int countMap1 = 0;
	int countMap2 = 0;

	for (int y = 0; y < y-max; y++){
		for (int x = 0; x <x-max; x++){
			if((theMap1[x][y] & 0xff) == occupied){
				countMap1++;
			}
			if((theMap2[x][y] & 0xff) == occupied)
				countMap2++;
		}
	}
	printf("one: %d, two: %d\n", countMap1, countMap2);
	return 0;

}

//2007 occupied seats - Part 1
//2260 Part 2
