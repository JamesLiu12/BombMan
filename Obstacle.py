class Obstacle:
    def __init__(self, HP = 1, speed = 0):
        # self.grids = [['\\', '-', '/'], ['|', 'O', '|'], ['/', '-', '\\']]
        self.isBlockPlayer = True
        self.isBlockBeam = True
        self.priority = 4
    