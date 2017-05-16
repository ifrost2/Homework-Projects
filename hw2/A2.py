#Ian Frost
#ifrost

# ASSIGNMENT 2

## Your goal is straightforward. Tell us who wins each game of NIM and what the winning moves are constrained to.

## Both functions should return tuples of this format:

#  (winningPlayer, winningMoves)

#       winningPlayer is either 1 or 2 depending on the player who wins (assume that it is player 1's move)
#       winningMoves is a tuple that stores ALL winning moves. It should follow this format:

#           ((winningPile1, stonesToTake1), (winningPile2, stonesToTake2), ... , (winningPileN, stonesToTakeN))
#           NOTE: If player 2 will win, winningMoves should be an empty tuple

# Both functions take a board. A board is a list of integers that represent how many stones are in each pile.
# For example, if the board is [1, 2, 3] there is one stone in pile one, two in pile two, and three in pile three.

# In nPileWinner, each player is allow to take as many stones out of any pile as they wish (limited to the pile
# size of course). This is equivalent to regular NIM or unlimited-NIM.

# In restrictedPileWinner, each player can only take a specified number of stones out of each pile. The rules are denoted
# in the tuple moves. If moves is (1, 3, 4), each player may only take one stone, three stones, or four stones out
# of any pile. This is equivalent to (1, 3, 4)-NIM. You should be able to handle any variation of the rules.


# We have provided some starter examples for your benefit:

###################################################
#               UTILITY FUNCTIONS
#     (You may use these, but you don't have to)
###################################################

#Needed to be beforehand as I was using these in my functions
#convert a binary array to a decimal number (big-endian form)
def binToDec(binary):
    output = 0
    for i in range(len(binary)):
        output += pow(2, i) * binary[i]
    return output

#XOR logic between two binary arrays (big-endian form)
def XOR(bin1, bin2):

    binOut = []

    for i in range(max(len(bin1), len(bin2))):

        if i == len(bin1):
            binOut.extend(bin2[i:])
            break

        elif i == len(bin2):
            binOut.extend(bin1[i:])
            break

        elif bin1[i] == bin2[i]:
            binOut.append(0)

        else:
            binOut.append(1)

    return binOut

###################################################
#               YOUR CODE HERE
###################################################
import numpy as np


def nPileWinner(board):
    #Holds XOR binary list
    binX = []
    #tuple of moves
    final = ()
    for num in range(len(board)):
        #XOR between all of the piles in the board
        binX = XOR(binX, decToBin(board[num]))
    #If this is 0 then player two wins
    if binToDec(binX) == 0:
        return (2,())
    else:
        #Check for valid moves
        for num in range(len(board)):
            #Check to see XOR between the binX and what the current pile is
            current = XOR(binX, decToBin(board[num]))
            #Make current to be decimal number this is the number after stones are removed
            stones = binToDec(current)
            #If we are not adding stones to the pile
            if board[num] >= stones:
                #add the pile number and how many stones to remove to the final tuple
                final += ((num, (board[num] - stones)),)
            else:
                pass

        return (1, (final))

#Holds dictionary for grundy numbers
#0 will always be 0
D = {0:0}
def restrictedPileWinner(board, moves):
    #Holds what moves are in binary
    moveBin = []
    #Tuple to return
    final = ()
    #populate moveBin
    for move in moves:
        moveBin.append(decToBin(move))
    #Determines the XOR between all of the piles in the board
    binX = []
    #Create binX
    for num in range(len(board)):
        grun = decToBin(grundy(board[num], moves))
        binX = XOR(binX, grun)
    #If this is 0 then player two wins 
    if binToDec(binX) == 0:
        return (2,())
    else:
        #Check for valid moves
        for num in range(len(board)):
            grun = decToBin(grundy(board[num], moves))
            decGrun = (grundy(board[num], moves))
            #Check to see XOR between the binX and what the current pile is
            current = XOR(binX, grun)
            #Make current to be decimal number
            stones = binToDec(current)
            #If we are not adding stones
            if decGrun >= stones:
                #Add the move to be returned
                final += ((num, decGrun - stones),)
            else:
                pass
        if final == ():
            return (2,())
        else:
            return (1, (final))
    

#Convert decimal to a binary array (big-endian)
def decToBin(decimal):
    output = []
    while (decimal > 0):
        if decimal % 2 == 1:
            output.append(1)
        else:
            output.append(0)
        if decimal == 1:
            break
        decimal = decimal//2
    return output

#Produces grundy number for game with pile amount and moves
def grundy(pile, moves):
    for i in range(1, pile + 1):
        #Hold the possibilities of numbers to be reached in this game
        poss = []
        #List all the possible numbers to be reached
        for m in moves:
            poss.append(i - m)
        #Holds the grundy numbers that the current number's descendants have
        desc = []
        #Check if any possibiliities are already in the dictionary, if not, add them
        for p in poss:
            if p in D.keys():
                desc.append(D[p])
            #Don't put negatives in the dictionary
            elif p < 0:
                pass
        #Set the current number in the dictionary to have min grundy number not appearing in its possibilities
        D[i] = mex(desc)
    return D.get(pile)

#Returns the minimum natural number not in the list
def mex(grundy):
    small = 0
    while small in grundy:
        small = small + 1
    return small

