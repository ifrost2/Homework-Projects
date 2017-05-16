from game import *
import queue
from priorityq import PQ
import time


############################################################
#*************************** Search ***********************
############################################################
'''
Parent class for the different types of searches. Contains
the mechanic to unwind the path from the parentTrace dictionary
and how to print the path as well.
'''
class Search:
    def __init__(self, start):
        
        #a mapping of nodes to their parents and the transformation move
        #example: parentTrace[child.hash()] = (parent.hash(), move)
        #this stores games as hashes to avoid object references
        self.parentTrace = {}
        
        #the starting game state for the search tree
        self.start = start
        
        #data structures to store the resulting solution paths
        self.gamePath = []
        self.movePath = []
        self.numMoves = 0

    #####################################################
    '''
    Traces the path from the objective state back to the starting
    state using the parentTrace dictionary that is filled during
    the search algorithm
    '''
    def unwindPath(self):
        target = constructTargetGame(self.start.numRods, self.start.numDisks, self.start.targetRod)
        startHash = self.start.hash()
        self.gamePath = [target]
        self.movePath = []
        nextHash = target.hash()

        # traces backwards from the target game state
        while (not startHash == nextHash):
            nextHash, moves = self.parentTrace[nextHash]
            self.gamePath.insert(0, constructGame(nextHash, self.start.numRods, self.start.numDisks, self.start.targetRod))
            self.movePath.insert(0, moves)

        #record number of moves
        self.numMoves = len(self.movePath)
    #####################################################


    #####################################################
    '''
    Provides a graphical representation of the trace
    '''
    def printPath(self, verbose=False):
        # prints out in order

        if verbose:
            counter = 0
            for i in range(len(self.gamePath)):
                if counter == 0:
                    print("ORIGINAL")
                    self.gamePath[i].printGame()
                else:
                    print("MOVE " + str(counter) + ": " + str(self.movePath[counter - 1]))
                    self.gamePath[i].printGame()
                print("--------------------------------------")
                counter += 1
        else:
            pass
            for i in range(len(self.movePath)):
                print("MOVE " + str(i + 1) + ": " + str(self.movePath[i]))
    ########################################################   
    


############################################################
#************* Uninformed DFS Search ***********************
############################################################
'''
 This is an example of how a search of the game tree might look. In this case,
 it is a depth first search. Use this template to familiarize yourself with
 the mechanics of the different data structures.
'''
class DFSSearch(Search):

    def __init__(self, start):
        super().__init__(start)
        self.search()

    #####################################################
    '''
    Completes a depth first search in iterative style (vs recursive).

    It stores all of the node relations in the parentTrace dictionary.
    The keys are the hashes of game states.
    The values are tuples with the hash of its parent combined with the move
    necessary to transform the parent into the key (see makeMove description in
    Game class. Upon finding the finished game state, it using the 
    '''
    def search(self):
        self.parentTrace = {}

        #The search is formatted iteratively (vs. recursively) because python is not optimized for deep recursion
        #and the rescursive solution would either crash the system or take excessively long
        stack = [(self.start,(0,0,0))]
        while(not len(stack) == 0):

            game = stack.pop()[0]
            hash = game.hash()

            #f game is finished, break the loop by returning and ending the search
            #note that there is no need to traverse the entire game tree 
            if game.isFinished():
                
                #before breaking, unwind the path (see parent class)
                self.unwindPath()
                return

            #generate a list of next possible game states
            successors = game.successors()

            #filter out game states that we have already seen
            successors[:] = filter(lambda x: x[0].hash() not in self.parentTrace, successors)

            #record the parent of the next games states and add them to the stack
            for successor in successors:
                self.parentTrace[successor[0].hash()] = (hash, successor[1])
                stack.append(successor)
    #####################################################




############################################################
# ************* Uninformed BFS Search ***********************
############################################################
'''
TODO

Using guidance provided by the template above, create a class
that completes a breadth first search (BFS) of the game tree.
'''


class BFSSearch(Search):
    def __init__(self, start):
        super().__init__(start)
        self.search()

    #####################################################
    '''
    Completes a breadth first search starting at the indicated starting node.
    '''
    #Basically the same as the DFS Search except for a minor change
    #Has to pop the first board in the fringe
    #Complete but not always optimal path
    def search(self):
        self.parentTrace = {}

        stack = [(self.start,(0,0,0))]
        while(not len(stack) == 0):

            game = stack.pop(0)[0]
            hash = game.hash()

            #If game is finished, break the loop by returning and ending the search
            #note that there is no need to traverse the entire game tree 
            if game.isFinished():
                
                #before breaking, unwind the path (see parent class)
                self.unwindPath()
                return

            #generate a list of next possible game states
            successors = game.successors()

            #filter out game states that we have already seen
            successors[:] = filter(lambda x: x[0].hash() not in self.parentTrace, successors)

            #record the parent of the next games states and add them to the stack
            for successor in successors:
                self.parentTrace[successor[0].hash()] = (hash, successor[1])
                stack.append(successor)

    #####################################################

############################################################
# ************* Informed A* Search *************************
############################################################
'''
TODO

Using what you have learned from the DFS and BFS examples, construct and A* search
algorithm that creates the desired parent graph.
'''

class AStarSearch(Search):
    def __init__(self, start):
        super().__init__(start)
        self.search()

    #####################################################
    '''
    TODO
    
    Define your A* search algorithm here.
    
    (1) You should use our priority queue implementation found in the PQ class
    (2) You may need to implement additional data structures in the class
        initialization
    (3) You should aim for an admissable heuristic (or nearly admissable).
        If you choose to implement optimizations based on the consistency of
        your heuristic, you must be able to show that your heuristic is consistent.
    '''
    #Fairly similar in format to the other searches except it utilizes
    #the priority queue and is based off of a heuristic rather than looking
    #for a goal anyway it can find one.
    def search(self):
        self.parentTrace = {}

        #Create priority queue and continue until the queue is empty
        #or the goal is found
        priority = PQ()
        priority.update(self.start, self.start.heuristic())
        while(not priority.isEmpty()):
            game = priority.pop()
            hash = game.hash()

            if game.isFinished():

                self.unwindPath()
                return
            
            successors = game.successors()
            successors[:] = filter(lambda x: x[0].hash() not in self.parentTrace, successors)

            for successor in successors:
                self.parentTrace[successor[0].hash()] = (hash, successor[1])
                #Must add 1 as the cost to get to this point so as not
                #to remove any other ways of getting there that would
                #potentially have less moves
                priority.update(successor[0], successor[0].heuristic() + 1)

    #####################################################

##g = constructGame(108760,5,6,3)
##g = constructGame(270540810,5,10,4)
##g.printGame()

#Used to find average length of time and average length of solutions
#not print
##avgTimeD = 0
##avgTimeB = 0
##avgTimeA = 0
##avgLengthD = 0
##avgLengthB = 0
##avgLengthA = 0
##start = time.time()
##for i in range(1000):
##    g = randomShuffle(5,4,random.randint(0,3))
##    b = DFSSearch(g)
##    avgLengthD += len(b.movePath)
##    if i % 100 == 0:
##        print("D")
##end = time.time()
##avgLengthD = avgLengthB/1000
##avgTimeD += end - start
##avgTimeD = avgTimeD / 1000
##
##start = time.time()
##for i in range(1000):
##    g = randomShuffle(5,4,random.randint(0,3))
##    b = BFSSearch(g)
##    avgLengthB += len(b.movePath)
##    if i % 100 == 0:
##        print("B")
##end = time.time()
##avgLengthB = avgLengthB/1000
##avgTimeB += end - start
##avgTimeB = avgTimeB / 1000
##
##start = time.time()
##for i in range(1000):
##    g = randomShuffle(5,4,random.randint(0,3))
##    b = AStarSearch(g)
##    avgLengthA += len(b.movePath)
##    if i % 100 == 0:
##        print("A")
##end = time.time()
##avgLengthA = avgLengthB/1000
##avgTimeA += end - start
##avgTimeA = avgTimeA / 1000
##
##print("Average DFS =",avgTimeD, "\nAverage BFS =",avgTimeB,
##      "\nAverage A* =",avgTimeA)
##print("Average Length DFS =",avgLengthD, "\nAverage Length BFS =",avgLengthB,
##      "\nAverage Length A* =",avgLengthA)

