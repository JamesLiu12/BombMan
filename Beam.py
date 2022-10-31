from turtle import delay
from BaseObject import BaseObject
from colorama import Fore, Back, Style
import time
class Beam(BaseObject):
    def __init__(self, maze, centerPosx, centerPosy, distance, damage, setTime, setBy):
        super().__init__(maze)
        self.isBlockPlayer = False
        self.isBlockBeam = False
        self.delay = 0.5
        self.centerPosx, self.centerPosy = centerPosx, centerPosy
        self.distance = distance
        self.damage = damage
        self.setTime = setTime
        self.setBy = setBy
        self.priority = 3
        self.backColors = [[Back.YELLOW for j in range(6)] for i in range(3)]
    def IsToDelete(self):
        return float(time.perf_counter()) - self.setTime >= self.delay
    def IsBelongTo(self, typ):
        return typ == Beam or super().IsBelongTo(typ)
    def DestroyBeam(self, posx, posy):
        self.maze.DeleteObject(posx, posy, self)
        dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        for dirx, diry in dir:
            for i in range(1, self.distance):
                newPosx = posx + dirx * i
                newPosy = posy + diry * i
                if self.maze.IsOutOfRange(newPosx, newPosy): break
                self.maze.DeleteObject(newPosx, newPosy, self)