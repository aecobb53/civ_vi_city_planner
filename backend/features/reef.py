from common_tile import CommonTile


class Reef(CommonTile):

    def __init__(self):
        super().__init__()
        self.food = 1
        self.production = 1
        self.acceptable_terrain = [
            'coast'
        ]
