from pynput.keyboard import Key,Listener


class Control():
    def __init__(self):
        self.dir_ = None

    def getdir(self):
        self.dir_ = None    
        def on_press(key):
            if key == Key.up:self.dir_ = 1
            elif key == Key.down:self.dir_ = -1
            elif key == Key.left:self.dir_ = -1
            elif key == Key.right:self.dir_ = 1
            elif key == Key.enter: self.dir_ = 2
        
            return False
        listener = Listener(on_press=on_press) # 创建监听器
        listener.start()    
        listener.join()     
        listener.stop()     
        return self.dir_
# c=Control()
# print(c.getdir())
