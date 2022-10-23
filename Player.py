from MoveObject import MoveObject
import keyboard

class Player(MoveObject):
    def __init__(self, key_up, key_down, key_left, key_right, id, posx, posy, HP = 3, speed = 1):
        super().__init__(HP, speed)
        self.key_up = key_up
        self.key_down = key_down
        self.key_left = key_left
        self.key_right = key_right
        self.id = id
        self.posx = posx
        self.posy = posy
        self.dirx = 0
        self.diry = 0
        self.inMove = False
        self.inLaser = False
        self.blockPlayer = True
        # self.grids
    
    def GetMove(self):
        #TODO
        if self.inMove or self.inLaser: return 0, 0
        if keyboard.is_pressed(self.key_up):
            self.inMove = True
            return -1, 0
    def ChangeHP(self, x): self.HP += x
    def StartMove(self, dirx, diry):
        self.inMove = True
        self.dirx = dirx
        self.diry = diry