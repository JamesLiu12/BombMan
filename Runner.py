import os
from Maze import Maze
import time

from Player import Player

class Runner:
    def __init__(self, fps):
        self.fps = fps

    def Run(self):
        maze = Maze(16, 16)
        p1 = Player('w', 's', 'a', 'd', 0, 0, 0, 0)
        maze.InsertObject(p1, 0, 0)
        players = [p1]
        bombs = []
        gameOver = False
        while not gameOver:
            for player in players:
                if player.IsMoving():
                    newPosx, newPosy = player.posx + player.dirx, player.posy + player.diry
                    if not player.IsCanMove(axis = 0 if dirx != 0 else 1): continue
                    player.Move()
                    if player.IsEndMove():
                        maze.DeleteObject(player.posx, player.posy, player)
                        player.InitParts()
                        player.SetPos(newPosx, newPosy)
                        player.InitDir()
                    else:
                        maze.updateGrid(newPosx, newPosy)
                    maze.updateGrid(player.posx, player.posy)
                else:
                    dirx, diry = player.GetMoveDir()
                    if dirx == 0 and diry == 0: continue
                    else:
                        newPosx = player.posx + dirx
                        newPosy = player.posy + diry
                        if maze.IsBolckPlayer(newPosx, newPosy): continue
                        player.StartMove(dirx, diry)
                        maze.InsertObject(player, newPosx, newPosy)
            os.system('cls')
            maze.Show()
            time.sleep(1 / self.fps)