import queue
import tree_node as treeNode

import referee
import communicator
import board
import time

"""Functions"""


class saucy_boy:

    def __init__(self, opponent):
        self.bd = board.Board(10, 10, "SaucyBoy")
        self.our_board = self.bd.create_board()
        self.queue = queue()  # TODO MAKE QUEUE CLASS
        self.tree = treeNode.treeNode()  # TODO make tree node
        self.name = "SaucyBoy"
        self.opponent = opponent # possibly change

    # Input: Array of the current board-state and the time limit for the AI
    # Output: Null
    # Purpose: Decides the optimal move and publishes it to the referee, this is the main function
    def decide_move(self, current_board, time_limit):
        pass

    # Input: Two tuples (representing the points for a potential move)
    # Input: Array of the current board-state
    # Output: Boolean (true if the move suggested is valid)
    # Purpose: To check if a given move is valid
    def valid_move(self, rowNum, colNum, isVertical, board):
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
    def generate_possible_moves(self, curr_board, name):
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
    def timer(self, time_limit):  # moved to decide_move
        pass

    """Search Method"""

    # Input: Array of the current board-state
    # Output: Two tuples of a valid move and it's value
    # Purpose: To decide the next move
    def mini_max(self, treeNode, depth, isMaximizing, alpha, beta):
        # if the game would be over or if this is the bottom node so far
        if not treeNode.children:
            return self.utility_fcn(treeNode.board, self.name, self.opponent)
        if isMaximizing:
            maxValue = 999
            for child in treeNode.children:
                value = self.mini_max(child, depth-1, False, alpha, beta)
                maxValue = max(value, maxValue)
                alpha = max(alpha, value)
                if beta <= alpha:
                    break
            return maxValue
        else:
            minValue = -999
            for child in treeNode.children:
                value = self.mini_max(child, depth-1, True, alpha, beta)
                minValue = min(value, minValue)
                beta = min(beta, value)
                if beta <= alpha:
                    break
            return minValue

    # Input:
    # Output:
    # Purpose:
    def alpha_beta(self, time_limit):
        pass

    """Heuristics"""

    # Input: Array of a suggested board state
    # Output: Int of how good that board state is for our AI
    # Purpose: To tell how good a theoretical move is
    def utility_fcn(self, curr_board, player_name, opponent_name):
        ai_score = 0
        opponent_score = 0

        # Count the number of completed boxes for each player.
        for box in curr_board.completed_boxes:
            if box.owner == player_name:
                ai_score += 1
            elif box.owner == opponent_name:
                opponent_score += 1

        # Evaluate edge control.
        ai_edges = len(curr_board.edges_controlled_by(player_name))
        opponent_edges = len(curr_board.edges_controlled_by(opponent_name))

        # Consider the number of available moves.
        ai_moves = len(curr_board.get_legal_moves())

        # Fine-tune the weights for different factors as needed.
        box_control_weight = 1.0
        edge_control_weight = 0.5
        available_moves_weight = 0.2

        # Calculate the heuristic score by combining factors.
        heuristic_score = (box_control_weight * (ai_score - opponent_score) +
                           edge_control_weight * (ai_edges - opponent_edges) +
                           available_moves_weight * ai_moves)

        return heuristic_score
