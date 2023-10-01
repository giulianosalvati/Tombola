# Project Specification: "Bingo Game"

The program implements the bingo game.

In particular, it does the following:

Randomly draw numbers from 1 to 90.
Create groups of 6 cards with the specified characteristics below.
Register N players.
Assign a number M of cards to each player (each player can be assigned a different number of cards; for simplicity, assume that M cannot exceed a predefined value).
Check if a drawn number is present on a card and, if present, check if a player has achieved two numbers in a row (ambo), three numbers (terna), four numbers (quaterna), five numbers (cinquina), or a full card (tombola), and if one of these results has not yet been achieved.
Start the game by drawing one number at a time and checking each time if any player has achieved ambo, terna, quaterna, cinquina, or tombola; for simplicity, assume that at most one player can achieve one of these results after each draw.
End the game when a player achieves a tombola.
A group of 6 cards must meet the following conditions:

Each card has 3 rows and 9 columns.
Each card has 15 cells marked with a number from 1 to 90 and 12 empty cells.
Each row must contain exactly 5 numbers.
Each column must contain 1 to 3 numbers.
The first column contains numbers from 1 to 9, the second from 10 to 19, the third from 20 to 29, and so on, with the ninth column containing numbers from 80 to 90.
When present on a card, the number 90 always occupies the bottom-right corner cell (row 3, column 9).
Each number from 1 to 90 must be present on one and only one card.

# Instructions for Playing

To play, type the following command from the command line:

> `python tombola.py -g numero_giocatori -n lista_numero_di_cartelle_per_giocatore`

For example:

> `python tombola.py -g 3 -n 3 2 4`

Starts the game with 3 players, each having 3, 6, and 4 cards, respectively.

To list all possible options, type:

> `python tombola.py -h`

Press return to draw a number. After each number, the corresponding result for each player is displayed.

> `Vuoi vedere le cartelle dei giocatori e quelle del cartellone? y/n :`


