import time
from colorama import Fore, Back, Style
from BaseObject import BaseObject

class Bomb(BaseObject):
    def __init__(self, posx, posy, distance, damage, delay, setTime):
        super().__init__()
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
    def explode(self):
        pass
    def IsBelongTo(self, typ):
        return typ == Bomb or super().IsBelongTo(typ)
