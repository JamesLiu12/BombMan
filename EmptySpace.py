from colorama import Fore, Back, Style

from BaseObject import BaseObject

class EmptySpace(BaseObject):
    def __init__(self, maze):
        super().__init__(maze)
        self.grids = [[' ' for j in range(6)] for i in range(3)]
        self.backColors = [[Back.BLACK for j in range(6)] for i in range(3)]
        self.isBlockPlayer = False
        self.isBlockBeam = False
        self.priority = 0
    def IsBelongTo(self, typ):
        return type == EmptySpace or super().IsBelongTo(typ)