from typing import Self
import referee
import communicator
import board

import time


line = [[[]]]


"""Functions"""

# Input: Array of the current board-state and the time limit for the AI
# Output: Null
# Purpose: Decides the optimal move and publishes it to the referee, this is the main function
def decide_move(current_board, time_limit):
    pass


# Input: Two tuples (representing the points for a potential move)
# Input: Array of the current board-state
# Output: Boolean (true if the move suggested is valid)
# Purpose: To check if a given move is valid
def valid_move(point1, point2):
    pass



"""Search Method"""


# Input: Array of the current board-state
# Output: Two tuples of a valid move and it's value
# Purpose: To decide the next move
def mini_max(time_limit):
    com = communicator.communicator
    board = com.read_board()
    timer_start_time = time.perf_counter()
    while ((curr - timer_start_time) <= time_limit):
        curr = time.perf_counter
    pass


# Input:
# Output:
# Purpose:
def alpha_beta(time_limit):
    pass


"""Heuristics"""

class heuristic:

    def __init__(self, name):
        self.name = name
    # Input:
    # Output:
    # Purpose:
    def h_control_center(self):
        board = communicator.communicator.read_board()
        print("here")
        #horizontal
        value = 0
        count = 0
        row_num = board[0][-1][0]
        column_num = board[0][-1][1]
        line = [[[]]]
        for i in range(row_num):
            if (board[0][i][0] >= 1):
                line[0][i].append(board[0][i][0])
                #Value add 0.5
                line[0][i][i] += 0.5
                
        for i in range(column_num):
            if (board[0][i][1] >= 1):
                line[0][i].append(board[0][i][1])
                #Value add 0.5
                line[0][i][i] += 0.5
                
        
        #vertical
        value = 0
        row_num = board[1][-1][0]
        column_num = board[1][-1][1]
        for j in range(row_num):
            if (board[1][i][0] >= 1):
                line[1][i+j].append(board[1][i][0])
                #Value add 0.5
                line[1][i+j][i] += 0.5
                
        for i in range(column_num):
            if (board[1][i][1] >= 1):
                line[1][i].append(board[1][i][1])
                #Value add 0.5
                line[1][i][i] += 0.5
        
        print("here")

    # Input:
    # Output:
    # Purpose:
    def h_maintain_connectivity(self):
        board_read = communicator.communicator.read_board()
        neighbors = board.getNeighbors()
        for neighbor in neighbors:
            #if (neighbor == taken): #are not taken then add to the current line
                #add 1 to value
                
                pass
        
        pass
    

    # Input:
    # Output:
    # Purpose:
    def h_avoid_single_dots():
        board_read = communicator.communicator.read_board()
        neighbors = board.getNeighbors()
        #this may not be needed to apply
        pass


    # Input: null
    # Output: returns an array of the score
    # Purpose: to show what the score is
    def h_counting_score(self):
        list_boxes, value = self.boxes()
        score = [0,0]
        for i in len(list_boxes):
            if(value[i] == 0):
                score[0] += 1
            if (value[i] == 1):
                score[1] += 1
        
        return score


    # Input: Array of a suggested board state
    # Output: Int of how good that board state is for our AI
    # Purpose: To tell how good a theoretical move is
    def utility_fcn():
        pass

    #*if __name__ == "__main__":
        #try:
        #    pass
        #except:
         #   pass

    

    def boxes(self):
        value = []
        count = 0
        box = [[]]
        for i in range(64):
            #add the lines
            horizontals = board[0][count]
            horizontals.append(board[0][count+9])

            verticals = board[1][count]
            verticals.append(board[1][count+9])
            box[count].append([horizontals, verticals])
            for i in range(2):
                #find who owns all the lines and adjust the value
                pass
            #find out how to count a score
            value[i] = 1 # 0 and 1 to distingish between self or opponent. 2 as the preinput

            count += 1
        
        return box & value

if __name__ == "__main__":
        try:
            print("save me")
            print(heuristic.h_control_center())
        except:
            pass
