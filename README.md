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
