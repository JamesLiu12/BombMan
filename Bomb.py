class Bomb():
    def __init__(self, damage, distance, speed = 0):
        super().__init__(0x3f3f3f3f, speed)
        self.damage = damage
        self.distance = distance
        self.isBlockPlayer = True
        self.isBlockBeam = False
        self.priority = 1
        # self.grids