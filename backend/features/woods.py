from backend.common_tile import CommonTile


class Woods(CommonTile):

    def __init__(self):
        super().__init__()
        self.production = 1
        self.acceptable_terrain = [
            'grassland',
            'plains',
            'tundra',
        ]
        self.hills = True
