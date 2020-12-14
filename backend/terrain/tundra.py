from common_tile import CommonTile

class Tundra(CommonTile):

    def __init__(
        self,
        hills=None
    ):
        super().__init__()
        self.food = 1
        self.production = 1 if hills == True else 0