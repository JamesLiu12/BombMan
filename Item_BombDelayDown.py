from Item import Item
from colorama import Fore, Back, Style

class Item_BombDelayDown(Item):
    def __init__(self, maze):
        super().__init__(maze)
        self.val = -0.5
        self.delay = 10
        self.grids=[
                    ['┌','─','─','─','─','┐'],
                    [None,'⏲','C','D','↓',None],
                    ['└', '─', '─', '─', '─', '┘']
                    ]
        self.foreColors=[[Fore.LIGHTGREEN_EX for j in range(6)] for i in range(3)]
    def IsBelongTo(self, typ):
        return typ == Item_BombDelayDown or super().IsBelongTo(typ)