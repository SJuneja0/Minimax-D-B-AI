import communicator

class dot:
    def __init__(self, row, column):
        self.row = row
        self.column = column

class Edge:
    def __init__(self, dot1, dot2):
        self.dot1 = dot1
        self.dot2 = dot2
        self.owner = None

class Box:
    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.owner = None
class board:

    def __init__(self):
        self.com = communicator.communicator("GG")
        self.board = self.com.read_board()
        self.edges = []
        self.dots = []
        self.row = 9
        self.column = 9
        self.box = []
        self.completed_boxes = []

    def getNeighbors(self, rowNum, colNum, isVertical, board):
        # neighbors is an array of 8 strings denoted as "[vertical indicator (0 or 1)]-[row number]-[col number]-[Owner]"
        # 0 is above, 1 is right, 2 is below, and 3 is left, and 4-7 are identical, except for opposing orientation
        neighbors = [[], [], [], [], [], [], [], []]
        if (isVertical):
            verNum = 1  # TODO changed verNum
            notVer = 0
        else:
            verNum = 0
            notVer = 1
        if (rowNum > 0):
            neighbors[0] = [verNum, (rowNum - 1), colNum, board[verNum][rowNum - 1][colNum]]
            neighbors[4] = [notVer, (rowNum - 1), colNum, board[notVer][rowNum - 1][colNum]]
        if (rowNum < len(board[0]) - 1):
            neighbors[2] = [verNum, (rowNum + 1), colNum, board[verNum][rowNum + 1][colNum]]
            neighbors[6] = [notVer, (rowNum + 1), colNum, board[notVer][rowNum + 1][colNum]]
        if (colNum > 0):
            neighbors[3] = [verNum, rowNum, (colNum - 1), board[verNum][rowNum][colNum - 1]]
            neighbors[7] = [notVer, rowNum, (colNum - 1), board[notVer][rowNum][colNum - 1]]
        if (colNum < len(board[0][0]) - 1):
            neighbors[1] = [verNum, rowNum, (colNum + 1), board[verNum][rowNum][colNum + 1]]
            neighbors[5] = [notVer, rowNum, (colNum + 1), board[notVer][rowNum][colNum + 1]]
        return neighbors

    def lineOwner(rowNum, colNum, isVertical, board):
        if (isVertical):
            verNum = 1
        else:
            verNum = 0
        return board[verNum][rowNum][colNum]

    def isTaken(self, rowNum, colNum, isVertical, board):
        if (isVertical):
            verNum = 1
        else:
            verNum = 0
        if (board[verNum][rowNum][colNum] != ""):
            return True
        return False

    def edges_controlled_by(self, player):
        controlled_edges = []
        for edge in self.edges:
            if edge.owner == player:
                controlled_edges.append(edge)
        return controlled_edges

    def get_legal_moves(self):
        # Return a list of legal moves (unclaimed edges).
        legal_moves = []
        for edge in self.edges:
            if edge.owner is None:
                legal_moves.append(edge)
        return legal_moves
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
    def box_check(self):
        count = 0
        for box in self.box:
            if (box.owner != None):
                self.completed_boxes.append(box)
    def generate_board(self):
        # Create dots and edges based on the board's width and height.
        for x in range(self.row + 1):
            for y in range(self.column + 1):
                self.dots.append(dot(x, y))

        # Create horizontal edges.
        for x in range(self.row):
            for y in range(self.column + 1):
                edge = Edge(self.dots[y + x * (self.column + 1)], self.dots[y + (x + 1) * (self.column + 1)])
                self.edges.append(edge)

        # Create vertical edges.
        for x in range(self.row + 1):
            for y in range(self.column):
                edge = Edge(self.dots[y + x * (self.column + 1)], self.dots[y + (x + 1) * (self.column + 1)])
                self.edges.append(edge)

        for x in range(self.row):
            for y in range(self.column):
                self.box.append()                                     #need to add 4 dots

    def is_game_over(self):
        # Check if the game is over by verifying that no more legal moves are available.
        return not any(edge.owner is None for edge in self.edges)

board_ish = board()
#print(board_ish.boxes())