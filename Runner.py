import os
from Bot import Bot
from Item_ATKup import Item_ATKup
from Beam import Beam
from Bomb import Bomb
from Item_HPup import Item_HPup
from Maze import Maze
import time
import keyboard
from Player import Player
from Wall import Wall

class Runner:
    def __init__(self, fps):
        self.fps = fps
        self.players = []
    def Run(self):
        maze = Maze(13, 13, 1)
        p1 = Player(maze, 'w', 's', 'a', 'd', ' ', 1, 1, 1)
        p2 = Player(maze, keyboard.KEY_UP, keyboard.KEY_DOWN, '4', '6', '0', 2, 1, maze.width - 2)
        maze.InsertObject(p1, 1, 1)
        maze.InsertObject(p2, 1, maze.width - 2)
        self.players = [p1, p2]
        gameOver = False
        while not gameOver:
            startTime = float(time.perf_counter())
            for player in self.players:
                player.CheckItems()
                deleteBombs = []
                for bomb in player.bombs:
                    if bomb.isToExplode():
                        bomb.GenerateBeam(bomb.posx, bomb.posy)
                        maze.DeleteObject(bomb.posx, bomb.posy, bomb)
                        deleteBombs.append(bomb)
                while len(player.beams):
                    beam = player.beams[0]
                    if not beam.IsToDelete(): break
                    beam.DestroyBeam(beam.centerPosx, beam.centerPosy)
                    del player.beams[0]
                for bomb in deleteBombs:
                    player.bombs.remove(bomb)
                if player.IsInDamage():
                    player.Flicking()
                else: 
                    player.returnToOrigGrid()
                if player.IsSetBombPress():
                    if not maze.IsContainType(player.posx, player.posy, Bomb) and not player.IsDead() and not player.IsInDamage():
                        player.SetBomb()
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
                        player.PeakUpItem(newPosx, newPosy)
            os.system('cls')
            maze.Show()
            time.sleep(max(0, 1 / self.fps - (float(time.perf_counter()) - startTime)))