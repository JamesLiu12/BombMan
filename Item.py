from BaseObject import BaseObject


class Item(BaseObject):
    def __init__(self, maze):
        super().__init__(maze)
        self.val = None
        self.delay = None
        self.priority = 4
    def IsBelongTo(self, typ):
        return typ == Item or super().IsBelongTo(typ)