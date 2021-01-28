from backend.common_tile import CommonTile


class Lake(CommonTile):

    def __init__(self):
        super().__init__()
        self.food = self.food + 1
        self.gold = self.gold + 1
