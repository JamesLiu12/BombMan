from re import L
import keyboard
import time
from colorama import Fore, Back, Style
from Item_ATKup import Item_ATKup
from BaseObject import BaseObject
from Item_BombDelayDown import Item_BombDelayDown
from Item_BombDistanceUp import Item_BombDistanceUp
from Item_BombTimeGapDown import Item_BombTimeGapDown
from Item_HPup import Item_HPup
from Item_SPDup import Item_SPDup
from Item import Item
from Bomb import Bomb
class Player(BaseObject):
    def __init__(self, maze, key_up, key_down, key_left, key_right, key_setBomb, id, posx, posy, HP = 3, speed = 4, bombDelay = 2):
        super().__init__(maze)
        self.HP = HP
        self.speed = speed
        self.key_up = key_up
        self.key_down = key_down
        self.key_left = key_left
        self.key_right = key_right
        self.key_setBomb = key_setBomb
        self.id = id
        self.posx = posx
        self.posy = posy
        self.bombDelay = bombDelay
        self.dirx = 0
        self.diry = 0
        self.atk = 1
        self.preDamageTime = False
        self.isBlockPlayer = True
        self.isBlockBeam = False
        self.preMoveTime = 0
        self.preSetBombTime = 0
        self.setBombTimeGap = 1.5
        self.damageTimeGap = 1.5
        self.flickTimeGap = 0.3
        self.preFlickTime = 0
        self.parts = [3, 6]
        self.bombs = []
        self.beams = []
        self.buffs = []
        self.bombDistance = 3
        self.bombDelay = 1.5
        self.damageMade = 0
        self.numberKilled = 0
        self.priority = 1
        self.flickGids = [[None for j in range(6)] for i in range(3)]
        self.origGrids = [['_', '_', '⁔', '_', '_', None], ['(', '≧', '▽', '≦', ')', 'o'], [None, '/', None, None, "\\", None]]
        self.grids = self.origGrids
        self.colorboard=[Fore.CYAN,Fore.LIGHTMAGENTA_EX,Fore.CYAN,Fore.LIGHTMAGENTA_EX]
        self.foreColors = [[self.colorboard[self.id-1] for j in range(6)] for i in range(3)]
        self.deadScore = 10
        self.score = 0
    def IsMoving(self):
        return self.dirx != 0 or self.diry != 0
    def GetMoveDir(self):
        #TODO AA
        if self.IsMoving() or self.IsInDamage() or self.IsDead(): return 0, 0
        if keyboard.is_pressed(self.key_up) and not keyboard.is_pressed(self.key_down):
            return -1, 0
        elif keyboard.is_pressed(self.key_down) and not keyboard.is_pressed(self.key_up):
            return 1, 0
        elif keyboard.is_pressed(self.key_left) and not keyboard.is_pressed(self.key_right):
            return 0, -1
        elif keyboard.is_pressed(self.key_right) and not keyboard.is_pressed(self.key_left):
            return 0, 1
        else: return 0, 0
    def IsSetBombPress(self):
        if float(time.perf_counter()) - self.preSetBombTime < self.setBombTimeGap: return False
        return keyboard.is_pressed(self.key_setBomb)
    def SetBomb(self):
        bomb = Bomb(self.maze, self, self.posx, self.posy, self.bombDistance, self.atk, self.bombDelay, float(time.perf_counter()))
        self.bombs.append(bomb)
        self.preSetBombTime = float(time.perf_counter())
        self.maze.InsertObject(bomb, self.posx, self.posy)
    def SetBeam(self, beam):
        self.beams.append(beam)
    def Move(self):
        if self.dirx != 0: self.parts[0] -= 1
        else: self.parts[1] -= 1
        self.preMoveTime = float(time.perf_counter())
    def StartMove(self, dirx, diry):
        self.dirx = dirx
        self.diry = diry
    def IsEndMove(self):
        return self.parts[0] == 0 or self.parts[1] == 0
    def GetDamage(self):
        self.preDamageTime = float(time.perf_counter())
    def IsInDamage(self):
        return float(time.perf_counter()) - self.preDamageTime <= self.damageTimeGap
    def Flicking(self):
        if float(time.perf_counter()) - self.preFlickTime >= self.flickTimeGap:
            self.grids = self.origGrids if self.grids == self.flickGids else self.flickGids
            self.maze.updateGrid(self.posx, self.posy)
            self.maze.updateGrid(self.posx + self.dirx, self.posy + self.diry)
    def returnToOrigGrid(self):
        self.grids = self.origGrids
        self.maze.updateGrid(self.posx, self.posy)
        self.maze.updateGrid(self.posx + self.dirx, self.posy + self.diry)
    def ChangeHP(self, x): 
        if x < 0:
            if self.IsInDamage(): return
            self.GetDamage()
        self.HP += x
    def ChangeATK(self, x):
        self.atk += x
    def ChangeSpeed(self, x):
        self.speed += x
    def ChangeBombDelay(self, x):
        self.bombDelay += x
    def ChangeSetBombTimeGap(self, x):
        self.setBombTimeGap += x
    def ChangeBombDistance(self, x):
        self.bombDistance += x
    def ChangeScore(self, x):
        self.score += x
    def GetTimeGap(self, axis):
        return 1 / self.speed / (3 if axis == 0 else 6)
    def GetDeadScore(self):
        return self.deadScore
    def GetScore(self):
        return self.score
    def IsCanMove(self, axis):
        return float(time.perf_counter()) - self.preMoveTime >= self.GetTimeGap(axis) and not self.IsDead()
    def InitParts(self):
        self.parts = [3, 6]
    def InitDir(self):
        self.dirx, self.diry = 0, 0
    def SetPos(self, posx, posy):
        self.posx, self.posy = posx, posy
    def IsDead(self):
        return self.HP <= 0
    def IsBelongTo(self, typ):
        return typ == Player or super().IsBelongTo(typ)
    def GetItem(self, item):
        if item.delay != None: self.buffs.append((item, time.perf_counter()))
        if item.IsBelongTo(Item_ATKup):
            self.ChangeATK(item.val)
        elif item.IsBelongTo(Item_HPup):
            self.ChangeHP(item.val)
        elif item.IsBelongTo(Item_SPDup):
            self.ChangeSpeed(item.val)
        elif item.IsBelongTo(Item_BombDelayDown):
            self.ChangeBombDelay(item.val)
        elif item.IsBelongTo(Item_BombTimeGapDown):
            self.ChangeSetBombTimeGap(item.val)
        elif item.IsBelongTo(Item_BombDistanceUp):
            self.ChangeBombDistance(item.val)
    def CheckItems(self):
        deleteList = []
        for buff in self.buffs:
            item, setTime = buff
            if float(time.perf_counter()) - setTime >= item.delay:
                deleteList.append(buff)
                if item.IsBelongTo(Item_ATKup):
                    self.ChangeATK(-item.val)
                elif item.IsBelongTo(Item_SPDup):
                    self.ChangeSpeed(-item.val)
                elif item.IsBelongTo(Item_BombDelayDown):
                    self.ChangeBombDelay(-item.val)
                elif item.IsBelongTo(Item_BombTimeGapDown):
                    self.ChangeSetBombTimeGap(-item.val)
                elif item.IsBelongTo(Item_BombDistanceUp):
                    self.ChangeBombDistance(item.val)
        for buff in deleteList:
            self.buffs.remove(buff)

    def GetBombDistance(self):
        return self.bombDistance

    def Getspeed(self):
        return self.speed

    def GetBombtime(self):
        return self.bombDelay
        
    def GetName(self):
        return 'Player ' + str(self.id)
        
    def PeakUpItem(self, posx, posy):
        for obj in self.maze.objectLists[posx][posy]:
            if obj.IsBelongTo(Item):
                self.GetItem(obj)
                self.maze.DeleteObject(posx, posy, obj)
                return
                