"""IMPORTS"""
import os


class communicator:

    def __init__(self, name):
        self.name = name

    # TODO: Check if the move being written is valid
    # Input: Two dots that make the edge/line
    # Output: Null
    # Purpose: Writes a new move_file to send the move to the referee
    def write_move(self, point1, point2):
        if self.is_our_turn():
            move_file = open("move_file", "r+")
            move_file.truncate()
            print("WRITE_MOVE: Our Turn")
            move_file = open("move_file", "a")
            point1_to_string = str(point1.row) + "," + str(point1.column)
            point2_to_string = str(point2.row) + "," + str(point2.column)
            move_file.write(self.name + " " + point1_to_string + " " + point2_to_string + "\n")
        else:
            print("WRITE_MOVE: Not our turn")

    """FUNCTIONS"""


    # Input: Null
    # Output: Boolean (true if our turn, false if opponent's turn)
    # Purpose:to read from a file telling us if it is our turn
    def is_our_turn(self):
        turn_path = "./" + self.name + ".go"
        move_path = "./move_file"
        return os.path.isfile(turn_path) and os.path.isfile(move_path)


"""TEST CODE"""
#COM = communicator("GG", 4)
#COM.read_board()
# COM.write_move((2, 2), (2, 3))
# COM.is_our_turn()
