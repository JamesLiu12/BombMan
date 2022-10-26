from Item import Item

class Item_HPup(Item):
    def __init__(self):
        super().__init__()
        self.grids = [['┌', '─', '─', '─', '─', '┐'], [None, None, 'H', 'P', '↑', None], ['└', '─', '─', '─', '─', '┘']]
        self.val = 1
        self.delay = None
        self.priority = 4
    def IsBelongTo(self, typ):
        return typ == Item_HPup or super().IsBelongTo(typ)