from Obstacle import Obstacle


class UnbreakWall(Obstacle):
    def __init__(self, item=None):
        super().__init__(item)
        self.HP = 9999
        # self.grids = [['▊' for j in range(6)] for i in range(3)]