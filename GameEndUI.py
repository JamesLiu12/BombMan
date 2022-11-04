from SelectUI import SelectUI
from numpy import *
from colorama import Fore, Back, Style
import os
from Runner import Runner
import platform
class GameEndUI:
    def __init__(self) -> None:
        self.choice = SelectUI()
    # input winner

    def ShowEndPic(self,survivors,playerl):
        board=[]
        playersName = []
        survive = []
        for player in playerl:
            board.append(player.GetScore())
            playersName.append(player.GetName())
        for survivor in survivors:
            survive.append(survivor.GetName())
        print("""\033[1;37;40m       
              _____                      ______           _           ⠄⠄⠄⠄⠄⠄⢠⣿⣋⣿⣿⣉⣿⣿⣯⣧⡰⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
             / ____|                    |  ____|         | |          ⠄⠄⠄⠄⠄⠄⣿⣿⣹⣿⣿⣏⣿⣿⡗⣿⣿⠁⠄⠄⠄⠄⠄⠄⠄⠄⠄
            | |  __  __ _ _ __ ___   ___| |__   _ __   __| |          ⠄⠄⠄⠄⠄⠄⠟⡛⣉⣭⣭⣭⠌⠛⡻⢿⣿⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄       _________________________________
            | | |_ |/ _` | '_ ` _ \ / _ \  __| | '_ \ / _` |          ⠄⠄⠄⠄⠄⠄⠄⠄⣤⡌⣿⣷⣯⣭⣿⡆⣈⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄      /                                 \\
            | |__| | (_| | | | | | |  __/ |____| | | | (_| |          ⠄⠄⠄⠄⠄⠄⠄⢻⣿⣿⣿⣿⣿⣿⣿⣷⢛⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄      |    This world needs more....... |
             \_____|\__,_|_| |_| |_|\___|______|_| |_|\__,_|          ⠄⠄⠄⠄⠄⠄⠄⠄⢻⣷⣽⣿⣿⣿⢿⠃⣼⣧⣀⠄⠄⠄⠄⠄⠄⠄⠄      |                                 |
                                                                      ⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣛⣻⣿⠟⣀⡜⣻⢿⣿⣿⣶⣤⡀⠄⠄⠄⠄      |    Bombs!!!                     |
                                                                      ⠄⠄⠄⠄⠄⠄⠄⠄⢠⣤⣀⣨⣥⣾⢟⣧⣿⠸⣿⣿⣿⣿⣿⣤⡀⠄⠄      |                                 |
                                                                      ⠄⠄⠄⠄⠄⠄⠄⠄⢟⣫⣯⡻⣋⣵⣟⡼⣛⠴⣫⣭⣽⣿⣷⣭⡻⣦⡀      |   ______________________________/
                                                                      ⠄⠄⠄⠄⠄⠄⠄⢰⣿⣿⣿⢏⣽⣿⢋⣾⡟⢺⣿⣿⣿⣿⣿⣿⣷⢹⣷      / ／
                                                                      ⠄⠄⠄⠄⠄⠄⠄⣿⣿⣿⢣⣿⣿⣿⢸⣿⡇⣾⣿⠏⠉⣿⣿⣿⡇⣿⣿     /／
                                                                      ⠄⠄⠄⠄⠄⠄⠄⣿⣿⣿⢸⣿⣿⣿⠸⣿⡇⣿⣿⡆⣼⣿⣿⣿⡇⣿⣿
                                                                      ⠇⢀⠄⠄⠄⠄⠄⠘⣿⣿⡘⣿⣿⣷⢀⣿⣷⣿⣿⡿⠿⢿⣿⣿⡇⣩⣿
                                                                      ⣿⣿⠃⠄⠄⠄⠄⠄⠄⢻⣷⠙⠛⠋⣿⣿⣿⣿⣿⣷⣶⣿⣿⣿⡇⣿⣿                                                                                                                    
        \033[0m""")
        winner = []
        try:
            combine = [[playersName[i],board[i]] for i in range(len(playerl))]
            combine = array(combine)
            combine = combine[combine[:,-1].argsort()][::-1]
            combine = [[i[0],str(i[1])]for i in combine]
            print(Fore.RED+Back.WHITE + 'Final Score:')
            for i in combine: 
                print(Fore.RED+Back.WHITE+' '.join(i))
            maxscore = max(board)
            for play in combine:
                if int(play[1])==maxscore:
                    winner.append(play[0])
            winner.reverse()
        except:
            pass
        if len(winner) == 0:
            print('No winner!')
        else:
            print(Fore.RED+Back.WHITE+('Congratulations '+ ', '.join(winner)+' win with the highest score!'))
        if len(survive) == 0:
            print('No one survive!')
        else:
            print(Fore.RED+Back.WHITE+('Congratulations '+ ', '.join(survive)+' survives from the bomb rain!'))
        print(Style.RESET_ALL)


    def ShowMainSelect(self,choice,menul):
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
     
      
    def OutMenu(self, survivors, playerl):
        menul = ['Restart','Back to menu','Quit']
        print('\r')
        pointer = 0
        os.system('cls' if platform.system() == 'Windows' else 'clear')
        self.ShowEndPic(survivors, playerl)
        self.ShowMainSelect(pointer,menul)
        choose = self.choice.getdir()
        while choose!=3:  #choose 
            if pointer+choose<0:
                pointer = len(menul)-1
            elif pointer+choose>len(menul)-1:
                pointer = 0  
            else:
            
                pointer+=choose
            os.system('cls' if platform.system() == 'Windows' else 'clear')
            self.ShowEndPic(survivors, playerl)
            self.ShowMainSelect(pointer,menul)
            
            choose = self.choice.getdir()
        if pointer ==0:
            return True
        elif pointer == 1:
            return False
        elif pointer == 2:
            os._exit(0)
        
# n= GameEndUI()
# n.endpic('Player2','Player2')
# n.OutRank([1,2,3,4])