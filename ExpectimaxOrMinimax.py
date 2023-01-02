import Helper
import numpy as np


def valueExpectimax(grid, maxdepth, isMaximizing):
    if maxdepth == 0:
        return Helper.heuristic(grid)
    if not Helper.canMove(grid):
        return Helper.heuristic(grid)
    if isMaximizing:
        v = -np.inf
        [children, moving] = Helper.getAvailableChildren(grid)
        for child in children:
            v = max(v, valueExpectimax(child, maxdepth-1, False))
                                     
        return v
    else:
        cells = [i for i, x in enumerate(grid) if x == 0]
        v = 0
        children = []
        probability_children = []
        for c in cells:
            gridcopy = grid[:]
            gridcopy[c]= 2
            children.append(gridcopy)
            probability_children.append((1/Helper.empty_tiles(grid))*0.9)
            gridcopy = grid[:]
            gridcopy[c]=4
            children.append(gridcopy)
            probability_children.append((1/Helper.empty_tiles(grid))*0.1)
        for child_index in range(len(children)):
            v += valueExpectimax(children[child_index],maxdepth-1,True) * probability_children[child_index]
            
        return v

def valueMinimax(grid, maxdepth, alpha, beta, isMaximizing):
    if maxdepth == 0:
        return Helper.heuristic(grid)
    if not Helper.canMove(grid):
        return Helper.heuristic(grid)
    if isMaximizing:
        v = -np.inf
        [children, moving] = Helper.getAvailableChildren(grid)
        for child in children:
            v = max(v, valueMinimax(child, maxdepth-1, alpha, beta, False))
            if v >= beta:
                return v
            alpha = max(alpha, v)
        return v
    else:
        cells = [i for i, x in enumerate(grid) if x == 0]
        children = []
        for c in cells:
            gridcopy = list(grid)
            gridcopy[c]=2
            children.append(gridcopy)
            gridcopy = list(grid)
            gridcopy[c]=4
            children.append(gridcopy)
        v = np.inf
        for child in children:
            v = min(v,valueMinimax(child,maxdepth-1,alpha,beta,True))
            if v <= alpha:
                return v
            beta = min(beta,v)
        return v
