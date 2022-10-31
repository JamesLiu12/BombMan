# new control
import platform
if platform.system() == 'Windows':     
    from pynput.keyboard import Key,Listener

    from pynput import keyboard
    class UI():
        def __init__(self):
            self.dir_ = None   
        def getdir(self):
            
            def on_press(Key):
                if Key.char=='w':self.dir_ = 1
                elif Key.char=='s':self.dir_ = -1
                elif Key.char=='a':self.dir_ = -1
                elif Key.char=='d':self.dir_ = 1
                elif Key.char=='q': self.dir_ = 2
                elif Key.char == 'e':self.dir_ = 3
                else:
                    print('fuck you')
            
                return False
            with keyboard.Listener(on_press=on_press) as listener:
                    listener.join()  

            return self.dir_
       
    # c=Control()
    # while True:   
    # print(c.getdir())
            
            
else:
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
                if key== 'w':return -1
                if key== 'a':
                    return -1
                if key== 's':
                    return 1
                if key== 'd':
                    return 1
                if key=='q':
                    return 2
                if key=='e':
                    return 3

# c = UI()
# for x in range(3):
#     print(c.getdir(),flush=True)
# c=UI()

# print(c.getdir())
