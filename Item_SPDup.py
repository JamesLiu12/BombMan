from Item import Item
from colorama import Fore, Back, Style

class Item_SPDup(Item):
    def __init__(self):
        super().__init__()
        self.val = 2
        self.delay = 10
        #若运行时出现字符宽度不等，去掉羽毛并将self.grids[1][0]和self.grids[1][5]改为'│' ——AA
        self.grids=[['┌','─','─','─','─','┐'],['🪶','S','P','D','↑',None],['└', '─', '─', '─', '─', '┘']]
        self.foreColors=[[Fore.LIGHTBLUE_EX for j in range(6)] for i in range(3)]