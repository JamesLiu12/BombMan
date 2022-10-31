from BaseObject import BaseObject
from colorama import Fore, Back, Style

class Obstacle(BaseObject):
    def __init__(self, maze, item = None):
        super().__init__(maze)
        self.HP = None
        self.isBlockPlayer = True
        self.isBlockBeam = True
        self.priority = 5
        self.item = item
        self.foreColors = [[Fore.WHITE for j in range(6)] for i in range(3)]
    def ChangeHP(self, val):
        self.HP += val

    def IsDead(self):
        return self.HP <= 0

    def IsBelongTo(self, typ):
        return typ == Obstacle or super().IsBelongTo(typ)