from BaseObject import BaseObject


class Obstacle(BaseObject):
    def __init__(self, item = None):
        super().__init__()
        self.HP = None
        self.isBlockPlayer = True
        self.isBlockBeam = True
        self.priority = 4
        self.item = item
    def ChangeHP(self, val):
        self.HP += val

    def IsDead(self):
        return self.HP <= 0

    def IsBelongTo(self, typ):
        return typ == Obstacle or super().IsBelongTo(typ)