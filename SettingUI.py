from Player import Player
from Bot import Bot
class SettingUI:
    def __init__(self):
        file = open('Setting.cfg', 'r')
        self.mapSates = [0, 1, None]
        self.playersSates =  [True if x == 'True' else False for x in file.readline().split(' ')]
        self.mapIndex = int(file.readline())
    def GetPlayerSates(self):
        return [Player if self.playersSates[i] else None for i in range(2)] + [Bot if self.playersSates[i] else None for i in range(2, 4)]
    def GetmapSate(self):
        if self.mapSates[self.mapIndex] == 'None': return None
        return int(self.mapSates[self.mapIndex])
    def ChangePlayerState(self, playerIndex):
        self.playersSates[playerIndex] ^= True
        self.WriteToFile()
    def ChangeMapNumber(self, dir):
        self.mapIndex -= dir
        if self.mapIndex == -1: self.mapIndex = len(self.mapSates) - 1
        elif self.mapIndex >= len(self.mapSates): self.mapIndex = 0
        self.WriteToFile()
    def WriteToFile(self):
        file = open('Setting.cfg', 'w')
        file.write(' '.join(list(map(str, self.playersSates))))
        file.write(self.mapIndex)