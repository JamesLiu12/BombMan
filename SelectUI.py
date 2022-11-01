# new control
import platform
if platform.system() == 'Windows':     
    from pynput.keyboard import Key,Listener

    from pynput import keyboard
    class SelectUI():
        def __init__(self):
            self.dir_ = None   
        def getdir(self):
            
            def on_press(Key):
                try:
                    if Key.char=='w':self.dir_ = -1
                    elif Key.char=='s':self.dir_ = 1
                    elif Key.char=='a':self.dir_ = -1
                    elif Key.char=='d':self.dir_ = 1
                    elif Key.char=='q': self.dir_ = 2
                    elif Key.char == 'e':self.dir_ = 3
                except:
                    pass
            
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
    class SelectUI():
        
        def __init__(self):
            tty.setcbreak(sys.stdin)
        def getdir(self):
            orig_settings = termios.tcgetattr(sys.stdin)
            tty.setcbreak(sys.stdin)
            key = sys.stdin.read(1)[0]
            termios.tcsetattr(sys.stdin, termios.TCSADRAIN, orig_settings)
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
