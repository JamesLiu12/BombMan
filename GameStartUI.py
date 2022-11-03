import sys
import time
from SelectUI import *
from Runner import Runner
import os
from colorama import Fore, Back, Style
import math
from SettingUI import SettingUI
import platform
from GameEndUI import GameEndUI
class GameStartUI():
    def __init__(self):
        
        GameStartUI.choice = SelectUI()
        self.backColor = Back.BLACK
        self.settingUI = SettingUI()
        # startUI.run = Runner(30)
    def title(self):
        print("""\033[1;40;31m       
                    .-'''-.                                                   
                   '   _    \                                                                
        /|       /   /` '.   \  __  __   ___   /|                   __  __   ___                _..._    
        ||      .   |     \  ' |  |/  `.'   `. ||                  |  |/  `.'   `.            .'     '.  
        ||      |   '      |  '|   .-.  .-.   '||                  |   .-.  .-.   '          .   .-.   . 
        ||  __  \    \     / / |  |  |  |  |  |||  __              |  |  |  |  |  |    __    |  '   '  | 
        ||/'__ '.`.   ` ..' /  |  |  |  |  |  |||/'__ '.           |  |  |  |  |  | .:--.'.  |  |   |  | 
        |:/`  '. '  '-...-'`   |  |  |  |  |  ||:/`  '. '          |  |  |  |  |  |/ |   \ | |  |   |  | 
        ||     | |             |  |  |  |  |  |||     | |          |  |  |  |  |  |`" __ | | |  |   |  | 
        ||\    / '             |__|  |__|  |__|||\    / '          |__|  |__|  |__| .'.''| | |  |   |  | 
        |/\'..' /                              |/\'..' /                           / /   | |_|  |   |  | 
        '  `'-'`                               '  `'-'`                            \ \._,\ '/|  |   |  | 
                                                                                    `--'  `" '--'   '--' 
        \033[0m""")
        print()
    def progress_bar(self):

        for i in range(1, 101):

            print("\r", end="")

            print("loading progress: {}%: ".format(i), "" * (i // 2), end="")

            sys.stdout.flush()
            if i < 90:
              time.sleep(0.05*math.ln(i))
            else:time.sleep(0.05)

    def ShowSelect(self,choice,menul):
        os.system ('cls' if platform.system() == 'Windows' else 'clear')
        self.title()
        
        for i in range(len(menul)):
            if i != choice:
            
                print(Fore.RED+Back.BLACK+menul[i],end='')
                print()
            else:

                print(Fore.RED+Back.WHITE+menul[i], end = '')
                print()
        print(Style.RESET_ALL)

        

    def ShowMainSelect(self,choice,menul):
        os.system ('cls' if platform.system() == 'Windows' else 'clear')
        self.title()
        print('\033[1;47;31muse direction key to control,w and d means go right menu, s and a means go left menu,use e to choose \033[0m')
        print()
        for i in range(len(menul)):
            if i != choice:
            
                print(Fore.RED+Back.BLACK+menul[i],end='')
                print()
            else:

                print(Fore.RED+Back.WHITE+menul[i], end = '')
                print()
        print(Style.RESET_ALL)

    def ShowSettingSelect(self,choice,menul):
        os.system ('cls' if platform.system() == 'Windows' else 'clear')
        self.title()
        print('\033[1;47;31muse direction key to control,w and d means go right menu, s and a means go left menu,use e to choose \033[0m')
        print()
        for i in range(len(menul)):
            if i != 2:
                if i != choice:
                
                    print(Fore.RED+Back.BLACK+menul[i],end='')
                    print()
                else:

                    print(Fore.RED+Back.WHITE+menul[i], end = '')
                    print()
            else:
                if i != choice:
                
                    print(Fore.RED+Back.BLACK+menul[i],str(self.settingUI.FPS),end='')
                    print()
                else:

                    print(Fore.RED+menul[i],Fore.RED+Back.WHITE+str(self.settingUI.FPS), end = '')
                    print()
        print(Style.RESET_ALL)

    def ShowPlayerSelect(self,choice,menul):
        os.system ('cls' if platform.system() == 'Windows' else 'clear')
        self.title()
        print('\033[1;47;31muse direction key to control,w and d means go right menu, s and a means go left menu,use e to choose \033[0m')
        print()
        for i in range(len(menul)):
            if i < len(menul)-1:
                if i != choice:
                
                    print(Fore.RED+Back.BLACK+menul[i],str(self.settingUI.playersStates[i]),end='')
                    print()
                else:

                    print(Fore.RED+menul[i],Fore.RED+Back.WHITE+str(self.settingUI.playersStates[i]),end = '')
                    print()
            else:
                if i != choice:
                
                    print(Fore.RED+Back.BLACK+menul[i],end='')
                    print()
                else:

                    print(Fore.RED+Back.WHITE+menul[i],end = '')
                    print()
        print(Style.RESET_ALL)

    def ShowMenu(self):
        menul = ['Start','Setting','Quit']
        print('\r')
        pointer = 0
        while True:
            self.ShowMainSelect(pointer,menul)
            choose = self.choice.getdir()
            while choose!=3:  #choose 
                if pointer+choose<0:
                    pointer = len(menul)-1
                elif pointer+choose>len(menul)-1:
                    pointer = 0  
                else:
                
                    pointer+=choose
                self.ShowMainSelect(pointer,menul)
                
                choose = self.choice.getdir()
            if pointer ==0:
                while True:
                    runner = Runner(self.settingUI.FPS, *self.settingUI.GetPlayerStates(), self.settingUI.GetmapState())
                    runner.Run()
                    gameEndUI = GameEndUI()
                    if not gameEndUI.OutMenu(runner.GetSurvivers(), runner.GetPlayers()):
                        break
            elif pointer == 1:
                self.ShowSettings(0)
                #add setting menu!!!!!!!!
            elif pointer == 2:
                os._exit(0)

    def ShowSettings(self,pointer):
        menul = ['Player Setting','Map Setting','FPS','Back']
        print('\r')
        pointer = pointer
        self.ShowSettingSelect(pointer,menul)
        choose = self.choice.getdir()
        while choose!=3:  #choose 
            if pointer+choose<0:
                pointer = len(menul)-1
            elif pointer+choose>len(menul)-1:
                pointer = 0  
            else:
            
                pointer+=choose
             
              
            self.ShowSettingSelect(pointer,menul)
            
            choose = self.choice.getdir()
        if pointer ==0:
            self.PlayerSetting(0)
        elif pointer == 1:
            self.MapSettings()
        elif pointer == 2:
            self.settingUI.changeFPS()
            self.ShowSettingSelect(pointer,menul)
            self.ShowSettings(pointer)
        elif pointer == 3:
            pass

    def PlayerSetting(self,pointer):
        menul = ['Player1','Player2','Computer1','Computer2','Back']
        print('\r')
        pointer = pointer
        self.ShowPlayerSelect(pointer,menul)
        choose = self.choice.getdir()
        while choose!=3:  #choose 
            if pointer+choose<0:
                pointer = len(menul)-1
            elif pointer+choose>len(menul)-1:
                pointer = 0  
            else:
            
                pointer+=choose
             
              
            self.ShowPlayerSelect(pointer,menul)
            
            choose = self.choice.getdir()
        if pointer ==0:
            self.settingUI.ChangePlayerState(pointer)
            self.ShowPlayerSelect(pointer,menul)
            self.PlayerSetting(pointer)
        elif pointer == 1:
            self.settingUI.ChangePlayerState(pointer)
            self.ShowPlayerSelect(pointer,menul)
            self.PlayerSetting(pointer)
        elif pointer == 2:
            self.settingUI.ChangePlayerState(pointer)
            self.ShowPlayerSelect(pointer,menul)
            self.PlayerSetting(pointer)
        elif pointer == 3:
            self.settingUI.ChangePlayerState(pointer)
            self.ShowPlayerSelect(pointer,menul)
            self.PlayerSetting(pointer)
        elif pointer == 4:
            self.ShowSettings(0)
    def MapSettings(self):
        menul = ['Map 1','Map 2','Custom','Back']
        print('\r')
        pointer = 0
        self.ShowMainSelect(pointer,menul)
        choose = self.choice.getdir()
        while choose!=3:  #choose 
            if pointer+choose<0:
                pointer = len(menul)-1
            elif pointer+choose>len(menul)-1:
                pointer = 0  
            else:
                pointer+=choose
             
            self.ShowMainSelect(pointer,menul)
            choose = self.choice.getdir()
        if pointer ==0:
            self.settingUI.ChangeMapNumber(0)
            self.ShowSettings(0)
        elif pointer == 1:
            self.settingUI.ChangeMapNumber(1)
            self.ShowSettings(0)
        elif pointer == 2:
            self.settingUI.ChangeMapNumber(2)
            self.ShowSettings(0)
        elif pointer == 3:
            self.ShowSettings(0)
        
        
n = GameStartUI()
# n.progress_bar()
n.title()
# print(p)                    
