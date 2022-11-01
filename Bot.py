from Player import Player
class Bot(Player):
    def __init__(self, maze, id, posx, posy, HP=3, speed=4, bombDelay=2):
        super().__init__(maze, None, None, None, None, None, id, posx, posy, HP, speed, bombDelay)
        self.origGrids=[[None,'\\','~','/',None,None],['┌','□','_','□','┘',')'],[None,'/',None,'⁊',None,None]]
    def IsBelongTo(self, typ):
        return typ == Bot or super().IsBelongTo(typ)
    def GetName(self):
        return 'Bot ' + str(self.id)