from ast import Delete
from EmptySpace import EmptySpace
from Item import Item
from Item_ATKup import Item_ATKup
from Item_BombDelayDown import Item_BombDelayDown
from Item_BombDistanceUp import Item_BombDistanceUp
from Item_BombTimeGapDown import Item_BombTimeGapDown
from Item_HPup import Item_HPup
from Item_SPDup import Item_SPDup
from Obstacle import Obstacle
from Player import Player
from colorama import Fore, Back, Style
from UnbreakWall import UnbreakWall
from Wall import Wall
from random import randint
from Bot import Bot
from collections import deque
from Storemap import Storemap

class Maze:
	def __init__(self, height, width, mapnum):
		self.height = height
		self.width = width
		self.objectLists = [[[EmptySpace(self)] for j in range(width)] for i in range(height)]
		self.backColors = [[[[Back.BLACK for p in range(6)] for k in range(3)] for j in range(width)] for i in range(height)]
		self.foreColors = [[[[Fore.WHITE for p in range(6)] for k in range(3)] for j in range(width)] for i in range(height)]
		self.grids = [[[[' ' for p in range(6)] for k in range(3)] for j in range(width)] for i in range(height)]
		self.mapnumber=mapnum
		if (mapnum == 514):
			self.blockMap=Storemap().readmap(self.height,self.width)
		else:
			self.blockMap=Storemap().choosemap(self.mapnumber)
		itemList = [Item_ATKup, Item_BombDelayDown, Item_BombTimeGapDown, Item_BombTimeGapDown, Item_HPup, Item_SPDup]
		maxRandomNumber = 10
		for i in range(self.height):
			for j in range(self.width):
				if self.blockMap[i][j] == 4: 
					self.InsertObject(UnbreakWall(self, self.blockMap[i][j]), i, j)
				elif self.blockMap[i][j] != 0:
					randomNumber = randint(0, maxRandomNumber)
					if randomNumber >= len(itemList):
						self.InsertObject(Wall(self, self.blockMap[i][j]), i, j)
					else:
						self.InsertObject(Wall(self, self.blockMap[i][j], itemList[randomNumber](self)), i, j)
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
			

	def IsOutOfRange(self, posx, posy):
		return posx < 0 or posx >= self.height or posy < 0 or posy >= self.width
	
	def IsBolckPlayer(self, posx, posy):
		for obj in self.objectLists[posx][posy]:
			if obj.isBlockPlayer: return True
		return False
	def IsBlockBeam(self, posx, posy):
		for obj in self.objectLists[posx][posy]:
			if obj.isBlockBeam: return True
		return False

	def IsContainType(self, posx, posy, typ):
		for obj in self.objectLists[posx][posy]:
			if obj.IsBelongTo(typ): return True
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

	def Path(self, posx, posy):
		min = 100000
		ans = []
		f = False
		for i in range(13):
			for j in range(13):
				if self.blockMap[i][j] == 0 and self.IfPosSafe(i,j,posx,posy):
					a,b = self.FindWay(posx,posy,i,j)
					if a <= ((Player.GetBombtime)//Bot.getspeed) and a <= min and a != 0:
						min = a
						ans = b
						f = True
		return f, ans

	def IfPosSafe(self, posx, posy, x, y):
		if posx != x and posy != y:
			return True
		if posx == x:
			if abs(posy-y)>Player.GetBombDistance:
				return True
			for i in range(posy,y,abs(y-poy)//(y-posy)):
				if self.IsBlockBeam(x,i):
					return True
		if posy == y:
			if abs(posx-x)>Player.GetBombDistance:
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