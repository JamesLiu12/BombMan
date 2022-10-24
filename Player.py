import keyboard
import time
class Player:
    def __init__(self, key_up, key_down, key_left, key_right, id, posx, posy, HP = 3, speed = 1):
        self.HP = HP
        self.speed = speed
        self.key_up = key_up
        self.key_down = key_down
        self.key_left = key_left
        self.key_right = key_right
        self.id = id
        self.posx = posx
        self.posy = posy
        self.dirx = 0
        self.diry = 0
        self.atk = 1
        self.inBeam = False
        self.inDamage = False
        self.isBlockPlayer = True
        self.isBlockBeam = False
        self.preMoveTime = 0
        self.parts = (3, 6)
        self.priority = 2
        # self.grids
    def IsMoving(self):
        return self.dirx != 0 or self.diry != 0
    def GetMoveDir(self):
        #TODO AA
        if self.inMove or self.inBeam or self.inDamage: return 0, 0
        if keyboard.is_pressed(self.key_up) and not keyboard.is_pressed(self.key_down):
            return -1, 0
        elif keyboard.is_pressed(self.key_down) and not keyboard.is_pressed(self.key_up):
            return 1, 0
    def Move(self):
        self.parts += (self.dirx, self.diry)
    def StartMove(self, dirx, diry):
        self.dirx = dirx
        self.diry = diry
    def IsEndMove(self):
        return self.dirx == 0 or self.diry == 0
    def ChangeHP(self, x): self.HP += x
    def GetTimeGap(self, axis):
        return 1 / self.speed / (3 if axis == 0 else 6)
    def IsCanMove(self, axis):
        return time.perf_counter() - self.preMoveTime >= self.GetTimeGap(axis)
    def InitPart(self):
        self.dirx, self.diry = 3, 6