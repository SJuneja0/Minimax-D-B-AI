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
    def update_board(self): # TODO: check to make sure it can handle false moves
        move_file = open("move_file", "r")
        text_move_file = move_file.read()
        move = text_move_file.split()
        row1, col1 = int(move[1][0]), int(move[1][2])
        row2, col2 = int(move[2][0]), int(move[2][2])
        dot1 = Dot(row1, col1)
        dot2 = Dot(row2, col2)
        curr_edge = Edge(dot1, dot2)
        curr_edge = self.find_edge_in_board(curr_edge)  # Finds an edge that is at the same location and spit's out the object on the board
        i = self.edges.index(curr_edge)
        edge = self.edges[i]
        if curr_edge in self.edges and edge.owner.equals(
                None):  # TODO: curr_edges may not be in self.edges, even if they are the same
            pass
        else:
            return curr_edge

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
    # Purpose: to create the wanted board, this will only work for boards that are 3x3 boxes or more
    def create_board(self):
        for x in range(self.row + 1):
            for y in range(self.column + 1):
                self.dots.append(Dot(x, y))

        # Create horizontal edges.
        for x in range(self.row):
            for y in range(self.column + 1):
                edge = Edge(self.dots[y + x * (self.column + 1)], self.dots[y + (x + 1) * (self.column + 1)])
                self.edges.append(edge)

        # Create vertical edges.
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

    def is_game_over(self):
        return not any(edge.owner is None for edge in self.edges)


# if __name__ == "__main__":
#     game_board = Board(4, 4, "SaucyBoy", "Enemy")
#     game_board.create_board()
#     for box in game_board.box:
#         print("Box:")
#         for edge in box.dots:
#             print(f"Edge: {edge.dot1.row}, {edge.dot1.column} - {edge.dot2.row}, {edge.dot2.column}, Owner: {edge.owner}")
#             print(f"Box Owner: {box.owner}")
#             print()
