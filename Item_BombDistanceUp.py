from Item import Item
class Item_BombDistanceUp(Item):
    def __init__(self):
        super().__init__()
        self.val = 1
        self.delay = 10
        self.grids = [['~' for j in range(6)] for i in range(3)]
    def IsBelongTo(self, typ):
        return typ == Item_BombDistanceUp or super().IsBelongTo(typ)