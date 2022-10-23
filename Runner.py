import os
from Maze import Maze
import time

class Runner:
    def __init__(self, fps):
        self.fps = fps

    def Run(self):
        maze = Maze(8, 8)
        players = []
        inMovePlayers = []
        bombs = []
        gameOver = False
        while not gameOver:
            for inMovePlayer in inMovePlayers:
                pass
            for player in players:
                dirx, diry = player.GetMove()
                if dirx == 0 and diry == 0: continue
                else:
                    # PlayerFromEmpty = PlayerFromEmpty(player, dirx, diry)
                    # maze.ChangeGrid(player.posx, player.posy, PlayerFromEmpty(player, dirx, diry))
                    newPosx = player.posx + dirx
                    newPosy = player.posy + diry
                    nextGrid = maze.getObject(newPosx, newPosy)
                    if nextGrid.block: continue
                    player.StartMove(dirx, diry)
                    nextGrid.StartEnter(player)
                    inMovePlayers.append(player)
            os.system('cls')
            maze.Show()
            time.sleep(self.fps)