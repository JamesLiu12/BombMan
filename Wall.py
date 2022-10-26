from Obstacle import Obstacle
class Wall(Obstacle):
    def __init__(self, HP, item = None):
        super().__init__(item)
        self.HP = HP
        self.HPGrids = [
            [['┌', '*', '#',None, '#', '┐'], ['#',None, '&',None, '#', '*'], ['└', '*', '*', '#',None, '┘']],
            [['┌', '#', '*', '*', '#', '┐'], ['#',None, '#', '#', '*', '#'], ['└', '#', '*', '*', '#', '┘']],
            [['┌', '#', '#', '#', '#', '┐'], ['#', '#', '#', '#', '#', '#'], ['└', '#', '#', '#', '#', '┘']],
        ]
        self.grids = self.HPGrids[HP - 1]
    def ChangeHP(self, val):
        self.HP += val
        if self.HP > 0:
            self.grids = self.HPGrids[self.HP - 1]
        