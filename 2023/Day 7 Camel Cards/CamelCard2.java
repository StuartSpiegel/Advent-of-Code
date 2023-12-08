// --- Part Two ---
// To make things a little more interesting, the Elf introduces one additional rule. Now, J cards are jokers - wildcards that can act like whatever card would make the hand the strongest type possible.

// To balance this, J cards are now the weakest individual cards, weaker even than 2. The other cards stay in the same order: A, K, Q, T, 9, 8, 7, 6, 5, 4, 3, 2, J.

// J cards can pretend to be whatever card is best for the purpose of determining hand type; for example, QJJQ2 is now considered four of a kind. However, for the purpose of breaking ties between two hands of the same type, J is always treated as J, not the card it's pretending to be: JKKK2 is weaker than QQQQ2 because J is weaker than Q.

// Now, the above example goes very differently:

// 32T3K 765
// T55J5 684
// KK677 28
// KTJJT 220
// QQQJA 483
// 32T3K is still the only one pair; it doesn't contain any jokers, so its strength doesn't increase.
// KK677 is now the only two pair, making it the second-weakest hand.
// T55J5, KTJJT, and QQQJA are now all four of a kind! T55J5 gets rank 3, QQQJA gets rank 4, and KTJJT gets rank 5.
// With the new joker rule, the total winnings in this example are 5905.

// Using the new joker rule, find the rank of every hand in your set. What are the new total winnings?
// import java.io.BufferedReader;
// import java.io.FileReader;
// import java.io.IOException;
// import java.util.ArrayList;
// import java.util.Arrays;
// import java.util.Comparator;

// public class CamelCard2 {
//     private static final String[] CARD_LABELS = {"2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"};

//     public static void main(String[] args) {
//         try (BufferedReader br = new BufferedReader(new FileReader("input.txt"))) {
//             String line;
//             int totalWinnings = 0;
//             ArrayList<HandWithBid> handsWithBidsList = new ArrayList<>();

//             // Read hands and bids from the file
//             while ((line = br.readLine()) != null) {
//                 String[] parts = line.split(" ");
//                 String hand = parts[0];
//                 int bid = Integer.parseInt(parts[1]);
//                 handsWithBidsList.add(new HandWithBid(hand, bid));
//             }

//             // Sort hands by strength and calculate total winnings
//             HandWithBid[] handsWithBids = handsWithBidsList.toArray(new HandWithBid[0]);
//             Arrays.sort(handsWithBids, Comparator.reverseOrder());

//             for (int i = 0; i < handsWithBids.length; i++) {
//                 totalWinnings += handsWithBids[i].getBid() * (i + 1);
//                 System.out.println("Hand: " + handsWithBids[i].getHand() + ", Rank: " + (i + 1));
//             }

//             System.out.println("Total Winnings: " + totalWinnings);

//         } catch (IOException e) {
//             e.printStackTrace();
//         }
//     }

//     static class HandWithBid implements Comparable<HandWithBid> {
//         private final String hand;
//         private final int bid;

//         public HandWithBid(String hand, int bid) {
//             this.hand = hand;
//             this.bid = bid;
//         }

//         public String getHand() {
//             return hand;
//         }

//         public int getBid() {
//             return bid;
//         }

//         @Override
//         public int compareTo(HandWithBid other) {
//             return compareHands(this.hand, other.hand);
//         }

//         private int compareHands(String hand1, String hand2) {
//             int typeComparison = getHandTypeValue(hand2) - getHandTypeValue(hand1);
//             if (typeComparison != 0) {
//                 return typeComparison;
//             } else {
//                 return compareCardLabels(hand1, hand2);
//             }
//         }

//         private int compareCardLabels(String hand1, String hand2) {
//             for (int i = 0; i < hand1.length(); i++) {
//                 char card1 = hand1.charAt(i);
//                 char card2 = hand2.charAt(i);

//                 int card1Value = getCardValue(card1);
//                 int card2Value = getCardValue(card2);

//                 if (card1Value != card2Value) {
//                     return card2Value - card1Value;
//                 }
//             }
//             return 0;
//         }

//         private int getCardValue(char cardLabel) {
//             if (cardLabel == 'J') {
//                 // Treat J as a wildcard for determining hand types
//                 return -1;
//             }

//             return Arrays.asList(CARD_LABELS).indexOf(String.valueOf(cardLabel));
//         }

//         private int getHandTypeValue(String hand) {
//             char[] cards = hand.toCharArray();
//             Arrays.sort(cards);

//             // Check for five of a kind
//             if (cards[0] == cards[4]) {
//                 return 7; // Five of a kind
//             }

//             // Check for four of a kind
//             if (cards[0] == cards[3] || cards[1] == cards[4]) {
//                 return 6; // Four of a kind
//             }

//             // Check for full house
//             if ((cards[0] == cards[2] && cards[3] == cards[4]) || (cards[0] == cards[1] && cards[2] == cards[4])) {
//                 return 5; // Full house
//             }

//             // Check for three of a kind
//             if (cards[0] == cards[2] || cards[1] == cards[3] || cards[2] == cards[4]) {
//                 return 4; // Three of a kind
//             }

//             // Check for two pair
//             if ((cards[0] == cards[1] && cards[2] == cards[3]) || (cards[0] == cards[1] && cards[3] == cards[4]) ||
//                     (cards[1] == cards[2] && cards[3] == cards[4])) {
//                 return 3; // Two pair
//             }

//             // Check for one pair
//             if (cards[0] == cards[1] || cards[1] == cards[2] || cards[2] == cards[3] || cards[3] == cards[4]) {
//                 return 2; // One pair
//             }

//             // High card
//             return 1;
//         }
//     }
// }

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;

public class CamelCard2 {
   // private static final String[] CARD_LABELS = {"2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"};

    public static void main(String[] args) {
        try (BufferedReader br = new BufferedReader(new FileReader("input.txt"))) {
            String line;
            int totalWinnings = 0;
            ArrayList<HandWithBid> handsWithBidsList = new ArrayList<>();

            // Read hands and bids from the file
            while ((line = br.readLine()) != null) {
                String[] parts = line.split(" ");
                String hand = parts[0];
                int bid = Integer.parseInt(parts[1]);
                handsWithBidsList.add(new HandWithBid(hand, bid));
            }

            // Sort hands by strength and calculate total winnings
            HandWithBid[] handsWithBids = handsWithBidsList.toArray(new HandWithBid[0]);
            Arrays.sort(handsWithBids, Comparator.reverseOrder());

            for (int i = 0; i < handsWithBids.length; i++) {
                totalWinnings += handsWithBids[i].getBid() * (i + 1);
                System.out.println("Hand: " + handsWithBids[i].getHand() + ", Rank: " + (i + 1));
            }

            System.out.println("Total Winnings: " + totalWinnings);

        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    static class HandWithBid implements Comparable<HandWithBid> {
        private final String hand;
        private final int bid;

        public HandWithBid(String hand, int bid) {
            this.hand = hand;
            this.bid = bid;
        }

        public String getHand() {
            return hand;
        }

        public int getBid() {
            return bid;
        }

        @Override
        public int compareTo(HandWithBid other) {
            return compareHands(this.hand, other.hand);
        }

        private int compareHands(String hand1, String hand2) {
            int typeComparison = getHandTypeValue(hand2) - getHandTypeValue(hand1);
            if (typeComparison != 0) {
                return typeComparison;
            } else {
                return compareCardLabels(hand1, hand2);
            }
        }
        
        private int compareCardLabels(String hand1, String hand2) {
            for (int i = 0; i < hand1.length(); i++) {
                if (hand1.charAt(i) != hand2.charAt(i)) {
                    return getCardValue(hand2.charAt(i)) - getCardValue(hand1.charAt(i));
                }
            }
            return 0;
        }
        
        private int getCardValue(char cardLabel) {
            switch (cardLabel) {
                case 'J': return 1; // J should now be the weakest card in Part 2.
                case '2': return 2;
                case '3': return 3;
                case '4': return 4;
                case '5': return 5;
                case '6': return 6;
                case '7': return 7;
                case '8': return 8;
                case '9': return 9;
                case 'T': return 10;
                case 'Q': return 12;
                case 'K': return 13;
                case 'A': return 14;
                default: throw new IllegalArgumentException("Invalid card label: " + cardLabel);
            }
        }
        
        private int getHandTypeValue(String hand) {
            char[] cards = hand.toCharArray();
            Arrays.sort(cards);

            // Check for five of a kind
            if (cards[0] == cards[4]) {
                return 7; // Five of a kind
            }

            // Check for four of a kind
            if (cards[0] == cards[3] || cards[1] == cards[4]) {
                return 6; // Four of a kind
            }

            // Check for full house
            if ((cards[0] == cards[2] && cards[3] == cards[4]) || (cards[0] == cards[1] && cards[2] == cards[4])) {
                return 5; // Full house
            }

            // Check for three of a kind
            if (cards[0] == cards[2] || cards[1] == cards[3] || cards[2] == cards[4]) {
                return 4; // Three of a kind
            }

            // Check for two pair
            if ((cards[0] == cards[1] && cards[2] == cards[3]) || (cards[0] == cards[1] && cards[3] == cards[4]) ||
                    (cards[1] == cards[2] && cards[3] == cards[4])) {
                return 3; // Two pair
            }

            // Check for one pair
            if (cards[0] == cards[1] || cards[1] == cards[2] || cards[2] == cards[3] || cards[3] == cards[4]) {
                return 2; // One pair
            }

            // High card
            return 1;
        }
    }
}

