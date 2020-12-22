from backend.common_tile import CommonTile

class Plains(CommonTile):

    def __init__(
        self,
        hills=None
    ):
        super().__init__()
        self.food = 1
        self.production = 2 if hills == True else 1
