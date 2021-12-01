import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.Reader;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.LinkedHashMap;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;
import java.util.Map.Entry;
import java.util.Queue;
import java.util.Scanner;
import java.util.Set;

/*
--- Day 9: Encoding Error ---
With your neighbor happily enjoying their video game, you turn your attention to an open data port on the little screen in the seat in front of you.
Though the port is non-standard, you manage to connect it to your computer through the clever use of several paperclips. Upon connection, the port outputs a series of numbers (your puzzle input).
The data appears to be encrypted with the eXchange-Masking Addition System (XMAS) which, conveniently for you, is an old cypher with an important weakness.
XMAS starts by transmitting a preamble of 25 numbers. After that, each number you receive should be the sum of any two of the 25 immediately previous numbers. The two numbers will have different values, and there might be more than one such pair.
For example, suppose your preamble consists of the numbers 1 through 25 in a random order. To be valid, the next number must be the sum of two of those numbers:

26 would be a valid next number, as it could be 1 plus 25 (or many other pairs, like 2 and 24).
49 would be a valid next number, as it is the sum of 24 and 25.
100 would not be valid; no two of the previous 25 numbers sum to 100.
50 would also not be valid; although 25 appears in the previous 25 numbers, the two numbers in the pair must be different.
Suppose the 26th number is 45, and the first number (no longer an option, as it is more than 25 numbers ago) was 20. Now, for the next number to be valid, there needs to be some pair of numbers among 1-19, 21-25, or 45 that add up to it:
26 would still be a valid next number, as 1 and 25 are still within the previous 25 numbers.
65 would not be valid, as no two of the available numbers sum to it.
64 and 66 would both be valid, as they are the result of 19+45 and 21+45 respectively.
Here is a larger example which only considers the previous 5 numbers (and has a preamble of length 5):
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
In this example, after the 5-number preamble, almost every number is the sum of two of the previous 5 numbers; the only number that does not follow this rule is 127.

The first step of attacking the weakness in the XMAS data is to find the first number in the list (after the preamble) which is not the sum of two of the 25 numbers before it. What is the first number that does not have


*/
public class EncodingError {
		
	private static List<Long> theData;
	static LinkedHashMap<Integer, Long> m = new LinkedHashMap<Integer, Long>();
	static long startTime = System.currentTimeMillis();
	static ArrayList<Long> input = new ArrayList<Long>();
	static long firstError = 0;
	static boolean invalidFound = false;
	
	//part 1 - my first stab at part 1 I tried to use a HashMap but had trouble so I brute forced this in main
	public static Map.Entry<Integer, Long> returnBadIndex(List<Long> allNumbers, int preambleNumbers){
		
		Set<Entry<Integer, Long>> s = m.entrySet();
		
		for (int k = 0; k < allNumbers.size() - preambleNumbers; k++) {
			List<Long> sublist = allNumbers.subList(k, k + preambleNumbers);
			Long numToCheck = allNumbers.get(k + preambleNumbers);
			
			for (Map.Entry<Integer, Long> it: s) {
				if(!checkArraySum(sublist, numToCheck)) {
					// return it.getValue(Map.Entry(k + preambleNumbers, numToCheck));
				}
				
			}
			
		}
		throw new RuntimeException("All numbers are following a good pattern");
	}
	
	
	private static boolean checkArraySum(List<Long> theArray, long numToCheck) {
		
		for (int j = 0; j < theArray.size(); j++) {
			for (int k = j + 1; k < theArray.size(); k++) {
				if(theArray.get(j) + theArray.get(k) == numToCheck ) {
					return true;
				}
			}
		}
		return false;
	}
	

	//part 2
	public static Long findPremableNumbersOfSum(List<Long> input, int preambleNumbers) {
		Map.Entry<Integer, Long> part1 = returnBadIndex(input, preambleNumbers);
		int index1 = 0;
		int index2 = 0;
		
		out:
		for (int k = 0; k <= part1.getKey(); k++) {
			int j = k + 1;
			Long theSum = input.get(k);
			while (true) {
				if(theSum != part1.getValue()) {
					theSum += input.get(j);
				}
				if(theSum == part1.getValue()) {
					index1 = k;
					index2 = j;
					break out;
				}
				if(theSum > part1.getValue()) {
					continue out;
				}
			}
		}
		List<Long> sublist = input.subList(index1, index2);
		long max = sublist.stream().mapToLong(a -> a).max().getAsLong();
		long min = sublist.stream().mapToLong(a -> a).min().getAsLong();
		return max + min;
		
	}
	
	public static void solvePart2BruteForce() {
		final long INVALID_NUM = firstError;
		int min = 0, max = 0;
		int i = 0;
		boolean setFound = false;

		while (!setFound) {
			int sum = 0;
			int j = i;
			min = Integer.MAX_VALUE;
			max = 0;
			while (sum < INVALID_NUM) {
				sum += input.get(j);
				min = (int) Math.min(min, input.get(j));
				max = (int) Math.max(max, input.get(j));
				j++;
			}
			if (sum == INVALID_NUM) {
				setFound = true;
			} else {
				i++;
			}
		}

		System.out.println("Sum of smallest + largest: " + (min + max));

		long endTime = System.currentTimeMillis();
		System.out.println((endTime - startTime) / 1000.0);

		
	}
	
	public static void main(String[] args) throws IOException {
		
		//brute force code for part 1 since i had trouble getting linked Hash map to work

		final int PREAMBLE_SIZE = 25;

		Scanner reader = new Scanner(new File("input.txt"));
		while (reader.hasNextLine())
			input.add(Long.parseLong(reader.nextLine()));

		// part1
		ArrayList<Long> preamble = new ArrayList<Long>();
		Queue<Long> restOfNums = new LinkedList<Long>();

		for (int i = 0; i < input.size(); i++) {
			if (i < PREAMBLE_SIZE)
				preamble.add(input.get(i));
			else
				restOfNums.add(input.get(i));
		}

		
		while (!invalidFound) {
			long n = restOfNums.poll();
			if (!checkArraySum(preamble, n)) {
				firstError = n;
				invalidFound = true;
			} else {
				preamble.remove(0);
				preamble.add(n);
			}
		}

		System.out.println("First invalid #: " + firstError);
		//end part 1 brute force
		
		// **Attempts at using Hash Map for better times here**
		//returnBadIndex(theData, PREAMBLE_SIZE);
		//System.out.println(findPremableNumbersOfSum(input, PREAMBLE_SIZE));
		solvePart2BruteForce();
	}
}


