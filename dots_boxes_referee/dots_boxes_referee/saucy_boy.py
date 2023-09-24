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
        start_timer = time.perf_counter()
        best_move = None
        root_node = treeNode.treeNode(current_board, [], None, True)
        while(start_timer + time_limit >= time.perf_counter):
            self.generate_search_tree()

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

    # TODO: REWRITE THIS TO WORK WITH THE TREE_NODE CLASS, INPUT IS NOW A TREE NODE
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

    """Search Method"""

    # Input: Array of the current board-state
    # Output: A path of the optimal move
    # Purpose: To decide the optimal move given a search tree
    def mini_max(self, treeNode, isMaximizing, alpha, beta, bestFinalPosition):
        # if the game would be over or if this is the bottom node so far (i.e., this position has no children)
        # generate the value of this node based on the utility function
        if not treeNode.children:
            return self.utility_fcn(treeNode.board, self.name, self.opponent)

        # if this node is maximizing (our turn to pick)
        if isMaximizing:
            maxValue = -999  # set the current maxValue to -infinity
            for child in treeNode.children:  # look through children for the greatest value among them
                value = self.mini_max(child, False, alpha, beta, bestFinalPosition)  # look through children's children
                if value > maxValue:
                    maxValue = value
                    if not child.children:  # if a node is the bottom node, and it is the current biggest
                        bestFinalPosition = child  # set it to be the best node
                # Alpha-Beta Pruning
                alpha = max(alpha, value)
                if beta <= alpha:
                    break
            # if this is the starting node, and it's done looking through its children, return the best bottom child
            if treeNode.isRootNode:
                return bestFinalPosition
            return maxValue

        # else if the node is minimizing (opponent's turn to pick)
        else:
            minValue = 999  # set current min value to infinity
            for child in treeNode.children:  # look through children for the greatest value among them
                value = self.mini_max(child, True, alpha, beta, bestFinalPosition)  # look through children's children
                if value < minValue:
                    minValue = value
                    if not child.children:  # if a node is the bottom node, and it is the current smallest
                        bestFinalPosition = child  # set it to be the best node
                beta = min(beta, value)
                if beta <= alpha:
                    break
            return minValue

    # TODO: NEED TO IMPLEMENT THE FACT THAT IF YOU GET A SQUARE, YOU GO AGAIN, DO THIS IN CHILD GENERATION
    # Input: A initial tree node that's children are empty
    # Output: A tree node with children who have children down to a specified depth
    # Purpose: Fills a starting tree node with children down to a specified depth
    def generate_search_tree(self, curr_tree_Node, depth, isOurTurn):
        # if this node is above the limiting depth, generate it's children
        if depth > 0:
            if isOurTurn:
                name = self.name
            else:
                name = self.opponent
            children_boards = self.generate_possible_moves(curr_tree_Node.board, name)
            curr_tree_Node.children = self.generate_possible_moves(curr_tree_Node, name)

        # for each child of this node, generate the children's children (recursively),
        # all editing the original treeNode
        # if there is a new square (one more then the previous boardstate), the player gets another turn
        if not curr_tree_Node.isRootNode:
            if len(curr_tree_Node.came_from.board.completed_boxes()) < curr_tree_Node.board.completed_boxes(): # if new square
                for child in curr_tree_Node.children:
                    self.generate_search_tree(child, depth-1, isOurTurn)
            else:
                for child in curr_tree_Node.children:
                    self.generate_search_tree(child, depth-1, (not isOurTurn))

        # if this node the function is inspecting is the first one, return it now that it is filled up
        if curr_tree_Node.isRootNode:
            return curr_tree_Node

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
