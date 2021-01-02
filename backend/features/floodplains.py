from backend.common_tile import CommonTile


class Floodplains(CommonTile):

    def __init__(self):
        super().__init__()
        self.food = 3
        self.acceptable_terrain = [
            'desert',
            'plains',
            'grassland',
        ]
