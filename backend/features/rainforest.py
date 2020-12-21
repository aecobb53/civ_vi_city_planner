from common_tile import CommonTile


class Rainforest(CommonTile):

    def __init__(self):
        super().__init__()
        self.food = 1
        self.acceptable_terrain = [
            'plains'
        ]
        self.hills = True
