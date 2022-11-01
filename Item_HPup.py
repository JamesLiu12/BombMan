from Item import Item
from colorama import Fore, Back, Style

class Item_HPup(Item):
    def __init__(self, maze):
        super().__init__(maze)
        self.grids = [['┌', '─', '─', '─', '─', '┐'], [None, '♥', 'H', 'P', '↑', None], ['└', '─', '─', '─', '─', '┘']]
        self.foreColors = [[Fore.LIGHTRED_EX for j in range(6)] for i in range(3)]
        self.val = 1
        self.delay = None
    def IsBelongTo(self, typ):
        return typ == Item_HPup or super().IsBelongTo(typ)