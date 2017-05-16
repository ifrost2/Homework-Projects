############################################################
#********************Rod Class*****************************
############################################################
"""
Abstraction representing a single game rod. Disks are stored
as integers (larger disks are larger integers).

Disks are stored in lists from bottom to top. In other words,
the top disk is the last element.

You should NOT edit ANYTHING in this class.
"""

class Rod:

    def __init__(self, height):
        self.disks = []
        self.height = height

    #adds specified disk to the rod
    #NOTE: Validation checking is completed in
    #the games makeMove function of the Game class
    def add(self, disk):
        self.disks.append(disk)

    #Removes a disk from rod
    def remove(self):
        return self.disks.pop()

    #Removes all disks from rod
    def removeAll(self):
        self.disks = []

    #returns true if the rod is empty
    def isEmpty(self):
        return len(self.disks) == 0

    #validates disk addition
    def isValidAddition(self,disk):
        return self.isEmpty() or self.disks[len(self.disks) - 1] > disk

    #returns number of disks on the rod
    def numDisks(self):
        return len(self.disks)

    #returns a string representation of the rod
    def toString(self):
        output = "| "

        for disk in self.disks:
            output += str(disk) + "  "

        for i in range(self.height -self.numDisks()):
            output += "--" + " "

        return output

    #helper function for the game hash
    def hash(self, rod):
        output = 0
        for disk in self.disks:
            output += rod * pow(8, (disk - 1))
        return output

    #helper function for the game copy function
    def makeCopy(self):
        new = Rod(self.height)
        for disk in self.disks:
            new.add(disk)
        return new