from backend.common_tile import CommonTile


class Oasis(CommonTile):

    def __init__(self):
        super().__init__()
        self.food = 3
        self.gold = 1
        self.acceptable_terrain = [
            'desert'
        ]
