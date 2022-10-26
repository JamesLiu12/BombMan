import os
from Bot import Bot
from Item_ATKup import Item_ATKup
from Beam import Beam
from Bomb import Bomb
from Item_HPup import Item_HPup
from Maze import Maze
import time

from Player import Player
from Wall import Wall

class Runner:
    def __init__(self, fps, typ1, typ2, typ3, typ4):
        self.fps = fps
        self.players = []
        self.bots = []
        classList = [(typ1, 0, 0), (typ2, 0, 12), (typ3, 12, 12), (typ4, 12, 0)]
        for typ, posx, posy in classList:
            if typ == Player:
                self.players.append(Player())
            if typ == Bot:
                self.bots.append()
    def Run(self):
        maze = Maze(13, 13)
        maze.InsertObject(Wall(2, Item_HPup()), 2, 2)
        maze.InsertObject(Wall(2, Item_ATKup()), 4, 4)
        maze.InsertObject(Wall(2), 6, 6)
        p1 = Player('w', 's', 'a', 'd', ' ', 0, 1, 1)
        maze.InsertObject(p1, 1, 1)
        players = [p1]
        gameOver = False
        while not gameOver:
            startTime = float(time.perf_counter())
            for player in players:
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
                    if not maze.IsContainType(player.posx, player.posy, Bomb):
                        bomb = Bomb(player.posx, player.posy, player.bombDistance, player.atk, player.bombDelay, float(time.perf_counter()))
                        player.SetBomb(bomb)
                        maze.InsertObject(bomb, player.posx, player.posy)
                if player.IsMoving():
                    newPosx, newPosy = player.posx + player.dirx, player.posy + player.diry
                    if not player.IsCanMove(axis = 0 if dirx != 0 else 1): continue
                    player.Move()
                    maze.PeakUpItem(newPosx, newPosy, player)
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
            time.sleep(max(0, 1 / self.fps - (float(time.perf_counter()) - startTime)))