from Player import Player
from Bot import Bot
from SelectUI import SelectUI
import os
from colorama import Fore, Back, Style
import math
class SettingUI:
    def __init__(self):
        file = open('Setting.cfg', 'r')
        self.mapSates = [0, 1, None]
        self.playersStates =  [True if 'True' in x else False for x in file.readline().split(' ')]
        self.mapIndex = int(file.readline())
        self.FPS=int(file.readline())
        self.difficulty=int(file.readline())
        if self.difficulty==3:
            self.difficulty=2
        self.platform=0
        self.CheatMode=False
    def GetPlayerStates(self):
        return [Player if self.playersStates[i] else None for i in range(2)] + [Bot if self.playersStates[i] else None for i in range(2, 4)]
    def GetmapState(self):
        return self.mapSates[self.mapIndex]
    def ChangePlayerState(self, playerIndex):
        self.playersStates[playerIndex] ^= True
        self.WriteToFile()
    def ChangeMapNumber(self, mapnum):
        self.mapIndex=mapnum
        self.WriteToFile()
    def ChangeDifficulty(self):
        self.difficulty+=1
        if self.difficulty==3 and self.CheatMode==False:
            self.difficulty=0
        if self.difficulty==4:
            self.difficulty=0
        self.WriteToFile()
    def CheatModeOn(self):
        self.CheatMode=True
    def WriteToFile(self):
        file = open('Setting.cfg', 'w')
        file.write(' '.join(list(map(str, self.playersStates)))+'\n')
        file.write(str(self.mapIndex)+'\n')
        file.write(str(self.FPS)+'\n')
        file.write(str(self.difficulty))
    def change_rate(rate):
        newr = int(input('enter prefered frame rate'))
        return newr
    def changeFPS(self):
        self.FPS+=10
        if self.FPS>100:
            self.FPS=20
        self.WriteToFile()
    def ShowSetting(self,choce,menul):
        os.system ('cls')
        
        for i in range(len(menul)):
           
            if i != choce:
            
                print(Fore.RED+Back.WHITE+str(menul[i]),end='')
                print()
            else:

                print(Fore.RED+Back.LIGHTGREEN_EX+str(menul[i]), end = '')
                print()
        print(Style.RESET_ALL)
    def choosing_map(self):
      
        mapl = self.mapSates
        mapchoice = mapl
        print('\r')
        print('\033[1;47;31muse direction key to control,w and d means go right setting, s and a means go left setting,use e to choose \033[0m')
        
        self.ShowSetting(self.mapIndex,mapchoice)
        choose = SelectUI.getdir(self)
        while choose!=3 and choose!=2:  #choose 
            if self.mapIndex+choose<0:
                self.mapIndex = len(mapl)-1
            elif self.mapIndex+choose>len(mapl)-1:
                self.mapIndex = 0  
            else:
             
                self.mapIndex+=choose
            self.ShowSetting(self.mapIndex)
            
            choose = SelectUI.getdir(self)
        if choose == 3:
            if  self.mapIndex !=2:
                pass
            else:
               self.WriteToFile()
               return False
        elif choose == 2:
            self.Setting()
    def PlayerSet(self):
        playerstate = self.GetPlayerStates()
        pass
    def Setting(self):#need mapl input[], frame rate input
        menul = ['choosing map','change frame rate','player-bot setting','exit']    
        print('\r')
        print('\033[1;47;31muse direction key to control,w and d means go right setting, s and a means go left setting,use e to choose \033[0m')
        pointer = 0
        self.ShowSetting(pointer,menul)
        choose = SelectUI.getdir(self)
        while choose!=3:  
            if pointer+choose<0:       
                pointer = len(menul)-1
            elif pointer+choose>=len(menul):
                pointer = 0  
            else:
             
                pointer+=choose
            self.ShowSetting(pointer,menul)
            
            choose = SelectUI.getdir(self)
        if pointer ==0:
            self.choosing_map()   #choose map
            
        elif pointer == 1:
            self.change_rate()            # change Hz
        elif pointer == 2:
            self.PlayerSet()  
        elif pointer == 3:
            return False  #return to menu
