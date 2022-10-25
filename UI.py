# new control
import tty
import termios
import sys
class UI():
    def __init__(self):
        pass
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
    def getdir(self):
       
            key = self.readkey()
            if key=='w':return 1
            if key=='a':
                return -1
            if key=='s':
                return -1
            if key=='d':
                return 1
            if key=='q':
                return 2
            if key=='e':
                return 3
