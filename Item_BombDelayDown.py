from Item import Item


class Item_BombDelayDown(Item):
    def __init__(self):
        super().__init__()
        self.val = -0.5
        self.delay = 10