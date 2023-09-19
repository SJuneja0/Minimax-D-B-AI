
class board:

    def __init__(self):
        pass

    def getNeighbors(rowNum, colNum, isVertical, board):
        if(isVertical):
            verNum = 0
            notVer = 1
        else:
            verNum = 1
            notVer = 0
        above = ""
        below = ""
        left = ""
        right = ""
        pass


    
    def lineOwner(rowNum, colNum, isVertical, board):
        if(isVertical):
            verNum = 0
        else:
            verNum = 1
        return board[verNum][rowNum][colNum]

    def isTaken(rowNum, colNum, isVertical, board):
        if(isVertical):
            verNum = 0
        else:
            verNum = 1
        if(board[verNum][rowNum][colNum] != ""):
            return True
        return False