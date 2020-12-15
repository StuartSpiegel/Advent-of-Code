import java.io.File;
import java.util.HashMap;
import java.util.Scanner;

public class RambunctiousRecitation {

	private static String[] input;
	
	public RambunctiousRecitation() {
		Scanner toRead =null;
		try {
			toRead = new Scanner(new File("input.txt"));
		} catch (Exception e) {
			System.out.println("File not found");
		}
		
		input = toRead.nextLine().split(",");
	}
	
	public void solvePart1() {
		playGame(2020);
	}
	
	public void solvePart2() {
		playGame(30_000_000);
	}
	
	public void playGame(int rounds) {
		HashMap<Integer, Integer> map = new HashMap<Integer, Integer>(); // <num spoken, turn number>
		for (int k = 0; k < input.length; k++) {
			map.put(Integer.parseInt(input[k]), (k + 1));
		}
		
		int turn = input.length + 1; //the next turn to be played
		int nextNum = 0; //the next number to be played (0 to start since last number spoken is unique)
		
		while(turn < rounds) {
			if(map.containsKey(nextNum)) {
				int difference = turn - map.get(nextNum); //when a number is spoken find the difference between current turn and the turn it was said on.
				map.put(nextNum, turn); //replace <curr-num, oldTurn> with <curr-num, thisTurn> in the hash-map
				nextNum = difference; //the difference becomes the next number to be said
			}
			else {
				//if the number has not yet been said
				map.put(nextNum, turn); //add <num, turn> to the map
				nextNum = 0; //the next number to be played will be zero because the number hasnt been said (is unique to the game)
			}
			turn++;
		}
		
		System.out.println(nextNum);
	}
	
	public static void main(String[] args) {
		RambunctiousRecitation call_obj = new RambunctiousRecitation();
		call_obj.solvePart1();
		call_obj.solvePart2();
		
	}

}
