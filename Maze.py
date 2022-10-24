from BombMan.EmptySpace import EmptySpace
from Wall import Wall


class Maze:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.objectLists = [[[EmptySpace()] for j in range(width)] for i in range(height)]
        self.grids = [[[[' ' for p in range(6)] for k in range(3)] for j in range(width)] for i in range(height)]
    def Show(self):
        for i in range(self.height):
            for j in range(3):
                print(''.join([''.join(self.grids[i][k][j]) for k in range(self.height)]))
    def GetObjectsInPos(self, posx, posy):
        return self.objectLists[posx][posy]
    def InsertObject(self, insertedObject, posx, posy):
        objectList = self.objectLists[posx][posy]
        lb = 0
        rb = len(objectList) - 1
        while lb <= rb:
            mid = lb + rb >> 1
            if objectList[mid].priority < insertedObject.priority: lb = mid + 1
            else: rb = mid - 1
            objectList.insert(rb, insertedObject)
    def updateGrid(self, posx, posy):
        objectList = self.objectLists[posx][posy]
        for obj in objectList:
            self.grids[posx][posy] = [obj.grids[i][j] if obj.grids[i][j] != None else self.grids[posx][posy] for j in range(6) for i in range(3)]
    def IsBolckPlayer(self, posx, posy):
        for obj in self.objectLists[posx][posy]:
            if obj.isBlockPlayer: return True
        return False