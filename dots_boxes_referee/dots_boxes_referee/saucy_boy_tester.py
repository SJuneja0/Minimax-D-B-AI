import referee
import communicator
import board

import time


line = [[[]]]


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
def valid_move(point1, point2):
    pass



"""Search Method"""


# Input: Array of the current board-state
# Output: Two tuples of a valid move and it's value
# Purpose: To decide the next move
def mini_max(time_limit):
    com = communicator.communicator
    board = com.read_board()
    timer_start_time = time.perf_counter()
    while ((curr - timer_start_time) <= time_limit):
        curr = time.perf_counter
    pass


# Input:
# Output:
# Purpose:
def alpha_beta(time_limit):
    pass


"""Heuristics"""

# class heuristic:
#
#     def __init__(self):
#         pass
#     # Input:
#     # Output:
#     # Purpose:
#     def h_control_center(self):
#         COM = communicator.communicator("plz")
#         board = COM.read_board()
#
#         #horizontal
#         value = 0
#         count = 0
#
#         #the board is empty wtf
#         row_num = board[1]#[-1][0]
#         column_num = board[0][-1][1]
#         line = [[[]]]
#         for i in range(row_num):
#             if (board[0][i][0] >= 1):
#                 line[0][i].append(board[0][i][0])
#                 #Value add 0.5
#                 line[0][i][i] += 0.5
#
#         for i in range(column_num):
#             if (board[0][i][1] >= 1):
#                 line[0][i].append(board[0][i][1])
#                 #Value add 0.5
#                 line[0][i][i] += 0.5
#
#         #vertical
#         value = 0
#         row_num = board[1][-1][0]
#         column_num = board[1][-1][1]
#         for j in range(row_num):
#             if (board[1][j][0] >= 1):
#                 line[1][i+j].append(board[1][j][0])
#                 #Value add 0.5
#                 line[1][i+j][j] += 0.5
#
#         for j in range(column_num):
#             if (board[1][j][1] >= 1):
#                 line[1][i+j].append(board[1][j][1])
#                 #Value add 0.5
#                 line[1][i+j][j] += 0.5
#
#         pass
#     # Input:
#     # Output:
#     # Purpose:
#     def h_maintain_connectivity(self, rowNum, colNum, isVertical):
#         coms = communicator.communicator("GG")
#         board_read = coms.read_board()
#         board_class = board.board()
#         neighbors = board_class.getNeighbors(rowNum, colNum, isVertical, board_read)
#         result = []
#         for neighbor in neighbors:
#             if (board_class.isTaken(neighbor[1], neighbor[2], neighbor[0], board_read) == False):
#                 result.append(neighbor[3])
#         return result
#
#
#     # Input:
#     # Output:
#     # Purpose:
#     #def h_avoid_single_dots(self):
#         #board_read = communicator.communicator.read_board()
#         #neighbors = board.getNeighbors()
#         #this may not be needed to apply
#         #pass
#
#
#     # Input: null
#     # Output: returns an array of the score
#     # Purpose: to show what the score is
#     def h_counting_score(self):
#         coms = communicator.communicator("GG")
#         board_read = coms.read_board()
#         board_class = board.board()
#         list_boxes, value = self.boxes()
#         score = [0, 0]
#         for i in range(len(list_boxes[0])):
#             if(value[i] == 0):
#                 score[0] += 1
#             if (value[i] == 1):
#                 score[1] += 1
#
#         return score


# Input: Array of a suggested board state
# Output: Int of how good that board state is for our AI
# Purpose: To tell how good a theoretical move is
def utility_fcn(self):
    ai_score = 0
    opponent_score = 0

    # Count the number of completed boxes for each player.
    for box in board.completed_boxes:
        if box.owner == 'AI':
            ai_score += 1
        elif box.owner == 'GG':
            opponent_score += 1

    # Evaluate edge control.
    ai_edges = len(board.edges_controlled_by('AI'))
    opponent_edges = len(board.edges_controlled_by('Opponent'))

    # Evaluate box control.
    ai_score += ai_score - opponent_score

    # Consider the number of available moves.
    ai_moves = len(board.get_legal_moves('AI'))
    opponent_moves = len(board.get_legal_moves('Opponent'))

    # Combine and balance the factors in your heuristic.
    heuristic_score = (ai_score - opponent_score) + (ai_edges - opponent_edges) + (ai_moves - opponent_moves)

    return heuristic_score

#*if __name__ == "__main__":
    #try:
    #    pass
    #except:
     #   pass


#may be useless
def boxes(self):
    value = []
    count = 0

    coms = communicator.communicator("GG")
    board_read = coms.read_board()
    board_class = board.board()
    box = [[]]

    for i in range(((len(board_read[1][1])%2) * (len(board_read[0][1])%2)) - 1):
        #add the lines
        print(len(board_read[1][1]))
        horizontals = [board_read[0][count]]
        horizontals.append([board_read[0][count+len(board_read[0][1][1])]])

        verticals = [board_read[1][count]]
        print(count)
        print(((len(board_read[1][1])%2) * (len(board_read[0][1])%2)) - 1)
        verticals.append([board_read[1][count+len(board_read[1][1][1])]])
        box[count].append([horizontals, verticals])

        #find out how to count a score
        #value[i] = 1  # 0 and 1 to distingish between self or opponent. 2 as the preinput

        count += 1
        value[i] = 1

    return box, value

#test = heuristic()
board_test = board.board
#test.boxes()
#test.h_counting_score()
#test.h_maintain_connectivity(1, 1, 1)
#test.utility_fcn()


# def minimax(board, depth, alpha, beta, maximizing_player):
#     if depth == 0 or game_over(board):
#         return evaluate_board(board)
#
#     if maximizing_player:
#         max_eval = float('-inf')
#         for move in possible_moves(board):
#             new_board = make_move(board, move)
#             eval = minimax(new_board, depth - 1, alpha, beta, False)
#             max_eval = max(max_eval, eval)
#             alpha = max(alpha, eval)
#             if beta <= alpha:
#                 break  # Prune the remaining branches
#         return max_eval
#     else:
#         min_eval = float('inf')
#         for move in possible_moves(board):
#             new_board = make_move(board, move)
#             eval = minimax(new_board, depth - 1, alpha, beta, True)
#             min_eval = min(min_eval, eval)
#             beta = min(beta, eval)
#             if beta <= alpha:
#                 break  # Prune the remaining branches
#         return min_eval
#
# def best_move(board):
#     best_score = float('-inf')
#     best_move = None
#     alpha = float('-inf')
#     beta = float('inf')
#     for move in possible_moves(board):
#         new_board = make_move(board, move)
#         score = minimax(new_board, 3, alpha, beta, False)  # Adjust the depth as needed.
#         if score > best_score:
#             best_score = score
#             best_move = move
#         alpha = max(alpha, score)
#     return best_move