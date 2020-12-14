from common_tile import CommonTile

class Desert(CommonTile):

    def __init__(
        self,
        hills=None
    ):
        super().__init__()
        self.production = 1 if hills == True else 0
