import requests
import json

PORT = 28464
URL = 'http://silo.cs.indiana.edu' + ':' + str(PORT) + '/'

# takes a board as a json string
# takes a difficulty: 1 (easy), 2 (medium), 3 (hard)
# returns the move from the server
def get_server_move(board,sid,difficulty=1):

    # go to proper url location
    url = URL + str(difficulty)

    # our query will be the board state
    payload = jsonify_board(board,sid)

    # send request, our response will be a move
    res = requests.put(url, data=payload)

    # check if the server sent a text message response
    # such as error, or you win
    try:
        message = int(res.text)
    except:
        print(res.text)
        return

    # return that move
    return int(res.text)

def jsonify_board(board,sid):
    to_json = {
            'board':board.board,
            'numMoves':board.numMoves,
            'lastMove':board.lastMove, 
            'sid':sid
            }
    return json.dumps(to_json)

