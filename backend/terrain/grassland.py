from backend.common_tile import CommonTile

class Grassland(CommonTile):

    def __init__(
        self,
        hills=None
    ):
        super().__init__()
        self.food = 2
        self.production = 1 if hills == True else 0
