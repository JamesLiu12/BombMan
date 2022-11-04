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
from colorama import Fore, Back, Style
import platform
import random

class Runner:
    def __init__(self, fps, playerType1, playerType2, botType3, botType4, mapState):
        self.fps = fps
        self.players = []
        self.maze = Maze(13, 13, mapState)
        self.gameDelayTime = 180
        self.gameStartTime = 0
        if playerType1 == Player: self.players.append(Player(self.maze, 'w', 's', 'a', 'd', ' ', 1, 1, 1))
        if playerType2 == Player: self.players.append(Player(self.maze, '8', '2', '4', '6', '0', 2, 1, self.maze.width - 2))
        if botType3 == Bot: self.players.append(Bot(self.maze, 3, self.maze.height - 2, 1,1,3))
        if botType4 == Bot: self.players.append(Bot(self.maze, 4, self.maze.height - 2, self.maze.width - 2,1,3))
        for player in self.players:
            self.maze.InsertObject(player, player.posx, player.posy)
    def ShowScores(self):
        print(Fore.WHITE + f'Time Remaining: {self.GetRemainTime()}s')
        print(Fore.WHITE + '         ' + 'Score  ' + 'HP')
        for player in self.players:
            space = '   ' if player.IsBelongTo(Bot) else ''
            print(Fore.WHITE + f'{player.GetName()}:{space} {player.GetScore()}     {player.GetHP()}', end = '')
            print()
    def GameOver(self):
        if time.perf_counter() - self.gameStartTime >= self.gameDelayTime: return True
        cnt = 0
        for player in self.players:
            if not player.IsDead(): cnt += 1
        return cnt <= 1
    def GetPlayers(self):
        return self.players
    def GetHighestScorePlayers(self):
        players = []
        for player in self.players:
            if len(players) == 0: players.append(player)
            elif players[0].GetScore() == player.GetScore(): players.append(player)
            elif players[0].GetScore() < player.GetScore(): players = [player]
        return players
    def GetSurvivers(self):
        survivers = []
        for player in self.players:
            if not player.IsDead(): survivers.append(player)
        return survivers
    def GetRemainTime(self):
        return int(self.gameDelayTime - (time.perf_counter() - self.gameStartTime))
    def Run(self):
        self.gameStartTime = time.perf_counter()
        while not self.GameOver():
            startTime = float(time.perf_counter())
            for player in self.players:
                player.CheckItems()
                deleteBombs = []
                for bomb in player.bombs:
                    if bomb.isToExplode():
                        bomb.GenerateBeam(bomb.posx, bomb.posy)
                        self.maze.DeleteObject(bomb.posx, bomb.posy, bomb)
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
                if not player.IsBelongTo(Bot):
                    if player.IsSetBombPress():
                        if not self.maze.IsContainType(player.posx, player.posy, Bomb) and not player.IsDead() and not player.IsInDamage():
                            player.SetBomb()
                if player.IsMoving():
                    newPosx, newPosy = player.posx + player.dirx, player.posy + player.diry
                    player.Move()
                    if player.IsEndMove():
                        self.maze.DeleteObject(player.posx, player.posy, player)
                        player.InitParts()
                        player.SetPos(newPosx, newPosy)
                        player.InitDir()
                    else:
                        self.maze.updateGrid(newPosx, newPosy)
                    self.maze.updateGrid(player.posx, player.posy)
                elif not player.IsInDamage() and not player.IsDead():
                    if not player.IsBelongTo(Bot):
                        dirx, diry = player.GetMoveDir()
                    else:
                        isToSetBomb = random.random() <= player.GetSetBombProb()
                        if isToSetBomb:
                            dirx, diry = player.FindPathToSafePos(True)
                            if dirx != 0 or diry != 0:
                                if not self.maze.IsContainType(player.posx, player.posy, Bomb) and not player.IsDead() and not player.IsInDamage():
                                    if player.IsSetBombTimeGapOver():
                                        player.SetBomb()
                        dirx, diry = player.FindPathToSafePos(False)
                    if not (dirx == 0 and diry == 0):
                        newPosx = player.posx + dirx
                        newPosy = player.posy + diry
                        if not self.maze.IsBlockPlayer(newPosx, newPosy):
                            player.StartMove(dirx, diry)
                            self.maze.InsertObject(player, newPosx, newPosy)
                            player.PeakUpItem(newPosx, newPosy)

            os.system('cls' if platform.system() == 'Windows' else 'clear')
            self.maze.Show()
            self.ShowScores()
            time.sleep(max(0, 1 / self.fps - (float(time.perf_counter()) - startTime)))