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

    # def mulArr(self,matr):
    #     return sum([self.map[i][j]*matr[i][j] for i in range(4) for j in range(4)])

    # def heu6(self):
    #     matr1 = [4**12,4**13,4**14,4**15,4**11,4**10,4**9,4**8,4**4,4**5,4**6,4**7,4**3,16,4,1]
    #     matr2 = [[4**15,4**14,4**13,4**12],[4**8,4**9,4**10,4**11],[4**7,4**6,4**5,4**4],[1,4,16,4**3]]
    #     matr3 = [[4**3,16,4,1],[4**4,4**5,4**6,4**7],[4**11,4**10,4**9,4**8],[4**12,4**13,4**14,4**15]]
    #     matr4 = [[1,4,16,4**3],[4**7,4**6,4**5,4**4],[4**8,4**9,4**10,4**11],[4**15,4**14,4**13,4**12]]
    #     # return max(self.mulArr(matr1),self.mulArr(matr2),self.mulArr(matr3),self.mulArr(matr4))
    #     return self.mulArr(matr



    # move the grid
    # def move(self, dir):
    #     """move the grid and return the boolean value
    #         that tell us that grid can move that way or not"""
    #     dir = int(dir)
    #     if dir == UP:
    #         return self.moveUD(False)
    #     if dir == DOWN:
    #         return self.moveUD(True)
    #     if dir == LEFT:
    #         return self.moveLR(False)
    #     if dir == RIGHT:
    #         return self.moveLR(True)
    #
    # # move up or down
    # def moveUD(self, down):
    #     """Move up or down depending on the boolean value
    #         if down == TRUE -> move Down , else -> move UP"""
    #     # We initialize the range that tell us the order. IF
    #     # we move down so that the considering order of cell is from the
    #     # bottom to the top (r = (3, 2, 1, 0)) . If we move up so that the
    #     # the considering order of cell is reverse ( r = (0,1,2,3))
    #     r = range(self.size -1, -1, -1) if down else range(self.size)
    #     moved = False
    #     # we go each block of cells in vertical ( that means we go all
    #     # cells in col 1, then work with col2,col3, col4) and merge cells in
    #     # that col with merge function. Then from that replace that merged value
    #     # into the grid.
    #     for j in range(self.size):
    #         cells = []
    #         for i in r:
    #             cell = self.map[i][j]
    #             if cell != 0:
    #                 cells.append(cell)
    #         self.merge(cells)
    #         for i in r:
    #             value = cells.pop(0) if cells else 0
    #             # check whether that cell in the bottom or top previous, then we do nothing
    #             # (we don't move)
    #             if self.map[i][j] != value:
    #                 moved = True
    #             self.map[i][j] = value
    #     return moved
    #
    # # move left or right
    # def moveLR(self, right):
    #     """Move right or left depending on the boolean value
    #         if right == TRUE -> move Right , else -> move LEFT"""
    #     # We initialize the range that tell us the order. IF
    #     # we move right so that the considering order of cell is from the
    #     # bottom to the top (r = (3, 2, 1, 0)) . If we move left so that
    #     # the considering order of cell is reverse ( r = (0,1,2,3))
    #     r = range(self.size - 1, -1, -1) if right else range(self.size)
    #     moved = False
    #     # we go each block of cells in horizontal ( that means we go all
    #     # cells in row 1, then work with row2,row3, row4) and merge cells in
    #     # that row with merge function. Then from that replace that merged value
    #     # into the grid.
    #     for i in range(self.size):
    #         cells = []
    #         for j in r:
    #             cell = self.map[i][j]
    #             if cell != 0:
    #                 cells.append(cell)
    #         self.merge(cells)
    #         for j in r:
    #             value = cells.pop(0) if cells else 0
    #             if self.map[i][j] != value:
    #                 moved = True
    #             self.map[i][j] = value
    #     return moved
    #
    # # merge tiles
    # def merge(self, cells):
    #     """Merge the block of cells"""
    #     if len(cells) <= 1:
    #         return cells
    #     i =0
    #     while i < len(cells) - 1:
    #         if cells[i] == cells[i+1]:
    #             cells[i] *= 2
    #             del cells[i+1]
    #         i += 1


    # return all vailable moves, can be optimized
    # def getAvailableMoves(self, dirs = vecIndex):
    #     availableMoves = []
    #     for x in dirs:
    #         gridCopy = self.clone()
    #         if gridCopy.move(x):
    #             availableMoves.append(x)
    #     return availableMoves


