from Item import Item
from colorama import Fore, Back, Style

class Item_HPup(Item):
    def __init__(self):
        super().__init__()
        #如果运行时出现字符宽度过大，可将self.grids[1][5]改为None(本地sublimetext与ed测试显示正常)——AA
        self.grids = [['┌', '─', '─', '─', '─', '┐'], ['│', '♥', 'H', 'P', '↑', '│'], ['└', '─', '─', '─', '─', '┘']]
        self.foreColors = [[Fore.LIGHTRED_EX for j in range(6)] for i in range(3)]
        self.val = 1
        self.delay = None
    def IsBelongTo(self, typ):
        return typ == Item_HPup or super().IsBelongTo(typ)