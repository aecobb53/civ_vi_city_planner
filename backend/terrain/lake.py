from common_tile import CommonTile

class Lake(CommonTile):

    def __init__(
        self,
        hills=None
    ):
        super().__init__()
        self.food = 1
        self.gold = 1