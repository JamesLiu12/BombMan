from Wall import Wall


class Maze:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.grids = [[Wall() for j in range(width)] for i in range(height)]
    def Show(self):
        for i in range(self.height):
            for j in range(3):
                print(''.join([''.join(self.grids[i][k].grids[j]) for k in range(self.height)]))
    def ChangeGrid(self, posx, posy, target):
        self.grids[posx][posy] = target
    def getObject(self, posx, posy):
        return self.grids[posx][posy]