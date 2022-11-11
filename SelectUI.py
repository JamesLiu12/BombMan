# new control
import platform

if platform.system() == 'Windows':     
    import msvcrt
    from pynput.keyboard import Key,Listener

    from pynput import keyboard
    class SelectUI():
        def __init__(self):
            self.dir_ = None   
            self.Cheatstep=0
            self.CheatOn=False
        def getdir(self):
            while True:
                key = msvcrt.getwch()
                """
                print(ord(key))
                print(type(key))
                if(ord(key)==80):print('down')
                if(ord(key)==72):print('up')
                if(ord(key)==75):print('left')
                if(ord(key)==77):print('right')"""
                if not self.CheatOn:
                    if self.Cheatstep==0 and ord(key)==72:
                        self.Cheatstep+=1
                    if self.Cheatstep==1 and ord(key)==72:
                        self.Cheatstep+=1
                    if self.Cheatstep==2 and ord(key)==80:
                        self.Cheatstep+=1
                    if self.Cheatstep==3 and ord(key)==80:
                        self.Cheatstep+=1
                    if self.Cheatstep==4 and ord(key)==75:
                        self.Cheatstep+=1
                    if self.Cheatstep==5 and ord(key)==77:
                        self.Cheatstep+=1
                    if self.Cheatstep==6 and ord(key)==75:
                        self.Cheatstep+=1
                    if self.Cheatstep==7 and ord(key)==77:
                        self.Cheatstep+=1
                    if self.Cheatstep==8 and (key=='b' or key=='B'):
                        self.Cheatstep+=1
                    if self.Cheatstep==9 and (key=='a' or key=='A'):
                        print('CheatModeOn!')
                        self.CheatOn=True
                        return 114514
                if key=='w': self.Cheatstep=0;return -1
                elif key == 's': self.Cheatstep=0;return 1
                elif key == 'a': self.Cheatstep=0;return -1
                elif key == 'd': self.Cheatstep=0;return 1
                elif key == 'q': self.Cheatstep=0;return 2
                elif key == 'e': self.Cheatstep=0;return 3
            
            
else:
    import tty
    import termios
    import sys
    class SelectUI():
        
        def __init__(self):
            tty.setcbreak(sys.stdin)
            self.Cheatstep=0
            self.CheatOn=False
        def getdir(self):
            while True:
                orig_settings = termios.tcgetattr(sys.stdin)
                tty.setcbreak(sys.stdin)
                key = sys.stdin.read(1)[0]
                termios.tcsetattr(sys.stdin, termios.TCSADRAIN, orig_settings)
                """
                print(ord(key))
                print(type(key))
                if(ord(key)==66):print('down')
                if(ord(key)==65):print('up')
                if(ord(key)==68):print('left')
                if(ord(key)==67):print('right')"""
                if not self.CheatOn:
                    if self.Cheatstep==0 and ord(key)==65:
                        self.Cheatstep+=1
                    if self.Cheatstep==1 and ord(key)==65:
                        self.Cheatstep+=1
                    if self.Cheatstep==2 and ord(key)==66:
                        self.Cheatstep+=1
                    if self.Cheatstep==3 and ord(key)==66:
                        self.Cheatstep+=1
                    if self.Cheatstep==4 and ord(key)==68:
                        self.Cheatstep+=1
                    if self.Cheatstep==5 and ord(key)==68:
                        self.Cheatstep+=1
                    if self.Cheatstep==6 and ord(key)==67:
                        self.Cheatstep+=1
                    if self.Cheatstep==7 and ord(key)==67:
                        self.Cheatstep+=1
                    if self.Cheatstep==8 and (key=='b' or key=='B'):
                        self.Cheatstep+=1
                    if self.Cheatstep==9 and (key=='a' or key=='A'):
                        print('CheatModeOn!')
                        self.CheatOn=True
                        return 114514
                if key== 'w':self.Cheatstep=0;return -1
                elif key== 'a':
                    self.Cheatstep=0
                    return -1
                elif key== 's':
                    self.Cheatstep=0;
                    return 1
                elif key== 'd':
                    self.Cheatstep=0;
                    return 1
                elif key=='q':
                    self.Cheatstep=0;
                    return 2
                elif key=='e':
                    self.Cheatstep=0;
                    return 3

# c = UI()
# for x in range(3):
#     print(c.getdir(),flush=True)
# c=UI()

# print(c.getdir())
