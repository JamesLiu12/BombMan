from BaseObject import BaseObject


class Item(BaseObject):
    def __init__(self):
        super().__init__()
        self.val = None
        self.delay = None
    def IsBelongTo(self, typ):
        return typ == Item or super().IsBelongTo(typ)