# Input: A row and column
# Output: null
# Purpose: To create a dot class that contains the row and column
class Dot:
    def __init__(self, row, column):
        self.row = row
        self.column = column


# Input: two Dot class dots
# Output: Creates an edge/line
# Purpose: to create all lines and their dots in the board, and who owns the line
class Edge:
    def __init__(self, dot1, dot2):
        self.dot1 = dot1
        self.dot2 = dot2
        self.owner = None  # string


# Input: the 4 dots in an array
# Output: creates a box with the 4 lines
# Purpose: to go through the boxes based on edges
class Box:
    def __init__(self, dots):
        self.dots = dots
        self.owner = None  # string


# Input: row, column, owner, and opponent
# Output: reads from the board
# Purpose: to create our own board to look through appropriately
class Board:
    def __init__(self, row, column, owner, opponent):
        self.row = row
        self.column = column
        self.edges = []
        self.dots = []
        self.box = []
        self.valid = True
        self.owner = owner
        self.opponent = opponent
        self.completed_boxes = []

    def valid_move(self, edge):
        if edge in self.edges and edge.owner.equals(None):
            return True
        else:
            return False

    # Input: Null
    # Output: Null
    # Purpose: Updates the boxes and lines and the owners on the board
    def update_board(self):
        move_file = open("move_file", "r")
        text_move_file = move_file.read()
        move = text_move_file.split()
        dot1 = Dot(int(move[1][0]), int(move[1][1]))
        dot2 = Dot(int(move[2][0]), int(move[2][1]))
        curr_edge = Edge(dot1, dot2)
        i = self.edges.index(curr_edge)
        edge = self.edges[i]
        try:
            if curr_edge in self.edges and edge.owner.equals(
                    None):  # TODO: curr_edges may not be in self.edges, even if they are the same
                pass
            else:
                return curr_edge
        except:
            return curr_edge  # REPORT EDGES THAT ARE NOT ON THE BOARD or edges that are too long or diagonals

        owner = move[0]

        # Update edge ownership based on the move
        for edge in self.edges:
            if (edge.dot1.equals(dot1) and edge.dot2.equals(dot2)) or (
                    edge.dot1.equals(dot2) and edge.dot2.equals(dot1)):
                edge.owner = owner

        # Check and update box ownership
        for box in self.box:
            if box.owner is None:
                count = 0
                this_box = False
                for i in range(4):
                    edge = box.dots[i]
                    if edge.owner == owner:
                        count += 1
                    if edge.owner is not None:
                        if (edge.dot1.equals(dot1) and edge.dot2.equals(dot2)) or (
                                edge.dot1.equals(dot2) and edge.dot2.equals(dot1)):
                            this_box = True
                if count == 4 and this_box:
                    box.owner = owner
        return True

    # Input: Null
    # Output: Null
    # Purpose: to create the wanted board
    def create_board(self):
        for x in range(self.row + 1):
            for y in range(self.column + 1):
                self.dots.append(Dot(x, y))

        for x in range(self.row):
            for y in range(self.column + 1):
                edge = Edge(self.dots[y + x * (self.column + 1)], self.dots[y + (x + 1) * (self.column + 1)])
                self.edges.append(edge)

        for x in range(self.row + 1):
            for y in range(self.column):
                edge = Edge(self.dots[y + x * (self.column + 1)], self.dots[y + x * (self.column + 1) + 1])
                self.edges.append(edge)

        for x in range(self.row):
            for y in range(self.column):
                top_edge = self.edges[y + x * (self.column + 1)]
                right_edge = self.edges[y + (x + 1) * (self.column + 1) + (self.row + 1)]
                bottom_edge = self.edges[y + (x + 1) * (self.column + 1) + (self.row + 1) + self.column]
                left_edge = self.edges[y + x * (self.column + 1) + self.row + 1]

                curr_box = Box([top_edge, right_edge, bottom_edge, left_edge])
                self.box.append(curr_box)

        # self.update_board(self)

    # Input:
    # Output:
    # Purpose:
    def edges_controlled_by(self, player):
        controlled_edges = []
        for edge in self.edges:
            if edge.owner == player:
                controlled_edges.append(edge)
        return controlled_edges

    def get_legal_moves(self):
        legal_moves = []
        for edge in self.edges:
            if edge.owner is None:
                legal_moves.append(edge)
        return legal_moves

    # def box_check(self):
    #     for box in self.box:
    #         if box.owner is not None:
    #             self.completed_boxes.append(box)
    #
    # def new_box_completed(self):
    #     prev_box_count = len(self.completed_boxes)
    #     self.box_check()
    #     if prev_box_count < len(self.completed_boxes):
    #         return True
    #     return False

    def is_game_over(self):
        return not any(edge.owner is None for edge in self.edges)

    #
    # # unused
    # def getNeighbors(self, rowNum, colNum, isVertical, board):
    #     # neighbors is an array of 8 strings denoted as "[vertical indicator (0 or 1)]-[row number]-[col number]-[
    #     # Owner]" 0 is above, 1 is right, 2 is below, and 3 is left, and 4-7 are identical, except for opposing
    #     # orientation
    #     neighbors = [[], [], [], [], [], [], [], []]
    #     if isVertical:
    #         verNum = 1
    #         notVer = 0
    #     else:
    #         verNum = 0
    #         notVer = 1
    #     if rowNum > 0:
    #         neighbors[0] = [verNum, (rowNum - 1), colNum, board[verNum][rowNum - 1][colNum]]
    #         neighbors[4] = [notVer, (rowNum - 1), colNum, board[notVer][rowNum - 1][colNum]]
    #     if rowNum < len(board[0]) - 1:
    #         neighbors[2] = [verNum, (rowNum + 1), colNum, board[verNum][rowNum + 1][colNum]]
    #         neighbors[6] = [notVer, (rowNum + 1), colNum, board[notVer][rowNum + 1][colNum]]
    #     if colNum > 0:
    #         neighbors[3] = [verNum, rowNum, (colNum - 1), board[verNum][rowNum][colNum - 1]]
    #         neighbors[7] = [notVer, rowNum, (colNum - 1), board[notVer][rowNum][colNum - 1]]
    #     if colNum < len(board[0][0]) - 1:
    #         neighbors[1] = [verNum, rowNum, (colNum + 1), board[verNum][rowNum][colNum + 1]]
    #         neighbors[5] = [notVer, rowNum, (colNum + 1), board[notVer][rowNum][colNum + 1]]
    #     return neighbors
    #
    # # unused
    # def lineOwner(self, rowNum, colNum, isVertical, board):
    #     if isVertical:
    #         verNum = 1
    #     else:
    #         verNum = 0
    #     return board[verNum][rowNum][colNum]
    #
    # def isTaken(self, rowNum, colNum, isVertical, board):
    #     if isVertical:
    #         verNum = 1
    #     else:
    #         verNum = 0
    #     if board[verNum][rowNum][colNum] != "":
    #         return True
    #     return False

# if __name__ == "__main__":
#     game_board = Board(9, 9, "SaucyBoy", "Enemy")
#     print(game_board.create_board())

# print(board_ish.boxes())
