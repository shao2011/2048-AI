#!/usr/bin/env python
#coding:utf-8

import Minimax_BetaApha_Pruning
from Grid import Grid
import numpy as np
import Helper


class PlayerAI:
        def __init__(self,depth: int):
                self.depth = depth
        def getMoveExpectimax(self, grid):
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
                        highest_value = Minimax_BetaApha_Pruning.valueExpectimax(c, maxdepth, False)
                        # if m == 0 or m == 2:
                        #     highest_value += 10e6
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
                        highest_value = Minimax_BetaApha_Pruning.valueMinimax(c, maxdepth,-np.infty, np.infty, False)
                        # if m == 0 or m == 2:
                        #     highest_value += 10e6
                        if highest_value > maxpath:
                            direction = m
                            maxpath = highest_value
                return direction


