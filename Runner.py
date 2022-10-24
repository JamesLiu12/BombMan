import os
from Maze import Maze
import time

class Runner:
    def __init__(self, fps):
        self.fps = fps

    def Run(self):
        maze = Maze(8, 8)
        players = []
        bombs = []
        gameOver = False
        while not gameOver:
            for player in players:
                if player.IsMoving():
                    newPosx, newPosy = player.posx + player.dirx, player.posy + player.posy
                    if not player.IsCanMove(): continue
                    player.Move()
                    if player.IsEndMove():
                        maze.DeleteObject(player.posx, player.posy)
                        player.InitPart()
                    else:
                        maze.updateGrid(newPosx, newPosy)
                    maze.updateGrid(player.posx, player.posy)
                else:
                    dirx, diry = player.GetMove()
                    if dirx == 0 and diry == 0: continue
                    else:
                        newPosx = player.posx + dirx
                        newPosy = player.posy + diry
                        if maze.IsBolckPlayer(newPosx, newPosy): continue
                        player.StartMove(dirx, diry)
                        maze.InsertObject(player, newPosx, newPosy)
            os.system('cls')
            maze.Show()
            time.sleep(self.fps)