import math
MAX_TILE_CREDIT = 10e6
weighted_list = [4**12,4**13,4**14,4**15,4**11,4**10,4**9,4**8,4**4,4**5,4**6,4**7,4**3,16,4,1]


def ChangeToOneDimension(grid):
    grid_1D = []
    for i in range(4):
        for j in range(4):
            grid_1D.append(grid.map[i][j])
    return grid_1D

def getAvailableChildren(grid):
    #gets all children and the moving directions
    allmoves = [0,1,2,3]
    children = []
    moving = []
    for m in allmoves:
        gridcopy = list(grid)
        moved = move(gridcopy, m)
        #move method returns True if moved and makes the change to gridcopy itself
        if moved == True:
            children.append(gridcopy)
            moving.append(m)
    return [children, moving]

def merge(cells):
    #merges the cells and sends back in order to be inserted
    if len(cells) <= 1:
        return cells
    i = 0
    while i < len(cells)-1:
        if cells[i] == cells[i+1]:
            cells[i] *= 2
            del cells[i+1]
        i += 1

def move(grid, direction):
    #if there is a move it is changed and return is True
    moved = False
    if direction == 0:
        #UP
        for i in range(4):
            cells = []
            #cells has all elements for a column from top to bottom
            for j in range(i,i+13,4):
                cell = grid[j]
                if cell != 0:
                    cells.append(cell)
            merge(cells)
            for j in range(i,i+13,4):
                value = cells.pop(0) if cells else 0
                if grid[j] != value:
                    moved = True
                grid[j] = value
        return moved
    elif direction == 1:
        #DOWN
        for i in range(4):
            cells = []
            #cells has all elements of column from bottom to top
            for j in range(i+12,i-1,-4):
                cell = grid[j]
                if cell != 0:
                    cells.append(cell)
            merge(cells)
            for j in range(i+12,i-1,-4):
                value = cells.pop(0) if cells else 0
                if grid[j] != value:
                    moved = True
                grid[j] = value
        return moved
    elif direction == 2:
        #LEFT
        for i in [0,4,8,12]:
            cells = []
            #cells has all elements of a row from left to right
            for j in range(i,i+4):
                cell = grid[j]
                if cell != 0:
                    cells.append(cell)
            merge(cells)
            for j in range(i,i+4):
                value = cells.pop(0) if cells else 0
                if grid[j] != value:
                    moved = True
                grid[j] = value
        return moved
    elif direction == 3:
        #RIGHT
        for i in [3,7,11,15]:
            cells = []
            #cells has all elements of a row from right to left
            for j in range(i,i-4,-1):
                cell = grid[j]
                if cell != 0:
                    cells.append(cell)
            merge(cells)
            for j in range(i,i-4,-1):
                value = cells.pop(0) if cells else 0
                if grid[j] != value:
                    moved = True
                grid[j] = value
        return moved

def canMove(grid):
    if 0 in grid:
        #if there is an empty space in the grid
        return True
    for i in range(16):
        if (i+1)%4!=0:
            #for all elements except the last column
            #if any element has same right element
            if grid[i]==grid[i+1]:
                return True
        if i<12:
            #for all except last row elements
            #if any element has same below element
            if grid[i]==grid[i+4]:
                return True
    return False

def empty_tiles(grid):
    return len([i for i, x in enumerate(grid) if x == 0])

def weighted_board(grid):
    result = 0
    for i in range(16):
        result += grid[i] * weighted_list[i]
    return result

def heuristic(grid):
    return weighted_board(grid)

# def heuristic(grid):
#     #Try to keep largest tile in top left and others in decreasing order from left to right
#     emptyTiles = len([i for i, x in enumerate(grid) if x == 0])
#     maxTile = max(grid)
#     Ord = 0
#     weights = [65536,32768,16384,8192,512,1024,2048,4096,256,128,64,32,2,4,8,16]
#     if maxTile == grid[0]:
#         Ord += (math.log(grid[0])/math.log(2))*weights[0]
#     for i in range(16):
#         if grid[i] >= 8:
#             Ord += weights[i]*(math.log(grid[i])/math.log(2))
#     return Ord/(16-emptyTiles)


# def max_tile_position(grid):
#     max_tile = max(grid)
#     if grid[0] == max_tile:
#         return MAX_TILE_CREDIT
#     else:
#         return -MAX_TILE_CREDIT