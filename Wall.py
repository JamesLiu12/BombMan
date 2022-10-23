from MoveObject import MoveObject


class Wall(MoveObject):
    def __init__(self, HP = 1, speed = 0):
        self.grids = [['\\', '-', '/'], ['|', 'O', '|'], ['/', '-', '\\']]
        self.blockPlayer = True
        self.blockLaser = True