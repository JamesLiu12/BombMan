from UI import UI
class GameEndUI(UI):
    def __init__(self) -> None:
        GameEndUI.quit = UI()
    # input winner

    def endpic(self,winner,surviver):
        print("""\033[1;37;40m       
                _..._       .-'''-.                                                                                               .-'''-.                           
            .-'_..._''.   '   _    \                                                              .---.                         '   _    \                         
        .' .'      '.\/   /` '.   \    _..._                                                    |   |                  .--. /   /` '.   \    _..._               
        / .'          .   |     \  '  .'     '.   .--./)                                         |   |                  |__|.   |     \  '  .'     '.             
        . '            |   '      |  '.   .-.   . /.''\\                            .|            |   |              .|  .--.|   '      |  '.   .-.   .            
        | |            \    \     / / |  '   '  || |  | |                 __      .' |_           |   |    __      .' |_ |  |\    \     / / |  '   '  |            
        | |             `.   ` ..' /  |  |   |  | \`-' /      _    _   .:--.'.  .'     |   _    _ |   | .:--.'.  .'     ||  | `.   ` ..' /  |  |   |  |       _    
        . '                '-...-'`   |  |   |  | /("'`      | '  / | / |   \ |'--.  .-'  | '  / ||   |/ |   \ |'--.  .-'|  |    '-...-'`   |  |   |  |     .' |   
        \ '.          .              |  |   |  | \ '---.   .' | .' | `" __ | |   |  |   .' | .' ||   |`" __ | |   |  |  |  |               |  |   |  |    .   | / 
        '. `._____.-'/              |  |   |  |  /'""'.\  /  | /  |  .'.''| |   |  |   /  | /  ||   | .'.''| |   |  |  |__|               |  |   |  |  .'.'| |// 
            `-.______ /               |  |   |  | ||     |||   `'.  | / /   | |_  |  '.'|   `'.  |'---'/ /   | |_  |  '.'                   |  |   |  |.'.'.-'  /  
                    `                |  |   |  | \'. __// '   .'|  '/\ \._,\ '/  |   / '   .'|  '/    \ \._,\ '/  |   /                    |  |   |  |.'   \_.'   
                                    '--'   '--'  `'---'   `-'  `--'  `--'  `"   `'-'   `-'  `--'      `--'  `"   `'-'                     '--'   '--'            
        \033[0m""")
        if winner == surviver:

           print(winner,end=' ')
           print("\033[5;31;40msurvives and wins the game, a living legend!!!'\033[0m")
        else:
            print(winner,'wins the game with highest rank!!!')
            print(surviver,'live to the last!!!')
    def outrank(self,ranklist):
        #waiting for list type
        print('use key ENTER to quit game'')
        quit = GameEndUI.quit.UI()
        while quit!=2:
              print('use key ENTER to quit game'')
              quit = GameEndUI.quit.UI()
        #quit function
              
#     endpic('player2','player2')
