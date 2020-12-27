from backend.common_tile import CommonTile

class Plains(CommonTile):

    def __init__(
        self,
        hills=None
    ):
        super().__init__()
        self.food = self.food + 1
        self.production = self.production + 1
        self._hills = None
        if hills:
            self.hills = True

    # hills
    @property
    def hills(self):
        if self._hills is None:
            return False
        return self._hills

    @hills.setter
    def hills(self, value):
        if value:
            self.production = self.production + 1
            self._hills = True
