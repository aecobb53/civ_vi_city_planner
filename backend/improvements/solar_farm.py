from backend.common_tile import CommonTile

class SolarFarm(CommonTile):

    def __init__(self):
        super().__init__()
        self.production = 1
        self.gold = 1
        self.power = 2
        self.acceptable_terrain = [
            'grassland',
            'plains',
            'tundra',
            'desert',
        ]
        self.acceptable_features = None
        self.resources = None
