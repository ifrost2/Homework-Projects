#------------------------------------------------------------#
#                 YOUR CODE BELOW                            #
#                                                            #
#                 ONLY MODIFY THIS FILE                      #
#------------------------------------------------------------#

'''
The board is represented as list of list. Something like this for a 5X5 board

row\cols 0 1 2 3 4
0
1
2
3

You can access the element of the board using, board[rowIndex][columnIndex].

Values on the board would be one of the following -

'-' => Indicating empty tile, Chaos can move some piece to this position or order can place the piece it picked randomly
		at this position

'A' => Indicating Red colored tile placed
'B' => Indicating Cyan colored tile placed
'C' => Indicating Green colored tile placed
'D' => Indicating Blue colored tile placed
'E' => Indicating Yellow colored tile placed

Mapping ==> 'A': 'Red', 'B': 'Cyan', 'C': 'Green','D':'Blue', 'E':'Yellow', '-':'-'}
Example -

board[0][0] will give the Piece on the top-left position.

board[1][3] will give the piece in 1st row and 3rd column

board[N - 1][N - 1] will give the piece on the bottom-right position



Read this entire file and understand the comments for the functions and variables

'''
import copy
# myAI.py
import sys
from random import random, choice

def printX(*message):
	for msg in message:
		sys.stderr.write(repr(msg) + ' ')
	sys.stderr.write('\n')

# boardSize, squared board with N = 5, 7..
#N = int(input())
N = 5

# Current role - ORDER or CHAOS
#ROLE = input()
ROLE = 'ORDER'

# initializing board with empty tile '-'
board = []
for i in range(0, N):
	boardRow = []
	for j in range(0, N):
		boardRow.append('-')
	board.append(boardRow)

# check if no empty tile left
def isGameOver():
	for i in range(0, N):
		for j in range(0, N):
			if (board[i][j] == '-'):
				return False
	return True


# gets all the possible moves order can make
# this can be used for getting the children from a given state
def getPossibleOrderMoves(x, y):
	possibleMoves = []

	for iterator in range(x-1,-1,-1):
		if board[iterator][y]=='-':
			possibleMoves.append((iterator,y))
		else:
			break

	for iterator in range(y-1,-1,-1):
		if board[x][iterator]=='-':
			possibleMoves.append((x,iterator))
		else:
			break

	for iterator in range(x+1,N):
		if board[iterator][y]=='-':
			possibleMoves.append((iterator,y))
		else:
			break

	for iterator in range(y+1,N):
		if board[x][iterator]=='-':
			possibleMoves.append((x,iterator))
		else:
			break

	return possibleMoves

#------------------------------------------------------------#
#                 MAIN FUNCTION              				 #
#                 FOR CHAOS BOT                      		 #
#------------------------------------------------------------#

# @input: piece, the key to the color picked,
# Example
# piece = 'A', Red tile is randomly drawn from the bag
# piece = 'E', Yellow tile is randome drawn from the bag
#
# @return: tuple of an EMPTY co-ordinate/x,y - position on the board, where you want to place the tile on the board
# Example
# If @input as a piece is 'D'
# @return (2,3)
# Place the Green colored tile ('D' corresponds to Green) in 3rd row and 4th column [Index starting from ZERO!, NOTE]

# currently it naively picks an empty position to place the tile on the board
# make it intelligent!
def chaosAI(piece):
	openSquares=[]
	for x in range(N):
		for y in range(N):
			if board[x][y]=="-":
				openSquares.append((x,y))
	openSquares
	return choice(openSquares)

#------------------------------------------------------------#
#                 MAIN FUNCTION              				 #
#                 FOR ORDER BOT                      		 #
#------------------------------------------------------------#

# @return: a tuple with 4 values a b c d
# ORDER wants to shift a tile from a non-empty co-ordinate/x-y position, (a, b) to an EMPTY position (c, d)
# CONSTRAINT - the shift can only be done to an EMPTY position in SAME ROW or SAME COLUMN as the current tile position

# currently it naively picks a random tile and tried to move it randomly in the same row or column as the tile
# to place the tile on the board
# make this intelligent too!

def orderAI():
    capturedSquares=[]
    for x in range(N):
        for y in range(N):
            if board[x][y]!="-":
                capturedSquares.append((x,y,board[x][y]))

    capturedSquares = sorted(capturedSquares, key=lambda t:(t[0],t[1]))

    while(True):
        fromPosition = choice(capturedSquares)
        possibleMoves = getPossibleOrderMoves(fromPosition[0], fromPosition[1])
        if len(possibleMoves)!=0:
                mv = choice(possibleMoves)
                ans = (fromPosition[0], fromPosition[1], mv[0], mv[1])
                break

    return ans

#------------------------------------------------------------#
#                 HELPER FUNCTIONS               	     #
#                & ADD MORE FUNCTION 			     #
# 			AND				     #
#		  MODIFY AS YOU FEEL                         #
#------------------------------------------------------------#

# Here are the following list of things that you'll need -
# 1. Finding the scores of the board in terms of palindromes of the board
# 2. Book keeping of the number of tiles of each color on the board, to be used for calculating the probability
# of next tile randomly
# 3. Generating children board for a move to be made by CHAOS & ORDER
# 4. Perform expectiMiniMax with Alph Beta pruning
# 5. Implement a heuristic
# 6. Prove your mettle and win the battle!


def getScore(board):
    # Given a board represented as a list of lists,
    # find the palindromic ordering of tiles in horizontal and vertical directions
    # and calculate the score of the board
    # return the score
    stringVert = ""
    stringHoriz = ""
    total = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            #Holds each of the values in the column at current j
            #Appends to the string that tracks vertically
            stringVert += board[j][i]
            for x in board[i][j]:
                #Appends to the string that tracks horizontally
                stringHoriz += x
        #Add both scores to the total
        total = total + isPalindrome(stringVert) + isPalindrome(stringHoriz)
        #Reset the strings
        stringHoriz = ""
        stringVert = ""
    return total

#Checks if a string is a palindrome and does not contain '-' and returns how many points should be given (aka length of the string)
#Also is based on children of the palindrome
def isPalindrome(string):
    length = len(string)
    if length < 2:
        return 0
    else:
        for i in range(len(string)):
            #If it isn't a palindrome or contains '-'
            if string[i] != string[length - i - 1] or string[i] == "-":
                #This returns the result of the current palindrome and its children removing any recounts that would have in between
                return 0 + isPalindrome(string[:-1]) + isPalindrome(string[1:]) - isPalindrome(string[1:-1])
        return len(string) + isPalindrome(string[:-1]) + isPalindrome(string[1:]) - isPalindrome(string[1:-1])

#Returns probability of picking each color for use with expectiminimax
def probability(board):
    D = {'R':5, 'C':5, 'G':5, 'B':5, 'Y':5}
    total = 0
    P = {}
    for i in board:
        for j in i:
            if j == '-':
                pass
            else:
                D[j] = D[j] - 1
                total += 1
    for color in D:
        P[color] = D[color]/total
    return P

def generateChaosChildren(board, computerTile):
    #This function takes a board state and a tile symbol and returns a
    #list of "children" states for Chaos,
    #i.e., a list of boards which represent possible moves.
    #This function will be helpful to use in your Alpha Beta function
    possible = []
    for i in getPossibleChaosMoves(board, computerTile):
        possible.append(i)
    return possible

def generateOrderChildren(board):
    #This function will take a current board state and return
    #All the possible board states that Order can reach
    possible = []
    for x in range(len(board)):
        for y in range(len(board[x])):
            possibleMoves = getPossibleOrderMoves(x,y)
            for p in possibleMoves:
                temp = copy.deepcopy(board)
                temp[p[0]][p[1]] = copy.deepcopy(temp[x][y])
                temp[x][y] = '-'
                if temp in possible:
                    pass
                else:
                    possible.append(temp)
    return possible


def expectiMiniMax(board, player, tile, depth, alpha, beta):
    # This recursive function will take the initial board state, a depth to go to and alpha and beta value
    # and return back the value
    # Gameplay: Chance -> Chaos -> Order -> Chance
    if isGameOver() or depth == 0:
        return Heuristic(board, player)
    if player == 'ORDER':
        a = -math.inf
        for i in generateOrderChildren(board):
            a = max(a, expectiMiniMax(board, 'CHANCE', '',
                                      depth - 1, alpha, beta))

    if player == 'CHAOS':
        a = math.inf
        for i in generateChaosChildren(board, tile):
            a = min(a, expectiMiniMax(board, 'ORDER', '',
                                      depth - 1, alpha, beta))

    if player == 'CHANCE':
        a = 0
        prob = probability(board)
        for color in prob:
            a = a + prob(color) * expectiMiniMax(board, 'CHAOS', color,
                                                 depth, alpha, beta)
    return a

        

def getPossibleChaosMoves(board, computerTile):
    #Lists all possible moves chaos can make with a given computer tile
    original = copy.deepcopy(board)
    possibleBoards = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            original = copy.deepcopy(board)
            if board[i][j] == '-':
                #Changes the empty tile and adds to list of moves then reverts back
                temp = original[i][j]
                original[i][j] = computerTile
                possibleBoards.append(original)
    return possibleBoards

def Heuristic(board, player):
    total = 0
    #For use in the same row or column, greater the more of the same value
    #Given a board, returns the value of that board when
    #evaluated with a heuristic, evaluation function
    #This one is based off of how many colors are the same in each row and column
    for i in range(len(board)):
        for j in range(len(board[i])):
            mult = 1
            #Check rows
            for x in range(i,(len(board))):
                #Don't count when they are the same spot
                if i == x:
                    pass
                #Don't count when they are empty spots either
                elif board[i][j] == '-' or board[x][j] == '-':
                    pass
                #If there are any matching spots, add up
                elif board[i][j] == board[x][j]:
                    total += mult
                    mult += 1
            mult = 1
            #Check columns
            for y in range(j, (len(board[i]))):
                #Don't count when they are the same spot
                if j == y:
                    pass
                #Don't count when they are empty spots either
                elif board[i][j] == '-' or board[i][y] == '-':
                    pass
                #If there are any matching spots, add up
                elif board[i][j] == board[i][y]:
                    total += mult
                    mult += 1
    if player == 'ORDER':
        return total
    else:
        return 0 - total
#------------------------------------------------------------#
#                 DO NOT CHANGE THE               		     #
#                    CODE BELOW                    		     #
#------------------------------------------------------------#

## --------------------
import os, sys
sys.path.insert(0, os.path.realpath('../utils'))
from log import *

COLORS = [
	bcolors.OKRED,
	bcolors.OKCYAN,
	bcolors.OKGREEN,
	bcolors.OKBLUE,
	bcolors.OKYELLOW,
	bcolors.OKMAGENTA,
	bcolors.OKCYAN,
	bcolors.OKWHITE
]

# MAPPING of Piece with Colors

TEXTCONV = {'A': 'R', 'B': 'C', 'C': 'G','D':'B', 'E':'Y', '-':'-'}
def color(tile): # character
	index = ord(tile) - ord('A')
	if (tile == '-'):
		index = -1

	if (N <= 5):
		# Not over riding 5x5's old behaviour
		return COLORS[index] + TEXTCONV[tile] + bcolors.ENDC
	else:
		return COLORS[min(index, len(COLORS)-1)] + tile + bcolors.ENDC

def printBoard():

	for x in range(N):
		print ("".join( list( map( lambda x: color(x), board[x] ) ) ), file=sys.stderr)
	print ('\n', file=sys.stderr)


# returns if the move was successful or not
def makeChaosMove(x, y, color):
	global board
	if (board[x][y] != '-'):
		return False
	board[x][y] = color
	return True

# returns if the move was successful or not
def makeOrderMove(a, b, c, d):
	global board
	board[c][d] = board[a][b]
	board[a][b] = '-'
	return True

def playAsOrder():
	global board
	printX('ORDER')
	while True:
		printBoard()
		line = input()
		# printX ('LINE:', line)
		(x, y, color) = line.split(' ')
		(x, y) = (int(x), int(y))
		board[x][y] = color
		if (isGameOver()):
			return

		(a, b, c, d) = orderAI()
		makeOrderMove(a, b , c, d)
		printBoard()
		print('%d %d %d %d' % (a, b, c, d))
		sys.stdout.flush()


def playAsChaos():
	global board
	printX('CHAOS')
	color = input()
	(x, y) = chaosAI(color)
	board[x][y] = color
	print('%d %d' %(x, y))
	printBoard()

	while True:
		if (isGameOver()):
			return

		his_move = input()
		# printX ('his move: %s'%his_move)
		(a, b, c, d) = map(lambda x: int(x), his_move.split(' '))
		makeOrderMove(a, b, c, d)
		color = input()
		(x, y) = chaosAI(color)
		board[x][y] = color
		printBoard()
		print ('%d %d' %(x, y))


##if (ROLE == 'ORDER'):
##	playAsOrder()
##elif(ROLE == 'CHAOS'):
##	playAsChaos()
##else:
##	print('I am not intelligent for this role: %s' %ROLE, file=sys.stderr)
##
##printX ('--graceful exit by myAI--')
##
getScore(board)

