from copy import deepcopy

# direction vectors
directionVectors = (UP_VEC, DOWN_VEC, LEFT_VEC, RIGHT_VEC) = ((-1, 0), (1, 0), (0, -1), (0, 1))
vecIndex = [UP, DOWN, LEFT, RIGHT] = range(4)

class Grid:
    def __init__(self, size = 4):
        self.size = size
        self.map = [[0] * self.size for i in range(self.size)]

    def makeGrid(self, matrix):
        gridCopy = Grid()
        gridCopy.map = deepcopy(matrix)
        gridCopy.size = self.size
        return gridCopy
    # make a deepcopy of this current object
    def clone(self):
        """Make the copy of the grid"""
        gridCopy = Grid()
        gridCopy.map = deepcopy(self.map)
        gridCopy.size = self.size
        return gridCopy

    # return all the empty cells
    def getAvailableCells(self):
        """Get a list of cells such that it having value 0 ( it means it's
            available"""
        cells = []
        for x in range(self.size):
            for y in range(self.size):
                if self.map[x][y] == 0:
                    cells.append((x,y))
        return cells

    # return the tile with maximum number
    def getMaxTile(self):
        """Get the value of title having the maximum value"""
        maxTile = 0
        for x in range(self.size):
            for y in range(self.size):
                maxTile = max(maxTile, self.map[x][y])
        return maxTile
