from Item import Item
from colorama import Fore, Back, Style

class Item_ATKup(Item):
    def __init__(self):
        super().__init__()
        self.grids = [['┌', '─', '─', '─', '─', '┐'], ['⚔', 'A', 'T', 'K', '↑', ''], ['└', '─', '─', '─', '─', '┘']]
        self.val = 1
        self.delay = 10
        self.foreColors = [[Fore.YELLOW for j in range(6)] for i in range(3)]
    def IsBelongTo(self, typ):
        return typ == Item_ATKup or super().IsBelongTo(typ)