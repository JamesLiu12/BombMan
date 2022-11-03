import sys
import time
from SelectUI import *
from Runner import Runner
import os
from colorama import Fore, Back, Style
import math
from SettingUI import SettingUI
import platform
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
        
        print("""\033[1;40;31m 
                ..  ...  ...  ...  ...  ...  ...  ...  ...  ~~;;z1uuua;..  ...  ...  ...  ...  ...  ...  ...  ...  .
                ..   ..   ..   ..   ..   ..   .. znnnniiiiii111uuuz++vaaz^+++~   ..   ..   ..   ..   ..   ..   .. 
                ..  ...  ...  ...  ...  ...  .!!uvnnnnoi~;***^11uuuuaaaaaaaaaaaaaaz6+...  ...  ...  ...  ...  ...  .
                ..   ..   ..   ..   ..  u3!!vnvnnnoi~~!n^^^++uuuuaaaaaaaaaaaaaaazaaz1a..   ..   ..   ..   ..   .. 
                ..   ..   ..   ..   .66333!1nnnnno!;***^^^i111uuuaaaaaaaaaaaaaaaaaaaaaz%n  ..   ..   ..   ..   .. 
                ..  ...  ...  ...  ..886333!!!inon!iu**^^^++1111uuuuaaaaaaaaaaaaaaazzzzzzzz%n+ ...  ...  ...  ...  .
                ..   ..   ..   .zv886333!!!!!!!iiiiiiiiii!6663368%%%83!!!!iuaaaazzzzzzzzzaa1z3  ..   ..   ..   .. 
                ..  ...  ...  ..n888886333!!!!!!iiiii666%88%%%%%%%%%$%%%%%8%%8638!iuazzzzzzvo;~nn*  ...  ...  ...  .
                ..   ..   .. 88888883333!!!!ii388$8%%%$%$633333333333!i1111111!866381zzzzn;;^iznna   ..   ..   .. 
                ..   ..   .8888888883333!i!68%8%$$$863333333333333333333!!i111111116336uzv;;;1vnn^   ..   ..   .. 
                ..  ...  ...8888888888633388$%$$$6666633333333333333333333!i1111111i6611836!^u*vuno^     ...  ...  .
                ..   .. -888888888888888%$$$38%66666333333333333!!!!i%$v^***********^o%333n++*1noooo  .   ..   .. 
                ..  ...  z8888888888886%$$$%%%%%%%%8886633333i!!8u;;;;;;;;;;;;;;;;*******^^6!-^-;unoo  . ...  ...  .
                ..   .~8888888888668$$$%%%%%%%%%%888888i66v;;;;;;;;;;;;;;*;;;;;;;;**^....^-i-a-vzoo+   .  ..   .. 
                ..   .8888888888668$$$%%%%%%%%%%%%8!66v;;~;;;;;;;;;;;;;;;;;;;^..  * .. ... .z^v^unooo     ..   .. 
                ..  ...88888888883$$$$%%%%%%%%%%%668%~~~~~~~~~;;;;;;;;;;;^...+ ....  .-        v^v^inoo*      ...  .
                ..  88888888866$$$%%%%%%%%%%88$;~~~~~~~~~~~~~;~~;-.-... .  -z.       ^        z^z^anoooo  ..   .. 
                ..  ..8888888866$$$%%%%%$%%%a~~~~~~~~~~~~~~~~;+....... .      ~--^               a^1^oaooooon ...  .
                .. 8888666666$$$$%%$&o~~~~~~~~~o~~~~~^; .....                ...-+o             o;*~;1zooon.   .. 
                .. 888886666%$%%v~~o~~oo~~o~~;^*;......^...                  *.....-v . .         u~1~oiu11~   .. 
                ..  .88886666%$$$~;~~~~~^-^......^a-...  .                  .  ; ......-z .+     ^    zn1n~;~v...  .
                ...8888666&$$a*;~~~;....;...   *an- ....                     .      .;-+^.*     +     ~~nvvo   .. 
                ..  ^8888666%~;;;o~~*  ...*. ..  i++o+   .     .           ..  .  n;;  . .-z^*     .     6~;1i...  .
                ..-8888a~ ~~~~o~~;-. .  *.   .;+.+^v-                    .-  -**     ....-^**           ~86*   .. 
                ..     ~~~~;n*o~~+.    .-    .~....+z-  .+ .          ....-...    -u;%on+-++*         -  i3;   .. 
                ..  .~~~~;;;&;*o~~;-.    ......*+.....+^+...-...............+*.- + *&#&&&&&$$$**        -+  %o...  .
                .. ;;v88$$&*^~~~;..  ....+.. i... . .-on-+-.*....^.-......*;-  ^886333%n$+..$a    -   -+u z.   .. 
                ..  .^8888$&&*^~~~*. .... .;^.*^-v*..      +;++*-...+.-..---*zz z-&vviuau ^!. -8+  .;   -+ u- ...  .
                ..  8888$$#*+~~~*..     .+*.*^..... .  .++  .;^~^+--o+--.**u   -$uuu%$3a~~1  ~v .-+  --a....   .. 
                ..   888%&&*+;~;*-       .**z^......^$&&&$866!o +.*^^^.o-^+n   . o;*1!z*+^~  +o -+   .+.nn..   .. 
                ..  ...8888&&n+*~;*+        v*i^+.--+&&$8333$&$--       .u          ;--.  ..+.~.+--z  -++.;.  ...  .
                ..   .888$&z+^~~;+..  ..  .~!+++^$$%$338ii1 .3--.                   v-..n---.---n  -+;++  ..   .. 
                ..  ...  %%%&&+;~~;+-.. +... .!++3$$-@zvaa%%zuvna                    ......-+--a-z+.+u*+  ..  ...  .
                ..   .. %%$&*o+~;^+.  .-....++868---1uoa6$3n^*^             -        ..-....v;^^+~;+.^    ..   .. 
                ..   ..  %%$$+n*~;+-  ..+.....^*8+   ;~++-..--~                          ....+^i1z^  ..   ..   .. 
                ..  ...  ...;$%3nn*~;+..  .^.....^**i   o+.    ~                             ...!^u1+ .  ...  ...  .
                ..   ..   ..;;;on6~~+.....*^....1^^+^v+++;-.....                            .!;~1;.  ..   ..   .. 
                ..  ...  ...  ..;^oo*z~~-.^...~++--.1^^+--.......             ...            .ioia1 ...  ...  ...  .
                ..   ..   ..   -aon*;3o^.^+++-;~;;;*^^**^-....                            i1111 ..   ..   ..   .. 
                ..   ..   ..   .. ^ovoo6z+;;^^+++a3*^^^^^+--.                           a33%1   ..   ..   ..   .. 
                ..  ...  ...  ...  ...^6u$1~vuz~;;;;**^11^^^^^+-.                       !i83o  ...  ...  ...  ...  .
                ..   ..   ..   ..   .. &1~nooo~iv~~~31u3;^^^^^+++-.                na;vn   ..   ..   ..   ..   .. 
                ..  ...  ...  ...  ...  ... ~o^^^ooooo~vv~o~!va3!1~^^+^++++---+^~vau;o..  ...  ...  ...  ...  ...  .
                ..   ..   ..   ..   ..   ..   -+^^~o~o~!v3za~~~zv~~~i;*********^ ..   ..   ..   ..   ..   ..   .. 
                ..   ..   ..   ..   ..   ..   ..   ..~~o~!o~~a~~~**u****on  ..   ..   ..   ..   ..   ..   ..   .. 
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

    def ShowSettingSelect(self,choice,menul):
        os.system ('cls')
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
        os.system ('cls')
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
            self.ShowMenu()

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
