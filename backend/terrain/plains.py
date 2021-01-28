from backend.common_tile import CommonTile


class Plains(CommonTile):

    def __init__(self):
        super().__init__()
        self.food = self.food + 1
        self.production = self.production + 1
