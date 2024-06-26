class treeNode:

    def __init__(self, board, children, came_from, isRootNode):
        self.board = board
        self.children = children  # array [treeNode...]
        self.came_from = came_from  # treeNode
        self.isRootNode = isRootNode  # is root node

    # Input: []
    # Output: A full array
    # Purpose: Finds a path from this node to the root node
    def construct_path(self, path):
        if self.came_from is not None: # While this node is not the root node
            path.append(self) # Add it to the path discovered
            self.came_from.construct_path(path) # And repeat this process with the parent
        if self.came_from is None:
            path.append(self)
        return path # When the root node is reached, return the path to the root node
