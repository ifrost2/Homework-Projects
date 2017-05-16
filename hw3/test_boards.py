from board import Board
import random


#######################        TestBoard Class        ########################
#
#  Below you can create test board classes that have different heuristics
# from your main Board (through method overriding). You can use these to test
# the efficacy of your main heuristic though a simulated game.
#
# Note: You must also overload the children function in order to call the correct
# constructor.
#  ##############################################################################



###################  TEST 1   ############################################

class TestBoard1(Board):

    def __init__(self, orig=None, hash=None):
        super().__init__(orig=orig, hash=hash)


    def children(self):
        children = []
        for i in range(7):
            if len(self.board[i]) < 6:
                child = TestBoard1(self)
                child.makeMove(i)
                children.append((i, child, child.hash()))
        return children

    ###################  YOUR TEST HEURISTIC HERE   ####################

    def heuristic(self):
        return 0


###################  TEST 2   ############################################

class TestBoard2(Board):
    def __init__(self, orig=None, hash=None):
        super().__init__(orig=orig, hash=hash)

    def children(self):
        children = []
        for i in range(7):
            if len(self.board[i]) < 6:
                child = TestBoard2(self)
                child.makeMove(i)
                children.append((i, child, child.hash()))
        return children

    ###################  YOUR TEST HEURISTIC HERE   ####################

    def heuristic(self):
        return 0


###################  TEST 3   ############################################

class TestBoard3(Board):
    def __init__(self, orig=None, hash=None):
        super().__init__(orig=orig, hash=hash)

    def children(self):
        children = []
        for i in range(7):
            if len(self.board[i]) < 6:
                child = TestBoard3(self)
                child.makeMove(i)
                children.append((i, child, child.hash()))
        return children

    ###################  YOUR TEST HEURISTIC HERE   ####################

    def heuristic(self):
        return 0


#######################        NaiveBoard Class        ########################
#
#  Heuristic based on pseudo-randomness. This is the bar you must beat.
#
#  DO NOT CHANGE - USE THE ABOVE CLASSES FOR YOUR TESTING
#  ##############################################################################


class NaiveBoard(Board):
    def __init__(self, orig=None, hash=None):
        super().__init__(orig=orig, hash=hash)

    def children(self):
        children = []
        for i in range(7):
            if len(self.board[i]) < 6:
                child = NaiveBoard(self)
                child.makeMove(i)
                children.append((i, child, child.hash()))
        return children

    def heuristic(self):
        return random.randint(-10,10)
