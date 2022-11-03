# new control
import platform
import msvcrt

if platform.system() == 'Windows':     
    from pynput.keyboard import Key,Listener

    from pynput import keyboard
    class SelectUI():
        def __init__(self):
            self.dir_ = None   
        def getdir(self):
            while True:
                key = msvcrt.getwch()
                if key=='w': return -1
                elif key == 's': return 1
                elif key == 'a': return -1
                elif key == 'd': return 1
                elif key == 'q': return 2
                elif key == 'e': return 3
            
            
else:
    import tty
    import termios
    import sys
    class SelectUI():
        
        def __init__(self):
            tty.setcbreak(sys.stdin)
        def getdir(self):
            while True:
                orig_settings = termios.tcgetattr(sys.stdin)
                tty.setcbreak(sys.stdin)
                key = sys.stdin.read(1)[0]
                termios.tcsetattr(sys.stdin, termios.TCSADRAIN, orig_settings)
                if key== 'w':return -1
                elif key== 'a':
                    return -1
                elif key== 's':
                    return 1
                elif key== 'd':
                    return 1
                elif key=='q':
                    return 2
                elif key=='e':
                    return 3

# c = UI()
# for x in range(3):
#     print(c.getdir(),flush=True)
# c=UI()

# print(c.getdir())
