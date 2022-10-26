from Item import Item

class Item_SPDup(Item):
    def __init__(self):
        super().__init__()
        self.val = 2
        self.delay = 10