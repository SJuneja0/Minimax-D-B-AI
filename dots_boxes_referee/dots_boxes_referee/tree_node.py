class treeNode:

    def __init__(self, children, came_from, depth, utility_value, value_range):
        self.children = children # array [treeNode...]
        self.came_from = came_from # treeNode
        self.depth = depth # int
        self.utility_value = utility_value # float
        self.value_range = value_range # array [float, float]

    # Input:
    # Output:
    # Purpose: Finds a path from this node to the root node
    def construct_path(self, path):
        while self.came_from is not None: # While this node is not the root node
            path.append(self) # Add it to the path discovered
            self.came_from.construct_path(path) # And repeat this process with the parent
        return path # When the root node is reached, return the path to the root node
