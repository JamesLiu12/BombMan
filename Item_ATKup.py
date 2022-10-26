from Item import Item

class Item_ATKup(Item):
    def __init__(self):
        super().__init__()
        self.grids = [['┌', '─', '─', '─', '─', '┐'], [None, 'A', 'T', 'K', '↑', None], ['└', '─', '─', '─', '─', '┘']]
        self.val = 1
        self.delay = 10
        self.priority = 4
    def IsBelongTo(self, typ):
        return typ == Item_ATKup or super().IsBelongTo(typ)