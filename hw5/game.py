import sys
import random
from rod import Rod

############################################################
#********************Game Class*****************************
############################################################
'''
The game class represents the state of a game (i.e., some combination
of disks on some number of pegs).

To create the starting game state, pass the constructor the number of rods,
number of disks, and target rod that you desire. Rods are zero-indexed, so keep that
in mind when you pass the target rod.

You can see a graphical representation of the game state by calling printGame. The
first rod (rod 0) will be on the top.

You can also construct a gameState using one of the utility functions below.

From a game state, you can move to other game states by calling the makeMove function.
You will need to utilize this function in order to generate the game tree,
so that you can traverse it.

NOTE: You can only create game boards with up to 8 rods.

'''
class Game:

    def __init__(self, numRods, numDisks, targetRod):
        self.rods = []
        self.numDisks = numDisks

        if(numRods < 9):
            self.numRods = numRods
        else:
            raise ValueError("Number of rods must be 8 or less!")

        if(targetRod < numRods):
            self.targetRod = targetRod
        else:
            raise ValueError("Target rod must be < number of rods!")

        for i in range(numRods):
            self.rods.append(Rod(numDisks))

        for disk in range(numDisks, 0, -1):
            self.rods[0].add(disk)

    #####################################################
    '''
    Returns true once the target rod contains all of the disks

    NOTE: This does NOT validate disk order. It assumes user has
    utilized makeMove function to validate all moves. This validation
    was bypasses for efficiency
    '''
    def isFinished(self):
        return self.rods[self.targetRod].numDisks() == self.numDisks

    #####################################################

    #####################################################
    '''
    Moves a disk from a rod to another rod

    Returns the move tuple (disk, fromRod, toRod) if it completes successfully

    If failure, NO MOVE IS MADE
    Returns -1 if the disk cannot be placed on the new rod
    Returns -2 if the old rod is empty
    '''
    def makeMove(self, fromRod, toRod):

        fRod = self.rods[fromRod]

        if(not fRod.isEmpty()):
           disk = fRod.remove()
        else:
           return -2

        tRod = self.rods[toRod]
        if(tRod.isValidAddition(disk)):
            tRod.add(disk)
        else:
            fRod.add(disk)
            return -1

        return (disk, fromRod, toRod)

    #####################################################


    #####################################################
    '''
    Hashing logic

    Returns a unique integer for every game state

    The hash is a set of 3-bit sequence.
    The numberical value of the ith sequnce represents the rod number
    upon which the ith disk is held. This will be unique for every game
    state.

    Since each combination only has 3 bits, only eight rods
    can be represented in a game if you want gauranteed unique hashes.

    '''
    def hash(self):
        output = 0
        for i in range(self.numRods):
            output += self.rods[i].hash(i)
        return output

    #####################################################


    #####################################################
    '''
    Instantiates a new game that has all of the same properties
    as the original
    '''

    def makeCopy(self):

        new = Game(self.numRods, self.numDisks, self.targetRod)
        for i in range(self.numRods):
            new.rods[i] = self.rods[i].makeCopy()
        return new

    #####################################################


    #####################################################
    '''
    Utility function that prints out the game horizontally
    '''

    def printGame(self):
        for rod in self.rods:
            sys.stdout.write(rod.toString() + "\n")
            sys.stdout.flush()
        sys.stdout.write("\n")
        sys.stdout.flush()

    #####################################################


    #####################################################
    '''
    TODO

    Develop a function that returns a list of all of the
    possible children (with their corresponding moves) for this
    game state.

    The list should contain tuples that are formatted as such:
    [(child1, move1), (child2, move2), ... (childn, moven)]

    The makeMove function returns the move structure that you need
    to combine with the children. See the makeMove function for
    more information.
    '''
    #Given by Scott as my successor function wouldn't work for some reason
    #Detailed issue before my commented-out successor function
##    def successor(self):
##        temp = self.makeCopy()
##        allChildren = [(i,j) for i in range(len(self.rods)) for j in range(len(self.rods))]
##        print(allChildren)
##        results = []
##        for x in allChildren:
##            copy = self.makeCopy()
##            res = copy.makeMove(x[0],x[1])
##            if res == -1 or res == -2 or x[0] == x[1]:
##                continue
##            results.append((copy, res))
##        return results

    # I believe the reason this didn't work is due to how Jack's hash
    # function works, so I updated it to be more like Scott's
    # The hash function of Jack's requires a new table to be created
    # in order for a new hash to be given to it.
    # My issue was that keeping the table the same doesn't play nice
    # With how Jack's hash function works.
    # It gives all the right moves, but the board is the same, so the
    # has function doesn't differentiate when passing to parentTrace
##    def succ(self):
##        possible = []
##        temp = self.makeCopy()
##        for i in range(temp.numRods):
##            #If it is an invalid move as the from rod is empty
##            if temp.rods[i].isEmpty():
##                    pass
##            else:
##                for j in range(temp.numRods):
##                    #If it is an invalid move as they are the same rod
##                    if i == j:
##                        pass
##                    elif temp.rods[j].isEmpty():
##                        #Get just the top element of the from Rod, then add it back
##                        fromTop = temp.rods[i].remove()
##                        temp.rods[i].add(fromTop)
##                        #Show what the move should be by moving
##                        move = temp.makeMove(i,j)
##                        possible.append((temp, move))
##                        #Move back
##                        temp.makeMove(j,i)
##                    else:
##                        #Get the top disc of the From Rod and the To Rod, then add them back
##                        fromTop = temp.rods[i].remove()
##                        temp.rods[i].add(fromTop)
##                        toTop = temp.rods[j].remove()
##                        temp.rods[j].add(toTop)
##                        #If it is possible to move from the current From rod to the current To Rod
##                        if fromTop < toTop:
##                            #Show what the move should be by moving
##                            move = temp.makeMove(i,j)
##                            possible.append((temp, move))
##                            #Move back 
##                            temp.makeMove(j,i)
##                        else:
##                            pass
##        return possible

    #Based on Scott's as it needed to be a new copy to get a different hash
    #Combine all three of my if cases to be how Scott's works
    def successors(self):
        possible = []
        temp = self.makeCopy()
        for i in range(temp.numRods):
            for j in range(temp.numRods):
                #Create a new copy each time
                temp = self.makeCopy()
                result = temp.makeMove(i,j)
                #If the move is invalid or moving to itself, continue on
                #This is utilizing the makeMove function instead of my if
                #statements in my original successor function
                if result == -1 or result == -2 or i == j:
                    continue
                possible.append((temp, result))
        return possible
        


    #####################################################

    #####################################################
    '''
    TODO

    Develop a heuristic that estimates the amount of moves left
    to complete the game

    You should aim for your heuristic to be admissable, but as
    close to the real value as possible
    '''
    def heuristic(self):
        #My heuristic is based on how many disks are not on Goal rod plus
        #2 times the number of disks on Goal that are less than at least 1
        #disk not on Goal
        #numDisks not on G + 2(numDisks on G < Di) where Di is not on G
        #It is admissible because whenever we have disks on the goal before
        #bigger disks, we must remove them and, eventually, put them back.
        #We must also get all disks not on the goal to the goal rod.
        temp = self.makeCopy()
        #Keeps track of disks not already on the goal rod
        others = 0
        #Keeps track of disks on the goal rod that are smaller than at least
        #one disk not on the goal rod
        greater = 0
        goalDisks = []
        smaller = []
        #Create a list of disks on the goal rod
        while(not temp.rods[temp.targetRod].isEmpty()):
            goalDisks.append(temp.rods[temp.targetRod].remove())
        #Check all other rod's disks to see how many disks are out there total
        #as well as how many are greater than at least one disk on the goal rod
        for i in range(temp.numRods):
            #Don't check against itself
            if i == temp.targetRod:
                pass
            else:
                #As long as the current rod isn't empty
                while(not temp.rods[i].isEmpty()):
                    others += 1
                    topDisk = temp.rods[i].remove()
                    #Check against the disks that are currently on the goal rod
                    for j in goalDisks:
                        #If the current disk is bigger than one of the disks and it isn't already
                        #listed as a smaller disk, add it to the smaller disks and increment greater
                        if j < topDisk and j not in smaller:
                            greater += 1
                            smaller.append(j)
        return others + (2 * greater)
        
    #####################################################


############################################################
#************* Utility Functions ***************************
############################################################

#####################################################
'''
Utility function that returns a random, valid configuration of
disks on the rods
'''
def randomShuffle(numRods, numDisks, targetRod):
    new = Game(numRods, numDisks, targetRod)

    for rod in new.rods:
        rod.removeAll()

    for disk in range(numDisks, 0, -1):
        random.choice(new.rods).add(disk)

    return new

#####################################################

#####################################################
'''
Utility function that creates the objective game state
(i.e., all of the disks are placed on the final rod.
'''
def constructTargetGame(numRods, numDisks, targetRod):
    new = Game(numRods, numDisks, targetRod)

    for rod in new.rods:
        rod.removeAll()

    for i in range(numDisks, 0, -1):
        new.rods[targetRod].add(i)

    return new
#####################################################


#####################################################
'''
Utility function that converts a hash value (see hash function above)
into the corresponding game state object.
'''
def constructGame(hash, numRods, numDisks, targetRod):
    new = Game(numRods, numDisks, targetRod)

    for rod in new.rods:
        rod.removeAll()

    for i in range(numDisks, 0, -1):
        bit1 = (hash >> (3 * (i - 1))) & 1
        bit2 = (hash >> (3 * (i - 1) + 1)) & 1
        bit3 = (hash >> (3 * (i - 1) + 2)) & 1

        rodNum = bit1 + (bit2 * 2) + (bit3 * 4)
        new.rods[rodNum].add(i)

    return new
#####################################################
