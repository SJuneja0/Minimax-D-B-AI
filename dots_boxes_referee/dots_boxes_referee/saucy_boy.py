import referee
import communicator
import board
import time

"""Functions"""



# Input: Array of the current board-state and the time limit for the AI
# Output: Null
# Purpose: Decides the optimal move and publishes it to the referee, this is the main function
def decide_move(current_board, time_limit):
    pass


# Input: Two tuples (representing the points for a potential move)
# Input: Array of the current board-state
# Output: Boolean (true if the move suggested is valid)
# Purpose: To check if a given move is valid
def valid_move(rowNum, colNum, isVertical, board):
    bd = board()
    if rowNum >= len(board[0]) or rowNum < 0 or colNum >= len(board[0][0]) or colNum < 0:
        return False
    elif bd.isTaken(rowNum, colNum, isVertical, board):
        return False
    return True


# Input: Board
# Input: Name to write to the spot
# Output: Array of possible valid board states
# Purpose: Given a board state, this finds all children states (next possible moves)
def generate_possible_moves(curr_board, name):
    valid_child_boards = []
    for i in len(board):
        direction = curr_board[i]
        for j in len(direction):
            row = direction[j]
            for k in len(row):
                line = row[k]
                if line == "":
                    new_valid_board = curr_board.copy()
                    new_valid_board[i][j][k] = name
                    valid_child_boards.append(new_valid_board)  # may need to be new_valid_board.copy
    # generate all possible horizontal lines and save them as new boards
    return valid_child_boards

# Input: Int of how long to run the timer
# Output: Boolean (true when timer runs out)
# Purpose: To tell how long a certain time has passed
def timer(time_limit): #moved to decide_move
    pass


"""Search Method"""


# Input: Array of the current board-state
# Output: Two tuples of a valid move and it's value
# Purpose: To decide the next move
def mini_max(time_limit):
    timer._start_time = time.perf_counter()
    while (curr - timer._start_time <= time_limit):
        curr = time.perf_counter
    pass


# Input:
# Output:
# Purpose:
def alpha_beta(time_limit):
    pass


"""Heuristics"""


# Input:
# Output:
# Purpose:
def h_control_center():
    pass


# Input:
# Output:
# Purpose:
def h_maintain_connectivity():
    pass


# Input:
# Output:
# Purpose:
def h_avoid_single_dots():
    pass


# Input:
# Output:
# Purpose:
def h_counting_score():
    pass


# Input: Array of a suggested board state
# Output: Int of how good that board state is for our AI
# Purpose: To tell how good a theoretical move is
def utility_fcn():
    pass


