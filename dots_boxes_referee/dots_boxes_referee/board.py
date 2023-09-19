
class board:

    def __init__(self):
        pass

    def getNeighbors(rowNum, colNum, isVertical, board):
        # neighbors is an array of 8 strings denoted as "[vertical indicator (0 or 1)]-[row number]-[col number]-[Owner]"
        # 0 is above, 1 is right, 2 is below, and 3 is left, and 4-7 are identical, except for opposing orientation
        neighbors = ["", "", "", "", "", "", "", ""]
        if(isVertical):
            verNum = 1
            notVer = 0
        else:
            verNum = 0
            notVer = 1
        if(rowNum > 0):
            neighbors[0] = verNum + "-" + (rowNum - 1) + "-" + colNum + "-" + board[verNum][rowNum - 1][colNum]
            neighbors[4] = notVer + "-" + (rowNum - 1) + "-" + colNum + "-" + board[notVer][rowNum - 1][colNum]
        if(rowNum < len(board[0]) - 1):
            neighbors[2] = verNum + "-" + (rowNum + 1) + "-" + colNum + "-" + board[verNum][rowNum + 1][colNum]
            neighbors[6] = notVer + "-" + (rowNum + 1) + "-" + colNum + "-" + board[notVer][rowNum + 1][colNum]
        if(colNum > 0):
            neighbors[3] = verNum + "-" + rowNum + "-" + (colNum - 1) + "-" + board[verNum][rowNum][colNum - 1]
            neighbors[7] = notVer + "-" + rowNum + "-" + (colNum - 1) + "-" + board[notVer][rowNum][colNum - 1]
        if(colNum < len(board[0][0]) - 1):
            neighbors[1] = verNum + "-" + rowNum + "-" + (colNum + 1) + "-" + board[verNum][rowNum][colNum + 1]
            neighbors[5] = notVer + "-" + rowNum + "-" + (colNum + 1) + "-" + board[notVer][rowNum][colNum + 1]
        return neighbors
        
    
    def lineOwner(rowNum, colNum, isVertical, board):
        if(isVertical):
            verNum = 1
        else:
            verNum = 0
        return board[verNum][rowNum][colNum]

    def isTaken(rowNum, colNum, isVertical, board):
        if(isVertical):
            verNum = 1
        else:
            verNum = 0
        if(board[verNum][rowNum][colNum] != ""):
            return True
        return False