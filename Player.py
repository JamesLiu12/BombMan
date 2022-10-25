import keyboard
import time
import pygame
import tty
import termios
import sys
class Player:
    def __init__(self, key_up, key_down, key_left, key_right, id, posx, posy, color, HP = 3, speed = 4):
        self.HP = HP
        self.speed = speed
        self.key_up = key_up
        self.key_down = key_down
        self.key_left = key_left
        self.key_right = key_right
        self.id = id
        self.posx = posx
        self.posy = posy
        self.color = color
        self.dirx = 0
        self.diry = 0
        self.atk = 1
        self.inBeam = False
        self.inDamage = False
        self.isBlockPlayer = True
        self.isBlockBeam = False
        self.preMoveTime = 0
        self.parts = [3, 6]
        self.damageMade = 0
        self.numberKilled = 0
        self.priority = 2
        self.grids=[[None, '_', '_', '△', '_', '_'], ['(', '≧', '▽', '≦', ')', 'o'], [None, '/', None, None, None, "\\"]]
        self.firstvertical=False
        self.firsthorizontal=False
    def read(self):
        fil= sys.stdin.fileno()
        osl = termios.tcgetattr(fil)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fil, termios.TCSADRAIN, osl)
        return ch
    def readkey(self,fn=None):
        getchar= self.read()or fn
        c1 = self.read()
        if ord(c1) != 0x1b:
            return c1
        c2 = getchar()
        if ord(c2) != 0x5b:
            return c1
        c3 = getchar()
        return chr(0x10 + ord(c3) - 65)
    def IsMoving(self):
        return self.dirx != 0 or self.diry != 0
    def GetMoveDir(self,keyspressed):
        #TODO AA
        if self.IsMoving() or self.inBeam or self.inDamage: 
            return 0, 0
        key = self.readkey()
        """
        isdown=keyboard.is_pressed(self.key_down)
        isup=keyboard.is_pressed(self.key_up)
        isleft=keyboard.is_pressed(self.key_left)
        isright=keyboard.is_pressed(self.key_right)
        """
        ifleft=(key==self.key_left)
        ifright=(key==self.key_right)
        ifup=(key==self.key_up)
        ifdown=(key==self.key_down)
        isvertical= isdown or isup
        ishorizontal= isright or isleft
        moveX=isdown-isup
        moveY=isright-isleft
        if isvertical and not ishorizontal:
            self.firstvertical=True
            self.firsthorizontal=False
        if ishorizontal and not isvertical:
            self.firsthorizontal=True
            self.firstvertical=False
        if (isvertical and ishorizontal):
            moveX*=self.firsthorizontal
            moveY*=self.firstvertical
        return moveX, moveY

    def Move(self):
        if self.dirx != 0: self.parts[0] -= 1
        else: self.parts[1] -= 1
        self.preMoveTime = float(time.perf_counter())
    def StartMove(self, dirx, diry):
        self.dirx = dirx
        self.diry = diry
    def IsEndMove(self):
        return self.parts[0] == 0 or self.parts[1] == 0
    def ChangeHP(self, x): self.HP += x
    def GetTimeGap(self, axis):
        return 1 / self.speed / (3 if axis == 0 else 6)
    def IsCanMove(self, axis):
        return float(time.perf_counter()) - self.preMoveTime >= self.GetTimeGap(axis)
    def InitParts(self):
        self.parts = [3, 6]
    def InitDir(self):
        self.dirx, self.diry = 0, 0
    def SetPos(self, posx, posy):
        self.posx, self.posy = posx, posy