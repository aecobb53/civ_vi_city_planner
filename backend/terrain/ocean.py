from backend.common_tile import CommonTile

class Ocean(CommonTile):

    def __init__(
        self,
        hills=None
    ):
        super().__init__()
        self.food = self.food + 1
        self.hills = False
