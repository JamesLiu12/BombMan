from Player import Player
from Bot import Bot
class SettingUI:
    def __init__(self):
        self.playerSates = [True, False, False, False]
    def GetPlayerSates(self):
        return [Player if self.playerSates[i] else None for i in range(2)] + [Bot if self.playerSates[i] else None for i in range(2, 4)]