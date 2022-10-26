from Obstacle import Obstacle
class Wall(Obstacle):
    def __init__(self, item = None):
        super().__init__(item)
        self.HP = 1
        self.grids = [['#', '*', '*', '#', '#', '*'], ['#', '*', '#', '*', '*', '#'], ['*', '#', '*', '#', '#', '*']]