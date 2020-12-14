from common_tile import CommonTile

class Seastead(CommonTile):

    def __init__(self):
        super().__init__()
        self.food = 2
        self.houseing = 2
        self.acceptable_terrain = [
            'lake',
            'coast',
            'ocean',
        ]
