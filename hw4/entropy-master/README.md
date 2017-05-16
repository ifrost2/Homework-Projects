# README #

Welcome to the Entropy AI Tournament Manager. Designed and Developed By Mausam, http://www.cs.washington.edu/homes/mausam. Modified by Chitesh Tewani

For rules of the game visit : [wikipedia: entropy board game](https://en.wikipedia.org/wiki/Entropy_(1977_board_game))

### Setting up ###

* Steps for a test run (no extra code):
* In different terminals do:
* * sh startServer.sh
* * cd client; python client.py
* * Interact with server's terminal for making the 2 clients(same copy of the basic AI program) to play bot vs ai

* Further:
* * myAI.py is a python program which adheres to the I/O specs and plays kiddishly
* * make it intelligent and play against other players and also against the TA-AI which is built into the server. The TA-AI which you currently see is Random.


Example 1:

```
#!python

stdin: 5
stdin: ORDER
stdin: 0 0 B
stdout: 0 0 1 1 
...

```

Example 2:

```
#!python

stdin: 5
stdin: CHAOS
stdin: B
stdout: 0 0
stdin: 0 0 1 1
stdin: A 
...

```

Explanation:
The first 2 lines define the board size and player's role.
The next lines depends on role:

For order:

1. Read chaos's move: "x y C", (C is a single alphabet in upper case A-Z, representing color)
1. Print "a b c d" which is your move: (a, b) => (c, d)
1. Goto (1) till game over...

For chaos: 

1. Read "C" (C is a single alphabet in upper case A-Z, representing color)
1. Print "x y" which are the coordinates of the sq where you want to place the piece
1. Read "a b c d" which is order's move
1. Goto (1) till game over...


### Feedback & Suggestions ###
We humbly welcome all suggestions, bug reports and feedback. You can email to the Associate Instructors of the course - I399 - Games and Puzzle
