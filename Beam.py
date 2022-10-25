from turtle import delay
from BaseObject import BaseObject
from colorama import Fore, Back, Style
import  time
class Beam(BaseObject):
    def __init__(self, centerPosx, centerPosy, distance, damage, setTime):
        super().__init__()
        self.isBlockPlayer = False
        self.isBlockBeam = False
        self.delay = 0.5
        self.centerPosx, self.centerPosy = centerPosx, centerPosy
        self.distance = distance
        self.damage = damage
        self.setTime = setTime
        self.priority = 3
        self.backColors = [[Back.YELLOW for j in range(6)] for i in range(3)]
    def isToDelete(self):
        return float(time.perf_counter()) - self.setTime >= self.delay