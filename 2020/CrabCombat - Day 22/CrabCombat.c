/*
--- Day 22: Crab Combat ---
It only takes a few hours of sailing the ocean on a raft for boredom to sink in. Fortunately, you brought a small deck of space cards! You'd like to play a game of Combat, and there's even an opponent available: a small crab that climbed aboard your raft before you left.
Fortunately, it doesn't take long to teach the crab the rules.
Before the game starts, split the cards so each player has their own deck (your puzzle input). Then, the game consists of a series of rounds: both players draw their top card, and the player with the higher-valued card wins the round. The winner keeps both cards, placing them on the bottom of their own deck so that the winner's card is above the other card. If this causes a player to have all of the cards, they win, and the game ends.
For example, consider the following starting decks:
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
Player 1:
9
2
6
3
1
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
Player 2:
5
8
4
7
10
This arrangement means that player 1's deck contains 5 cards, with 9 on top and 1 on the bottom; player 2's deck also contains 5 cards, with 5 on top and 10 on the bottom.
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
The first round begins with both players drawing the top card of their decks: 9 and 5. Player 1 has the higher card, so both cards move to the bottom of player 1's deck such that 9 is above 5. In total, it takes 29 rounds before a player has all of the cards:
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
-- Round 1 --
Player 1's deck: 9, 2, 6, 3, 1
Player 2's deck: 5, 8, 4, 7, 10
Player 1 plays: 9
Player 2 plays: 5
Player 1 wins the round!
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
-- Round 2 --
Player 1's deck: 2, 6, 3, 1, 9, 5
Player 2's deck: 8, 4, 7, 10
Player 1 plays: 2
Player 2 plays: 8
Player 2 wins the round!
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
-- Round 3 --
Player 1's deck: 6, 3, 1, 9, 5
Player 2's deck: 4, 7, 10, 8, 2
Player 1 plays: 6
Player 2 plays: 4
Player 1 wins the round!
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
-- Round 4 --
Player 1's deck: 3, 1, 9, 5, 6, 4
Player 2's deck: 7, 10, 8, 2
Player 1 plays: 3
Player 2 plays: 7
Player 2 wins the round!
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
-- Round 5 --
Player 1's deck: 1, 9, 5, 6, 4
Player 2's deck: 10, 8, 2, 7, 3
Player 1 plays: 1
Player 2 plays: 10
Player 2 wins the round!

...several more rounds pass...
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
-- Round 27 --
Player 1's deck: 5, 4, 1
Player 2's deck: 8, 9, 7, 3, 2, 10, 6
Player 1 plays: 5
Player 2 plays: 8
Player 2 wins the round!
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
-- Round 28 --
Player 1's deck: 4, 1
Player 2's deck: 9, 7, 3, 2, 10, 6, 8, 5
Player 1 plays: 4
Player 2 plays: 9
Player 2 wins the round!
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
-- Round 29 --
Player 1's deck: 1
Player 2's deck: 7, 3, 2, 10, 6, 8, 5, 9, 4
Player 1 plays: 1
Player 2 plays: 7
Player 2 wins the round!
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
== Post-game results ==
Player 1's deck:
Player 2's deck: 3, 2, 10, 6, 8, 5, 9, 4, 7, 1
Once the game ends, you can calculate the winning player's score. The bottom card in their deck is worth the value of the card multiplied by 1, the second-from-the-bottom card is worth the value of the card multiplied by 2, and so on. With 10 cards, the top card is worth the value on the card multiplied by 10. In this example, the winning player's score is:
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
   3 * 10
+  2 *  9
+ 10 *  8
+  6 *  7
+  8 *  6
+  5 *  5
+  9 *  4
+  4 *  3
+  7 *  2
+  1 *  1
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
= 306
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
So, once the game ends, the winning player's score is 306.
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
Play the small crab in a game of Combat using the two decks you just dealt. What is the winning player's score?
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>

/* Limit the number of rounds (2000) should be good instead of checking game history or a graph */
#define N_CARDS 52
#define MAX_ROUNDS 2000

struct state {
  int cards[2][N_CARDS]; /* The player has all the cards or they dont */
  int ncards[2];
}

/* Returns the winner, score is an optional return*/
static int game(struct state *initst, int part, int *score)
{
  struct state st, state2;
  int p, c, round, win; /* Game control variables */

  st = *initst; /* Make the current state the initial starting state */

  for (round=0 ; round++){
    if (round > MAX_ROUNDS) /* Check for Max Round */
      { win=0; break; }

    if (part == 2 && st.cards[0][0] < st.ncards[0] && st.cards[1][0] < st.ncards[1]){
      for (p=0; p < 2; p++){
        state2.ncards[p] = st.cards[p][0];
        memcpy(state2.cards[p], st.cards[p] + 1, sizeof(**st.cards) * state2.ncards[p])
      }
      win = game(&state2, part, NULL);
    } else {
      win = st.cards[0][0] < st.cards[1][0];
    }
    assert(st.ncards[win]+2 <= N_CARDS);
    st.cards[win][st.ncards[win]++] = st.cards[win][0];
    st.cards[win][st.ncards[win]++] = st.cards[!win][0];

    for (m=0 m < 2; m++){ /* Move the memory pointers for the Deck state */
      memmove(st.cards[m], st.cards[m]+1, sizeof(**stcards) * --st.ncards[m]);
    }
    if(!st.ncards[!win]){ /* If there isnt a winning solution in the set */
        break;
    }
    if(score){
      for (c=0; c < st.ncards[win]; c++){
        *score += st.cards[win][c] * (st.ncards - c); /* Assign Score the value of the current card (*) the Cards inverse position in the deck (bottom-up) - deque */
      }
    }
  }
  return win;
}

int main()
{
struct state st = {};
char buf[16]; /* The char input buffer for reading in player decks */
int p=0, val, pt1=0, pt2=0; /* Program Control Variables */

while (fgets(buf, sizeof(buf), stdin)) /* Read in the Decks with a buffer */
		if (sscanf(buf, "Player %d", &p) == 1) {
			p--;
			assert(p>=0 && p<2);
		} else if (sscanf(buf, "%d", &val) == 1) {
			assert(st.ncards[p] < NCARDS);
			st.cards[p][st.ncards[p]++] = val;
		}

game(&st, 1, &pt1); /* game(gamestate, part-number, ->score)*/
game(&st, 2, &pt2);
printf("%d %d\n", pt1, pt2);

}
