
import math
from board import Board


class Search:


    def __init__(self):

        #for dynamic programming
        self.resolved = {}

        #for iterative deppening
        self.orderingFunction = self.defaultOrder
        self.oldResolved = {}



    ########################################################################
    #                       Alpha Beta Implementation
    ########################################################################

    #returns the optimal column to move in
    def findMoveAB(self, board, depth):

        #used later for iterative deepening and dynamic programming
        self.orderingFunction = self.defaultOrder
        self.resolved = {}

        #state initializations
        if board.numMoves % 2:
            player = False
        else:
            player = True
        return self.alpha_beta(board, depth, player, -math.inf, math.inf)[1]

    # returns a tuple (value, move) indicating the game value of the game
    # created by moving in the optimal column
    def alpha_beta(self, board, depth, player, alpha, beta):
        #If this is its first move
        #Based on research it is always best to start in the middle spot
        if type(board) == type(Board()) and (board.numMoves == 0 or board.numMoves == 1):
            return (10000, 3)
        bestMove = 0
        bestValue = 0
        #Which child are we currently looking at (aka which move are we potentially doing)
        i = 0
        #Keep getting children until board state is terminal or depth is 0
        if board.isFull():
            return (0, 0)
        #If the current player is the player who is evaluating the board state
        if board.isWinner():
            if (player + depth) % 2 == 0:
                return (100000, bestMove)
            else:
                return (-100000, bestMove)
        if depth > 0:
            for child in board.children():
                #Checks if it in the dictionary of moves
                #Assuming the hash function allows = board states to be equal
                if child[1].hash() in self.resolved:
                    (bestValue, bestMove) = self.resolved[child[1].hash()]
                #if it isn't already defined, set the value to be equal to the best value of the children
                else:
                    bestValue = self.alpha_beta(child[1], depth - 1, (player + 1) % 2, alpha, beta)[0]
                    self.resolved[child[1].hash()] = (bestValue, i)
                if (player + depth) % 2 == 0:
                    if bestValue >= alpha:
                        alpha = bestValue
                        bestMove = child[0]
                else:
                    if bestValue <= beta:
                        beta = bestValue
                        bestMove = child[0]
                
                if alpha >= beta:
                    break
                i += 1
            return (bestValue, bestMove)
        else:
            print(len(self.resolved))
            return (board.heuristic(), bestMove)

##        #This was a previous version that worked but didn't have dynamic programming or alpha beta working fully
##        #However, since the dynamic programming one was acting funny, I decided to use this one
##        #I am going to bring my computer to class because I ran into this problem on Sunday night.
##        pastChildren = [board]
##        currentChildren = []
##        while depth > 0 and not board.isFull():
##            #Get a list of all possible moves
##            for b in pastChildren:
##                c = b.children()
##                #Check each move if it is better than a previous one
##                for child in c:
##                    if player == 0:
##                        if child[1].heuristic() > alpha:
##                            alpha = child[1].heuristic()
##                            bestMove = child[0]
##                            bestValue = child[1].heuristic()
##                        else:
##                            pass
##                    else:
##                        if child[1].heuristic() < beta:
##                            beta = child[1].heuristic()
##                            bestMove = child[0]
##                            bestValue = beta
##                    #This stops it from looking at the rest of the children
##                    if alpha > beta:
##                        break
##                    currentChildren.append(child[1])
##            pastChildren = currentChildren
##            currentChildren = []
##            depth -= 1
##        return(bestValue, bestMove)
    
        
        
            
            
        



    ########################################################################
    #             Iterative Deepning - Bonus
    ########################################################################

    #used for normal alpha-beta
    def defaultOrder(self, children, player):
        return children

    #used for ordering with ID algorithm
    def bestFirstOrder(self, children, player):
        pass


    #returns the best move using ID approach to generating best-first
    #search alpha-beta
    def findMoveID(self, board):
        pass
