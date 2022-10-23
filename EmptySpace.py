class EmptySpace():
    def __init__(self):
        self.grids = [[' ' for j in range(6)] for i in range(3)]
        self.coverObject = None
        self.blockPlayer = False
    def StartEnter(self, player):
        self.coverObject = player
        self.blockPlayer = True