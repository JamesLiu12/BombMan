from Item import Item
from colorama import Fore, Back, Style
class Item_BombDistanceUp(Item):
    def __init__(self, maze):
        super().__init__(maze)
        self.val = 1
        self.delay = 10
        self.grids = [['┌','─','─','─','─','┐'],['🔥','L','E','N','','↑'],['└', '─', '─', '─', '─', '┘']]
        self.foreColors=[[Fore.YELLOW for j in range(6)] for i in range(3)]
    def IsBelongTo(self, typ):
        return typ == Item_BombDistanceUp or super().IsBelongTo(typ)