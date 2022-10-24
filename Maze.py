from EmptySpace import EmptySpace
from Player import Player


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
            objectList.insert(lb, insertedObject)
    def DeleteObject(self, posx, posy, obj):
        objIndex = None
        for i in range(self.objectLists[posx][posy]):
            if self.objectLists[posx][posy][i] == obj:
                objIndex = i
                break
        if objIndex != None: del self.objectLists[posx][posy][objIndex]
    def updateGrid(self, posx, posy):
        objectList = self.objectLists[posx][posy]
        for obj in objectList:
            if type(obj) == Player:
                player = obj
                if player.posx == posx and player.posy == player.posy: #Leaving
                    pass
                else: #Entering
                    pass
            else:
                self.grids[posx][posy] = [obj.grids[i][j] if obj.grids[i][j] != None else self.grids[posx][posy] for j in range(6) for i in range(3)]
    def IsBolckPlayer(self, posx, posy):
        for obj in self.objectLists[posx][posy]:
            if obj.isBlockPlayer: return True
        return False