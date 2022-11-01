from Player import Player
from Bot import Bot
class SettingUI:
    def __init__(self):
        file = open('Setting.cfg', 'r')
        self.mapSates = [0, 1, None]
        self.playersSates =  [True if 'True' in x else False for x in file.readline().split(' ')]
        self.mapIndex = int(file.readline())
    def GetPlayerSates(self):
        return [Player if self.playersSates[i] else None for i in range(2)] + [Bot if self.playersSates[i] else None for i in range(2, 4)]
    def GetmapSate(self):
        return self.mapSates[self.mapIndex]
    def ChangePlayerState(self, playerIndex):
        self.playersSates[playerIndex] ^= True
        self.WriteToFile()
    def ChangeMapNumber(self, mapnum):
        self.mapIndex=mapnum
        self.WriteToFile()
    def WriteToFile(self):
        file = open('Setting.cfg', 'w')
        file.write(' '.join(list(map(str, self.playersSates)))+'\n')
        file.write(str(self.mapIndex))