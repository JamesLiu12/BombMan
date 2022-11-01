from Player import Player
from collections import deque
class Bot(Player):
    def __init__(self, maze, id, posx, posy, HP=3, speed=4, bombDelay=2):
        super().__init__(maze, None, None, None, None, None, id, posx, posy, HP, speed, bombDelay)
        self.origGrids=[[None,'\\','~','/',None,None],['┌','□','_','□','┘',')'],[None,'/',None,'⁊',None,None]]
    def IsBelongTo(self, typ):
        return typ == Bot or super().IsBelongTo(typ)
    def GetName(self):
        return 'Bot ' + str(self.id)

    def IfPosSafe(self, posx, posy, x, y):
        if posx != x and posy != y:
            return True
        if posx == x:
            if abs(posy-y)>self.GetBombDistance:
                return True
            for i in range(posy+abs(y-posy)//(y-posy), y, abs(y-posy)//(y-posy)):
                if self.maze.IsBlockBeam(x, i):
                    return True
        if posy == y:
            if abs(posx-x)>self.GetBombDistance:
                return True
            for i in range(posx+abs(x-posx)//(x-posx), x, abs(x-posx)//(x-posx)):
                if self.maze.IsBlockBeam(i, y):
                    return True
        return False
    def IfPathSafe(self, path):
        for i in player.bombs:
            for j in path:
                if j in self.Bombrange(i.posx,i.posy):
                    if i.setTime + Player.bombDelay - self.flickTimeGap < j / self.speed < i.setTime + Player.bombDelay +self.flickTimeGap:
                        return False
        return True


    def FindWay(self, posx, posy):
        direc = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        dui = deque()
        dui.append([posx,posy])
        path = []
        h = [[0 for i in range(13)] for j in range(13)]
        a = [[0 for i in range(13)] for j in range(13)]
        while dui:
            b = dui.popleft()
            x , y = b[0] , b[1]
            if not self.maze.IsBolckPlayer(x,y) and self.IfPosSafe(x, y, posx, posy):
                x2 = x
                y2 = y
                while h[x2][y2] != (posx, posy):
                    path.append((x2,y2))
                    x3 = h[x2][y2][0]
                    y3 = h[x2][y2][1]
                    x2 ,y2 = x3, y3
                path.append((x2,y2))
                path.reverse()
                f = True
                for i in path:
                    if not self.IfPathSafe(path):
                        f = False
                if f:
                    return True, path
            for i in direc:
                x1 = x + i[0]
                y1 = y + i[1]
                if 0 <= x1 < 13 and 0 <= y1 < 13:
                    if a[x1][y1] == 0 and not self.maze.IsBolckPlayer(x,y):
                        dui.append([x1,y1])
                        h[x1][y1] = (x,y)
                        a[x1][y1] = a[x][y] + 1
        return False, []

    def Bombrange(self,x,y):
        a = []
        for i in range(x,x+self.GetBombDistance+1):
            if not self.IfPosSafe(i,y,x,y):
                a.append((x,y))
        for i in range(x,x-self.GetBombDistance-1,-1):
            if not self.IfPosSafe(i,y,x,y):
                a.append((x,y))
        for i in range(y,y+self.GetBombDistance+1):
            if not self.IfPosSafe(x,i,x,y):
                a.append((x,y))
        for i in range(y,y-self.GetBombDistance-1,-1):
            if not self.IfPosSafe(x,i,x,y):
                a.append((x,y))
        return a

