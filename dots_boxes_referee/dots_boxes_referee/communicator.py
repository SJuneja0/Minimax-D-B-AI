"""IMPORTS"""
import os


class communicator:

    def __init__(self, name):
        self.name = name

    # TODO: Check if the move being written is valid
    # Input: Two tuples representing the line to be played
    # Output: Null
    # Purpose: Writes a new move_file to send the move to the referee
    def write_move(self, point1, point2):
        if self.is_our_turn():
            print("WRITE_MOVE: Our Turn")
            move_file = open("move_file", "a")
            point1_to_string = str(point1[0]) + "," + str(point1[1])
            point2_to_string = str(point2[0]) + "," + str(point2[1])
            move_file.write(self.name + " " + point1_to_string + " " + point2_to_string + "\n")
        else:
            print("WRITE_MOVE: Not our turn")

    """FUNCTIONS"""
    # Input:
    # Output:
    # Purpose: Separates all the moves
    def separate_lines(self, text_move_file):
        list_of_lines = []
        curr_line = []

        # take the first three 'words' (player name, point1, point2)
        # turn them into a list, and append them to the list of lines
        for item in text_move_file.split():
            curr_line.append(item)
            if len(curr_line) == 3:
                list_of_lines.append(curr_line.copy())
                curr_line = []
        # print(list_of_lines)
        return list_of_lines

    # TODO: check if board is valid, or IRL check if the referee always gives a valid board
    # TODO: think about if multiple of the same line are given, probably throw an error or exception in that case
    # Input:
    # Output:
    # Purpose:
    def construct_horizontal_board(self, text_move_file, n):
        # Construct the empty board
        horizontal_board = []
        empty_row = []
        for i in range(n-1): # fill the empty columns
            empty_row.append("")
        for j in range(n): # create the right number of columns
            horizontal_board.append(empty_row.copy())

        # Sort the occupied lines into the board
        lines = self.separate_lines(text_move_file)
        for line in lines:
            if line[1][0] == line[2][0]: # if the x values of a line are the same, it is vertical
                pass
            elif line[1][2] == line[2][2]: # else, if the y values of a line are the same, it is horizontal
                right_most_value = None
                y_value = int(line[1][2])
                if line[1][0] < line[2][0]:
                    right_most_value = int(line[1][0])
                else:
                    right_most_value = int(line[2][0])
                horizontal_board[y_value-1][right_most_value-1] = line[0]
                for row in horizontal_board:
                    print(row)
                print("===============")
        return horizontal_board

    def construct_vertical_board(self, text_move_file, n):
        # Construct the empty board
        vertical_board = []
        empty_row = []
        for i in range(n):  # fill the empty columns
            empty_row.append("")
        for j in range(n-1):  # create the right number of columns
            vertical_board.append(empty_row.copy())

        # Sort the occupied lines into the board
        lines = self.separate_lines(text_move_file)
        for line in lines:
            if line[1][0] == line[2][0]:  # if the x values of a line are the same, it is vertical
                top_value = None
                x_value = int(line[1][0])
                if line[1][2] < line[2][2]:
                    top_value = int(line[1][2])
                else:
                    top_value = int(line[2][2])
                vertical_board[top_value-1][x_value-1] = line[0]
                for row in vertical_board:
                    print(row)
                print("===============")
            elif line[1][2] == line[2][2]:  # else, if the y values of a line are the same, it is horizontal
                pass
        return vertical_board

    # Input: Null
    # Output: Array of current board-state
    # Purpose: Takes the newest move_file and converts it into a readable format for the AI
    def read_board(self):
        if self.is_our_turn():
            print("READ_BOARD: Our turn")
            move_file = open("move_file", "r")
            text_move_file = move_file.read()
            # print(text_move_file)
            horizontal_lines = self.construct_horizontal_board(text_move_file, 4)
            vertical_lines = self.construct_vertical_board(text_move_file, 4)
            board = (horizontal_lines, vertical_lines)
        else:
            print("READ_BOARD: Not our turn")

    # Input: Null
    # Output: Boolean (true if our turn, false if opponent's turn)
    # Purpose:to read from a file telling us if it is our turn
    def is_our_turn(self):
        path = "./" + self.name + ".go"
        return os.path.isfile(path)


"""TEST CODE"""
COM = communicator("GG")
COM.read_board()
COM.write_move((2, 2), (2, 3))
COM.is_our_turn()

