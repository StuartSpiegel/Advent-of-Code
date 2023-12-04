import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class ScratchcardSolver {
    public static void main(String[] args) {
        try {
            BufferedReader reader = new BufferedReader(new FileReader("input.txt"));

            String line;
            int totalPoints = 0;

            while ((line = reader.readLine()) != null) {
                int points = calculatePoints(line);
                totalPoints += points;
            }

            System.out.println("Total Points: " + totalPoints);

            reader.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    private static int calculatePoints(String line) {
        String[] parts = line.split("\\|");
        String[] winningNumbers = parts[0].trim().split("\\s+");
        String[] yourNumbers = parts[1].trim().split("\\s+");

        int points = 0;

        for (String yourNumber : yourNumbers) {
            for (String winningNumber : winningNumbers) {
                if (yourNumber.equals(winningNumber)) {
                    points++;
                    break;
                }
            }
        }

        // Double the points for each match after the first
        if (points > 1) {
            points = points * 2;
        }

        return points;
    }
}
