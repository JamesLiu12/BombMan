from SelectUI import SelectUI
from numpy import *
from colorama import Fore, Back, Style
class GameEndUI:
    def __init__(self) -> None:
        self.quit = SelectUI
    # input winner

    def ShowEndPic(self,board,playerl,survivor):
        
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
        for s in survivor:
             if s == True:
                    survive.append(playerl[survivor.index(s)])
        print(Fore.RED+Back.WHITE+('congratulations'+ ', '.join(winner)+'win with highest score'))
        print(Fore.RED+Back.WHITE+('congratulations'+ ', '.join(survivor)+'survives from bomb rain'))
        print(Style.RESET_ALL)


          
      
    def OutGame(self,ranklist):
        #waiting for list type
        print('use q to quit game')
        quit = self.quit.getdir()
        while True:
        
              quit = self.quit.getdir()
        
# n= GameEndUI()
# n.endpic('Player2','Player2')
# n.OutRank([1,2,3,4])