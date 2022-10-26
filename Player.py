import keyboard
import time
from colorama import Fore, Back, Style
from BaseObject import BaseObject
class Player(BaseObject):
    def __init__(self, key_up, key_down, key_left, key_right, key_setBomb, id, posx, posy, HP = 3, speed = 4, bombDelay = 2):
        super().__init__()
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
        self.bombDistance = 3
        self.bombDelay = 1.5
        self.damageMade = 0
        self.numberKilled = 0
        self.priority = 1
        self.flickGids = [[None for j in range(6)] for i in range(3)]
        self.origGrids = [['_', '_', '⁔', '_', '_', None], ['(', '≧', '▽', '≦', ')', 'o'], [None, '/', None, None, "\\", None]]
        self.grids = self.origGrids
        self.foreColors = [[Fore.WHITE for j in range(6)] for i in range(3)]
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
    def SetBomb(self, bomb):
        self.bombs.append(bomb)
        self.preSetBombTime = float(time.perf_counter())
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
    def returnToOrigGrid(self):
        self.grids = self.origGrids
    def ChangeHP(self, x): 
        if x < 0:
            if self.IsInDamage(): return
            self.GetDamage()
        self.HP += x
    def GetTimeGap(self, axis):
        return 1 / self.speed / (3 if axis == 0 else 6)
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