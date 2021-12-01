
/*
Advent of code 2020: Day 1 : Report Pair Problem 

--- Day 1: Report Repair ---
After saving Christmas five years in a row, you've decided to take a vacation at a nice resort on a tropical island. Surely, Christmas will go on without you.
The tropical island has its own currency and is entirely cash-only. The gold coins used there have a little picture of a starfish; the locals just call them stars. None of the currency exchanges seem to have heard of them, but somehow, you'll need to find fifty of these coins by the time you arrive so you can pay the deposit on your room.
To save your vacation, you need to get all fifty stars by December 25th.
Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!
Before you leave, the Elves in accounting just need you to fix your expense report (your puzzle input); apparently, something isn't quite adding up.
Specifically, they need you to find the two entries that sum to 2020 and then multiply those two numbers together.

For example, suppose your expense report contained the following:
1721
979
366
299
675
1456
In this list, the two entries that sum to 2020 are 1721 and 299. Multiplying them together produces 1721 * 299 = 514579, so the correct answer is 514579.
Of course, your expense report is much larger. Find the two entries that sum to 2020; what do you get if you multiply them together?

- This problem is a restructuring / Reconfiguration of the classic 2-Sum problem in Mathematics: Given an array of integers, find two numbers such that they sum to a specific target number

*/


public class TwoSum {
	
public static int[] twoSum(int[] input, int target) {
	for (int i = 0; i < input.length; i++){
		int first = input[i]; //set the first comparator to the first element in the array for brute force check against remaining options O(N^2).
		for (int k = i + 1; k < input.length; k++){
			int second = input[k]; //set the second comparator using window sliding/increment
			int total = first + second; //find the sum of the comparator elements

			if(total == target) { //do the actual comparison to our passed target int
				System.out.println(first); //debug
				System.out.println(second); //debug
				return new int[] {i + 1, k + 1};
			}
		}
	}
	
	return null;
}


public static int[] threeSum(int[] input, int target) {
	for (int i = 0; i < input.length; i++){
		int first = input[i]; //set the first comparator to the first element in the array for brute force check against remaining options O(N^2).
		for (int k = i + 1; k < input.length; k++){
			int second = input[k]; //set the second comparator using window sliding/increment
			for (int j = k + 1; j < input.length; j++) {
				int third = input[j];
			
			
			int total = first + second + third; //find the sum of the comparator elements

			if(total == target) { //do the actual comparison to our passed target int
				System.out.println(first); //debug
				System.out.println(second); //debug
				System.out.println(third); //debug
				return new int[] {i + 1, k + 1, j + 1};
			}
			}
		}
	}
	
	return null;
	
}




public static void main(String args[]) {
	
	int [] theInput = {1293,1207,1623,1675,1842,1410,85,1108,557,1217,1506,1956,1579,1614,1360,1544,1946,1666,1972,1814,1699,1778,1529,2002,1768,1173,1407,1201,1264,1739,1774,1951,1980,1428,1381,1714,884,1939,1295,1694,1168,1971,1352,1462,1828,1402,1433,1542,1144,1331,1427,1261,1663,1820,1570,1874,1486,1613,1769,1721,1753,1142,1677,2010,1640,1465,1171,534,1790,2005,1604,1891,1247,1281,1867,1403,2004,1668,1416,2001,1359,686,1965,1728,1551,1565,1128,1832,1757,1350,1808,1711,1799,1590,1989,1547,1140,1905,1368,1179,1902,1473,1908,1859,1257,1394,1244,1800,1695,1731,1474,1781,1885,1154,1990,1929,1193,1302,1831,1226,1418,1400,1435,1645,1655,1843,1227,1481,1754,1290,1685,1498,71,1286,1137,1288,1758,1987,1471,1839,1545,1682,1615,1475,1849,1985,1568,1795,1184,1863,1362,1271,1802,1944,1821,1880,1788,1733,1150,1314,1727,1434,1833,1312,1457,160,1629,1967,1505,1239,1266,1838,1687,1630,1591,1893,1450,1234,1755,1523,1533,1499,1865,1725,1444,1517,1167,1738,1519,1263,1901,1627,1644,1771,1812,1270,1497,1707,1708,1396};
	
	//twoSum(theInput, 2020); 
    threeSum(theInput, 2020);
}

}

