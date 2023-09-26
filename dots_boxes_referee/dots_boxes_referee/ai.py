import tree_node as treeNode
import communicator
import board
import time
import os
import copy

"""Functions"""


class AI:

    def __init__(self, opponent):
        self.i =0
        self.bd = board.Board(9, 9, "SaucyBoy", opponent)
        self.bd.create_board()
        self.tree = treeNode.treeNode(self.bd, [], None, True)
        self.name = "SaucyBoy"
        self.opponent = opponent
        self.score = [0, 0]  # index 0 is SaucyBoy and index 1 is the opponent
        self.coms = communicator.communicator(self.name)
        print("INITIALIZED")
        #  TODO: May need a flag to see if we get an extra turn

    def main(self):
        # TODO: NEED something to handle going first, getting an empty board
        while not os.path.isfile("move_file"):
            pass
        move_file = open("./move_file", "r")
        content = move_file.read()
        if move_file.read() == "":
            best_move_board = self.decide_move(self.bd)  # returns a board that is one level below curr_board
            best_move = self.separate_move(best_move_board)  # finds the move to get to that best_board
            self.coms.write_move(best_move.dot1, best_move.dot2)  # writes that move
            self.bd.update_board()  # update's the internal board with our move

        # TODO: adjust for if opponents or we get a point/take another turn
        isWeWin = True
        print(self.bd.is_game_over())
        while not self.bd.is_game_over():  # while the game is not over
            print("RUNNING CORE LOOP")
            print(self.coms.is_our_turn())
            if self.coms.is_our_turn():  # check to see if it's our turn
                # start core gameplay loop

                # if there is a new box that was taken by the opp, write a false move
                curr_boxes_taken = len(self.bd.completed_boxes)  # num of boxes before new move is added
                isValid = self.bd.update_board()
                new_box_taken = len(self.bd.completed_boxes)  # num of boxes after new move is added
                if curr_boxes_taken != new_box_taken:
                    self.coms.write_false_move()

                # else if an invalid move was given, report it and end the game
                elif type(isValid) == board.Edge:
                    self.coms.report_invalid_move(isValid, self.bd)
                    break

                # if the move was valid/a false move, and they haven't gotten a new box
                # take a turn
                else:
                    best_move_board = self.decide_move(self.bd)  # returns a board that is one level below curr_board
                    best_move = self.separate_move(best_move_board)  # finds the move to get to that best_board
                    self.coms.write_move(best_move.dot1, best_move.dot2)  # writes that move
                    self.bd.update_board()  # update's the internal board with our move
        # DO GAME TERMINATION HERE
        print("GAME IS OVER")
        print("Saucy boy scored ", self.score[0], " points and the opponent scored ", self.score[1], " points")
        return 1

    # Input: Array of the current board-state and the time limit for the AI
    # Output: Null
    # Purpose: Decides the optimal move and publishes it to the referee, this is the main function
    def decide_move(self, current_board, time_limit=15):
        start_timer = time.perf_counter()
        best_move = None
        root_node = treeNode.treeNode(current_board, [], None, True)
        depth = 0
        while start_timer + time_limit >= time.perf_counter():
            depth += 2
            searchTree = self.generate_search_tree(root_node, depth, True)
            best_final_node = self.mini_max(searchTree, True, -9999, 9999, None)
            best_path = best_final_node.construct_path([])
            best_move = best_path[-2]

        return best_move.board

    def separate_move(self, new_board):
        for i in range(len(new_board.edges)):
            if not new_board.edges[i].owner == self.bd.edges[i].owner:
                return new_board.edges[i]
        return -1

    # Input: Two tuples (representing the points for a potential move)
    # Input: Array of the current board-state
    # Output: Boolean (true if the move suggested is valid)
    # Purpose: To check if a given move is valid
    def valid_move(self, edge):
        if self.bd.find_edge_in_board(edge) != -1 & edge.owner.equals(None):
            return True
        else:
            return False

    # Input: Board
    # Input: Name to write to the spot
    # Output: Array of possible valid board states
    # Purpose: Given a board state, this finds all children states (next possible moves)
    def generate_possible_moves(self, curr_board, name):
        print(type(curr_board))
        valid_child_boards = []
        for line in curr_board.edges:
            if line.owner is None:
                copy_board = copy.deepcopy(curr_board)
                i = curr_board.edges.index(line)
                edge = copy_board.edges[i]  # TODO could be problem in indexing line
                edge.owner = name
                valid_child_boards.append(copy_board)

        return valid_child_boards

    """Search Method"""

    # Input: Array of the current board-state
    # Output: A path of the optimal move
    # Purpose: To decide the optimal move given a search tree
    def mini_max(self, tree_Node, isMaximizing, alpha, beta, bestFinalPosition):
        # if the game would be over or if this is the bottom node so far (i.e., this position has no children)
        # generate the value of this node based on the utility function
        if not tree_Node.children:
            return self.utility_fcn(tree_Node.board, self.name, self.opponent)

        # if this node is maximizing (our turn to pick)
        if isMaximizing:
            maxValue = -9999  # set the current maxValue to -infinity
            for child in tree_Node.children:  # look through children for the greatest value among them
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
            if tree_Node.isRootNode:
                return bestFinalPosition
            return maxValue

        # else if the node is minimizing (opponent's turn to pick)
        else:
            minValue = 9999  # set current min value to infinity
            for child in tree_Node.children:  # look through children for the greatest value among them
                value = self.mini_max(child, True, alpha, beta, bestFinalPosition)  # look through children's children
                if value < minValue:
                    minValue = value
                    if not child.children:  # if a node is the bottom node, and it is the current smallest
                        bestFinalPosition = child  # set it to be the best node
                beta = min(beta, value)
                if beta <= alpha:
                    break
            return minValue

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

            # generate the child boards, make a tree node for each, and append it to the curr_node's children
            children_boards = self.generate_possible_moves(curr_tree_Node.board, name)
            empty_child_node = treeNode.treeNode(None, [], curr_tree_Node, False)
            for child_board in children_boards:
                child_node = copy.copy(empty_child_node)
                child_node.children = [].copy()
                child_node.board = child_board

                if len(curr_tree_Node.children) <= 2:
                    curr_tree_Node.children.append(child_node)
                else:
                    self.h_sort(curr_tree_Node.children)
                    curr_child_value = self.utility_fcn(child_node.board, self.name, self.opponent)
                    worst_child_value = self.utility_fcn(curr_tree_Node.children[-1].board, self.name, self.opponent)
                    if curr_child_value > worst_child_value:
                        curr_tree_Node.children[-1] = child_node

            curr_tree_Node_children_boards = self.generate_possible_moves(curr_tree_Node.board, name)
            empty_child_node = treeNode.treeNode(None, [], curr_tree_Node, False)
            for child_board in curr_tree_Node_children_boards:
                child_node = copy.copy(empty_child_node)
                child_node.children = [].copy()
                child_node.board = child_board
                curr_tree_Node.children.append(child_node)

        # for each child of this node, generate the children's children (recursively),
        # all editing the original treeNode
        # if there is a new square (one more then the previous boardstate), the player gets another turn
        if not curr_tree_Node.isRootNode:
            if len(curr_tree_Node.came_from.board.completed_boxes()) < curr_tree_Node.board.completed_boxes():  # if new square
                for child in curr_tree_Node.children:
                    self.generate_search_tree(child, depth - 1, isOurTurn)
            else:
                for child in curr_tree_Node.children:
                    self.generate_search_tree(child, depth - 1, (not isOurTurn))

        # if this node the function is inspecting is the first one, return it now that it is filled up
        if curr_tree_Node.isRootNode:
            return curr_tree_Node

    def h_sort(self, children):
        value = [self.utility_fcn(children[0].board, self.name, self.opponent),
                 self.utility_fcn(children[1].board, self.name, self.opponent),
                 self.utility_fcn(children[2].board, self.name, self.opponent)]

        index = value.index(min(value))
        holder = children[-1]
        children[-1] = children[index]
        children[index] = holder
        del value[index]

        index = value.index(min(value))
        holder = children[-2]
        children[-2] = children[index]
        children[index] = holder
        del value[index]

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

        self.score[0] = ai_score
        self.score[1] = opponent_score
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

    def evaluation_fcn(self, curr_board, player_name, opponent_name):
        return self.utility_fcn(curr_board, player_name, opponent_name)

    def doesOppGiveFalseMove(self):
        # read the move file check to see if the components are "opponent name 0,0 0,0"
        move_file = open("move_file", "r")
        text_move_file = move_file.read()
        move = text_move_file.split()
        dot1 = board.Dot(int(move[1][0]), int(move[1][1]))
        dot2 = board.Dot(int(move[2][0]), int(move[2][1]))
        emptyDot = board.Dot(0, 0)
        if move[0].equals(self.opponent) and dot1.equals(emptyDot) and dot2.equals(emptyDot):
            return True
        else:
            return False


# Testing
# if __name__ == "__main__":
program = AI("opp")
program.main()
