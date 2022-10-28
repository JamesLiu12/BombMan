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
        maze.InsertObject(Wall(2, Item_HPup()), 2, 2)
        maze.InsertObject(Wall(2, Item_ATKup()), 4, 4)
        maze.InsertObject(Wall(2), 6, 6)
        p1 = Player('w', 's', 'a', 'd', ' ', 1, 1, 1)
        p2 = Player(keyboard.KEY_UP, keyboard.KEY_DOWN, '4', '6', '0', 2, 1, maze.width - 2)
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
                        beam = Beam(bomb.posx, bomb.posy, bomb.distance, bomb.damage, float(time.perf_counter()))
                        player.SetBeam(beam)
                        maze.GenerateBeam(bomb.posx, bomb.posy, beam)
                        maze.DeleteObject(bomb.posx, bomb.posy, bomb)
                        deleteBombs.append(bomb)
                while len(player.beams):
                    beam = player.beams[0]
                    if not beam.isToDelete(): break
                    maze.DestroyBeam(beam.centerPosx, beam.centerPosy, beam)
                    del player.beams[0]
                for bomb in deleteBombs:
                    player.bombs.remove(bomb)
                if player.IsInDamage():
                    player.Flicking()
                    maze.updateGrid(player.posx, player.posy)
                    maze.updateGrid(player.posx + player.dirx, player.posy + player.diry)
                else: 
                    player.returnToOrigGrid()
                    maze.updateGrid(player.posx, player.posy)
                    maze.updateGrid(player.posx + player.dirx, player.posy + player.diry)
                if player.IsSetBombPress():
                    if not maze.IsContainType(player.posx, player.posy, Bomb) and not player.IsDead() and not player.IsInDamage():
                        bomb = Bomb(player.posx, player.posy, player.bombDistance, player.atk, player.bombDelay, float(time.perf_counter()))
                        player.SetBomb(bomb)
                        maze.InsertObject(bomb, player.posx, player.posy)
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
                        maze.PeakUpItem(newPosx, newPosy, player)
            os.system('cls')
            maze.Show()
            time.sleep(max(0, 1 / self.fps - (float(time.perf_counter()) - startTime)))