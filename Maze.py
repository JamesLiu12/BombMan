from ast import Delete
from EmptySpace import EmptySpace
from Item import Item
from Obstacle import Obstacle
from Player import Player
from colorama import Fore, Back, Style
from UnbreakWall import UnbreakWall
from Wall import Wall
from collections import deque
class Maze:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.objectLists = [[[EmptySpace()] for j in range(width)] for i in range(height)]
        self.backColors = [[[[Back.BLACK for p in range(6)] for k in range(3)] for j in range(width)] for i in range(height)]
        self.foreColors = [[[[Fore.WHITE for p in range(6)] for k in range(3)] for j in range(width)] for i in range(height)]
        self.grids = [[[[' ' for p in range(6)] for k in range(3)] for j in range(width)] for i in range(height)]
        self.blockmap=[
                        [4,4,4,4,4,4,4,4,4,4,4,4,4],
                        [4,0,0,0,1,1,1,2,1,0,0,0,4],
                        [4,0,4,1,4,1,4,0,4,1,4,0,4],
                        [4,0,1,2,0,0,2,0,1,1,1,0,4],
                        [4,1,4,0,4,2,4,2,4,1,4,1,4],
                        [4,0,2,0,2,3,3,3,2,0,1,0,4],
                        [4,1,4,2,4,3,4,3,4,2,4,1,4],
                        [4,1,1,0,2,3,3,3,2,0,2,0,4],
                        [4,1,4,0,4,2,4,2,4,1,4,1,4],
                        [4,0,1,2,0,0,2,0,1,1,1,0,4],
                        [4,0,4,1,4,2,4,1,4,1,4,0,4],
                        [4,0,0,0,1,0,1,0,1,0,0,0,4],
                        [4,4,4,4,4,4,4,4,4,4,4,4,4]
                    ]
        self.blocktype=[EmptySpace(),Wall(1),Wall(2),Wall(3),UnbreakWall()]
        for i in range(self.height):
            for j in range(self.width):
                self.InsertObject(self.blocktype[self.blockmap[i][j]], i, j)
        """
        for i in range(self.height):
            self.InsertObject(UnbreakWall(), i, 0)
            self.InsertObject(UnbreakWall(), i, self.width - 1)
        for i in range(self.width):
            self.InsertObject(UnbreakWall(), 0, i)
            self.InsertObject(UnbreakWall(), self.height - 1, i)"""
    def Show(self):
        for i in range(self.height):
            for j in range(3):
                print(''.join([''.join([self.backColors[i][k][j][p] + self.foreColors[i][k][j][p] + self.grids[i][k][j][p] for p in range(6)]) for k in range(self.width)]), end = '')
                print()
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
            if obj.IsBelongTo(Player):
                player = obj
                if player.posx == posx and player.posy == posy: #Leaving
                    if player.dirx == -1:
                        for i, ii in zip(range(0, player.parts[0]), range(3 - player.parts[0], 3)):
                            for j in range(0, 6):
                                if player.grids[ii][j] != None: self.grids[posx][posy][i][j] = player.grids[ii][j]
                                if player.foreColors[ii][j] != None: self.foreColors[posx][posy][i][j] = player.foreColors[ii][j]
                    elif player.dirx == 1:
                        for i, ii in zip(range(3 - player.parts[0], 3), range(0, player.parts[0])):
                            for j in range(6):
                                if player.grids[ii][j] != None: self.grids[posx][posy][i][j] = player.grids[ii][j]
                                if player.foreColors[ii][j] != None: self.foreColors[posx][posy][i][j] = player.foreColors[ii][j]
                    elif player.diry == -1:
                        for i in range(0, 3):
                            for j, jj in zip(range(0, player.parts[1]), range(6 - player.parts[1], 6)):
                                if player.grids[i][jj] != None: self.grids[posx][posy][i][j] = player.grids[i][jj]
                                if player.foreColors[i][jj] != None: self.foreColors[posx][posy][i][j] = player.foreColors[i][jj]
                    elif player.diry == 1:
                        for i in range(0, 3):
                            for j, jj in zip(range(6 - player.parts[1], 6), range(0, player.parts[1])):
                                if player.grids[i][jj] != None: self.grids[posx][posy][i][j] = player.grids[i][jj]
                                if player.foreColors[i][jj] != None: self.foreColors[posx][posy][i][j] = player.foreColors[i][jj]
                    else: #Static 
                        for i in range(0, 3):
                            for j in range(0, 6):
                                if player.grids[i][j] != None: self.grids[posx][posy][i][j] = player.grids[i][j]
                                if player.foreColors[i][j] != None: self.foreColors[posx][posy][i][j] = player.foreColors[i][j]
                else: #Entering
                    if player.dirx == -1:
                        for i, ii in zip(range(player.parts[0], 3), range(0, 3 - player.parts[0])):
                            for j in range(0, 6):
                                if player.grids[ii][j] != None: self.grids[posx][posy][i][j] = player.grids[ii][j]
                                if player.foreColors[ii][j] != None: self.foreColors[posx][posy][i][j] = player.foreColors[ii][j]
                    elif player.dirx == 1:
                        for i, ii in zip(range(0, 3 - player.parts[0]), range(player.parts[0], 3)):
                            for j in range(6):
                                if player.grids[ii][j] != None: self.grids[posx][posy][i][j] = player.grids[ii][j]
                                if player.foreColors[ii][j] != None: self.foreColors[posx][posy][i][j] = player.foreColors[ii][j]
                    elif player.diry == -1:
                        for i in range(0, 3):
                            for j, jj in zip(range(player.parts[1], 6), range(0, 6 - player.parts[1])):
                                if player.grids[i][jj] != None: self.grids[posx][posy][i][j] = player.grids[i][jj]
                                if player.foreColors[i][jj] != None: self.foreColors[posx][posy][i][j] = player.foreColors[i][jj]
                    elif player.diry == 1:
                        for i in range(0, 3):
                            for j, jj in zip(range(0, 6 - player.parts[1]), range(player.parts[1], 6)):
                                if player.grids[i][jj] != None: self.grids[posx][posy][i][j] = player.grids[i][jj]
                                if player.foreColors[i][jj] != None: self.foreColors[posx][posy][i][j] = player.foreColors[i][jj]
            else:
                for i in range(0, 3):
                    for j in range(0, 6):
                        if obj.grids[i][j] != None: self.grids[posx][posy][i][j] = obj.grids[i][j]
                        if obj.backColors[i][j] != None: self.backColors[posx][posy][i][j] = obj.backColors[i][j]
                        if obj.foreColors[i][j] != None: self.foreColors[posx][posy][i][j] = obj.foreColors[i][j]
    def IsBolckPlayer(self, posx, posy):
        for obj in self.objectLists[posx][posy]:
            if obj.isBlockPlayer: return True
        return False
    def IsBlockBeam(self, posx, posy):
        for obj in self.objectLists[posx][posy]:
            if obj.isBlockBeam: return True
        return False
    def BeamEffect(self, posx, posy, damage):
        deadList = []
        for obj in self.objectLists[posx][posy]:
            if obj.IsBelongTo(Obstacle) or obj.IsBelongTo(Player):
                obj.ChangeHP(-damage)
                if obj.IsDead(): deadList.append(obj)
        for obj in deadList:
            if obj.IsBelongTo(Obstacle):
                if obj.item != None:
                    self.InsertObject(obj.item, posx, posy)
            elif obj.IsBelongTo(Player):
                if obj.IsMoving(): self.DeleteObject(posx + obj.dirx, posy + obj.diry, obj)
            self.DeleteObject(posx, posy, obj)
            
    def GenerateBeam(self, posx, posy, beam):
        self.InsertObject(beam, posx, posy)
        self.BeamEffect(posx, posy, beam.damage)
        dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        for dirx, diry in dir:
            for i in range(1, beam.distance):
                newPosx = posx + dirx * i
                newPosy = posy + diry * i
                if self.IsOutOfRange(newPosx, newPosy): break
                isBlock = False
                if self.IsBlockBeam(newPosx, newPosy): isBlock = True
                self.BeamEffect(newPosx, newPosy, beam.damage)
                self.InsertObject(beam, newPosx, newPosy)
                if isBlock: break
    def IsOutOfRange(self, posx, posy):
        return posx < 0 or posx >= self.height or posy < 0 or posy >= self.width
    def DestroyBeam(self, posx, posy, beam):
        self.DeleteObject(posx, posy, beam)
        dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        for dirx, diry in dir:
            for i in range(1, beam.distance):
                newPosx = posx + dirx * i
                newPosy = posy + diry * i
                if self.IsOutOfRange(newPosx, newPosy): break
                self.DeleteObject(newPosx, newPosy, beam)
    def IsContainType(self, posx, posy, typ):
        for obj in self.objectLists[posx][posy]:
            if obj.IsBelongTo(typ): return True
        return False
    def PeakUpItem(self, posx, posy, player):
        for obj in self.objectLists[posx][posy]:
            if obj.IsBelongTo(Item):
                player.GetItem(obj)
                self.DeleteObject(posx, posy, obj)
                return
    def Path(self, posx, posy):
        min = 100000
        ans = []
        f = False
        for i in range(13):
            for j in range(13):
                if self.blockmap[i][j] == 0 and self.IfPosSafe(i,j,posx,posy):
                    a,b = self.FindWay(posx,posy,i,j)
                    if a<= ((player.setBombTimeGap+player.bombDelay)//Bot.speed) and a <= min:
                        min = a
                        ans = b
                        f = True
        return f, ans

    def IfPosSafe(self, posx, posy, x, y):
        if posx != x and posy != y:
            return True
        if posx == x:
            if abs(posy-y)>player.GetBombDistance:
                return True
            for i in range(posy,y,abs(y-poy)//(y-posy)):
                if self.IsBlockBeam(x,i):
                    return True
        if posy == y:
            if abs(posx-x)>player.GetBombDistance:
                return True
            for i in range(posx,x,abs(x-pox)//(x-posx)):
                if self.IsBlockBeam(i,y):
                    return True
        return False

    def FindWay(self, posx, posy, xx, yy):
        direc = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        dui = deque()
        dui.append([posx,posy])
        path=[]
        h = [[0 for i in range(13)] for j in range(13)]
        a = [[0 for i in range(13)] for j in range(13)]
        while dui:
            b = dui.popleft()
            x , y = b[0] , b[1]
            if x == xx and y == yy:
                x2 = xx
                y2 = yy
                while h[x2][y2] != (posx, posy):
                    path.append((x2,y2))
                    x3 = h[x2][y2][0]
                    y3 = h[x2][y2][1]
                    x2 ,y2 = x3, y3
                path.append((x2,y2))
                path.reverse()
                break
            for i in direc:
                x1 = x + i[0]
                y1 = y + i[1]
                if 0 <= x1 < 13 and 0 <= y1 < 13:
                    if a[x1][y1] == 0 and self.blockmap[x1][y1] == 0:
                        dui.append([x1,y1])
                        h[x1][y1] = (x,y)
                        a[x1][y1] = a[x][y] + 1
        return a[xx][yy], path




