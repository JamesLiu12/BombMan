目前确定的类：
Player
Bomb
Wall
Beam
EmptySpace
Maze
Runner
一个方格的大小：
3*6
┌────┐┌────┐
│    ││    │
└────┘└────┘
现在需要设计一下玩家在3*6格子中的造型，以及其他物品的造型。
包括炸弹，激光，墙。
地图设计+物品设计 #AA
数值策划 #WCJ
大标题 #WCJ
UI逻辑 #WCJ
人物行走，炸弹爆炸破坏逻辑 #LSZ
除了EmptySpace，其余所有的物品中的空格字符用None表示
伤害计算：
炸弹damage = player的atk
player的HP -= damage 受到伤害

player的移动：
speed为player可以在一秒移动多少个大的单元格
1/speed为player移动一个大的单元格要多少秒
对于vertical的移动，及axis=0，角色的移动时间间隔为1/speed/3
对于horizontal，为1/speed/6
写description
做UI, GAMEOVER, BOMBMAN
上下左右键的逻辑 #AA
TOTO:
player的part

Description:
Bomb Man
1.	Game Introduction
A game contains n players, n can be chosen (n <= 4, recommended 3). Each player has infinite bomb to plant but have a 1.5s CD. Each bomb will release cross shape laser after 1.5s bomb have been planted. The laser can be stopped by obstacles and boundaries but will lower HP of obstacles (initial 2, -1 when be shotted), once HP of a obstacle below 0, it will be removed. Because of system difference, we recommand to play on windows system, the unroot linux(ed) version only support 1 player playing with bots. Also movement in unroot linux will have delay.
Each player has same initial HP 10, HP will decrease by 2 if they are shotted by laser, laser will penetrate the player. After being shotten by laser, the player will get 2s dodging all lasers. If HP downs below 0, the player is removed from the map. If there is 1 player left, game stopped

2.	Winning conditions
Once the game stops, there is a rating for each player. Surviving rank contains 80% of it and damage done contains 20%. This score will multiply with 1.5^n while n is killing number to form final score. Player with highest score wins.
3.	Game Menu
The game menu contains three choices (start, setting and quit). Player can use direction key to select, and use enter to confirm. Setting is for player to change keyboard settings (not recommended change default). If play is chosen, turn to the page of entering number of players and start the game. 
After the game, the program will show congratulations to winner and give a list of ranking of final score, containing diverse scores (placement, damage done and killing score).
