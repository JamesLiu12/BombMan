class BaseObject:
    def __init__(self, maze):
        self.grids = [[None for j in range(6)] for i in range(3)]
        self.backColors = [[None for j in range(6)] for i in range(3)]
        self.foreColors = [[None for j in range(6)] for i in range(3)]
        self.isBlockPlayer = False
        self.isBlockBeam = False
        self.priority = 0
        self.maze = maze
    def IsBelongTo(self, typ):
        return typ == BaseObject