import sys
import time
from SelectUI import *
from Runner import Runner
import os
from colorama import Fore, Back, Style
import math
from SettingUI import SettingUI
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

            print("loading progress: {}%: ".format(i), "▋" * (i // 2), end="")

            sys.stdout.flush()
            if i < 90:
              time.sleep(0.05*math.ln(i))
            else:time.sleep(0.05)
    def ShowSelect(self,choice,menul):
        os.system ('cls')
        self.title()
        
        for i in range(len(menul)):
            if i != choice:
            
                print(Fore.RED+Back.BLACK+menul[i],end='')
                print()
            else:

                print(Fore.RED+Back.WHITE+menul[i], end = '')
                print()
        print(Style.RESET_ALL)

        

    def ShowMenu(self):
        menul = ['Start','Setting','Quit']
        print('\r')
        print('\033[1;47;31muse direction key to control,w and d means go right menu, s and a means go left menu,use e to choose \033[0m')
        pointer = 0
        self.ShowSelect(pointer,menul)
        choose = self.choice.getdir()
        while choose!=3:  #choose 
            if pointer+choose<0:
                pointer = len(menul)-1
            elif pointer+choose>len(menul)-1:
                pointer = 0  
            else:
            
                pointer+=choose
             
              
            self.ShowSelect(pointer,menul)
            
            choose = self.choice.getdir()
        if pointer ==0:
            runner = Runner(40, *self.settingUI.GetPlayerSates(), self.settingUI.GetmapSate())
            runner.Run()
        elif pointer == 1:
            pass         #add setting menu!!!!!!!!
        elif pointer == 2:
            os._exit(0)

        
# n = GameStartUI()
# n.progress_bar()
# n.menu()
# print(p)                    
