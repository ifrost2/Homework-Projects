#######################        BOARD CLASS        ###########################
# The Board class is the data structure that holds the Connect 4 boards and the game operations

# The Connect 4 board is 7 cells wide and 6 cells tall

# The underlying data structure is a 2-d list
# The first dimension is the column; the second dimension is the row
# Note: each column ONLY contains pieces (no empty cell). Thus, the array is jagged.

# Every cell in the above list contains either a 0 or a 1. Player 1 is represented by 0 tiles, and Player
# 2 is represented by 1 tiles. Yes, this is confusing, but it helps with the efficiency of the code.
#
##############################################################################
class Board(object):

    #static class variables - shared across all instances
    HEIGHT = 6
    WIDTH = 7

    ########################   Constructor   ###############################
    #
    #
    #  No arguments --> Creates a brand new empty board
    #
    #  orig         --> If you pass an existing board as the orig argument,
    #                   this will create a copy of that board
    #
    #  hash         --> Constructs a board from an integer hash heuristic; to
    #                   be used in conjunction with the hash method
    #
    # *NOTE: orig and hash are mutually exclusive
    ########################################################################
    def __init__(self, orig=None, hash=None):

        #copy
        if(orig):
            self.board = [list(col) for col in orig.board]
            self.numMoves = orig.numMoves
            self.lastMove = orig.lastMove
            return

        #creates from hash - NOTE: Does not understand move order
        elif(hash):
            self.board = []
            self.numMoves = 0
            self.lastMove = None

            #convert to base 3
            digits = []
            while hash:
                digits.append(int(hash % 3))
                hash //= 3

            col = []
            
            for item in digits:
                
                #2 indicates new column
                if item == 2:
                    self.board.append(col)
                    col = []
                
                #otherwise directly append base number
                else:
                    col.append(item)
                    self.numMoves += 1
            return

        #create new
        else:
            self.board = [[] for x in range(self.WIDTH)]
            self.numMoves = 0
            self.lastMove = None
            return


    ########################################################################
    #                           Mutations
    ########################################################################

    # Puts a piece in the appropriate column and checks to see if it was a winning move
    # Pieces are either 1 or 0; automatically decided
    # NOTE: does NOT check if the move is valid
    def makeMove(self, column):
        
        #update board data
        piece = self.numMoves % 2
        self.lastMove = (piece, column)
        self.numMoves += 1
        self.board[column].append(piece)


    # Generates a list of the valid children of the board
    # A child is of the form (move_to_make_child, child_object)
    def children(self):
        children = []
        for i in range(7):
            if len(self.board[i]) < 6:
                child = Board(self)
                child.makeMove(i)
                children.append((i, child))
        return children


    ########################################################################
    #                           Observations
    ########################################################################
    
    # Returns a unique decimal number for each board object based on the
    # underlying data
    # NOTE: it is not important that you understand how this works
    def hash(self):

        power = 0
        hash = 0

        for column in self.board:
            
            #add 0 or 1 depending on piece
            for piece in column:
                hash += piece * (3 ** power)
                power += 1
            
            #add a 2 to indicate end of column
            hash += 2 * (3 ** power)
            power += 1

        return hash

    # Prints out a visual representation of the board
    # X's are 1's and 0's are 0s
    def print(self):
        print("")
        print("+" + "---+" * self.WIDTH)
        for rowNum in range(self.HEIGHT - 1, -1, -1):
            row = "|"
            for colNum in range(self.WIDTH):
                if len(self.board[colNum]) > rowNum:
                    row += " " + ('X' if self.board[colNum][rowNum] else 'O') + " |"
                else:
                    row += "   |"
            print(row)
            print("+" + "---+" * self.WIDTH)

    # Return true iff the game is full
    def isFull(self):
        return self.numMoves == 42

    ###################  Your Code Here ################################################

    # Returns true iff the board is in a terminal position (4-in-a-row somewhere in board)
    def isWinner(self):
        #Loop through the columns
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                #Check for horizontal win (Only looks if there are at least three pieces before it)
                if i > 2:
                    #Make sure there are pieces in each place in that board
                    if len(self.board[i-1]) > j and len(self.board[i-2]) > j and len(self.board[i-3]) > j:
                        if self.board[i][j] == self.board[i-1][j] == self.board[i-2][j] == self.board[i-3][j]:
                            return True
                        else:
                            pass
                    else:
                        pass
                #Check for the vertical win(Only looks if there are at least three pieces below it)
                if j > 2:
                    if self.board[i][j] == self.board[i][j-1] == self.board[i][j-2] == self.board[i][j-3]:
                        return True
                    else:
                        pass
                #Check for top right->bottom left diagonal win(Only looks if there are at least three pieces
                #above and before it)
                if i > 2 and j > 2:
                    #Check to make sure there are pieces in the other places to be checked
                    if len(self.board[i-1]) > j-1 and len(self.board[i-2]) > j-2 and len(self.board[i-3]) > j-3:
                        if self.board[i][j] == self.board[i-1][j-1] == self.board[i-2][j-2] == self.board[i-3][j-3]:
                            return True
                        else:
                            pass
                    else:
                        pass
                #Check for top left->bottom right diagonal win(Only looks if there are at
                #least three pieces below and ahead of it)
                if i < 4 and j > 2:
                    #Check to make sure there are pieces in the other places to be checked
                    if len(self.board[i+1]) > j - 1 and len(self.board[i+2]) > j-2 and len(self.board[i+3]) > j-3:
                        if self.board[i][j] == self.board[i+1][j-1] == self.board[i+2][j-2] == self.board[i+3][j-3]:
                            
                            return True
                        else:
                            pass
                    else:
                        pass
                else:
                    pass
        return False
    


    # Returns a heuristic for the board position
    # Good positions for 0 pieces should be positive and good positions for 1 pieces
    # should be negative
    #Checks for current player then subtracts in-a-rows for opposing player
    def heuristic(self):
        player = self.numMoves % 2
        count = 0
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                #Check each board piece to see if that one has the current player's piece
                #Update count depending on how many in a row
                if self.board[i][j] == player:
                    count += self.verticals(player, i, j)
                    count -= self.verticals((player + 1) % 2, i,j)
                    count += self.horizontals(player, i, j)
                    count -= self.horizontals((player + 1) % 2, i, j)
                else:
                    pass
        return count

##    #OTHER HEURISTIC
##        count = 0
##        count += self.middle(player)
##        count -= self.middle((player + 1) % 2)
##        return count

##OTHER HEURISTIC HELPER FUNCTIONS
##    #Checks how many pieces this player has in the middle 3 columns
##    #Gives more priority to pieces in the middle than pieces on the outside edges
##    def middle(self, player):
##        count = 0
##        for i in range(2, 4):
##            for j in range(len(self.board[i])):
##                if self.board[i][j] == player:
##                    count += 10
##                else:
##                    pass
##        for i in [1,5]:
##            for j in range(len(self.board[i])):
##                if self.board[i][j] == player:
##                    count += 3
##                else:
##                    pass
##        for i in [0,6]:
##            for j in range(len(self.board[i])):
##                if self.board[i][j] == player:
##                    count += 1
##                else:
##                    pass
##        return count
    
    #Checks for horizontal in-a-row (left -> right / right -> left)
    #This function will double count but its fine
    def horizontals(self, player, col, row):
        #Holds how many pieces are in a row (1 to start with)
        if self.board[col][row] == player:
            count = 1
        else:
            count = 0
        #Makes sure we stay in index
        colBack = max(col - 1, 0)
        colFor = min(col + 1, 6)
        #Keep adding if there are pieces to the right that match current player
        #Return 1000 to ensure choosing this board
        if colBack == col:
            #Each of these if statements makes sure that there are enough pieces to
            #reach this rows height
            if len(self.board[colFor]) >= row + 1:
                while self.board[colFor][row] == player:
                    count += 1
                    colFor += 1
                    #Each of these similar if statements in the other while loops
                    #Is there to prevent the indexing to get out of range
                    if len(self.board[colFor]) < row + 1 or colFor > 6:
                        break
        #Keep adding if there are pieces to the left that match current player
        elif colFor == col:
            if len(self.board[colBack]) >= row + 1:
                while self.board[colBack][row] == player and colBack > 0:
                    count += 1
                    colBack -= 1
                    if len(self.board[colBack]) < row + 1 or colBack < 0:
                        break
        #If it is in the middle
        #Add until left is exhausted, then until right is exhausted
        else:
            if len(self.board[colBack]) >= row + 1:
                while self.board[colBack][row] == player:
                    count += 1
                    colBack -= 1
                    if len(self.board[colBack]) < row + 1 or colBack < 0:
                        break
            if len(self.board[colFor]) >= row + 1:
                while self.board[colFor][row] == player and colFor < 6:
                    count += 1
                    colFor += 1
                    if len(self.board[colFor]) < row + 1:
                        break
        #Returns weight based on how many in a row for this player
        if count >= 4:
            return 1000
        elif count == 3:
            return count * 100
        elif count == 2:
            return count * 10
        else:
            return count
                               
    #Checks for vertical in-a-row (up -> down / down -> up)
    #This function will double count but its fine
    def verticals(self, player, col, row):
        if self.board[col][row] == player:
            count = 1
        else:
            count = 0
        rowDown = max(row - 1, 0)
        rowUp = min(row + 1, len(self.board[col]) - 1)
        #If the piece is the bottom one
        if rowDown == row:
            #Make sure that there are elements in the current column to be reached
            if rowUp + 1 <= len(self.board[col]):
                while self.board[col][rowUp] == player and rowUp < 7:
                    count += 1
                    rowUp += 1
                    if rowUp + 1 > len(self.board[col]):
                        break
        #If the piece is the top in the row
        elif rowUp == row:
            #Make sure that there are elements to be reached
            if rowDown + 1 <= len(self.board[col]):
                while self.board[col][rowDown] == player and rowDown > 0:
                    count += 1
                    rowDown -= 1
                    if rowDown + 1 < 0:
                        break
        #If the piece is in the middle of the column
        else:
            if rowUp + 1 <= len(self.board[col]):
                while self.board[col][rowUp] == player:
                    count += 1
                    rowUp += 1
                    if rowUp + 1 > len(self.board[col]):
                        break
            if rowDown + 1 <= len(self.board[col]):
                while self.board[col][rowDown] == player:
                    count += 1
                    rowDown -= 1
                    if rowDown < 0:
                        break
        if count >= 4:
            return 1000
        elif count == 3:
            return count * 100
        elif count == 2:
            return count * 10
        else:
            return count

