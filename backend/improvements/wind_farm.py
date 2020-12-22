from backend.common_tile import CommonTile

class WindFarm(CommonTile):

    def __init__(self):
        super().__init__()
        self.production = 1
        self.gold = 1
        self.power = 2
        self.acceptable_terrain = [
            'desert',
            'grassland',
            'plains',
            'snow',
            'tundra',
        ]
        self.hills = True
