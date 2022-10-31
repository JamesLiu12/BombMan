from Player import Player
class Bot(Player):
    def __init__(self, maze, key_up, key_down, key_left, key_right, key_setBomb, id, posx, posy, HP=3, speed=4, bombDelay=2):
        super().__init__(maze, key_up, key_down, key_left, key_right, key_setBomb, id, posx, posy, HP, speed, bombDelay)