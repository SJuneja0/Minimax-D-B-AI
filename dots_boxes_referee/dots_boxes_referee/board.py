import communicator


class Dot:
    def __init__(self, row, column):
        self.row = row
        self.column = column


class Edge:
    def __init__(self, dot1, dot2):
        self.dot1 = dot1
        self.dot2 = dot2
        self.owner = None  # string


class Box:
    def __init__(self, dots):
        self.dots = dots
        self.owner = None  # string


class Board:
    def __init__(self, row, column, owner, opponent):
        self.row = row
        self.column = column
        self.edges = []
        self.dots = []
        self.box = []
        self.owner = owner
        self.opponent = opponent
        self.completed_boxes = []

    # Input:
    # Output:
    # Purpose:
    def update_board(self):
        move_file = open("move_file", "r")
        text_move_file = move_file.read()
        move = text_move_file.split()
        dot1 = Dot(move[1][0], move[1][1])
        dot2 = Dot(move[2][0], move[2][1])
        owner = move[0]
        for edge in self.edges:
            if edge.dot1.equals(dot1) & edge.dot2.equals(dot2):
                edge.owner = owner

        for box in self.box:
            if box.owner is None:
                count = 0
                this_box = False
                for i in range(4):
                    edge = box.dots[i]
                    if edge.owner is not None:
                        count += 1
                        if edge.dot1.equals(dot1) & edge.dot2.equals(dot2):
                            edge.owner = owner
                            this_box = True
                        if count >= 4 & this_box:
                            box.owner = owner

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
                edge = Edge(self.dots[y + x * (self.column + 1)], self.dots[y + (x + 1) * (self.column + 1)])
                self.edges.append(edge)

        for x in range(self.row):
            for y in range(self.column):
                curr_box = Box([Edge(self.dots[x * (self.column + 1) + y], self.dots[x * (self.column + 1) + (y + 1)]),
                                Edge(self.dots[x * (self.column + 1) + (y + 1)], self.dots[(x + 1) * (self.column + 1) + y]),
                                Edge(self.dots[(x + 1) * (self.column + 1) + y], self.dots[(x + 1) * (self.column + 1) + (y + 1)]),
                                Edge(self.dots[self.dots[(x + 1) * (self.column + 1) + (y + 1)], self.dots[x * (self.column + 1) + y]])])
                self.box.append(curr_box)

        self.update_board(self.oppenent)

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

    def box_check(self):
        for box in self.box:
            if box.owner is not None:
                self.completed_boxes.append(box)
    
    def new_box_completed(self):
        prev_box_count = len(self.completed_boxes)
        self.box_check()
        if(prev_box_count < len(self.completed_boxes)):
            return True
        return False

    def is_game_over(self):
        return not any(edge.owner is None for edge in self.edges)

    def getNeighbors(self, rowNum, colNum, isVertical, board):
        # neighbors is an array of 8 strings denoted as "[vertical indicator (0 or 1)]-[row number]-[col number]-[
        # Owner]" 0 is above, 1 is right, 2 is below, and 3 is left, and 4-7 are identical, except for opposing
        # orientation
        neighbors = [[], [], [], [], [], [], [], []]
        if isVertical:
            verNum = 1
            notVer = 0
        else:
            verNum = 0
            notVer = 1
        if rowNum > 0:
            neighbors[0] = [verNum, (rowNum - 1), colNum, board[verNum][rowNum - 1][colNum]]
            neighbors[4] = [notVer, (rowNum - 1), colNum, board[notVer][rowNum - 1][colNum]]
        if rowNum < len(board[0]) - 1:
            neighbors[2] = [verNum, (rowNum + 1), colNum, board[verNum][rowNum + 1][colNum]]
            neighbors[6] = [notVer, (rowNum + 1), colNum, board[notVer][rowNum + 1][colNum]]
        if colNum > 0:
            neighbors[3] = [verNum, rowNum, (colNum - 1), board[verNum][rowNum][colNum - 1]]
            neighbors[7] = [notVer, rowNum, (colNum - 1), board[notVer][rowNum][colNum - 1]]
        if colNum < len(board[0][0]) - 1:
            neighbors[1] = [verNum, rowNum, (colNum + 1), board[verNum][rowNum][colNum + 1]]
            neighbors[5] = [notVer, rowNum, (colNum + 1), board[notVer][rowNum][colNum + 1]]
        return neighbors

    def lineOwner(self, rowNum, colNum, isVertical, board):
        if isVertical:
            verNum = 1
        else:
            verNum = 0
        return board[verNum][rowNum][colNum]

    def isTaken(self, rowNum, colNum, isVertical, board):
        if isVertical:
            verNum = 1
        else:
            verNum = 0
        if board[verNum][rowNum][colNum] != "":
            return True
        return False


if __name__ == "__main__":
    game_board = Board(9, 9, "SaucyBoy", "Enemy")
    game_board.create_board()

    # def boxes(self):
    #     box = []
    #     coms = communicator.communicator("GG")
    #     board_read = coms.read_board()
    #     count = 0
    #
    #     for i in range(((len(board_read[1][1]) % 2) * (len(board_read[0][1]) % 2)) - 1):
    #         # add the lines
    #         print(len(board_read[1][1]))
    #         dot = self.dots() #how to
    #         horizontals = board_read[0][count]
    #         horizontals.append(board_read[0][count + len(board_read[0][1][1])])
    #
    #         verticals = board_read[1][count]
    #         print(1)
    #         verticals.append(board_read[1][count + len(board_read[1][1][1])])
    #         box[count].append(horizontals, verticals)
    #
    #         count += 1
    #
    #     return box

# print(board_ish.boxes())
