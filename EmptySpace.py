class EmptySpace():
    def __init__(self):
        self.grids = [[' ' for j in range(6)] for i in range(3)]
        self.isBlockPlayer = False
        self.isBlockBeam = False
        self.priority = 0