import ExpectimaxOrMinimax
from Grid import Grid
import numpy as np
import Helper


class PlayerAI:
        def __init__(self,depth: int):
                self.depth = depth
        def getMoveExpectimax(self, grid: Grid):
                mapgrid = []
                for i in range(4):
                        mapgrid.extend(grid.map[i])
                [children, moving] = Helper.getAvailableChildren(mapgrid)
                maxpath = -np.inf
                direction = 0
                for i in range(len(children)):
                        c = children[i]
                        m = moving[i]
                        highest_value = -np.inf
                        maxdepth = self.depth
                        highest_value = ExpectimaxOrMinimax.valueExpectimax(c, maxdepth, False)
                        
                        if highest_value > maxpath:
                            direction = m
                            maxpath = highest_value
                return direction
        
        def getMoveMinimax(self, grid):
                mapgrid = []
                for i in range(4):
                        mapgrid.extend(grid.map[i])
                [children, moving] = Helper.getAvailableChildren(mapgrid)
                maxpath = -np.inf
                direction = 0
                for i in range(len(children)):
                        c = children[i]
                        m = moving[i]
                        highest_value = -np.inf
                        maxdepth = self.depth
                        highest_value = ExpectimaxOrMinimax.valueMinimax(c, maxdepth,-np.infty, np.infty, False)
                        
                        if highest_value > maxpath:
                            direction = m
                            maxpath = highest_value
                return direction
