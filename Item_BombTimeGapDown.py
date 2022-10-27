from Item import Item

class Item_BombTimeGapDown(Item):
    def __init__(self):
        super().__init__()
        self.val = -0.5
        self.delay = 10
    def IsBelongTo(self, typ):
        return typ == Item_BombTimeGapDown or super().IsBelongTo(typ)