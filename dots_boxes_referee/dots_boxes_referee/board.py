import communicator
class Dot:
    def __init__(self, row, column):
        self.row = row
        self.column = column

class Edge:
    def __init__(self, dot1, dot2):
        self.dot1 = dot1
        self.dot2 = dot2
        self.owner = None   #string

class Box:
    def __init__(self, dots):
        self.dots = dots
        self.owner = None   #string

class Board:
    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.edges = []
        self.dots = []
        self.box = []
        self.completed_boxes = []

    # Input:
    # Output:
    # Purpose:
    def update_board(self, owner):
        move_file = open("move_file", "r")
        text_move_file = move_file.read()
        move = text_move_file.split()
        move_file = open("move_file", "a")
        dot1 = Dot(move[1][0], move[1][1])
        dot2 = Dot(move[2][0], move[2][1])
        for edge in self.edges:
            if edge.dot1 == dot1 & edge.dot2 == dot2:
                edge.owner = owner
        # point1_to_string = str(move[1][0]) + "," + str(move[1][1])
        # point2_to_string = str(move[2][0]) + "," + str(move[2][1])
        # move_file.write(self.name + " " + point1_to_string + " " + point2_to_string + "\n")
        # name, point 1, point 2
        pass


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
                curr_box = Box([self.dots[x * (self.column + 1) + y], self.dots[x * (self.column + 1) + (y + 1)],
                                self.dots[(x + 1) * (self.column + 1) + y], self.dots[(x + 1) * (self.column + 1) + (y + 1)]])
                self.box.append(curr_box)

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

    def is_game_over(self):
        return not any(edge.owner is None for edge in self.edges)

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

if __name__ == "__main__":
    game_board = Board(9, 9)
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


#print(board_ish.boxes())