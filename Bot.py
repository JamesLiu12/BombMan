from Player import Player
from collections import deque
from Bomb import Bomb
import time
import random

class Bot(Player):
    def __init__(self, maze, id, posx, posy, HP=3, speed=4, bombDelay=2):
        super().__init__(maze, None, None, None, None, None, id, posx, posy, HP, speed, bombDelay)
        self.origGrids=[[None,'\\','~','/',None,None],['┌','□','_','□','┘',')'],[None,'/',None,'⁊',None,None]]
        self.setBombProb = 0.5
    def IsBelongTo(self, typ):
        return typ == Bot or super().IsBelongTo(typ)
    def GetName(self):
        return 'Bot ' + str(self.id)
    def GetSetBombProb(self):
        return self.setBombProb
    
    def IsPosSafeToPass(self, posx, posy, distance, speed, newBomb = None):
        timeBeamAppearList = self.maze.GetTimeBeamAppearLists()[posx][posy]
        deviate = 0.1
        for appearTime in timeBeamAppearList:
            if (distance - 1) / speed + time.perf_counter() - deviate < appearTime < (distance + 1) / speed + time.perf_counter() + deviate: return False
        if newBomb != None:
            if (distance - 1) / speed + time.perf_counter() - deviate < newBomb.setTime + newBomb.delay < (distance + 1) / speed + time.perf_counter() +  deviate: return False
        return True
    def IsPosSafeToStay(self, posx, posy, newBomb = None):
        if len(self.maze.GetTimeBeamAppearLists()[posx][posy]) != 0: return False
        if newBomb != None:
            if (posx == newBomb.posx or posy == newBomb.posy) and (abs(posx - newBomb.posx) < newBomb.GetDistance() or abs(posy - newBomb.posy) < newBomb.GetDistance()):
                return False
        return True

    def FindPathToSafePos(self, isToSetBomb):
        newBomb = None
        if isToSetBomb: newBomb = Bomb(self.maze, self, self.posx, self.posy, self.bombDistance, self.atk, self.bombDelay, time.perf_counter())
        # if self.IsPosSafeToStay(self.posx, self.posy, newBomb): return 0, 0
        dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        random.shuffle(dir)
        que = [(self.posx, self.posy)]
        dis = [[0x3f3f3f3f for j in range(self.maze.GetWidth())] for i in range(self.maze.GetHeight())]
        prePos = [[(None, None) for j in range(self.maze.GetWidth())] for i in range(self.maze.GetHeight())]
        dis[self.posx][self.posy] = 0
        destination = self.posx, self.posy
        isFoundWay = False
        while len(que) and not isFoundWay:
            prePosx, prePosy = que[0]
            del que[0]
            for dirx, diry in dir:
                newPosx = prePosx + dirx
                newPosy = prePosy + diry
                isSafeToPass = self.IsPosSafeToPass(newPosx, newPosy, dis[prePosx][prePosy] + 1, self.speed, newBomb)
                if dis[newPosx][newPosy] <= dis[prePosx][prePosy] + 1: continue
                if self.maze.IsOutOfRange(newPosx, newPosy) or self.maze.IsBlockPlayer(newPosx, newPosy) or not isSafeToPass:
                    continue
                if isSafeToPass:
                    destination = newPosx, newPosy
                que.append((newPosx, newPosy))
                prePos[newPosx][newPosy] = prePosx, prePosy
                dis[newPosx][newPosy] = dis[prePosx][prePosy] + 1
                if self.IsPosSafeToStay(newPosx, newPosy, newBomb):
                    destination = newPosx, newPosy
                    isFoundWay = True
                    break
        path = []
        tempPosx, tempPosy = destination
        while tempPosx != self.posx or tempPosy != self.posy:
            path.append((tempPosx, tempPosy))
            tempPosx, tempPosy = prePos[tempPosx][tempPosy]
        path.reverse()
        # prePosx, prePosy = path[0]
        # for i in range(1, len(path)):
        #     tempPosx, tempPosy = path[i][0], path[i][1]
        #     path[i] = path[i][0] - prePosx, path[i][1] - prePosy
        #     prePosx, prePosy = tempPosx, tempPosy
        # path[0] = path[0][0] - self.posx, path[0][1] - self.posy
        # return path
        if len(path) == 0: return 0, 0
        return path[0][0] - self.posx, path[0][1] - self.posy