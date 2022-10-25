from UI import *
class GameEndUI():
    def __init__(self) -> None:
        GameEndUI.quit = UI()
    # input winner

    def endpic(self,winner,surviver):
        print("""\033[1;37;40m       
          _____                            _         _       _   _                 
         / ____|                          | |       | |     | | (_)                
        | |     ___  _ __   __ _ _ __ __ _| |_ _   _| | __ _| |_ _  ___  _ __  ___ 
        | |    / _ \| '_ \ / _` | '__/ _` | __| | | | |/ _` | __| |/ _ \| '_ \/ __|
        | |___| (_) | | | | (_| | | | (_| | |_| |_| | | (_| | |_| | (_) | | | \__ /
        \_____\___/|_| |_|\__, |_|  \__,_|\__|\__,_|_|\__,_|\__|_|\___/|_| |_|___/
                            __/ |                                                  
                            |___/                                                                                                                                               
        \033[0m""")
        if winner == surviver:

           print(winner,end=' ')
           print("\033[5;31;40msurvives and wins the game, a living legend!!!'\033[0m")
        else:
            print(winner,'wins the game with highest rank!!!')
            print(surviver,'live to the last!!!')
    def outrank(self,ranklist):
        #waiting for list type
        print('use key ENTER to quit game')
        quit = GameEndUI.quit.getdir()
        while quit!=2:
              print('use key ENTER to quit game')
              quit = GameEndUI.quit.getdir()
        
n= GameEndUI()
# n.endpic('Player2','Player2')
n.outrank([1,2,3,4])
