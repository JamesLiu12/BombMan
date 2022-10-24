import sys
import time
from UI import UI
from Runner import Runner

class startUI():
    def __init__(press):
        startUI.choice = UI()
        startUI.run = Runner(30)
    def title(self):
        print("""\033[1;47;31m       
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



    def progress_bar(self):

        for i in range(1, 101):

            print("\r", end="")

            print("Download progress: {}%: ".format(i), "▋" * (i // 2), end="")

            sys.stdout.flush()

            time.sleep(0.05)

    def menu(self):
        menul = ['Start','Setting','Quit']
      
        print('\r')
        print('\033[1;47;31muse direction key to control,↑ and --> means go right menu, ↓ and <-- means go left menu \033[0m')
        pointer = 0
        menul.insert(pointer,'*')
        
        print('\r',' '.join(menul),end="",flush=True)

        choose = startUI().choice.getdir()
        while choose!=2:
            if pointer == 0 and choose == -1:
                pointer = 2
            elif pointer ==2 and choose == 1:
                pointer = 0   
            else:
             
                pointer+=choose
            menul.remove('*')
            menul.insert(pointer,'*')
            print('\r',' '.join(menul),end="",flush=True)
            choose = startUI().choice.getdir()
        if pointer ==0:
           startUI.run.Run()
        elif pointer == 1:
            pass         #add setting menu!!!!!!!!
        elif pointer == 2:
            pass         #add quit function !!!!!!!

        
# n = startUI()

# p=n.menu()
# print(p)
