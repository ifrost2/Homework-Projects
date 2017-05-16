
from search import Search
from test_boards import TestBoard1, TestBoard2, TestBoard3, NaiveBoard
from board import Board
import client
import random


class Game:


    ########################################################################
    #                     Simulate a Local Game
    #
    #  isPlayer1 - True iff you want to be player 1
    #  opponentBoard - One of the TestBoards in test_boards.py
    #  depth - How far do you want each player to look
    #
    #  DO NOT EDIT! Use the custom local game to work with in the bonus problem
    ########################################################################

    def simulateLocalGame(self, isPlayer1, opponentBoard, depth):

        you = Board()
        opponent = opponentBoard

        search = Search()

        for i in range(42):

            if isPlayer1:
                move = search.findMoveAB(you, depth)
            else:
                move = search.findMoveAB(opponent, depth)

            you.makeMove(move)
            opponent.makeMove(move)

            you.print()

            if you.isWinner():
                if you.numMoves % 2:
                    print("Player 1 Wins!")
                else:
                    print("Player 2 Wins!")

                break

            isPlayer1 = not isPlayer1




    ########################################################################
    #                     Simulate a Custom Local Game
    #
    #  Same as above, but you can edit the parameters and gameplay algorithm
    #  to test your AI for the bonus problem
    ########################################################################

    def simulateCustomLocalGame(self, isPlayer1, youBoard, opponentBoard, depth):

        you = youBoard
        opponent = opponentBoard

        search = Search()

        for i in range(42):

            if isPlayer1:
                move = search.findMoveAB(you, depth)
            else:
                move = search.findMoveAB(opponent, depth)

            you.makeMove(move)
            opponent.makeMove(move)

            you.print()

            if you.won:
                if you.numMoves % 2:
                    print("Player 1 Wins!")
                else:
                    print("Player 2 Wins!")

                break

            isPlayer1 = not isPlayer1

        ########################################################################
        #               Simulate a Remote Game (against our server)
        #
        #  youBoard - The board you want to have play against the server AI
        #  isPlayer1 - true iff you want to be player 1
        #  difficulty - 1 (easy), 2 (med), 3 (hard) | deafult = 1
        #  depth - How deep do you want your search to look
        #
        #  DO NOT EDIT!
        ########################################################################

        def simulateRemoteGame(self, yourBoard, isPlayer1, difficulty, depth):

            #checks if proper difficulty
            if difficulty < 1 or difficulty > 3:
                print("Invalid difficulty! Choose 1, 2, or 3!")
                return

            #initialize
            session = random.randint(0, 100000)
            you = yourBoard
            search = Search()

            #play game
            for i in range(42):
                if isPlayer1:
                    move = search.findMoveAB(you, depth)
                else:
                    move = client.get_server_move(you, session, difficulty)

                    #check to see if you sent your move back in time
                    if move == -1:
                        print("Your algorithm took too long to make a move. The AI got bored and quit.")
                        return

                #execute move and print
                you.makeMove(move)
                you.print()

                #check if terminal position
                if you.won:
                    if isPlayer1:
                        client.get_server_move(you, session, difficulty)
                    if you.numMoves % 2:
                        print("Player 1 wins")
                    else:
                        print("Player 2 wins")

                    break

                #switch players
                isPlayer1 = not isPlayer1



########################################################################
#                     Benchmark Game
#
# You, as Player 1, must consistently win the below game in order to score
# maximum points on this assignment. Uncomment the game once you are ready
# to run the game.
#
########################################################################

#Game().simulateRemoteGame(NaiveBoard(), True, 1, 4)
Game().simulateLocalGame(True, NaiveBoard(), 4)
