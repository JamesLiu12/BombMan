class Laser:
    def __init__(self):
        self.coverObject = None
        self.isBlockPlayer = False
        self.isBlockLaser = False
        self.priority = 0
        # self.grids = [['~' for j in range(6)] for i in range(3)]
    def StartEnter(self, player):
        self.coverObject = player
        self.blockPlayer = True