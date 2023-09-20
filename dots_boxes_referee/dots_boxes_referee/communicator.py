"""IMPORTS"""
import os


class communicator:

    def __init__(self, name, board_size):
        self.name = name
        self.board = self.gen_board(board_size)

    def gen_board(self, board_size):
        # Constructing h_board
        h_row = []
        h_board = []
        for i in range(board_size-1):
            h_row.append("")
        for j in range (board_size):
            h_board.append(h_row.copy())

        # Constructing v_board
        v_row = []
        v_board = []
        for i in range(board_size):
            v_row.append("")
        for j in range(board_size-1):
            v_board.append(v_row.copy())

        board = [h_board, v_board]
        return board

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
    # # Input:
    # # Output:
    # # Purpose: Separates all the moves
    # def separate_lines(self, text_move_file):
    #     list_of_lines = []
    #     curr_line = []
    #
    #     # take the first three 'words' (player name, point1, point2)
    #     # turn them into a list, and append them to the list of lines
    #     for item in text_move_file.split():
    #         curr_line.append(item)
    #         if len(curr_line) == 3:
    #             list_of_lines.append(curr_line.copy())
    #             curr_line = []
    #     # print(list_of_lines)
    #     return list_of_lines

    # # TODO: check if board is valid, or IRL check if the referee always gives a valid board
    # # TODO: think about if multiple of the same line are given, probably throw an error or exception in that case
    # # Input:
    # # Output:
    # # Purpose:
    # def construct_horizontal_board(self, text_move_file, n):
    #     # Construct the empty board
    #     horizontal_board = []
    #     empty_row = []
    #     for i in range(n-1): # fill the empty columns
    #         empty_row.append("")
    #     for j in range(n): # create the right number of columns
    #         horizontal_board.append(empty_row.copy())
    #
    #     # Sort the occupied lines into the board
    #     lines = self.separate_lines(text_move_file)
    #     for line in lines:
    #         if line[1][0] == line[2][0]: # if the x values of a line are the same, it is vertical
    #             pass
    #         elif line[1][2] == line[2][2]: # else, if the y values of a line are the same, it is horizontal
    #             right_most_value = None
    #             y_value = int(line[1][2])
    #             if line[1][0] < line[2][0]:
    #                 right_most_value = int(line[1][0])
    #             else:
    #                 right_most_value = int(line[2][0])
    #             horizontal_board[y_value-1][right_most_value-1] = line[0]
    #             for row in horizontal_board:
    #                 print(row)
    #             print("===============")
    #     return horizontal_board
    #
    # def construct_vertical_board(self, text_move_file, n):
    #     # Construct the empty board
    #     vertical_board = []
    #     empty_row = []
    #     for i in range(n):  # fill the empty columns
    #         empty_row.append("")
    #     for j in range(n-1):  # create the right number of columns
    #         vertical_board.append(empty_row.copy())
    #
    #     # Sort the occupied lines into the board
    #     lines = self.separate_lines(text_move_file)
    #     for line in lines:
    #         if line[1][0] == line[2][0]:  # if the x values of a line are the same, it is vertical
    #             top_value = None
    #             x_value = int(line[1][0])
    #             if line[1][2] < line[2][2]:
    #                 top_value = int(line[1][2])
    #             else:
    #                 top_value = int(line[2][2])
    #             vertical_board[top_value-1][x_value-1] = line[0]
    #             for row in vertical_board:
    #                 print(row)
    #             print("===============")
    #         elif line[1][2] == line[2][2]:  # else, if the y values of a line are the same, it is horizontal
    #             pass
    #     return vertical_board

    def is_board_read(self):
        return True

    def update_board(self, board):
        if self.is_our_turn() and self.is_board_read():
            print("READ_MOVE: Our turn")
            move_file = open("move_file", "r")
            text_move_file = move_file.read()
            text_move_file.split()


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
            return board
        else:
            print("READ_BOARD: Not our turn")

    # Input: Null
    # Output: Boolean (true if our turn, false if opponent's turn)
    # Purpose:to read from a file telling us if it is our turn
    def is_our_turn(self):
        turn_path = "./" + self.name + ".go"
        move_path = "./move_file"
        return os.path.isfile(turn_path) and os.path.isfile(move_path)


"""TEST CODE"""
COM = communicator("GG", 4)
COM.read_board()
# COM.write_move((2, 2), (2, 3))
# COM.is_our_turn()

