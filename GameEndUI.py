from SelectUI import SelectUI
from numpy import *
from GameStartUI import GameStartUI
from colorama import Fore, Back, Style
import os
from Runner import Runner
class GameEndUI:
    def __init__(self) -> None:
        self.quit = SelectUI
    # input winner

    def ShowEndPic(self,survivors,playerl):
        board=[]
        playersName = []
        survive = []
        for player in playerl:
            board.append(player.GetScore())
            playersName.append(player.GetName())
        for survivor in survivors:
            survive.append(player.GetName())
        print("""\033[1;37;40m       
              _____                      ______           _ 
             / ____|                    |  ____|         | |
            | |  __  __ _ _ __ ___   ___| |__   _ __   __| |
            | | |_ |/ _` | '_ ` _ \ / _ \  __| | '_ \ / _` |
            | |__| | (_| | | | | | |  __/ |____| | | | (_| |
             \_____|\__,_|_| |_| |_|\___|______|_| |_|\__,_|
                                                                                                                                                                                          
        \033[0m""")
        combine = [[playerl[i],board[i]] for i in range(len(playerl))]
        combine = array(combine)
        combine = combine[combine[:,-1].argsort()][::-1]
        combine = [[i[0],str(i[1])]for i in combine]
        for i in combine: 
           print(Fore.RED+Back.WHITE+' '.join(i))
        maxscore = max(board)
        winner = []
        survive = []
        for play in combine:
            if play[1]==maxscore:
                winner.append(play[0])
        for s in survivors:
             if s == True:
                    survive.append(playerl[survivors.index(s)])
        print(Fore.RED+Back.WHITE+('congratulations'+ ', '.join(winner)+'win with highest score'))
        print(Fore.RED+Back.WHITE+('congratulations'+ ', '.join(survivors)+'survives from bomb rain'))
        print(Style.RESET_ALL)


    def ShowMainSelect(self,choice,menul):
        os.system ('cls')
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
     
      
    def OutMenu(self):
        menul = ['Restart','Back to menu','Quit']
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
            runner = Runner(self.settingUI.FPS, *self.settingUI.GetPlayerStates(), self.settingUI.GetmapState())
            runner.Run()
        elif pointer == 1:
            newmenu = GameStartUI()
            newmenu.menu()
        elif pointer == 2:
            os._exit(0)
        
# n= GameEndUI()
# n.endpic('Player2','Player2')
# n.OutRank([1,2,3,4])