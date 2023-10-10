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
            move_file.close()
        else:
            print("WRITE_MOVE: Not our turn")

    # Input: None
    # Output: None
    # Purpose: Write a 'false move' to the ref to signal that we know it's not our turn
    def write_false_move(self):
        print("WRITE_FALSE_MOVE: Our Turn")
        move_file = open("move_file", "r+")
        move_file.truncate()
        move_file = open("move_file", "a")
        move_file.write(self.name + " 0,0 0,0")
        move_file.close()

    """FUNCTIONS"""

    # Input: Null
    # Output: Boolean (true if our turn, false if opponent's turn)
    # Purpose:to read from a file telling us if it is our turn
    def is_our_turn(self):
        turn_path = "./" + self.name + ".go"
        move_path = "./move_file"
        pass_path = "./" + self.name + ".pass"
        return os.path.isfile(turn_path) and os.path.isfile(move_path) or os.path.isfile(pass_path)

    def is_pass_file(self):
        pass_path = "./" + self.name + ".pass"
        if os.path.isfile(pass_path):
            print(self.name + "PASS SEEN, SENDING FALSE MOVE NEXT")
        return os.path.isfile(pass_path)

    # Input: A edge that describes the invalid move and the current board
    # Output: None
    # Purpose: to tell the Ref that there is an invalid move and why
    def report_invalid_move(self, invalid_move, curr_board):
        dot1 = invalid_move.dot1
        dot2 = invalid_move.dot2
        for edge in curr_board.edges:
            if not invalid_move.equals(edge):
                print("The move ", dot1.row, ",", dot1.column, " to", dot2.row, ",", dot2.column, " is out of range")
                break
            else:
                print("The move ", dot1.row, ",", dot1.column, " to", dot2.row, ",", dot2.column, " is already taken")
                break






"""TEST CODE"""
# os.remove("./GG.go")
# os.remove("./move_file")
# COM = communicator("GG")  # Constructor
#
# # Testing Variables
# p1 = board.Dot(0, 0)
# p2 = board.Dot(1, 1)
# p3 = board.Dot(1, 2)
#
# print("No GG.go or move_file: " + str(not COM.is_our_turn()))  # No GG.go or move_file
# with open("GG.go", "xt") as f:
#     f.write("")
#     f.close()
# print("No move_file: " + str(not COM.is_our_turn()))  # No move_file
# os.remove("./GG.go")
# with open("move_file", "xt") as f:
#     f.write("")
#     f.close()
# print("No GG.go: " + str(not COM.is_our_turn()))  # No GG.go
# with open("GG.go", "xt") as f:
#     f.write("")
#     f.close()
# print("Both GG.go and move_file: " + str(COM.is_our_turn()))  # both GG.go and move_file
#
# COM.write_move(p1, p2)  # Write move tester
# COM.write_move(p1, p3)  # Truncates tester
# COM.write_move(p2, p1)  # Inverse order tester
# COM.write_false_move()  # Write false move tester
