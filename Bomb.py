import time
from colorama import Fore, Back, Style
from BaseObject import BaseObject
from Beam import Beam
from Obstacle import Obstacle
class Bomb(BaseObject):
    def __init__(self, maze, player, posx, posy, distance, damage, delay, setTime):
        super().__init__(maze)
        self.setBy = player
        self.posx = posx
        self.posy = posy
        self.distance = distance
        self.damage = damage
        self.delay = delay
        self.setTime = setTime
        self.isBlockPlayer = True
        self.isBlockBeam = False
        self.priority = 2
        self.grids = [[None for j in range(6)] for i in range(3)]
        self.grids[0][1]='︵'
        self.grids[0][3]=''
        self.grids[0][5]='∗'
        self.grids[1][0]='('
        self.grids[1][3]=')'
        self.grids[1][4]='╯'
        self.grids[2][1]='︶'
        self.grids[2][3]=''
        self.backColors = [[Back.RED for j in range(6)] for i in range(3)]
    def isToExplode(self):
        return float(time.perf_counter()) - self.setTime >= self.delay
    def IsBelongTo(self, typ):
        return typ == Bomb or super().IsBelongTo(typ)
    def GenerateBeam(self, posx, posy):
        beam = Beam(self.maze, posx, posy, self.distance, self.damage, time.perf_counter())
        self.setBy.SetBeam(beam)
        self.maze.InsertObject(beam, posx, posy)
        self.maze.BeamEffect(posx, posy, beam.damage)
        dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        for dirx, diry in dir:
            for i in range(1, beam.distance):
                newPosx = posx + dirx * i
                newPosy = posy + diry * i
                if self.maze.IsOutOfRange(newPosx, newPosy): break
                isBlock = False
                if self.maze.IsBlockBeam(newPosx, newPosy): isBlock = True
                self.maze.BeamEffect(newPosx, newPosy, beam.damage)
                self.maze.InsertObject(beam, newPosx, newPosy)
                if isBlock: break