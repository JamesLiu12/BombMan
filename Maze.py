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
        self.updateGrid(posx, posy)
    def DeleteObject(self, posx, posy, obj):
        objIndex = None
        for i in range(len(self.objectLists[posx][posy])):
            if self.objectLists[posx][posy][i] == obj:
                objIndex = i
                break
        if objIndex != None: 
            del self.objectLists[posx][posy][objIndex]
            self.updateGrid(posx, posy)
    def updateGrid(self, posx, posy):
        objectList = self.objectLists[posx][posy]
        for obj in objectList:
            if type(obj) == Player:
                player = obj
                if player.posx == posx and player.posy == posy: #Leaving
                    if player.dirx == -1:
                        for i, ii in zip(range(0, player.parts[0]), range(3 - player.parts[0], 3)):
                            for j in range(0, 6):
                                if player.grids[ii][j] != None: self.grids[posx][posy][i][j] = player.grids[ii][j]
                    elif player.dirx == 1:
                        for i, ii in zip(range(3 - player.parts[0], 3), range(0, player.parts[0])):
                            for j in range(6):
                                if player.grids[ii][j] != None: self.grids[posx][posy][i][j] = player.grids[ii][j]
                    elif player.diry == -1:
                        for i in range(0, 3):
                            for j, jj in zip(range(0, player.parts[1]), range(6 - player.parts[1], 6)):
                                if player.grids[i][jj] != None: self.grids[posx][posy][i][j] = player.grids[i][jj]
                    elif player.diry == 1:
                        for i in range(0, 3):
                            for j, jj in zip(range(6 - player.parts[1], 6), range(0, player.parts[1])):
                                if player.grids[i][jj] != None: self.grids[posx][posy][i][j] = player.grids[i][jj]
                    else: #Static 
                        for i in range(0, 3):
                            for j in range(0, 6):
                                if player.grids[i][j] != None: self.grids[posx][posy][i][j] = player.grids[i][j]
                else: #Entering
                    if player.dirx == -1:
                        for i, ii in zip(range(player.parts[0], 3), range(0, 3 - player.parts[0])):
                            for j in range(0, 6):
                                if player.grids[ii][j] != None: self.grids[posx][posy][i][j] = player.grids[ii][j]
                    elif player.dirx == 1:
                        for i, ii in zip(range(0, 3 - player.parts[0]), range(player.parts[0], 3)):
                            for j in range(6):
                                if player.grids[ii][j] != None: self.grids[posx][posy][i][j] = player.grids[ii][j]
                    elif player.diry == -1:
                        for i in range(0, 3):
                            for j, jj in zip(range(player.parts[1], 6), range(0, 6 - player.parts[1])):
                                if player.grids[i][jj] != None: self.grids[posx][posy][i][j] = player.grids[i][jj]
                    elif player.diry == 1:
                        for i in range(0, 3):
                            for j, jj in zip(range(0, 6 - player.parts[1]), range(player.parts[1], 6)):
                                if player.grids[i][jj] != None: self.grids[posx][posy][i][j] = player.grids[i][jj]
            else:
                for i in range(0, 3):
                    for j in range(0, 6):
                        if obj.grids[i][j] != None: self.grids[posx][posy][i][j] = obj.grids[i][j]
    def IsBolckPlayer(self, posx, posy):
        for obj in self.objectLists[posx][posy]:
            if obj.isBlockPlayer: return True
        return False