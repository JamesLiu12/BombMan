目前确定的类：
Player
Bomb
Wall
Laser
EmptySpace
Maze
Runner
一个方格的大小：
3*6
┌────┐
│    │
└────┘
现在需要设计一下玩家在3*6格子中的造型，以及其他物品的造型。
包括炸弹，激光，墙。
伤害计算：
炸弹damage = player的atk
player的HP -= damage 受到伤害

player的移动：
speed为player可以在一秒移动多少个大的单元格
1/speed为player移动一个大的单元格要多少秒
对于vertical的移动，及axis=0，角色的移动时间间隔为1/speed/3
对于horizontal，为1/speed/6