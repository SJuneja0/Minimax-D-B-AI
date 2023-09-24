"""IMPORTS"""
import os


class communicator:

    def __init__(self, name):
        self.name = name

    # Input: Two dots that make the edge/line
    # Output: Null
    # Purpose: Writes a new move_file to send the move to the referee
    def write_move(self, point1, point2):
        if self.is_our_turn():
            print("WRITE_MOVE: Our Turn")
            move_file = open("move_file", "r+")
            move_file.truncate()
            move_file = open("move_file", "a")
            point1_to_string = str(point1.row) + "," + str(point1.column)
            point2_to_string = str(point2.row) + "," + str(point2.column)
            move_file.write(self.name + " " + point1_to_string + " " + point2_to_string + "\n")
        else:
            print("WRITE_MOVE: Not our turn")

    # Input: None
    # Output: None
    # Purpose: Write a 'false move' to the ref to signal that we know it's not our turn
    def write_false_move(self):
        if self.is_our_turn():
            print("WRITE_FALSE_MOVE: Our Turn")
            move_file = open("move_file", "r+")
            move_file.truncate()
            move_file = open("move_file", "a")
            move_file.write(self.name + " 0,0 0,0")
        else:
            print("WRITE_FALSE_MOVE: Not our Turn")

    """FUNCTIONS"""

    # Input: Null
    # Output: Boolean (true if our turn, false if opponent's turn)
    # Purpose:to read from a file telling us if it is our turn
    def is_our_turn(self):
        turn_path = "./" + self.name + ".go"
        move_path = "./move_file"
        return os.path.isfile(turn_path) and os.path.isfile(move_path)

    # Input: A edge that describes the invalid move
    # Output: None
    # Purpose: to tell the Ref that there is an invalid move and why
    def report_invalid_move(self, invalid_move):
        pass


"""TEST CODE"""
# COM = communicator("GG", 4)
# COM.read_board()
# COM.write_move((2, 2), (2, 3))
# COM.is_our_turn()
