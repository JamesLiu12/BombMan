from BaseObject import BaseObject


class Obstacle(BaseObject):
    def __init__(self, HP = 1, speed = 0):
        super().__init__()
        # self.grids = [['\\', '-', '/'], ['|', 'O', '|'], ['/', '-', '\\']]
        self.isBlockPlayer = True
        self.isBlockBeam = True
        self.priority = 4
    